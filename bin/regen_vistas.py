#!/usr/bin/env python3
"""Regenera las tres vistas derivadas del archivo, determinísticamente.

  archive/topics/lista-personal-maestra-indice.md
  archive/topics/luchadores-conteo-personal.md
  archive/topics/eventos-watch-list-vehemiurgo.md

Doctrina (CLAUDE.md §5): "generadas, no se editan a mano; se regeneran
al cierre de toda sesión que agregue fichas". Este script reemplaza al
sub-agente LLM: mismo contrato de cada vista, derivación mecánica.

Decisiones explícitas:
  - El texto de cada entrada se muestra cuasi-verbatim PERO con los
    nombres normalizados al canon (contrato declarado de las vistas;
    preserva mayúsculas del original).
  - La maestra y la watch-list son fieles a la fuente: bullets
    duplicados del notebook generan filas duplicadas.
  - El conteo deduplica bullets idénticos (misma fecha + mismo texto
    normalizado): un dictado repetido no es una segunda vista.
    Revertir con --contar-duplicados.
  - En el conteo, solo se cuentan nombres que el archivo conoce
    (fichas de people/, promotions/ y canónicos del registro); la
    cobertura se reporta en la vista.
  - Las secciones curadas del conteo ("Lectura editorial",
    "Resoluciones aplicadas...") se preservan del archivo anterior.

Uso:
  python3 bin/regen_vistas.py            # escribe las tres vistas
  python3 bin/regen_vistas.py --fecha 2026-08-22   # sella otra fecha
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import archivo_lib as al

HOY = "2026-08-22"
if "--fecha" in sys.argv:
    HOY = sys.argv[sys.argv.index("--fecha") + 1]
CONTAR_DUP = "--contar-duplicados" in sys.argv

T_MAESTRA = al.ROOT / "archive/topics/lista-personal-maestra-indice.md"
T_CONTEO = al.ROOT / "archive/topics/luchadores-conteo-personal.md"
T_WATCH = al.ROOT / "archive/topics/eventos-watch-list-vehemiurgo.md"

EMPRESAS = ("WWE", "AEW", "TNA", "NJPW", "AAA", "CMLL", "ROH", "NWA",
            "WCW", "WWF", "STARDOM", "GCW", "CZW", "MLW", "TJPW", "DDT")

BANNER = ("> **VISTA GENERADA — no editar a mano.** Regenerar con "
          "`python3 bin/regen_vistas.py` tras integrar fichas. "
          f"Última regeneración: {HOY}.")


# ── canonización de texto visible ────────────────────────────────

def _canonizer():
    pares = sorted(al.load_variantes(), key=lambda p: -len(p[0]))
    out = []
    for var, canon in pares:
        rx = re.compile(rf"(?<![\w]){re.escape(var)}(?![\w])", re.IGNORECASE)
        out.append((rx, var, canon))
    return out


CANON = _canonizer()


def canonize(text):
    """Variantes prohibidas → canónico, preservando ALL-CAPS."""
    for rx, var, canon in CANON:
        def rep(m, canon=canon):
            return canon.upper() if m.group(0).isupper() else canon
        text = rx.sub(rep, text)
    return text


# ── datos base ───────────────────────────────────────────────────

BULLETS = al.lista_bullets()
FICHAS = {f.path.name: f for f in al.iter_fichas()}


def bullet_fecha(b):
    """Fecha completa, o placeholder XX para parciales, o ''.
    Busca en el texto del bullet (no en el raw: el link de un bullet
    marcado contiene años que contaminarían el fallback)."""
    if b.fecha:
        return b.fecha
    t = b.texto
    m = re.search(r"(\d{2})\.(\d{4})", t)
    if m:
        return f"{m.group(2)}-{m.group(1)}-XX"
    m = re.search(r"\b(19[5-9]\d|20[0-2]\d)\b", t)
    if m:
        return f"{m.group(1)}-XX-XX"
    return ""


def bullet_empresa(texto):
    up = texto.upper()
    for e in EMPRESAS:
        if re.search(rf"\b{e}\b", up):
            return e
    return ""


def bullet_show(texto):
    """Etiqueta de show: texto entre la última empresa y la fecha."""
    up = texto.upper()
    dm = re.search(r"\d{2}\.\d{2}\.\d{4}", texto)
    corte = dm.start() if dm else len(texto)
    best = None
    for e in EMPRESAS:
        for m in re.finditer(rf"\b{e}\b", up[:corte]):
            if best is None or m.end() > best[1]:
                best = (e, m.end())
    if best:
        label = texto[best[1]:corte].strip(" —-·,")
        return label if label else best[0]
    palabras = texto[:corte].strip().split()
    return " ".join(palabras[-3:]) if palabras else "?"


ROWS = []  # (fecha, tipo, texto_canon, empresa, ficha|None, bullet)
for b in BULLETS:
    ficha = FICHAS.get(b.link.split("/")[-1]) if b.link else None
    # la ficha linkeada es la autoridad de fecha; el texto del bullet
    # es fallback (con placeholder XX para fechas parciales)
    fecha = b.fecha or (ficha.fecha if ficha else bullet_fecha(b))
    tipo = al.bullet_tipo(b.texto) or "match"
    ROWS.append((fecha, tipo, canonize(b.texto), bullet_empresa(b.texto), ficha, b))

# orden: cronológico moderno primero; sin fecha al final; estable
ROWS.sort(key=lambda r: (r[0] == "", r[0]), reverse=False)
ROWS.sort(key=lambda r: r[0], reverse=True)
ROWS = [r for r in ROWS if r[0]] + [r for r in ROWS if not r[0]]

integrados = sum(1 for r in ROWS if r[5].marked)
pendientes = len(ROWS) - integrados
n_matches = sum(1 for f in FICHAS.values() if f.kind == "matches")
n_segments = len(FICHAS) - n_matches


# ── vista 1: maestra ─────────────────────────────────────────────

def gen_maestra():
    filas = []
    for i, (fecha, tipo, texto, emp, ficha, b) in enumerate(ROWS, 1):
        if ficha:
            kind_lbl = {"matches": "match", "segments": "segment"}[ficha.kind]
            filas.append(f"| {i} | {fecha or '—'} | {kind_lbl} | {texto} | "
                         f"{emp or ficha.empresa} | {ficha.clase_abbr} | integrado | "
                         f"[→](../{ficha.kind}/{ficha.path.name}) |")
        else:
            filas.append(f"| {i} | {fecha or '—'} | {tipo} | {texto} | {emp} |  | pendiente |  |")
    linkeadas = sum(1 for r in ROWS if r[4])
    return f"""---
