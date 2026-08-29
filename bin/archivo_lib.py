#!/usr/bin/env python3
"""Núcleo compartido del archivo El Vehemiurgo.

Un solo lugar para el conocimiento que antes vivía cuadruplicado:
  - parsing de frontmatter (escalares con comillas escapadas,
    comentarios inline, listas inline y en bloque)
  - corpus de fichas (matches + segments) como objetos
  - registro de nombres canónicos (tabla "Variantes prohibidas",
    con mapeo posicional token-a-token)
  - bullets de la lista personal (scoped a "## La lista")
  - clasificación de tipo de bullet (segment-keyword gana sobre "VS":
    "X VS Y PROMO VIDEO" es un segment)

Consumidores: lint_archivo.py, reconciliar_lista.py, regen_vistas.py.
"""
import re
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LISTA = ROOT / "notebook/2026-05-09-2-lista-personal-completa.md"
REGISTRO = ROOT / "glossary/nombres-canonicos.md"
PANTEON = ROOT / "archive/topics/heroes-fundamentales-vehemiurgia.md"

# WE+ es un ESCALÓN por encima de Wrestling Entertainment, declarado por
# el Vehemiurgo el 2026-08-26 (s54): "segmentos simplemente demasiado
# buenos que definen el entertainment y el wrestling booking
# inteligente". No es una combinación — es una clase propia, y a
# diferencia de las coronas SÍ toca la jerarquía. Una pieza lleva
# `wrestling-entertainment` o `wrestling-entertainment-plus`, nunca las
# dos.
CLASES_OK = {"perfect-wrestling", "fighting-spirit", "wrestling-entertainment",
             "wrestling-entertainment-plus"}
ABBR = {"perfect-wrestling": "PW", "fighting-spirit": "FS",
        "wrestling-entertainment": "WE", "wrestling-entertainment-plus": "WE+"}

# Coronas: premios DERIVADOS de la combinación de clases (ley del
# Vehemiurgo 2026-08-26 s52 — "no hay que modificar la jerarquía, solo
# agregar premios"). Nunca viven en frontmatter: se calculan.
CORONAS = {
    frozenset({"fighting-spirit", "wrestling-entertainment"}): "FC",
    frozenset({"perfect-wrestling", "fighting-spirit",
               "wrestling-entertainment"}): "ICC",
}
CORONA_NOMBRE = {"FC": "Feeling Crown", "ICC": "Instant Classic Crown"}

# (Las equivalencias legacy tipo elias→elijah viven en el registro,
# sección "Equivalencias de matching" — ver load_equivalencias().)

SEG_KEYS = ("PROMO", "SEGMENT", "RETURN", "VIDEO", "PACKAGE", "IN-RING", "BACKSTAGE")

STOP = {"the", "and", "with", "match", "team", "title", "wwe", "aew", "tna",
        "nxt", "raw", "smackdown", "impact", "dynamite", "collision", "njpw",
        "roh", "wcw", "wwf", "cmll", "aaa", "stardom", "night", "week",
        "thursday", "monday", "live", "event", "house", "show", "ppv", "vs"}


# ── normalización ────────────────────────────────────────────────

def norm(s):
    """ascii + lowercase + solo [a-z0-9 ]."""
    s = unicodedata.normalize("NFD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9 ]", " ", s)


# ── frontmatter ──────────────────────────────────────────────────

