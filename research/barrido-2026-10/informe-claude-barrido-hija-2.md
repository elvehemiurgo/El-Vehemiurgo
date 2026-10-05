# Informe — claude/barrido-hija-2

Sesión hija del barrido de datos duros 2026-10. Procesó lotes 04, 05 y
06 (`research/barrido-2026-10/lote-04.md`, `lote-05.md`, `lote-06.md`),
cubriendo shows de WWE/AAA de julio y agosto de 2026 (04/07 a 24/08).

## Método

Para cada lote se lanzó un sub-agente de research (WebSearch, un show
a la vez, reutilizando resultados para todas las fichas de ese show)
que devolvió un reporte estructurado por show con ciudad/recinto,
duración, réferi y finish cuando se encontraban. Sobre ese reporte se
aplicaron las reglas de edición del `README.md`: solo se reemplazaron
placeholders con valor hallado, fuente débil o aislada se marcó
`[una fuente]`, fuentes en desacuerdo se registraron ambas, y nada se
inventó. WebFetch estuvo bloqueado por el proxy en todos los sitios de
wrestling (403); todo el research se hizo con snippets de WebSearch.

## Conteos por lote

| Lote | Fichas editadas | Ítems de pendiente cerrados | Discrepancias nuevas |
|---|---|---|---|
| 04 | 18 | 24 | 0 |
| 05 | 16 | 20 | 0 |
| 06 | 17 | 20 | 1 |
| **Total** | **51** | **64** | **1** |

Cada lote tiene su propio commit (`barrido datos duros lote NN: ...`)
en esta rama.

## Discrepancia registrada

- **`archive/matches/2026-08-11-lexis-king-vs-lucien-price-nxt.md`**:
  la ficha registra como ganador a **Lexis King**, pero la fuente
  (Fightful, vía el sub-agente de research) describe el finish como un
  **One-Armed Powerbomb (pinfall) de Price**, sin aclarar si fue Price
  rematando a King o King contrarrestando y cubriendo. Se agregó la
  nota de discrepancia en `## Pendientes` sin reescribir el ganador —
  queda pendiente de verificación contra video o fuente más precisa.

## Dato notable fuera de discrepancia formal

- En `archive/matches/2026-08-21-cm-punk-vs-kevin-owens-wwe-smackdown.md`
  el sub-agente de research devolvió **"Dan Engler"** como réferi, pero
  explícitamente advirtió que no pudo atribuirlo a un sitio único y lo
  marcó como no confiable. Como el mismo nombre ya se había usado (con
  mejor atribución) para el réferi de Nick Aldis vs Gunther en
  SummerSlam Noche 1 (01/08, lote 05), **no se escribió ese dato** en
  la ficha de Punk/Owens por riesgo de ser un artefacto de la búsqueda
  agregada (posible confusión entre dos shows distintos). Queda
  `referee: "[verif]"` sin tocar.

## Qué quedó sin cubrir y por qué

El dato más sistemáticamente ausente es el **réferi de TV semanal**:
de las decenas de matches de Raw/SmackDown/NXT en los tres lotes,
prácticamente ninguna fuente de cobertura estándar (Fightful, WWE.com,
PostWrestling, PWTorch, Wrestling Inc, Cageside Seats, khelnow) nombra
al réferi — solo aparecieron nombres para PPV con cobertura detallada
(SummerSlam: Dan Engler, Chad Patton, Ryan Tran). Eso es consistente
con lo anticipado en el `README.md` y no es una laguna de research mal
hecho: es un dato que WWE no publica en coverage regular de TV.

También quedaron sin resolver, por falta de fuente (no por falta de
búsqueda):

- Duración de la mayoría de **segmentos y promos** (no-matches): el
  coverage de resultados casi nunca da timestamp de segmentos
  backstage/promos, solo de luchas.
- Varias duraciones exactas de matches de TV semanal (julio-agosto),
  donde ninguna fuente dio clock — se dejaron como `[verif]` sin
  fabricar una cifra.
- El recinto exacto de NXT del 28/07/2026 (`archive/segments/2026-07-28-*.md`,
  tres fichas): el sub-agente encontró "WWE Performance Center" pero
  **advirtió explícitamente baja confianza** (contradice el patrón de
  esas fechas, que debería ser Capitol Wrestling Center) — se decidió
  **no escribirlo** para no introducir un dato probablemente erróneo.
- Duración del fatal 4-way `2026-08-11-cruz-montana-vs-grayson-waller-debut-zilla-fatu-nxt.md`:
  el sub-agente encontró 13:52 pero lo marcó explícitamente como "no
  atribuible a un sitio único — tratar como no confirmado de fuente
  primaria", más allá del umbral normal de "una fuente débil" — se
  dejó sin escribir por la misma razón de cautela.
- `archive/matches/2026-08-24-roxanne-perez-vs-stephanie-vaquer-wwe-raw.md`:
  la única duración hallada (3:17) parece provenir del título de un
  video "(2/2)" — probablemente la duración de solo la segunda mitad
  del clip, no del match completo — y las descripciones del finish
  variaban entre fuentes. No se escribió nada nuevo; la ficha ya tenía
  un finish bien sourceado de research previo y se dejó intacto.
- Varias fichas de 2026-07-04, 07-06, 07-27, 07-28, 07-31 y 08-10 no
  tuvieron ningún placeholder resuelto porque ni duración ni réferi
  aparecieron en ninguna fuente consultada — permanecen exactamente
  como estaban, sin tocar.

Todas las fichas tocadas llevan la línea de `fuentes_principales` del
sub-agente de barrido (`Sub-agente barrido-datos-duros-2026-10 ...`) y
`ultima_actualizacion: 2026-10-05`, según lo pedido por el `README.md`.
No se abrió ningún pull request.
