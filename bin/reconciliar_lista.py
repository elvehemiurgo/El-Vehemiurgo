#!/usr/bin/env python3
"""Reconcilia la lista personal maestra con el archivo: marca (✓)
los bullets cuyo match/segment ya tiene ficha, derivándolo de los
índices. El texto verbatim del bullet se preserva intacto (solo se
envuelve en negrita + se agrega el link).

Matching: fecha exacta (DD.MM.YYYY del bullet vs fecha del archivo)
+ solapamiento de tokens distintivos (≥2, o ≥1 si la fecha es
inequívoca), con mapa de variantes de glossary/nombres-canonicos.md.

Uso:
  python3 bin/reconciliar_lista.py            # dry-run (propuestas)
  python3 bin/reconciliar_lista.py --apply    # escribe las marcas
"""
import re, sys, unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LISTA = ROOT / "notebook/2026-05-09-2-lista-personal-completa.md"
APPLY = "--apply" in sys.argv

STOP = {"the", "and", "with", "match", "team", "title", "wwe", "aew", "tna",
        "nxt", "raw", "smackdown", "impact", "dynamite", "collision", "njpw",
        "roh", "wcw", "wwf", "cmll", "aaa", "stardom", "night", "week",
        "thursday", "monday", "live", "event", "house", "show", "ppv", "vs"}


def norm(s):
    s = unicodedata.normalize("NFD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9 ]", " ", s)


def variant_map():
    reg = ROOT / "glossary/nombres-canonicos.md"
    vmap = {}
    if reg.exists():
        in_t = False
        for ln in reg.read_text().split("\n"):
            if ln.startswith("## Variantes prohibidas"):
                in_t = True; continue
            if in_t and ln.startswith("## "):
                break
            m = re.match(r"\| ([^|]+) \| ([^|]+) \|", ln)
            if in_t and m and "Canónico" not in m.group(1):
                canon_tokens = norm(m.group(1)).split()
                for v in m.group(2).split(","):
                    for tok in norm(v).split():
                        if tok not in canon_tokens and canon_tokens:
                            vmap[tok] = canon_tokens[-1]  # apellido canónico
    vmap.update({"elias": "elijah", "mickey": "mickie"})
    return vmap


VMAP = variant_map()


def tokens(s):
    out = set()
    for t in norm(s).split():
        t = VMAP.get(t, t)
        if len(t) >= 4 and t not in STOP and not t.isdigit():
            out.add(t)
    return out


def archive_entries():
    entries = []
    for sub in ("archive/matches", "archive/segments"):
        for f in (ROOT / sub).glob("*.md"):
            if f.name in ("index.md", "README.md"):
                continue
            m = re.search(r"^fecha:\s*(\d{4}-\d{2}-\d{2})", f.read_text(), re.M)
            if m:
                entries.append((m.group(1), f))
    return entries


ENTRIES = archive_entries()
BY_DATE = {}
for d, f in ENTRIES:
    BY_DATE.setdefault(d, []).append(f)

lines = LISTA.read_text().split("\n")

# límites: solo la sección "## La lista" (verbatim), no el análisis posterior
start = next((i for i, l in enumerate(lines) if l.startswith("## La lista")), 0)
end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))

# archivos ya linkeados desde alguna línea (✓) no se vuelven a proponer
ya_linkeados = set(re.findall(r"archive/(?:matches|segments)/([^)`\s]+\.md)", "\n".join(lines)))

SEG_KEYS = ("PROMO", "SEGMENT", "RETURN", "VIDEO", "PACKAGE", "IN-RING", "BACKSTAGE")

proposals, applied = [], 0
for i, ln in enumerate(lines):
    if not (start < i < end):
        continue
    if not ln.startswith("- ") or ln.startswith("- (✓)"):
        continue
    dm = re.search(r"(\d{2})\.(\d{2})\.(\d{4})", ln)
    if not dm:
        continue
    fecha = f"{dm.group(3)}-{dm.group(2)}-{dm.group(1)}"
    up = ln.upper()
    es_segment = any(k in up for k in SEG_KEYS) and " VS " not in up
    cands = [f for f in BY_DATE.get(fecha, []) if f.name not in ya_linkeados]
    cands = [f for f in cands
             if (f.parent.name == "segments") == es_segment or " VS " not in up]
    if not cands:
        continue
    btoks = tokens(ln)
    best, best_n, best_cov = None, 0, 0.0
    for f in cands:
        ft = tokens(f.stem)
        n = len(btoks & ft)
        cov = n / len(ft) if ft else 0
        if (n, cov) > (best_n, best_cov):
            best, best_n, best_cov = f, n, cov
    ok = best is not None and best_cov >= 0.6 and (
        best_n >= 2 or (best_n == 1 and len(cands) == 1 and best_cov >= 0.67))
    if ok:
        rel = f"../archive/{best.parent.name}/{best.name}"
        texto = ln[2:].strip()
        nuevo = f"- (✓) **{texto}** → [`archive/{best.parent.name}/{best.name}`]({rel}) (reconciliación automática)"
        proposals.append((i + 1, texto[:60], best.name, f"{best_n}/{best_cov:.2f}"))
        ya_linkeados.add(best.name)
        if APPLY:
            lines[i] = nuevo
            applied += 1

for n, txt, f, score in proposals:
    print(f"L{n} [{score}] {txt}  ->  {f}")
print(f"\n{len(proposals)} propuestas" + (f", {applied} aplicadas" if APPLY else " (dry-run; usar --apply)"))
if APPLY and applied:
    LISTA.write_text("\n".join(lines))
