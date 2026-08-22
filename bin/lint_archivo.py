#!/usr/bin/env python3
"""Lint del archivo El Vehemiurgo.

Checks (ERROR = exit 1; WARNING = solo informa):
  E1  index <-> files sync (matches y segments, ambas direcciones)
  E2  filas duplicadas en los índices
  E3  índices ordenados por fecha descendente
  E4  links relativos rotos en archive/** (incluye same-dir)
  E5  clases_vehemiurgo con vocabulario inválido (solo slugs)
  E6  links de tabla del panteón (SoT) a fichas inexistentes
  W1  estado fuera de vocabulario {stub, en-investigacion, verificado, vivo, fallecido}
  W2  variantes de nombre prohibidas (glossary/nombres-canonicos.md)
      fuera de notebook/ y fuera de líneas quote (>)

W2 corre siempre (también en --pre-commit): el conteo del resumen es
honesto. En --pre-commit solo se imprimen errores, no los warnings.

Uso:
  python3 bin/lint_archivo.py               # todo, warnings listados
  python3 bin/lint_archivo.py --pre-commit  # solo errores, salida corta
  python3 bin/lint_archivo.py --stats       # métricas para estado-sesion
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import archivo_lib as al

ROOT = al.ROOT
QUIET = "--pre-commit" in sys.argv
errors, warnings = [], []

ESTADOS_OK = {"stub", "en-investigacion", "verificado", "vivo", "fallecido"}
ROW_RE = re.compile(r"^\| (\d{4}-[\dX]{2}-[\dX]{2}) \|")
LINK_RE = re.compile(r"\]\((?!https?:)((?:\.\.?/)?[^)#\s:]+\.md)\)")


def stats():
    """Métricas con las definiciones correctas, para estado-sesion.sh."""
    counts = {}
    for kind in ("matches", "segments", "people", "topics"):
        counts[kind] = sum(1 for f in (ROOT / "archive" / kind).glob("*.md")
                           if f.name not in ("index.md", "README.md"))
    bullets = al.lista_bullets()
    print(f"fichas: {counts['matches']} matches · {counts['segments']} segments "
          f"· {counts['people']} people · {counts['topics']} topics")
    print(f"lista personal: {sum(1 for b in bullets if b.marked)} de {len(bullets)} "
          f"bullets reconciliados (✓)")


def check_index(index_path, files_dir):
    p = ROOT / index_path
    text = p.read_text()
    rows = [(i + 1, ln) for i, ln in enumerate(text.split("\n")) if ROW_RE.match(ln)]
    # E2 duplicados (por archivo linkeado)
    seen = {}
    linked = set()
    for n, ln in rows:
        m = re.search(r"\[→\]\(([^)]+)\)", ln)
        if not m:
            errors.append(f"E2 {index_path}:{n} fila sin link de archivo")
            continue
        f = m.group(1)
        linked.add(f)
        if f in seen:
            errors.append(f"E2 {index_path}:{n} fila duplicada (ya en línea {seen[f]}): {f}")
        seen[f] = n
    # E3 orden desc
    dates = [ln.split("|")[1].strip() for _, ln in rows]
    for i in range(1, len(dates)):
        if dates[i] > dates[i - 1]:
            errors.append(f"E3 {index_path} fuera de orden: {dates[i]} después de {dates[i-1]} (fila {rows[i][0]})")
    # E1 sync
    real = {f.name for f in (ROOT / files_dir).glob("*.md")} - {"index.md", "README.md"}
    for f in linked - real:
        errors.append(f"E1 {index_path} linkea archivo inexistente: {f}")
    for f in real - linked:
        errors.append(f"E1 {files_dir}/{f} sin fila en {index_path}")


def check_links():
    for f in (ROOT / "archive").rglob("*.md"):
        text = f.read_text()
        for m in LINK_RE.finditer(text):
            target = (f.parent / m.group(1)).resolve()
            if not target.exists():
                n = text[: m.start()].count("\n") + 1
                errors.append(f"E4 {f.relative_to(ROOT)}:{n} link roto -> {m.group(1)}")


def check_frontmatter():
    for sub in ("archive/matches", "archive/segments", "archive/people",
                "archive/promotions", "archive/topics"):
        for f in (ROOT / sub).glob("*.md"):
            if f.name in ("index.md", "README.md"):
                continue
            fm = al.parse_fm(f.read_text())
            estado = fm.get("estado")
            if isinstance(estado, str) and estado and estado not in ESTADOS_OK:
                warnings.append(f"W1 {f.relative_to(ROOT)} estado fuera de vocabulario: {estado}")
            clases = fm.get("clases_vehemiurgo")
            for v in clases if isinstance(clases, list) else []:
                if v not in al.CLASES_OK:
                    errors.append(f"E5 {f.relative_to(ROOT)} clase inválida: \"{v}\" (usar slugs)")


def check_panteon():
    text = al.PANTEON.read_text()
    for m in re.finditer(r"\[→\]\((\.\./people/[^)]+\.md)\)", text):
        if not (al.PANTEON.parent / m.group(1)).resolve().exists():
            errors.append(f"E6 panteón SoT linkea ficha inexistente: {m.group(1)}")


def check_names():
    variants = al.load_variantes()
    if not variants:
        return
    # precompilado: alternación única como descarte rápido + regex por
    # variante para atribuir. Baja el costo de ~14 s a <0,5 s y permite
    # que W2 corra también en el gate diario.
    per = [(re.compile(rf"\b{re.escape(al.norm(v))}\b"), v, al.norm(c), c)
           for v, c in variants]
    alt = re.compile("|".join(rf"\b{re.escape(al.norm(v))}\b" for v, _ in variants))
    dash = re.compile(r"[-_]")
    for base in ("archive", "dossiers"):
        for f in (ROOT / base).rglob("*.md"):
            for i, ln in enumerate(f.read_text().split("\n"), 1):
                if ln.lstrip().startswith(">"):
                    continue  # quotes verbatim exentos
                lnn = dash.sub(" ", al.norm(ln))
                if not alt.search(lnn):
                    continue
                for rx, v, ncanon, canon in per:
                    # El canónico en la misma línea desactiva el chequeo:
                    # cubre variantes que son subcadena del canónico y las
                    # glosas legítimas que declaran la equivalencia.
                    if rx.search(lnn.replace(ncanon, " ")):
                        warnings.append(f"W2 {f.relative_to(ROOT)}:{i} variante \"{v}\" (canónico: {canon})")


if "--stats" in sys.argv:
    stats()
    sys.exit(0)

check_index("archive/matches/index.md", "archive/matches")
check_index("archive/segments/index.md", "archive/segments")
check_links()
check_frontmatter()
check_panteon()
check_names()

for e in errors:
    print(f"ERROR  {e}")
if not QUIET:
    for w in warnings:
        print(f"WARN   {w}")
print(f"\nlint: {len(errors)} errores, {len(warnings)} warnings")
sys.exit(1 if errors else 0)
