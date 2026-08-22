#!/usr/bin/env python3
"""Shim de compatibilidad: valida las fichas nombradas y regenera los
índices completos vía regen_index.py.

El mantenimiento incremental (inserción ordenada, modo --rm con danza
de dos comandos para renames) se retiró: el índice es 100% derivable
del corpus, así que cada corrida regenera las dos tablas enteras —
estados inválidos irrepresentables, renames sin pasos extra. La
auditoría 2026-08-22 encontró 62 filas (~8%) desincronizadas de su
ficha por el modelo incremental; la regeneración total lo hace
imposible.

Uso (contrato de siempre — /volcado paso 3):
  python3 bin/index_add.py archive/matches/2026-XX-XX-slug.md [más...]
  python3 bin/index_add.py --rm archive/matches/slug-viejo.md   # no-op:
      tras un `git mv` basta cualquier corrida; se acepta por
      compatibilidad.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import archivo_lib as al
import regen_index

args = [a for a in sys.argv[1:] if a != "--rm"]

for arg in args:
    p = (al.ROOT / arg).resolve() if not Path(arg).is_absolute() else Path(arg)
    if not p.exists():
        if "--rm" in sys.argv:
            continue  # retirada: el archivo ya no existe, la regen la absorbe
        sys.exit(f"no existe: {arg}")
    ficha = al.load_ficha(p)
    if ficha is None:
        sys.exit(f"frontmatter ilegible o sin cierre: {p.name}")
    if not re.match(r"\d{4}-[\dX]{2}-[\dX]{2}$", ficha.fecha):
        sys.exit(f"fecha inválida o ausente ({ficha.fecha!r}): {p.name}")
    print(f"ok: {p.name}")

regen_index.regen("matches")
regen_index.regen("segments")
