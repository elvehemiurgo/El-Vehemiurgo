#!/usr/bin/env python3
"""Renombrador de mediateca — El Vehemiurgo (satélite LOCAL).

Aplica una tabla de renombrado de una guía `vehemiurgia/` sobre los
archivos reales de una carpeta. Formato de destino:
`YYYY MM DD Nombre del Show` + la extensión original (doctrina
CLAUDE.md §4 / vehemiurgia/README.md).

REGLAS DURAS
  - Dry-run por defecto. Renombra SOLO con --aplicar.
  - Nunca borra, nunca sobrescribe, nunca toca subcarpetas salvo
    --recursivo.
  - Lo que no matchea sin ambigüedad NO se renombra: se reporta.

Uso:
    python3 renombrar.py --carpeta "D:\\VEHEWRES\\ECW 1997" \
        --mapa mapas/ecw-hardcore-tv-1997.tsv \
        --mapa mapas/ecw-supercards-y-ppv-1997.tsv
    # ...revisar el informe, y recién entonces:
    python3 renombrar.py ... --aplicar
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from collections import defaultdict

EXT_VIDEO = {".mp4", ".mkv", ".avi", ".m4v", ".mpg", ".mpeg", ".wmv",
             ".mov", ".ts", ".flv", ".divx", ".ogm", ".rmvb", ".webm"}

RE_ISO = re.compile(r"\b((?:19|20)\d{2})[-_. ]?(0[1-9]|1[0-2])[-_. ]?(0[1-9]|[12]\d|3[01])\b")
RE_NUM_SLASH = re.compile(r"\b(\d{1,2})[-_./](\d{1,2})[-_./]((?:19|20)?\d{2})\b")
RE_MARCA_TV = re.compile(r"hardcore\s*tv|hctv", re.IGNORECASE)
RE_EP_ETIQUETA = re.compile(
    r"(?:hardcore\s*tv|hctv|ecwhctv|episodio|episode|\bep\b|#)\s*[-_. ]*(\d{2,4})",
    re.IGNORECASE)


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s.replace("_", " ").replace(".", " ")).strip().lower()


class Fila:
    __slots__ = ("numero", "nombre", "emision", "taping", "nota", "mapa",
                 "es_tv", "titulo", "excluida")

    def __init__(self, numero, nombre, emision, taping, nota, mapa):
        self.numero = int(numero) if str(numero).strip() else None
        self.nombre = nombre.strip()
        self.excluida = self.nombre.startswith("!")
        if self.excluida:
            self.nombre = self.nombre[1:].strip()
        self.es_tv = "hardcore tv" in norm(self.nombre)
        self.titulo = norm(re.sub(r"^\d{4} \d{2} \d{2} ", "", self.nombre))
        self.emision = emision.strip()
        self.taping = taping.strip()
        self.nota = nota.strip()
        self.mapa = mapa


def leer_mapa(ruta):
    filas, encabezado_visto = [], False
    with open(ruta, encoding="utf-8") as fh:
        for linea in fh:
            linea = linea.rstrip("\n")
            if not linea.strip() or linea.lstrip().startswith("#"):
                continue
            campos = linea.split("\t")
            if not encabezado_visto:
                encabezado_visto = True
                if campos[0].strip().lower() == "numero":
                    continue
            campos += [""] * (5 - len(campos))
            filas.append(Fila(campos[0], campos[1], campos[2], campos[3],
                              campos[4], os.path.basename(ruta)))
    return filas


def fechas_en(nombre):
    """Devuelve (set de fechas ISO halladas, texto con las fechas borradas)."""
    hallazgos, restante = set(), nombre
    for m in RE_ISO.finditer(nombre):
        hallazgos.add(f"{m.group(1)}-{m.group(2)}-{m.group(3)}")
        restante = restante.replace(m.group(0), " ")
    for m in RE_NUM_SLASH.finditer(restante):
        a, b, c = int(m.group(1)), int(m.group(2)), m.group(3)
        anio = int(c) if len(c) == 4 else (1900 + int(c) if int(c) >= 70 else 2000 + int(c))
        cands = []
        if a > 12 and b <= 12:            # dd/mm
            cands = [(b, a)]
        elif b > 12 and a <= 12:          # mm/dd
            cands = [(a, b)]
        elif a <= 12 and b <= 12:         # ambiguo: las dos lecturas
            cands = [(a, b), (b, a)]
        for mes, dia in cands:
            try:
                hallazgos.add(f"{anio:04d}-{mes:02d}-{dia:02d}")
            except ValueError:
                pass
        restante = restante.replace(m.group(0), " ")
    return hallazgos, restante


def numeros_en(nombre, restante, validos):
    nums = set()
    for m in RE_EP_ETIQUETA.finditer(nombre):
        n = int(m.group(1))
        if n in validos:
            nums.add(n)
    if not nums:
        for m in re.finditer(r"(?<!\d)(\d{2,4})(?!\d)", restante):
            n = int(m.group(1))
            if n in validos:
                nums.add(n)
    return nums


def resolver(archivo, filas, por_numero, por_emision, por_taping, validos):
    base, _ = os.path.splitext(archivo)
    fechas, restante = fechas_en(base)
    nums = numeros_en(base, restante, validos)
    nbase = norm(base)
    marca_tv = bool(RE_MARCA_TV.search(base))

    def serie_ok(f):
        # Un archivo que se anuncia como Hardcore TV no puede ser una
        # supercard, por mucho que comparta la fecha del taping.
        if f.excluida:
            return True
        return f.es_tv if marca_tv else True

    # Evidencia por titulo: SOLO para filas sin nº (PPVs, supercards) y
    # para las filas de corpus ajeno. Los programas de TV se identifican
    # por nº — si no, "ECW Hardcore TV 199" matchea dentro de "...1997...".
    por_titulo = {f for f in filas
                  if f.titulo and (f.numero is None or f.excluida)
                  and f.titulo in nbase and serie_ok(f)}

    # Corpus ajeno declarado en el mapa (filas con "!"): cortar aca.
    for f in por_titulo:
        if f.excluida:
            return None, "FUERA DE CORPUS", f.nota or "no pertenece a este corpus"

    cands, via = set(), []
    if len(nums) == 1:
        n = next(iter(nums))
        if n in por_numero:
            cands = {f for f in por_numero[n] if serie_ok(f)}
            via.append(f"nº {n}")
    elif len(nums) > 1:
        return None, "AMBIGUO", f"el nombre trae varios nº de programa: {sorted(nums)}"

    em = {f for d in fechas for f in por_emision.get(d, []) if serie_ok(f)}
    tp = {f for d in fechas for f in por_taping.get(d, []) if serie_ok(f)}

    if cands:
        # El nº manda. La fecha solo corrobora — muchos rips vienen
        # fechados por taping, o con el dia y el mes dados vuelta.
        todas = em | tp
        if todas and not (cands & todas):
            return (None, "AMBIGUO",
                    f"el nº y la fecha apuntan a programas distintos "
                    f"({sorted(x.nombre for x in cands)} vs "
                    f"{sorted(x.nombre for x in todas)})")
        cruce = (cands & todas) if todas else cands
        if todas:
            via.append("fecha de emisión" if cands & em else "fecha de taping")
    elif em or tp:
        cruce = em if em else tp
        via.append("fecha de emisión" if em else "fecha de taping")
        if por_titulo and por_titulo & cruce:
            cruce = por_titulo & cruce
            via.append("título")
    elif por_titulo:
        cruce = por_titulo
        via.append("título")
    else:
        return None, "SIN MATCH", "ni nº de programa, ni fecha, ni título reconocibles"

    if len(cruce) > 1:
        etiquetas = sorted(x.nombre for x in cruce)
        return (None, "AMBIGUO",
                f"la fecha de taping la comparten {len(etiquetas)} programas "
                f"({', '.join(etiquetas)}) — hace falta el nº de programa")
    return next(iter(cruce)), "OK", " + ".join(via)


def main():
    ap = argparse.ArgumentParser(description="Renombrador de mediateca VEHEMIURGIA")
    ap.add_argument("--carpeta", required=True)
    ap.add_argument("--mapa", action="append", required=True)
    ap.add_argument("--aplicar", action="store_true", help="ejecuta el renombrado (por defecto: dry-run)")
    ap.add_argument("--recursivo", action="store_true")
    ap.add_argument("--informe", help="ruta de un .md donde volcar el informe")
    ap.add_argument("--todas-las-extensiones", action="store_true")
    args = ap.parse_args()

    filas = []
    for m in args.mapa:
        filas += leer_mapa(m)
    if not filas:
        print("mapa vacío", file=sys.stderr)
        return 2

    por_numero, por_emision, por_taping = defaultdict(list), defaultdict(list), defaultdict(list)
    for f in filas:
        if f.excluida:
            continue
        if f.numero is not None:
            por_numero[f.numero].append(f)
        if f.emision:
            por_emision[f.emision].append(f)
        if f.taping:
            por_taping[f.taping].append(f)
    validos = set(por_numero)

    if not os.path.isdir(args.carpeta):
        print(f"no existe la carpeta: {args.carpeta}", file=sys.stderr)
        return 2

    archivos = []
    for raiz, _dirs, nombres in os.walk(args.carpeta):
        for n in sorted(nombres):
            ext = os.path.splitext(n)[1].lower()
            if args.todas_las_extensiones or ext in EXT_VIDEO:
                archivos.append(os.path.join(raiz, n))
        if not args.recursivo:
            break

    listos, renombrar, problemas = [], [], []
    vistos = set()
    for ruta in archivos:
        nombre = os.path.basename(ruta)
        base, ext = os.path.splitext(nombre)
        fila, estado, detalle = resolver(nombre, filas, por_numero, por_emision,
                                         por_taping, validos)
        if estado != "OK":
            problemas.append((nombre, estado, detalle))
            continue
        destino = fila.nombre + ext
        if norm(base) == norm(fila.nombre):
            listos.append((nombre, fila))
            continue
        ruta_destino = os.path.join(os.path.dirname(ruta), destino)
        if destino.lower() in vistos:
            problemas.append((nombre, "CONFLICTO",
                              f"otro archivo ya reclama «{destino}»"))
            continue
        if os.path.exists(ruta_destino):
            problemas.append((nombre, "CONFLICTO",
                              f"«{destino}» ya existe en la carpeta"))
            continue
        vistos.add(destino.lower())
        renombrar.append((ruta, ruta_destino, nombre, destino, detalle, fila))

    lineas = []
    def p(s=""):
        print(s)
        lineas.append(s)

    p(f"# Renombrado — {args.carpeta}")
    p()
    p(f"Archivos leídos: **{len(archivos)}** · ya correctos: **{len(listos)}** · "
      f"a renombrar: **{len(renombrar)}** · sin resolver: **{len(problemas)}**")
    p(f"Modo: **{'APLICAR' if args.aplicar else 'dry-run (no se toca nada)'}**")
    p()
    if renombrar:
        p("## A renombrar")
        p()
        p("| Archivo actual | Nombre canónico | Matcheado por |")
        p("|---|---|---|")
        for _o, _d, viejo, nuevo, detalle, _f in renombrar:
            p(f"| `{viejo}` | `{nuevo}` | {detalle} |")
        p()
    if problemas:
        p("## Sin resolver — requieren ojo humano")
        p()
        p("| Archivo | Estado | Por qué |")
        p("|---|---|---|")
        for nombre, estado, detalle in problemas:
            p(f"| `{nombre}` | **{estado}** | {detalle} |")
        p()
    esperados = {f.nombre for f in filas if not f.excluida}
    cubiertos = {f.nombre for _o, _d, _v, _n, _de, f in renombrar} | {f.nombre for _n, f in listos}
    faltantes = esperados - cubiertos
    if faltantes:
        p(f"## Faltan en la carpeta ({len(faltantes)})")
        p()
        por_mapa = defaultdict(list)
        for f in filas:
            if f.nombre in faltantes and not f.excluida:
                por_mapa[f.mapa].append(f.nombre)
        for mapa in sorted(por_mapa):
            p(f"**{mapa}** ({len(por_mapa[mapa])})")
            p()
            for n in sorted(set(por_mapa[mapa])):
                p(f"- `{n}`")
            p()

    if args.aplicar:
        hechos = 0
        for origen, destino, viejo, nuevo, _d, _f in renombrar:
            try:
                os.rename(origen, destino)
                hechos += 1
            except OSError as e:
                p(f"ERROR al renombrar `{viejo}` → `{nuevo}`: {e}")
        p(f"**Renombrados: {hechos}/{len(renombrar)}**")
    elif renombrar:
        p("_Dry-run: no se tocó ningún archivo. Volvé a correr con `--aplicar` cuando el mapeo esté bien._")

    if args.informe:
        with open(args.informe, "w", encoding="utf-8") as fh:
            fh.write("\n".join(lineas) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