topic: "Lista personal maestra del Vehemiurgo — índice operativo"
slug: lista-personal-maestra-indice
tipo: topic
categoria: indice-operativo
estado: vivo
ultima_actualizacion: {HOY}
fuentes_principales:
  - "Lista personal verbatim: notebook/2026-05-09-2-lista-personal-completa.md"
  - "Índices de archivo: archive/matches/index.md + archive/segments/index.md"
  - "Registro canónico: glossary/nombres-canonicos.md"
  - "Generador: bin/regen_vistas.py"
tags: [lista-personal-maestra, indice-operativo, integracion-pendiente, ranking-fuente, watch-list-fuente]
---

{BANNER}

# Lista personal maestra del Vehemiurgo — índice operativo

Este archivo es el **índice tabulado** de la lista personal maestra del
Vehemiurgo. La lista verbatim vive en
[`../../notebook/2026-05-09-2-lista-personal-completa.md`](../../notebook/2026-05-09-2-lista-personal-completa.md)
— ese archivo es **sagrado y no se reescribe**. Este índice es la vista
reescribible: parsing posicional, normalización de nombres al canon
(`../../glossary/nombres-canonicos.md`), cruce con los indexes de
`archive/matches/` y `archive/segments/`.

**Conteo actual ({HOY})**: **{len(ROWS)} entradas** en la lista verbatim —
**{integrados} integradas** (con marca `(✓)` y ficha) · **{pendientes} pendientes**.
El archive tiene **{len(FICHAS)} fichas individuales** ({n_matches} matches +
{n_segments} segments); {linkeadas} de ellas están linkeadas 1-a-1 desde bullets
`(✓)` — el resto son piezas abiertas sin bullet propio (centerpieces de
cluster, drops mid-sesión, dossiers).

