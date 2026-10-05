# Informe — sesión hija `claude/barrido-hija-7`

Barrido de datos duros 2026-10, lotes 19, 20 y 21 (AEW, julio–septiembre
2026). Trabajo autónomo, sin preguntas al Vehemiurgo; ambigüedades
resueltas aplicando `research/barrido-2026-10/README.md`.

## Resumen

| Lote | Shows | Fichas en el lote | Fichas modificadas | Ítems de pendientes cerrados | Discrepancias |
|---|---|---|---|---|---|
| 19 | 8 (AEW, 8/7–12/8) | 33 | 14 | 14 | 1 |
| 20 | 7 (AEW, 15/8–2/9) | 37 | 5 | 5 | 1 |
| 21 | 5 (AEW, 5/9–26/9) | 25 | 4 | 4 | 0 |
| **Total** | **20** | **~95** | **23** | **23** | **2** |

Commits: `barrido datos duros lote 19/20/21`, uno por lote, push a
`claude/barrido-hija-7`. Lint (`bin/lint_archivo.py --pre-commit`): 0
errores en los tres commits.

## Método

Una o dos búsquedas WebSearch por show (card completa, resultados,
ciudad/recinto), reutilizadas para todas las fichas de esa fecha.
Presupuesto usado: ~25 WebSearch de las ~200 disponibles para la
sesión completa (compartidas con sub-agentes, que no fueron necesarios
dado el volumen manejable).

**Patrón detectado y adoptado a partir del lote 19**: el campo
`referee` prácticamente nunca se reporta en coberturas de TV de AEW
(Dynamite/Collision semanales) — solo aparece cuando hay un spot o
bump notable que lo hace parte de la nota (ej. un paro médico, una
distracción del árbitro). En PPVs (Redemption, Grand Slam Mexico, All
In, All Out) sí aparece ocasionalmente, generalmente en notas sobre el
réferi principal o en artículos post-show donde un luchador lo
menciona. Por esto, la tasa de resolución de `referee` es mucho más
baja que la de `ciudad`/`recinto`/`finish`/`ganador`, que casi siempre
están en el primer resultado de una búsqueda de resultados del show.

