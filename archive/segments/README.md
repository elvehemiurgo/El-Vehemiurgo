# Segments — Registro personal del Vehemiurgo

Base de datos viva de **segmentos, promos y momentos puntuales** que el
Vehemiurgo ha visto, está estudiando o quiere documentar. Hermano del
registro de matches (`archive/matches/`), schema separado.

> "Quiero añadir segmentos, o partes específicas del performance de
> algún luchador o parte del show." — El Vehemiurgo, kickoff de la
> categoría.

---

## Diferencia con matches

- **Match**: pelea entera, con su mecánica (finish, duración, encuentros
  previos, gate, etc.).
- **Segment**: el momento *fuera* del match — o **dentro** del match
  pero aislado como pieza performativa: una promo, un face-off, un
  vignette, un post-match angle, una entrada que importó por sí sola,
  un *spot* aislado que se volvió icónico.

Un mismo show puede generar entradas en ambas carpetas: el match en
`matches/`, el promo previo o el post-match angle en `segments/`. Si
el momento es **el match entero**, va a `matches/`. Si es **un trozo**
de cualquier cosa, va a `segments/`.

## Tipos de segmento que registramos

- **Promo** — cut on the mic, in-ring o backstage.
- **In-ring confrontation / face-off** — cara a cara con o sin diálogo.
- **Post-match angle** — ataque, rescate, declaración después del
  match.
- **Backstage segment** — entrevista, ambush, conversación.
- **Vignette** — pre-recorded video package, character introduction,
  hype reel narrativo.
- **Sketch** — pieza cómica o teatral.
- **Entrance** — entrada específica que importa por sí sola (debut,
  retorno, gimmick change).
- **Celebration** — title win, retorno, retiro.
- **Turn** — el momento exacto de un face/heel turn cuando es lo
  suficientemente dramático.
- **Run-in** — interferencia que abre o redirige un ángulo (cuando es
  el evento central, no parte del finish del match).
- **Spot aislado** — un *spot* dentro de un match más largo que se
  volvió referente por sí mismo.
- **Interview** — entrevista on-screen kayfabe.

## Cómo se usa

### Para sumar un segmento

El Vehemiurgo escribe en chat algo así:

> "Sumá segmento *Sol Ruca: 'You didn't wanted a team!'*, NXT
> 2026-03-24."
> "Agregá la promo de *Cody Rhodes en Dynamite Grand Slam*, AEW
> 2022-09-21."
> "Sumá el post-match de *MJF vs Punk Revolution Pro*, AEW 2022-06-01."

También funciona sin la palabra *"segmento"* si la estructura es
**protagonista + línea o moment description + show + fecha**, sin
*"vs"* (porque "vs" dispara el flujo de match).

Yo abro un nuevo archivo en `archive/segments/<slug>.md` con la
plantilla `templates/segment.md` y arranco a poblar lo que tengo de
fuente fiable. Lo que no tengo, queda como **pendiente** o se marca con
`[verif]`. Nunca fabrico datos. Si la fecha no está confirmada, el slug
usa `YYYY-XX-XX`.

### Para consultar si un segmento ya está

> "¿Tengo el segmento de *Sol Ruca You Didn't Wanted A Team* en la
> base?"
> "¿Tengo la promo de *Cody Grand Slam* registrada?"

Yo grepo el `archive/segments/index.md` y los slugs, le confirmo si
está, y le muestro el último estado del registro.

### Para sumar review personal a un segmento existente

> "En *Sol Ruca You Didn't Wanted A Team* sumá: lo vi 8 veces, me
> gusta porque…"

Yo abro el archivo, actualizo `veces_visto_vehemiurgo`, agrego/expando
la sección **Lectura del Vehemiurgo**, y actualizo
`ultima_actualizacion`.

### Para profundizar un segmento

> "Investigá el contexto del segmento de Sol Ruca: qué storyline lo
> enmarca, qué dijeron los protagonistas después, reacción de Reddit y
> X."

Yo abro un sub-agente de research si el alcance lo justifica (ver
`workflow.md` §3), integro lo que vuelve, cito todo, y actualizo el
archivo. Lo que no se confirma queda marcado como rumor o como
**opinión documentada**.

---

## Estados del registro

Mismo cuadro que en matches:

- **`stub`** — el archivo existe pero está casi vacío.
- **`en-investigacion`** — research en curso.
- **`verificado`** — los campos críticos están confirmados con fuente
  fiable o video directo.
- **`vivo`** — verificado y siendo expandido (notas del Vehemiurgo,
  *look-backs* nuevos).

---

## Naming convention

`YYYY-MM-DD-<protagonista-slug>-<tag-corto>-<show>.md`

- Protagonista en kebab-case sin acentos.
- Tag corto: la línea anchor o el descriptor del momento, en
  kebab-case, sin signos.
- Show: abreviatura conocida (raw, smackdown, nxt, dynamite, etc.).

Ejemplos:
- `2026-03-24-sol-ruca-you-didnt-wanted-a-team-nxt.md`
- `2022-09-21-cody-rhodes-pec-tear-promo-dynamite.md`
- `1996-11-09-bret-hart-i-need-to-be-the-man-survivor-series.md`

Si la fecha no está confirmada: `YYYY-XX-XX-...md`. Se renombra al
verificar.

---

## Schema (frontmatter)

Definido en `templates/segment.md`. Campos clave:

- **Identificación**: segmento, slug, tipo_segmento, protagonistas,
  empresa, programa, fecha.
- **Datos del show**: ciudad, recinto, attendance, gate, rating TV,
  ubicación en el show, duración del segmento.
- **Performativo**: linea_textual, gimmick_momento, storyline.
- **Personal**: veces_visto_vehemiurgo, calificacion_vehemiurgo.
- **Operativo**: estado, ultima_actualizacion, fuentes_principales,
  tags.

---

## Secciones del cuerpo

1. **Resumen** (1–2 frases).
2. **Qué pasó** (descripción cronológica honesta).
3. **Líneas destacadas** (citas textuales con atribución y verificación).
4. **Contexto del storyline** (qué venía pasando, qué pasó después).
5. **Booking / función dentro del show** (lugar en card, payoff
   planeado, quién bookeó).
6. **Recepción** (in-arena, broadcast, social media, prensa).
7. **Impacto en carrera / personaje**.
8. **Datos curiosos**.
9. **Voces** — mismo schema y misma doctrina que matches: cinco rangos,
   peso editorial superior a la escuela Cornette.
10. **Lectura del Vehemiurgo** — review personal.
11. **Fuentes**.
12. **Pendientes de investigación**.

### Doctrina de Voces y de Meltzer

Igual que en matches: las afirmaciones llevan atribución completa
(quién, dónde, cuándo, cita o paráfrasis marcada, link/timestamp). Las
voces de fans / foros se marcan como **opinión documentada**, no como
hecho. Y el reporte factual de WON se cita como archivo, mientras que
las opiniones de la escuela Meltzer entran como contexto histórico —
no como veredicto. El veredicto se construye desde la escuela
Cornette.

---

## Lo que esta carpeta no es

- No es lista de "los 100 promos imprescindibles".
- No es review-aggregator de momentos virales.
- Es **memoria operativa de un historiador old-school**: los segmentos
  que importan **al Vehemiurgo**, con la profundidad que el Vehemiurgo
  quiera darles.