Orden: **cronológico moderno primero** (2026 arriba, décadas viejas
abajo), tal como solicitó el Vehemiurgo.

| # | Fecha | Tipo | Participantes / Entrada | Empresa | Clase | Estado | Ficha |
|---|---|---|---|---|---|---|---|
{chr(10).join(filas)}

---

## Leyenda

- **Tipo**: `match` si el bullet dice *"X VS Y"* (y no trae keyword de
  segmento); `segment` si trae keyword (PROMO, SEGMENT, RETURN, VIDEO,
  PACKAGE, IN-RING, BACKSTAGE) — la keyword gana sobre el "VS"
  (*"X VS Y PROMO VIDEO"* es segment). Ambiguos defaultean a `match`.
- **Entrada**: texto del bullet cuasi-verbatim, con nombres
  normalizados al canon. El verbatim con typos vive solo en el
  notebook.
- **Estado**: `integrado` = el bullet tiene marca `(✓)` y link a
  ficha; `pendiente` = todavía sin ficha propia.
- **Fechas parciales**: mes-año o solo año reciben placeholder `XX`.

## Limitaciones del parseo

- **Duplicados de la fuente**: bullets repetidos en la lista generan
  filas repetidas. Fiel a la fuente.
- **Empresa**: derivada por keyword ({", ".join(EMPRESAS[:8])}…);
  entradas sin keyword quedan con la celda vacía.
- Generado por `bin/regen_vistas.py` — reportar cualquier deriva de
  contrato como bug del generador, no editar la tabla a mano.
"""


# ── vista 2: conteo por presencia ────────────────────────────────

def _gazetteer():
    """nombre canónico → (slug de ficha o '', norm(nombre))."""
    gaz = {}
    for sub in ("people", "promotions"):
        for f in (al.ROOT / "archive" / sub).glob("*.md"):
            if f.name in ("index.md", "README.md"):
                continue
            fm = al.parse_fm(f.read_text())
            nombre = fm.get("nombre")
            if isinstance(nombre, str) and nombre:
                gaz.setdefault(nombre, (f"{sub}/{f.stem}", al.norm(nombre).strip()))
    for _, canon in al.load_variantes():
        gaz.setdefault(canon, ("", al.norm(canon).strip()))
    return gaz


def gen_conteo(viejo_texto):
    gaz = _gazetteer()
    rxs = [(nombre, slug, re.compile(rf"\b{re.escape(n)}\b"))
           for nombre, (slug, n) in gaz.items() if n]
    panteon = al.panteon_slugs()

    vistos = set()
    conteo = {}   # nombre → [total, integrados]
    con_nombre = 0
    for fecha, tipo, texto, emp, ficha, b in ROWS:
        key = (fecha, al.norm(texto).strip())
        if not CONTAR_DUP and key in vistos:
            continue
        vistos.add(key)
        ntexto = al.norm(texto)
        hit = False
        for nombre, slug, rx in rxs:
            if rx.search(ntexto):
                hit = True
                c = conteo.setdefault(nombre, [0, 0])
                c[0] += 1
                if b.marked:
                    c[1] += 1
        if hit:
            con_nombre += 1

    def nota(nombre):
        slug = gaz[nombre][0]
        partes = []
        if slug.startswith("people/") and slug.split("/")[1] in panteon:
            partes.append("**panteón** ([→](./heroes-fundamentales-vehemiurgia.md))")
        if slug:
            partes.append(f"ficha [→](../{slug}.md)")
        return "; ".join(partes)

    ranking = sorted(conteo.items(), key=lambda kv: (-kv[1][0], kv[0]))
    filas_top, filas_cola = [], []
    dos, uno = [], []
    for i, (nombre, (tot, integ)) in enumerate(ranking, 1):
        if tot == 2:
            dos.append(nombre)
            continue
        if tot == 1:
            uno.append(nombre)
            continue
        fila = f"| {i} | {nombre} | {tot} | {integ} | {tot - integ} | {nota(nombre)} |"
        (filas_top if i <= 50 else filas_cola).append(fila)

    # secciones curadas preservadas del archivo anterior, con nota de
    # procedencia para que no contradigan a la tabla vigente
    curadas = ""
    m = re.search(r"(## Lectura editorial.*?)(?=## Limitaciones del parseo|\Z)",
                  viejo_texto, re.S)
    if m:
        curadas = m.group(1).rstrip() + "\n\n"
        nota = ("\n\n> *(Secciones curadas por el Vehemiurgo, preservadas "
                "verbatim entre regeneraciones; los números que citan "
                "corresponden al snapshot en que se escribieron — la tabla "
                "vigente de arriba manda.)*\n")
        if "Secciones curadas por el Vehemiurgo" not in curadas:
            curadas = re.sub(r"(## Lectura editorial[^\n]*\n)", r"\1" + nota,
                             curadas, count=1)

    total_uni = len(vistos)
    return f"""---