También se detectó un patrón de **alucinación de cifras redondas** en
la síntesis de WebSearch: duraciones como "9:00", "14:00", "17:00",
"20:00", "22:00" aparecían sin cita textual de respaldo y, al
contrastar con una segunda búsqueda, no se repetían o contradecían
cifras ya confirmadas con más precisión. Se descartaron como fuente
("nunca inventar" — tampoco se hereda la invención ajena) y **no se
usaron para llenar placeholders de `duracion`** salvo cuando venían
envueltas en una oración con cita de artículo reconocible (p. ej. "the
near 30-minute bout saw...") o coincidían con un segundo hallazgo
independiente.

## Discrepancias registradas

1. **Lote 19** — `archive/matches/2026-07-26-jay-juice-vs-finlay-connors-dog-collar-aew-redemption.md`:
   la ficha (nombre de archivo y `estipulacion`) registra la
   estipulación como **"dog collar match"**; múltiples coberturas
   (Wrestling Inc., Wrestleview, PWTorch, ProWrestling.net) la
   reportan como **"Double Chain Match" / "Tag Team Double Chain
   Match"**. El propio volcado verbatim del Vehemiurgo solo menciona
   "cadenas", no "dog collar" literalmente. No se renombró el archivo
   ni se tocó `estipulacion` (fuera del alcance de esta ley); se dejó
   anotado como pendiente de discrepancia.

2. **Lote 20** — `archive/matches/2026-08-15-lethal-twist-vs-page-bandido-brody-king-trios-aew-collision.md`:
   la ficha trae `duracion: "13:00"` (de research previo, s57);
   Sportskeeda reporta **9:46 (tiempo al aire)** para el mismo finish
   confirmado (piledriver de Brody King sobre Lee Johnson). No se
   reescribió `duracion` (no es placeholder en este lote); se anotó la
   discrepancia en Pendientes.

## Qué quedó sin cubrir, y por qué

- **`referee` en la inmensa mayoría de matches de TV semanal** (Dynamite
  y Collision): no reportado por ninguna cobertura accesible vía
  WebSearch. Patrón sistemático, no un vacío de búsqueda — se intentó
  en varios shows (7/30, 8/12, 8/15, 8/22, 9/9, 9/12, 9/16, 9/26) sin
  resultado. Ejemplos puntuales sí se resolvieron cuando hubo un spot
  con el árbitro como parte de la noticia (Beach Break 8/7 → Bryce
  Remsburg; All In: London 30/8 → Paul Turner, Aubrey Edwards, Rick
  Knox; All Out 26/9 → Bryce Remsburg, por el paro médico de Steven
  Borden).
- **`duracion` exacta al segundo** en varios matches de PPV (Fletcher
  vs Takeshita vs Okada, Omega vs Ospreay, Bandido vs Fletcher en
  Redemption, Persephone vs Maya World en el Buy In de All In, Trios
  Roulette Royale, Casino Gauntlet de MJF/Andrade): ninguna cobertura
  accesible da el segundo exacto; las fichas ya tenían aproximaciones
  de research previo (`~13:00`, `~34:00`, etc.) que se dejaron como
  están, sin inventar precisión falsa.
- **Duración de segmentos** (promos, videos de hype, backstage): como
  regla casi sin excepción, ninguna cobertura de prensa especializada
  reporta la duración de un segmento de TV — solo el timestamp dentro
  del show, que estas fichas ya registran en `ubicacion_en_show`. Tras
  confirmar el patrón en los primeros shows del lote 19, se dejó de
  gastar presupuesto de búsqueda en este campo específico para el
  resto de los tres lotes, salvo cuando la búsqueda del show ya en
  curso (por los matches) revelaba de paso ciudad/recinto del
  segmento, que sí se completó en esos casos.
- **Fichas ya cubiertas por research extenso de sesiones previas**
  (s57, s58, s01-s02 según notebook): varias — sobre todo en Grand Slam
  Mexico (5/8) y All In: London (30/8) — ya tenían casi todo cerrado
  salvo `referee`; el research de esta sesión no aportó más que lo que
  esas sesiones ya habían dejado, excepto los tres referees de All In
  mencionados arriba.

## Fichas modificadas por lote

**Lote 19** (14): `2026-07-08-mjf-vs-kenny-omega-aew-beach-break`,
`2026-07-15-andrade-vs-jake-doyle-aew-dynamite`,
`2026-07-15-komander-vs-kyle-fletcher-aew-dynamite`,
`2026-07-22-darby-allin-vs-kevin-knight-aew-dynamite`,
`2026-07-22-jay-white-vs-clark-connors-aew-dynamite`,
`2026-07-26-andrade-vs-mark-davis-aew-redemption`,
`2026-07-26-bandido-vs-kyle-fletcher-aew-redemption`,
`2026-07-26-jay-juice-vs-finlay-connors-dog-collar-aew-redemption`,
`2026-07-26-kevin-knight-vs-kenny-omega-aew-redemption`,
`2026-07-26-ladder-match-opener-aew-redemption`,
`2026-07-26-ospreay-moxley-vs-young-bucks-aew-redemption`, y los
segments `2026-07-26-guns-vs-dogs-promo-video`,
`2026-07-26-kevin-knight-vs-omega-promo-video`,
`2026-07-26-segmento-final-ospreay-dropea-mox-omega-tease` (todos
`-aew-redemption`).

**Lote 20** (5): `2026-08-15-lethal-twist-vs-page-bandido-brody-king-trios-aew-collision`,
`2026-08-19-jay-white-vs-jon-moxley-aew-dynamite`,
`2026-08-30-kenny-omega-vs-will-ospreay-world-title-aew-all-in`,
`2026-08-30-trios-roulette-royale-aew-all-in`,
`2026-08-30-young-bucks-vs-cage-cope-tag-titles-aew-all-in`.

**Lote 21** (4): `2026-09-12-andy-williams-battle-royal-aew-collision`,
`2026-09-26-fletcher-knight-vs-darby-borden-contender-aew-all-out`, y
los segments `2026-09-05-bang-bang-gang-backstage-aew-collision`,
`2026-09-05-promo-video-gabe-kidd-vs-andrade-aew-collision`.

## Nota de alcance

Se respetaron en todo momento los límites de la ley: solo se tocaron
los campos `duracion`/`referee`/`finish`/`ganador`/`ciudad`/`recinto`
cuando eran placeholders, más `ultima_actualizacion` y la línea de
`fuentes_principales` en las fichas efectivamente modificadas, más
checklist de `## Pendientes`. No se tocaron verbatims, clases,
calificaciones, slugs, nombres de archivo, índices, vistas derivadas
ni notebooks. No se abrieron pull requests.
