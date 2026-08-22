#!/usr/bin/env python3
"""Inserta (o actualiza) la fila de un match/segment en su índice,
manteniendo orden por fecha descendente. Deriva la fila del
frontmatter del archivo — nunca editar la tabla a mano.

Uso:
  python3 bin/index_add.py archive/matches/2026-XX-XX-slug.md [más archivos...]

Renames: tras un `git mv`, retirar la fila vieja (el archivo ya no
existe) y sumar la nueva:
  python3 bin/index_add.py --rm archive/matches/slug-viejo.md
  python3 bin/index_add.py archive/matches/slug-nuevo.md
"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ABBR = {"perfect-wrestling": "PW", "fighting-spirit": "FS", "wrestling-entertainment": "WE"}


def fm_get(fm, key, default=""):
    m = re.search(rf'^{re.escape(key)}:[ \t]*(.*)$', fm, re.M)
    if not m:
        return default
    v = m.group(1).strip()
    if v.startswith('"'):
        # valor entre comillas, respetando \" escapadas
        mm = re.match(r'"((?:[^"\\]|\\.)*)"', v)
        return mm.group(1).replace('\\"', '"') if mm else default
    # sin comillas: cortar comentario inline de template
    return v.split("#")[0].strip() or default


def build_row(path):
    text = path.read_text()
    end = text.find("\n---", 3)
    fm = text[:end]
    fecha = fm_get(fm, "fecha")
    empresa = fm_get(fm, "empresa")
    programa = fm_get(fm, "programa")
    estado = fm_get(fm, "estado", "stub")
    veces = fm_get(fm, "veces_visto_vehemiurgo", "0")
    cm = re.search(r"clases_vehemiurgo:\s*\[([^\]]*)\]", fm, re.S)
    clases = re.findall(r'"([^"]+)"', cm.group(1)) if cm else []
    clase = "·".join(ABBR.get(c, c) for c in clases) or "—"
    emp = f"{empresa} / {programa}" if programa else empresa
    if path.parent.name == "matches":
        titulo = fm_get(fm, "match")
        row = f"| {fecha} | {titulo} | {emp} | {clase} | {estado} | {veces} | [→]({path.name}) |"
    else:
        titulo = fm_get(fm, "segmento")
        tipo = fm_get(fm, "tipo_segmento")
        row = f"| {fecha} | {titulo} | {emp} | {tipo} | {clase} | {estado} | {veces} | [→]({path.name}) |"
    return fecha, row


def insert(index_path, fecha, row, fname):
    lines = index_path.read_text().split("\n")
    row_re = re.compile(r"^\| (\d{4}-[\dX]{2}-[\dX]{2}) \|")
    idxs = [i for i, ln in enumerate(lines) if row_re.match(ln)]
    # update si ya existe fila para este archivo
    for i in idxs:
        if f"({fname})" in lines[i]:
            lines[i] = row
            index_path.write_text("\n".join(lines))
            return "actualizada"
    pos = None
    for i in idxs:
        if row_re.match(lines[i]).group(1) <= fecha:
            pos = i
            break
    if pos is None:
        pos = (idxs[-1] + 1) if idxs else len(lines)
    lines.insert(pos, row)
    index_path.write_text("\n".join(lines))
    return "insertada"


def remove(index_path, fname):
    lines = index_path.read_text().split("\n")
    keep = [ln for ln in lines if f"({fname})" not in ln]
    if len(keep) == len(lines):
        return "sin fila"
    index_path.write_text("\n".join(keep))
    return "retirada"


args = sys.argv[1:]
rm_mode = args and args[0] == "--rm"
if rm_mode:
    args = args[1:]

for arg in args:
    p = (ROOT / arg).resolve() if not Path(arg).is_absolute() else Path(arg)
    index = p.parent / "index.md"
    if rm_mode:
        result = remove(index, p.name)
        print(f"{result}: {p.name} <- {index.relative_to(ROOT)}")
        continue
    if not p.exists():
        sys.exit(f"no existe: {arg}")
    fecha, row = build_row(p)
    result = insert(index, fecha, row, p.name)
    print(f"{result}: {p.name} -> {index.relative_to(ROOT)}")