topic: "Luchadores en la lista personal — conteo por presencia"
slug: luchadores-conteo-personal
tipo: topic
categoria: ranking-presencia
estado: vivo
ultima_actualizacion: {HOY}
fuentes_principales:
  - "Lista personal verbatim: notebook/2026-05-09-2-lista-personal-completa.md"
  - "Registro canónico: glossary/nombres-canonicos.md"
  - "Panteón SoT: archive/topics/heroes-fundamentales-vehemiurgia.md"
  - "Generador: bin/regen_vistas.py"
tags: [ranking-presencia, luchadores, lista-personal-maestra, conteo-editorial]
---

{BANNER}

# Luchadores en la lista personal — conteo por presencia

> **Aclaración doctrinal**. Este conteo **NO es ranking de calidad**, ni
> work-rate, ni *star rating*. Es ranking de **presencia en la lista
> personal del Vehemiurgo** — qué tantas veces un talent aparece
> documentado en el archivo personal del historiador. Eso ya es, por sí
> mismo, **una declaración de peso editorial**: la lista no es enciclopedia,
> es selección curada. Aparecer mucho significa que el Vehemiurgo
> *vuelve compulsivamente* a ese talent.

Conteo: cada nombre reconocido en cada entrada suma 1. Un tag a 4 suma
4 individuales. La métrica honra la doctrina old-school de que **cada
nombre en el cartel importa**. Los **segmentos también cuentan**.

**Snapshot {HOY}**: {total_uni} entradas contadas
({len(ROWS)} bullets{'' if CONTAR_DUP else ', duplicados exactos deduplicados'}) ·
{con_nombre} con ≥1 nombre reconocido ·
{len(conteo)} talents/entidades distintos.
Se cuentan los nombres que el archivo conoce (fichas de `people/` y
`promotions/` + canónicos del registro), normalizados al canon
**antes** de contar; el verbatim con typos vive solo en el notebook.

## Top 50

| # | Luchador | Total | Integrados | Pendientes | Notas |
|---|---|---|---|---|---|
{chr(10).join(filas_top)}

## Cola — 3+ menciones (fuera del top 50)

| # | Luchador | Total | Integrados | Pendientes | Notas |
|---|---|---|---|---|---|
{chr(10).join(filas_cola)}

## Cola larga — 2 menciones ({len(dos)} talents)

{", ".join(dos)}.

## Cola larga — 1 mención ({len(uno)} talents)

{", ".join(uno)}.

{curadas}## Limitaciones del parseo

- **Cobertura por gazetteer**: solo cuentan nombres con ficha o
  canónico registrado. Un talent mencionado en la lista pero sin
  ficha ni entrada en el registro no aparece — abrirle ficha lo
  incorpora en la próxima regeneración.
- **Duplicados del notebook**: bullets idénticos (misma fecha + mismo
  texto) cuentan una vez; `--contar-duplicados` revierte la decisión.