def parse_fm(text):
    """Frontmatter → dict {clave: str | list[str]}.

    Soporta: escalar con comillas (respetando \\"), escalar sin comillas
    (cortando comentario inline), lista inline (["a", "b"]) y lista en
    bloque (- a). Devuelve {} si no hay frontmatter bien cerrado.
    """
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    out = {}
    lines = text[3:end].split("\n")
    i = 0
    while i < len(lines):
        m = re.match(r"^([A-Za-z_][\w]*):[ \t]*(.*)$", lines[i])
        if not m:
            i += 1
            continue
        key, rest = m.group(1), m.group(2).strip()
        if rest.startswith("["):
            # lista inline (puede continuar en líneas siguientes)
            buf = rest
            while "]" not in buf and i + 1 < len(lines):
                i += 1
                buf += " " + lines[i].strip()
            inner = buf[1:buf.rfind("]")] if "]" in buf else buf[1:]
            out[key] = re.findall(r'"([^"]+)"', inner) or \
                [t for t in re.findall(r"[^,\s\[\]]+", inner)]
        elif rest == "":
            # posible lista en bloque
            items = []
            while i + 1 < len(lines) and re.match(r"^[ \t]+-", lines[i + 1]):
                i += 1
                iv = re.sub(r"^[ \t]+-[ \t]*", "", lines[i]).strip()
                items.append(_unquote(iv))
            out[key] = items  # [] si era clave vacía sin bloque
        else:
            out[key] = _unquote(rest)
        i += 1
    return out


def _unquote(v):
    if v.startswith('"'):
        m = re.match(r'"((?:[^"\\]|\\.)*)"', v)
        return m.group(1).replace('\\"', '"') if m else ""
    return v.split("#")[0].strip()


# ── fichas ───────────────────────────────────────────────────────

@dataclass
class Ficha:
    path: Path
    kind: str            # "matches" | "segments"
    fecha: str
    titulo: str
    empresa: str
    programa: str
    tipo_segmento: str
    estado: str
    veces: str
    clases: list = field(default_factory=list)
    participantes: list = field(default_factory=list)

    @property
    def clase_abbr(self):
        return "·".join(ABBR.get(c, c) for c in self.clases) or "—"

    @property
    def corona(self):
        """Sigla de la corona que la combinación de clases otorga, o "—"."""
        return CORONAS.get(frozenset(self.clases), "—")

    @property
    def emp(self):
        return f"{self.empresa} / {self.programa}" if self.programa else self.empresa


def load_ficha(path):
    fm = parse_fm(path.read_text())
    if not fm:
        return None
    kind = path.parent.name
    lst = lambda k: fm.get(k) if isinstance(fm.get(k), list) else []
    scl = lambda k, d="": fm.get(k, d) if isinstance(fm.get(k, d), str) else d
    return Ficha(
        path=path, kind=kind,
        fecha=scl("fecha"),
        titulo=scl("match") if kind == "matches" else scl("segmento"),
        empresa=scl("empresa"), programa=scl("programa"),
        tipo_segmento=scl("tipo_segmento"),
        estado=scl("estado", "stub"),
        veces=scl("veces_visto_vehemiurgo", "0"),
        clases=lst("clases_vehemiurgo"),
        participantes=lst("participantes") or lst("protagonistas"),
    )


def iter_fichas(kinds=("matches", "segments")):
    for kind in kinds:
        for f in sorted((ROOT / "archive" / kind).glob("*.md")):
            if f.name in ("index.md", "README.md"):
                continue
            ficha = load_ficha(f)
            if ficha:
                yield ficha


# ── filas de índice ──────────────────────────────────────────────

ROW_RE = re.compile(r"^\| (\d{4}-[\dX]{2}-[\dX]{2}) \|")


def format_index_row(f):
    """La fila de índice de una Ficha — única definición del formato."""
    cell = lambda s: s.replace("|", "\\|")
    if f.kind == "matches":
        return (f"| {f.fecha} | {cell(f.titulo)} | {cell(f.emp)} | {f.clase_abbr} "
                f"| {f.corona} | {f.estado} | {f.veces} | [→]({f.path.name}) |")
    return (f"| {f.fecha} | {cell(f.titulo)} | {cell(f.emp)} | {cell(f.tipo_segmento)} "
            f"| {f.clase_abbr} | {f.corona} | {f.estado} | {f.veces} | [→]({f.path.name}) |")


# ── registro de nombres canónicos ────────────────────────────────

def load_variantes():
    """[(variante, canónico)] desde la tabla 'Variantes prohibidas'."""
    if not REGISTRO.exists():
        return []
    out, in_t = [], False
    for ln in REGISTRO.read_text().split("\n"):
        if ln.startswith("## Variantes prohibidas"):
            in_t = True
            continue
        if in_t and ln.startswith("## "):
            break
        m = re.match(r"\| ([^|]+) \| ([^|]+) \|", ln)
        if in_t and m and "Canónico" not in m.group(1):
            canon = m.group(1).strip()
            for v in m.group(2).split(","):
                out.append((v.strip(), canon))
    return out


