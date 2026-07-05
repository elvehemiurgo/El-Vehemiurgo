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
proposals, applied = [], 0
for i, ln in enumerate(lines):
    if not ln.startswith("- ") or ln.startswith("- (✓)"):
        continue
    dm = re.search(r"(\d{2})\.(\d{2})\.(\d{4})", ln)
    if not dm:
        continue
    fecha = f"{dm.group(3)}-{dm.group(2)}-{dm.group(1)}"
    cands = BY_DATE.get(fecha, [])
    if not cands:
        continue
    btoks = tokens(ln)
    best, best_n = None, 0
    for f in cands:
        n = len(btoks & tokens(f.stem))
        if n > best_n:
            best, best_n = f, n
    threshold = 2 if len(cands) > 1 else 1
    if best and best_n >= threshold:
        rel = f"../archive/{best.parent.name}/{best.name}"
        texto = ln[2:].strip()
        nuevo = f"- (✓) **{texto}** → [`archive/{best.parent.name}/{best.name}`]({rel}) (reconciliación automática)"
        proposals.append((i + 1, texto[:60], best.name, best_n))
        if APPLY:
            lines[i] = nuevo
            applied += 1

for n, txt, f, score in proposals:
    print(f"L{n} [{score}] {txt}  ->  {f}")
print(f"\n{len(proposals)} propuestas" + (f", {applied} aplicadas" if APPLY else " (dry-run; usar --apply)"))
if APPLY and applied:
    LISTA.write_text("\n".join(lines))