- Generado por `bin/regen_vistas.py`.
"""


# ── vista 3: watch-list ──────────────────────────────────────────

def gen_watch():
    pend = [r for r in ROWS if not r[5].marked]
    grupos = {}
    for r in pend:
        fecha, tipo, texto, emp, ficha, b = r
        show = canonize(bullet_show(b.texto))
        grupos.setdefault((fecha, show), []).append(r)

    eventos = {k: v for k, v in grupos.items() if len(v) >= 3 and k[0]}
    sueltos = [r for k, v in grupos.items() if k not in eventos for r in v]
    sueltos.sort(key=lambda r: r[0], reverse=True)
    n_agrupadas = sum(len(v) for v in eventos.values())

    bloques = []
    for (fecha, show), rs in sorted(eventos.items(), key=lambda kv: kv[0][0], reverse=True):
        bloques.append(f"### {fecha} — {show} ({len(rs)} entradas)\n")
        for _, tipo, texto, _, _, _ in rs:
            bloques.append(f"- *{tipo}* — {texto}")
        bloques.append("")

    lineas_sueltos = [f"- {r[0] or 's/f'} · *{r[1]}* — {r[2]}" for r in sueltos]

    return f"""---
topic: "Eventos / shows pendientes de ver — watch-list del Vehemiurgo"
slug: eventos-watch-list-vehemiurgo
tipo: topic
categoria: watch-list
estado: vivo
ultima_actualizacion: {HOY}
fuentes_principales:
  - "Lista personal verbatim: notebook/2026-05-09-2-lista-personal-completa.md"
  - "Derivado de archive/topics/lista-personal-maestra-indice.md"
  - "Generador: bin/regen_vistas.py"
tags: [watch-list, pendientes, lista-personal-maestra, eventos-cluster]
---

{BANNER}

# Eventos / shows pendientes de ver — watch-list del Vehemiurgo

Esta es la **watch-list operativa**: entradas de la lista personal
maestra que **todavía no tienen marca `(✓)` ni ficha individual** en
`archive/matches/` o `archive/segments/`. Agrupadas por evento cuando
3+ bullets corresponden al mismo show (típicamente PPV o programa con
cobertura densa); el resto va como matches/segments sueltos.

**Conteo actual ({HOY})**: **{len(pend)} entradas pendientes** —
**{len(eventos)} eventos agrupados** ({n_agrupadas} entradas) +
**{len(sueltos)} sueltos**. Todo lo que ya tiene ficha fue
removido de esta vista.

Orden: **cronológico moderno primero** (2026 arriba, décadas viejas
abajo).

---

## Eventos completos pendientes (3+ entradas)

Cada bloque agrupa entries del mismo show. Tomar nota: muchos
programas semanales (Raw, SmackDown, NXT, Dynamite, Impact) tienen
cobertura match-y-segment densa — ese es el patrón Vehemiurgia
ortodoxo (booking + segmentos + matches como liturgia completa).

{chr(10).join(bloques)}
## Matches / segments sueltos pendientes

{chr(10).join(lineas_sueltos)}

## Notas operativas

- **Texto cuasi-verbatim**: las entradas se muestran como fueron
  dictadas, con los nombres normalizados al canon
  (`../../glossary/nombres-canonicos.md`). El verbatim con typos vive
  solo en el notebook.
- **Show**: derivado del texto del bullet (empresa por keyword + lo
  que sigue hasta la fecha); bullets sin fecha o sin grupo de 3+ van
  a sueltos.
- Generado por `bin/regen_vistas.py`.
"""


# ── main ─────────────────────────────────────────────────────────

viejo_conteo = T_CONTEO.read_text() if T_CONTEO.exists() else ""
for path, contenido in ((T_MAESTRA, gen_maestra()),
                        (T_CONTEO, gen_conteo(viejo_conteo)),
                        (T_WATCH, gen_watch())):
    path.write_text(contenido)
    print(f"regenerada: {path.relative_to(al.ROOT)} ({len(contenido.splitlines())} líneas)")