def load_equivalencias():
    """token → token desde la tabla 'Equivalencias de matching' del
    registro: nombres legacy/de época que resuelven al canónico sin
    ser variantes prohibidas (no alimentan W2)."""
    if not REGISTRO.exists():
        return {}
    out, in_t = {}, False
    for ln in REGISTRO.read_text().split("\n"):
        if ln.startswith("## Equivalencias de matching"):
            in_t = True
            continue
        if in_t and ln.startswith("## "):
            break
        m = re.match(r"\| ([^|]+) \| ([^|]+) \|", ln)
        if in_t and m and "Token" not in m.group(1) and "---" not in m.group(1):
            out[norm(m.group(1)).strip()] = norm(m.group(2)).strip()
    return out


def token_map():
    """token de variante → token canónico, por posición.

    "Mickey James" vs "Mickie James" → mickey→mickie (posicional);
    la heurística vieja de "último token" derivaba mickey→james.
    Si los largos difieren, cae al último token del canónico.
    """
    vmap = {}
    for v, canon in load_variantes():
        vt, ct = norm(v).split(), norm(canon).split()
        if not ct:
            continue
        for i, tok in enumerate(vt):
            if tok in ct:
                continue
            vmap[tok] = ct[i] if i < len(vt) == len(ct) else ct[-1]
    vmap.update(load_equivalencias())
    return vmap


def tokens(s, vmap):
    """Tokens distintivos (≥4 chars, sin stopwords, canonizados)."""
    out = set()
    for t in norm(s).split():
        t = vmap.get(t, t)
        if len(t) >= 4 and t not in STOP and not t.isdigit():
            out.add(t)
    return out


# ── lista personal ───────────────────────────────────────────────

@dataclass
class Bullet:
    lineno: int          # 1-based
    raw: str             # línea completa verbatim
    fecha: str           # YYYY-MM-DD o ""
    marked: bool         # tiene (✓)
    link: str            # "matches/x.md" | "segments/x.md" | ""

    @property
    def texto(self):
        """Contenido del bullet sin el prefijo '- ' ni la marca."""
        t = self.raw[2:].strip()
        if self.marked:
            m = re.match(r"\(✓\)\s*\*\*(.+?)\*\*", t)
            if m:
                return m.group(1)
        return t


def lista_bullets():
    """Bullets de la sección '## La lista' del archivo maestro."""
    lines = LISTA.read_text().split("\n")
    start = next((i for i, l in enumerate(lines) if l.startswith("## La lista")), 0)
    end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
    out = []
    for i in range(start + 1, end):
        ln = lines[i]
        if not ln.startswith("- "):
            continue
        dm = re.search(r"(\d{2})\.(\d{2})\.(\d{4})", ln)
        fecha = f"{dm.group(3)}-{dm.group(2)}-{dm.group(1)}" if dm else ""
        lm = re.search(r"archive/(matches|segments)/([^)`\s]+\.md)", ln)
        out.append(Bullet(
            lineno=i + 1, raw=ln, fecha=fecha,
            marked=ln.startswith("- (✓)"),
            link=f"{lm.group(1)}/{lm.group(2)}" if lm else "",
        ))
    return out


def bullet_tipo(texto):
    """'segment' | 'match' | None. Keyword de segmento gana sobre 'VS':
    "SOL RUCA VS SARIA PROMO VIDEO" es un segment."""
    up = texto.upper()
    if any(k in up for k in SEG_KEYS):
        return "segment"
    if " VS " in up or " VS. " in up:
        return "match"
    return None


# ── panteón ──────────────────────────────────────────────────────

def panteon_slugs():
    """Slugs de people linkeados desde el SoT del panteón."""
    if not PANTEON.exists():
        return set()
    return set(re.findall(r"\(\.\./people/([^)]+)\.md\)", PANTEON.read_text()))
