#!/usr/bin/env python3
"""Regenera las tablas índice de matches y segments desde el corpus.

El índice es 100% derivable de las fichas (glob + frontmatter), así
que se regenera entero en vez de mantenerse incrementalmente: los
estados inválidos (filas duplicadas, desorden, filas huérfanas) se
vuelven irrepresentables por construcción. La prosa del header y el
footer de cada index.md se preservan; solo el cuerpo de filas se
reemplaza.

Orden: fecha descendente; a igual fecha, filename ascendente
(determinístico e idempotente).

Los checks E1/E2/E3 del lint se conservan como guardas baratas: E1
sigue atrapando el "olvidé regenerar tras crear una ficha", y E2/E3
atrapan ediciones a mano (que la doctrina prohíbe, pero ocurren).

Uso:
  python3 bin/regen_index.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import archivo_lib as al


def regen(kind):
    index = al.ROOT / "archive" / kind / "index.md"
    lines = index.read_text().split("\n")

    row_idx = [i for i, ln in enumerate(lines) if al.ROW_RE.match(ln)]
    if row_idx:
        header, footer = lines[:row_idx[0]], lines[row_idx[-1] + 1:]
    else:
        # sin filas todavía: cortar tras el separador de la tabla
        sep = next(i for i, ln in enumerate(lines) if ln.startswith("|---"))
        header, footer = lines[:sep + 1], lines[sep + 1:]

    fichas = sorted(al.iter_fichas((kind,)),
                    key=lambda f: (f.fecha, f.path.name))
    fichas.sort(key=lambda f: f.fecha, reverse=True)
    rows = [al.format_index_row(f) for f in fichas]

    index.write_text("\n".join(header + rows + footer))
    print(f"regenerado: archive/{kind}/index.md ({len(rows)} filas)")


if __name__ == "__main__":
    regen("matches")
    regen("segments")
