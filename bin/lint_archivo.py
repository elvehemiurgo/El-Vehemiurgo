#!/usr/bin/env python3
"""Lint del archivo El Vehemiurgo.

Checks (ERROR = exit 1; WARNING = solo informa):
  E1  index <-> files sync (matches y segments, ambas direcciones)
  E2  filas duplicadas en los índices
  E3  índices ordenados por fecha descendente
  E4  links relativos rotos en archive/**
  E5  clases_vehemiurgo con vocabulario inválido (solo slugs)
  E6  links de tabla del panteón (SoT) a fichas inexistentes
  W1  estado fuera de vocabulario {stub, en-investigacion, verificado, vivo, fallecido}
  W2  variantes de nombre prohibidas (glossary/nombres-canonicos.md)
      fuera de notebook/ y fuera de líneas quote (>)

Uso:
  python3 bin/lint_archivo.py            # todo, warnings incluidos
  python3 bin/lint_archivo.py --pre-commit  # solo errores, salida corta
"""
import re, sys, unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
QUIET = "--pre-commit" in sys.argv
errors, warnings = [], []

CLASES_OK = {"perfect-wrestling", "fighting-spirit", "wrestling-entertainment"}
ESTADOS_OK = {"stub", "en-investigacion", "verificado", "vivo", "fallecido"}
ROW_RE = re.compile(r"^\| (\d{4}-[\dX]{2}-[\dX]{2}) \|")
LINK_RE = re.compile(r"\]\(((?:\.\.?/)[^)#\s]+\.md)\)")


def frontmatter(text):
    if not text.startswith("---"):
        return ""
    end = text.find("\n---", 3)
    return text[:end] if end != -1 else ""


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
            fm = frontmatter(f.read_text())
            m = re.search(r"^estado:\s*([\w-]+)", fm, re.M)
            if m and m.group(1) not in ESTADOS_OK:
                warnings.append(f"W1 {f.relative_to(ROOT)} estado fuera de vocabulario: {m.group(1)}")
            cm = re.search(r"clases_vehemiurgo:\s*\[([^\]]*)\]", fm, re.S)
            if cm:
                vals = re.findall(r'"([^"]+)"', cm.group(1))
                for v in vals:
                    if v not in CLASES_OK:
                        errors.append(f"E5 {f.relative_to(ROOT)} clase inválida: \"{v}\" (usar slugs)")


def check_panteon():
    sot = ROOT / "archive/topics/heroes-fundamentales-vehemiurgia.md"
    text = sot.read_text()
    for m in re.finditer(r"\[→\]\((\.\./people/[^)]+\.md)\)", text):
        if not (sot.parent / m.group(1)).resolve().exists():
            errors.append(f"E6 panteón SoT linkea ficha inexistente: {m.group(1)}")


def norm(s):
    return unicodedata.normalize("NFD", s).encode("ascii", "ignore").decode().lower()


def check_names():
    reg = ROOT / "glossary/nombres-canonicos.md"
    if not reg.exists():
        return
    variants = []  # (variante, canonico)
    in_table = False
    for ln in reg.read_text().split("\n"):
        if ln.startswith("## Variantes prohibidas"):
            in_table = True
            continue
        if in_table and ln.startswith("## "):
            break
        m = re.match(r"\| ([^|]+) \| ([^|]+) \|", ln)
        if in_table and m and "Canónico" not in m.group(1):
            canon = m.group(1).strip()
            for v in m.group(2).split(","):
                variants.append((v.strip(), canon))
    for base in ("archive", "dossiers"):
        for f in (ROOT / base).rglob("*.md"):
            for i, ln in enumerate(f.read_text().split("\n"), 1):
                if ln.lstrip().startswith(">"):
                    continue  # quotes verbatim exentos
                lnn = norm(ln)
                for v, canon in variants:
                    # El canónico en la misma línea desactiva el chequeo:
                    # cubre variantes que son subcadena del canónico
                    # ("Cardona" en "Matt Cardona") y las glosas legítimas
                    # que declaran la equivalencia en la propia ficha.
                    # guiones a espacios para que los slugs cuenten
                    # como el canónico (matt-cardona.md == Matt Cardona)
                    resto = re.sub(r"[-_]", " ", lnn).replace(norm(canon), " ")
                    if re.search(rf"\b{re.escape(norm(v))}\b", resto):
                        warnings.append(f"W2 {f.relative_to(ROOT)}:{i} variante \"{v}\" (canónico: {canon})")


check_index("archive/matches/index.md", "archive/matches")
check_index("archive/segments/index.md", "archive/segments")
check_links()
check_frontmatter()
check_panteon()
if not QUIET:
    check_names()

for e in errors:
    print(f"ERROR  {e}")
if not QUIET:
    for w in warnings:
        print(f"WARN   {w}")
print(f"\nlint: {len(errors)} errores, {len(warnings)} warnings")
sys.exit(1 if errors else 0)
