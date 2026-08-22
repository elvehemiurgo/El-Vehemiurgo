#!/usr/bin/env python3
"""Reconcilia la lista personal maestra con el archivo: marca (✓)
los bullets cuyo match/segment ya tiene ficha, derivándolo de los
índices. El texto verbatim del bullet se preserva intacto (solo se
envuelve en negrita + se agrega el link).

Matching: fecha exacta (DD.MM.YYYY del bullet vs fecha del archivo)
+ solapamiento de tokens distintivos (≥2, o ≥1 si la fecha es
inequívoca), con el registro canónico vía archivo_lib.

Uso:
  python3 bin/reconciliar_lista.py            # dry-run (propuestas)
  python3 bin/reconciliar_lista.py --apply    # escribe las marcas
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import archivo_lib as al

APPLY = "--apply" in sys.argv
VMAP = al.token_map()

# fichas por fecha
BY_DATE = {}
for ficha in al.iter_fichas():
    BY_DATE.setdefault(ficha.fecha, []).append(ficha.path)

lines = al.LISTA.read_text().split("\n")
bullets = al.lista_bullets()

# archivos ya linkeados desde alguna línea (✓) no se vuelven a proponer
ya_linkeados = {b.link.split("/")[-1] for b in bullets if b.link}

proposals, applied = [], 0
for b in bullets:
    if b.marked or not b.fecha:
        continue
    cands = [f for f in BY_DATE.get(b.fecha, []) if f.name not in ya_linkeados]
    tipo = al.bullet_tipo(b.texto)
    if tipo == "match":
        cands = [f for f in cands if f.parent.name == "matches"]
    elif tipo == "segment":
        cands = [f for f in cands if f.parent.name == "segments"]
    if not cands:
        continue
    btoks = al.tokens(b.raw, VMAP)
    best, best_n, best_cov = None, 0, 0.0
    for f in cands:
        ft = al.tokens(f.stem, VMAP)
        n = len(btoks & ft)
        cov = n / len(ft) if ft else 0
        if (n, cov) > (best_n, best_cov):
            best, best_n, best_cov = f, n, cov
    ok = best is not None and best_cov >= 0.6 and (
        best_n >= 2 or (best_n == 1 and len(cands) == 1 and best_cov >= 0.67))
    if ok:
        rel = f"../archive/{best.parent.name}/{best.name}"
        texto = b.raw[2:].strip()
        nuevo = f"- (✓) **{texto}** → [`archive/{best.parent.name}/{best.name}`]({rel}) (reconciliación automática)"
        proposals.append((b.lineno, texto[:60], best.name, f"{best_n}/{best_cov:.2f}"))
        ya_linkeados.add(best.name)
        if APPLY:
            lines[b.lineno - 1] = nuevo
            applied += 1

for n, txt, f, score in proposals:
    print(f"L{n} [{score}] {txt}  ->  {f}")
print(f"\n{len(proposals)} propuestas" + (f", {applied} aplicadas" if APPLY else " (dry-run; usar --apply)"))
if APPLY and applied:
    al.LISTA.write_text("\n".join(lines))
