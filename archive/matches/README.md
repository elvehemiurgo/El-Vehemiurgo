# Matches — Registro personal del Vehemiurgo

Base de datos viva de los matches que el Vehemiurgo ha visto, está
estudiando o quiere documentar. **No es una lista enciclopédica de matches
relevantes de la historia**: es la colección personal, con review propia,
*rewatch count*, datos de booking, financieros y backstage.

> "Esta base de datos debe estar siempre disponible si a mí se me ocurre
> añadir un comentario o preguntar si tal lucha ya está en nuestra base de
> datos." — El Vehemiurgo, kickoff del proyecto.

---

## Cómo se usa

### Para sumar un match
El Vehemiurgo escribe en chat algo así:

> "Sumá *Christian Cage vs Batista, WWE Raw 2005*."
> "Agregá *Misawa vs Kawada, Triple Crown 1994-06-03*."

Yo abro un nuevo archivo en `archive/matches/<slug>.md` con la plantilla
`templates/match.md` y arranco a poblar lo que tengo de fuente fiable. Lo
que no tengo, queda como **pendiente** o se marca con `[verif]`. Nunca
fabrico datos. Si la fecha no está confirmada, el slug usa `YYYY-XX-XX`.

### Para consultar si un match ya está
El Vehemiurgo escribe:

> "¿Tengo *Hogan vs Andre WMIII* ya en la base?"

Yo grepo el `archive/matches/index.md` y los slugs, le confirmo si está,
y le muestro el último estado del registro.

### Para sumar review personal a un match existente
El Vehemiurgo escribe:

> "En *Christian vs Batista 2005* sumá: lo vi 4 veces, me gusta porque…"

Yo abro el archivo, actualizo `veces_visto_vehemiurgo`, agrego/expando la
sección **Lectura del Vehemiurgo**, y actualizo `ultima_actualizacion`.

### Para profundizar un match
El Vehemiurgo dice:

> "Investigá el booking previo de Christian vs Batista 2005. Quiero saber
> qué planes había, qué cambió y qué dijeron los protagonistas en
> entrevistas posteriores."

Yo abro un sub-agente de research si el alcance lo justifica (ver
`workflow.md` §3), integro lo que vuelve, cito todo, y actualizo el
archivo. Lo que no se confirma queda marcado como rumor.

---

## Estados del registro

Cada match tiene un campo `estado:` en el frontmatter:

- **`stub`** — el archivo existe pero está casi vacío. Pendiente de pase
  de research.
- **`en-investigacion`** — research en curso. Algunos campos completos,
  otros marcados.
- **`verificado`** — todos los campos críticos (fecha, finish, gate si
  aplica, fuentes) están confirmados con fuente fiable.
- **`vivo`** — verificado y siendo expandido (notas del Vehemiurgo,
  *look-backs* nuevos, etc.).

---

## Naming convention

`YYYY-MM-DD-<wrestler1>-vs-<wrestler2>-<promo|programa>.md`

Ejemplos:
- `2005-01-31-christian-cage-vs-batista-raw.md`
- `1987-03-29-hogan-vs-andre-wrestlemania-iii.md`
- `1994-06-03-misawa-vs-kawada-triple-crown.md`
- `2005-XX-XX-christian-cage-vs-batista-raw.md` (fecha pendiente)

Wrestlers en kebab-case, sin acentos, en orden de billing oficial cuando se
sabe (face primero o como aparezca en el cartel).

---

## Schema (frontmatter)

Definido en `templates/match.md`. Campos clave:

- **Identificación**: match, slug, participantes, empresa, programa,
  fecha.
- **Datos del show**: ciudad, recinto, attendance (anunciada/paga), gate,
  rating TV, buy rate.
- **Match en sí**: tipo, estipulación, duración, finish, ganador, referee.
- **Histórico**: encuentros_previos.
- **Personal**: veces_visto_vehemiurgo, calificacion_vehemiurgo.
- **Operativo**: estado, ultima_actualizacion, fuentes_principales, tags.

---

## Secciones del cuerpo

1. **Resumen** (1–2 frases).
2. **Storyline y construcción** (300+ palabras).
3. **Booking timeline** (cronología pre / match / post).
4. **Encuentros previos**.
5. **Datos del show / box office**.
6. **Planes de booking** — lo que se hizo, lo que cambió, lo que se
   canceló.
7. **Impacto en carrera**.
8. **Datos curiosos**.
9. **Entrevistas y look-backs**.
10. **Lectura del Vehemiurgo** — review personal, rewatch count, por qué.
11. **Fuentes**.
12. **Pendientes de investigación**.

Cuando un match esté `stub` o `en-investigacion`, las secciones que faltan
se dejan con el header pero sin contenido. Esto hace explícito qué falta y
permite ir llenándolo en pases sucesivos.

---

## Index

El archivo `index.md` lleva una tabla con todos los matches en la base.
Se actualiza con cada alta. Útil para "¿qué tengo?" y "¿qué me falta de tal
era / luchador / promotion?".

---

## Lo que esta carpeta no es

- No es Cagematch ni un dump de results.
- No es lista de "los 100 matches imprescindibles".
- No es review-aggregator con estrellas.
- Es **memoria operativa de un historiador old-school**. Los matches que
  importan **al Vehemiurgo**, con la profundidad que el Vehemiurgo quiera
  darles, en el ritmo que el Vehemiurgo defina.
