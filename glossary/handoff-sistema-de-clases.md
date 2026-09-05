---
titulo: "Handoff — el sistema de calificación por clases del Vehemiurgo"
tipo: handoff
estado: vivo
ultima_actualizacion: 2026-09-05
fuente_de_verdad: "glossary/clases-vehemiurgo.md (doctrina completa) + CLAUDE.md §4 (ley operativa) + bin/archivo_lib.py (implementación)"
tags: [handoff, clases-vehemiurgo, perfect-wrestling, fighting-spirit, wrestling-entertainment, wrestling-entertainment-plus, coronas, feeling-crown, instant-classic-crown, coronas-plus, perfect-declarado]
---

# Handoff — el sistema de calificación por clases

> **Para quién es esto**: para cualquier persona o sesión que tenga
> que leer, escribir o auditar una ficha de match/segment del archivo
> y necesite entender **exactamente** cómo se califica. Es un resumen
> operativo completo. La doctrina larga vive en
> `glossary/clases-vehemiurgo.md`; la ley en `CLAUDE.md §4`; el
> código en `bin/archivo_lib.py`. **Si este documento y esos tres
> discrepan, ganan los tres.**

---

## 0. La idea en una frase

**El Vehemiurgo no da estrellas. Declara clases.** Una pieza (match o
segment) puede llevar cero, una, dos o tres clases, y ciertas
combinaciones reciben un nombre propio llamado **corona**. **Nada de
esto se infiere jamás: la clase existe solo cuando el Vehemiurgo la
dijo.**

---

## 1. Las cuatro clases

| Clase | Slug en frontmatter | Sigla | Qué mide | Frases típicas que la disparan |
|---|---|---|---|---|
| **Perfect Wrestling** | `perfect-wrestling` | **PW** | El techo absoluto: la pieza que **define era, carrera o temporada**. No es "match de la semana": es **evento**. Rara por construcción. | *"perfecta"*, *"clásico"*, *"define el wrestling"*, *"se merece las 3 clases"* |
| **Fighting Spirit** | `fighting-spirit` | **FS** | **Pelea real**: física, stiff, contacto que se cree. *"Old-school class"* es sinónimo. **Aplica también a promos.** | *"lo mantuvieron real"*, *"muy dura"*, *"stiff"*, *"se sintió como una pelea"*, *"masacre"* |
| **Wrestling Entertainment** | `wrestling-entertainment` | **WE** | **Character work, gimmick, promo, stakes narrativos.** La clase más frecuente. | *"se merece una WE"*, *"buen segmento"*, *"cool"*, *"entretenido"* |
| **Wrestling Entertainment Plus** | `wrestling-entertainment-plus` | **WE+** | **Un escalón por encima de WE**: *"segmentos simplemente demasiado buenos que definen el entertainment y el wrestling booking inteligente"*. | *"se merece una WE+"*, *"imperdible"*, *"legendaria"*, *"segmentazo"* |

**Regla dura sobre WE y WE+**: **una pieza lleva WE o WE+, nunca las
dos.** WE+ **sí toca la jerarquía** (está arriba de WE); las coronas
(sección 3) **no** la tocan.

**Sobre las siglas en prosa**: siempre en este orden y separadas por
punto medio: `PW·FS·WE`, `FS·WE`, `PW·FS·WE+`. La columna *Clase* de
los índices las genera así.

---

## 2. La regla que gobierna todo: solo declarada, nunca inferida

1. **La clase existe si el Vehemiurgo la dijo.** *"Se merece una WE"*,
   *"ponle FS"*, *"las 3 clases"* → se escribe. Cualquier otra cosa →
   no se escribe.
2. **"El booking estuvo genial" ≠ clase.** Booking y clase son ejes
   distintos. Se puede elogiar el booking sin dar clase, y dar clase
   criticando el booking. Precedente: *"la estipulación no les
   benefició [...] se merece una WE, pero el booking sí está cool"*
   (AAA Ola de Calor, s59).
3. **Silencio editorial**: si el Vehemiurgo **no menciona** una pieza,
   **no existe ficha** ni se investiga. Si la menciona y dice *"mid"*,
   *"estuvo ok"*, *"no me gustó"* **sin darle clase**, la ficha se
   abre **con `clases_vehemiurgo: []`** y ese juicio es la lectura
   completa. **`[]` no es un hueco: es un estado.**
4. **Si el copiloto infiere una clase por lectura** (caso raro, a
   evitar), **debe marcarla** en `calificacion_vehemiurgo` y en la
   sección *Lectura* como *"asignada por lectura, pendiente de
   ratificación"*. No se hace silenciosamente.
5. **Contradicción de dictado** (el Vehemiurgo dice dos cosas
   incompatibles en el mismo párrafo — p. ej. *"las 3 clases"* y
   *"WE y FS"*): **el archivo no adjudica**. Registra la más específica
   y de cierre como lectura operativa, deja la otra anotada como
   pendiente de ratificación, y lo dice en la ficha. Precedente: La
   Parka vs Priest vs Fiscal vs Wagner (AAA Ola de Calor, s59).

---

## 3. Las coronas — premios **derivados**

**Ley del Vehemiurgo (2026-08-26, s52)**: *"no hay que modificar la
jerarquía, solo agregar premios que se llamarán coronas"*. Una corona
es **el nombre que recibe una combinación de clases que ya existía**.
**Nunca se declara, nunca se escribe en frontmatter: se calcula.**

| Combinación exacta | Corona | Sigla | Ley |
|---|---|---|---|
| `fighting-spirit` + `wrestling-entertainment` | **Feeling Crown** | **FC** | s52 (2026-08-26) |
| `perfect-wrestling` + `fighting-spirit` + `wrestling-entertainment` | **Instant Classic Crown** | **ICC** | s52 (2026-08-26) |
| `fighting-spirit` + `wrestling-entertainment-plus` | **Feeling Crown+** | **FC+** | s59 (2026-09-03) |
| `perfect-wrestling` + `fighting-spirit` + `wrestling-entertainment-plus` | **Instant Classic Crown+** | **ICC+** | s59 (2026-09-03) |

**Las Coronas+** son la misma corona marcada con `+` cuando el
componente de entertainment es WE+ en vez de WE. *"WE+ entra en las
coronas pero sería una Corona+"* (Vehemiurgo, 2026-09-03). **No son
coronas nuevas: son la variante alta de las que existen.**

**Toda combinación no listada no lleva corona** — ni `PW+FS`, ni
`PW+WE`, ni una clase sola. **El archivo no inventa coronas por
simetría.** Se agregan **solo por declaración explícita**.

**Dónde viven**:
- **Frontmatter**: en ningún lado. **No hay campo de corona y no debe
  haberlo** — sería estado duplicado que se desincroniza.
- **Código**: `bin/archivo_lib.py` → dict `CORONAS` + propiedad
  `Ficha.corona`. Devuelve la sigla o `—`.
- **Índices** (`archive/matches/index.md`, `archive/segments/index.md`):
  columna **Corona**, generada por `bin/regen_index.py`. **No se edita
  a mano.**
- **Prosa**: se nombran en el blockquote-lead de la ficha cuando
  corresponde (*"Instant Classic Crown"*, *"Feeling Crown"*).

**Consecuencia operativa**: si el Vehemiurgo retira una clase, la
corona desaparece sola al regenerar. Si agrega la que faltaba, aparece
sola.

---

## 4. Lo que está ABIERTO — *"la corona más un PERFECT"* (s62, 2026-09-05)

**Declaración verbatim**, sobre Roode & Aries vs Chavo & Hernandez
(2013 02 07 TNA Impact Wrestling):

> *"se merece las 3 clases, top tier wrestling [...] es un clásico
> instantaneo; pero a este démosle la corona más un PERFECT, esta es la
> definición de wrestling"*

**Lo que está claro**: la pieza lleva PW·FS·WE (→ ICC derivada) **y
además** una distinción llamada **PERFECT**, por encima de la corona.

**Lo que NO está claro y el archivo no resuelve solo**:

1. ¿Es un **marcador que se suma** a la corona (lectura provisional,
   por el *"más"*) o una corona nueva?
2. ¿Aplica **solo sobre ICC** o sobre cualquier corona?
3. **Cómo se almacena** — y acá hay un hecho estructural: PERFECT **no
   puede derivarse**, porque dos piezas con las mismas tres clases
   reciben distinta distinción (Chavo vs Aries del 31/1 es ICC sin
   PERFECT; el tag del 7/2 es ICC con PERFECT). **Sería la primera
   marca del sistema que necesariamente se declara en frontmatter en
   vez de calcularse.** Eso la hace de otra naturaleza que las
   coronas.

**Estado actual**: la declaración vive en la ficha del match
(blockquote-lead, `calificacion_vehemiurgo`, tag `perfect-declarado`).
**No hay campo nuevo, no hay columna nueva, no se tocó
`archivo_lib.py`.** Cuando el Vehemiurgo fije la mecánica, se
implementa de una vez.

**Ojo terminológico**: el archivo usa *"Perfect Match"* informalmente
como sinónimo de *pieza con Perfect Wrestling Class*. **PERFECT como
distinción sobre la ICC es otra cosa** — la ICC ya incluye PW por
definición.

---

## 5. Reglas operativas — la lista completa

Las cinco fundacionales (2026-06-17) más las que se sumaron después:

1. **Vocabulario único en frontmatter**: solo los cuatro slugs de la
   sección 1. Nada más (`WE`, `Perfect`, `old-school` **no** son
   valores válidos en el campo).
2. **Booking ≠ clase.** Elogiar el diseño narrativo no asigna clase.
3. **Triple clase admite reserva técnica puntual**, declarada junto al
   elogio. La reserva **no baja la clase**. Precedentes: Fletcher vs
   Bailey (*"no es prolijo"*), Knight vs Jericho (*"todavía nada muy
   entertainment"*), Maya vs Persephone (*"solo me quejaría de los
   spots en ringside"*), el main event de NXT Heatwave (*"el intercambio
   de suplexes [...] tontería sin fundamento"*). **Regla extendida a
   WE+** en s58 (Knight/Borden/Callis: *"solo me quejaría del golpe
   con el título"*).
4. **Clase inferida se marca** como *"asignada por lectura, pendiente
   de ratificación"* hasta llamado explícito.
5. ***Old-school class* = Fighting Spirit**, y **FS aplica también a
   promos**.
6. **Clase con destinatario**: el Vehemiurgo puede asignar la clase **a
   una persona dentro de la pieza**, no al conjunto. Se registra la
   clase en la ficha **y se anota el destinatario** en
   `calificacion_vehemiurgo` y en la lectura. Precedentes: *"se
   merecen todas las clases todos aquí menos Moxley"* (Collision 30/7,
   s37); *"la lucha se merece una WE por ver a MJF en acción"* (Dynamite
   12/8, s57); *"se merece una WE y FS por la actuación de Drake sobre
   todo"* (NXT Heatwave, s61); *"Christian se merece una WE"* (Dynamite
   26/8, s58).
7. **WE+ por consistencia**: la WE+ puede otorgarse por **estándar
   sostenido**, no solo por un pico. Precedente: Jay White, *"sublime
   **como siempre**"* (Collision 22/8, s58).
8. **WE+ sin diálogo**: la WE+ **no requiere una sola línea hablada**
   si la composición hace el trabajo. Precedentes: post-match
   MCMG/FTR en Wembley (*"momentazo sin palabras"*), careo Penta/Roman
   (cierre de Raw 31/8).
9. **Elaboración**: si el Vehemiurgo vuelve sobre una pieza que ya
   tiene ficha, **no se abre archivo nuevo** — se agrega una sección
   *"Segunda lectura — sNN"* con el nuevo verbatim. Si en la segunda
   lectura **declara la clase que faltaba**, se actualiza el
   frontmatter y se registra la fecha. Precedente: MJF embosca a
   Andrade (sin clase en s37 → WE en s57, 26 días después).
10. **Separación**: si el Vehemiurgo califica **por separado** algo que
    el archivo había registrado como una sola pieza (p. ej. un
    segmento que incluía el match), **se separa**: cada pieza con su
    clase. Precedente: Zilla Fatu vs Tristan Angels (segmento WE+ en
    s61 → match con 3 clases separado en s62).
11. **Ratificación pendiente se cierra con una palabra.** Cuando el
    Vehemiurgo ratifica (*"sí, sube a WE+"*, *"sí, WS era WE"*), se
    actualiza el frontmatter, se marca el pendiente como cerrado
    `[x]`, y se registra la fecha de ratificación en
    `calificacion_vehemiurgo`.

---

## 6. Schema exacto en frontmatter

```yaml
# Sin clasificar (estado válido, no hueco):
clases_vehemiurgo: []

# Una clase:
clases_vehemiurgo: ["wrestling-entertainment"]

# Feeling Crown (derivada — no se escribe la corona):
clases_vehemiurgo: ["fighting-spirit", "wrestling-entertainment"]

# Instant Classic Crown (derivada):
clases_vehemiurgo: ["perfect-wrestling", "fighting-spirit", "wrestling-entertainment"]

# WE+ sola:
clases_vehemiurgo: ["wrestling-entertainment-plus"]

# Feeling Crown+ (derivada):
clases_vehemiurgo: ["fighting-spirit", "wrestling-entertainment-plus"]
```

**Inválido** (el lint E5 lo atrapa):
`["WE"]`, `["perfect"]`, `["wrestling-entertainment", "wrestling-entertainment-plus"]`
(WE y WE+ juntas), cualquier slug fuera de los cuatro.

**Campo hermano obligatorio**: `calificacion_vehemiurgo` — una cita
corta o paráfrasis fiel del llamado, **incluyendo la reserva si la
hubo** y **el destinatario si la clase fue a una persona**. Si hubo
ratificación posterior, se anota ahí con fecha.

---

## 7. Cómo se ve en una ficha

```markdown
# Título — Show (fecha)

> **Feeling Crown** (FS + WE). *"Cita corta del Vehemiurgo que
> justifica la clase."*

## Lectura del Vehemiurgo

**Cita verbatim**:

> *"...verbatim completo, typos preservados..."*
>
> — El Vehemiurgo, YYYY-MM-DD sNN (verbatim, typos preservados)

**Lectura sintética**: ejes numerados que conectan la clase con la
doctrina, sin inflar.
```

**El blockquote-lead siempre dice la clase/corona primero.** Si hay
reserva declarada, va ahí también (*"Instant Classic Crown, con
reserva técnica declarada"*). Si no hay clase, lo dice: *"**Sin clase
declarada** — el Vehemiurgo lo lee como 'estuvo ok'"*.

---

## 8. Triggers de chat que el copiloto reconoce

| El Vehemiurgo dice | El copiloto hace |
|---|---|
| *"Esto es Perfect Wrestling"* / *"ponle FS"* / *"se merece una WE"* | Agrega la clase a la pieza de contexto. Si no hay ficha, la abre. |
| *"Se merece las 3 clases"* / *"todas las clases"* | `[perfect-wrestling, fighting-spirit, wrestling-entertainment]` → ICC derivada. |
| *"Se merece WE y FS"* / *"la WE y FS class"* | `[fighting-spirit, wrestling-entertainment]` → FC derivada. |
| *"Se merece una WE+"* | `[wrestling-entertainment-plus]` (reemplaza WE si la había). |
| *"Sumá WE a [X]"* | Agrega sin tocar las que ya están. |
| *"Quitá [clase] de [X]"* | Remueve; la corona se recalcula sola. |
| *"Sí, sube a WE+"* / *"sí, WS era WE"* | Ratificación: actualiza frontmatter, cierra pendiente, fecha. |
| *"Esto es solo una nota sobre el booking"* | **Sin clase**, y la ficha lo dice explícitamente. |
| *"¿Qué tengo en Perfect Wrestling?"* / *"¿cuántas ICC tengo?"* | Grep sobre el corpus; devuelve lista o count desde los índices. |

**Skill**: `/clase` (`.claude/skills/clase/SKILL.md`) ejecuta esto.

---

## 9. Dónde vive cada cosa

| Qué | Dónde |
|---|---|
| Doctrina completa (definiciones largas, historia, ejemplos) | `glossary/clases-vehemiurgo.md` |
| Ley operativa resumida | `CLAUDE.md §4` (bullets *Sistema de clases*, *Coronas*, *Coronas+*, *WE+*) |
| Implementación (slugs válidos, siglas, coronas) | `bin/archivo_lib.py` → `CLASES_OK`, `ABBR`, `CORONAS`, `CORONA_NOMBRE`, `Ficha.clase_abbr`, `Ficha.corona` |
| Validación | `bin/lint_archivo.py` (E5: slug inválido / WE+WE+ juntas) |
| Índices con columnas *Clase* y *Corona* | `archive/matches/index.md`, `archive/segments/index.md` — **generados**, vía `bin/index_add.py <ficha>` |
| Skill de chat | `.claude/skills/clase/SKILL.md` |
| Templates | `templates/match-stub.md`, `templates/segment.md` |
| Este handoff | `glossary/handoff-sistema-de-clases.md` |

---

## 10. Historial de leyes (para saber de dónde sale cada cosa)

| Fecha | Sesión | Ley |
|---|---|---|
| 2026-05-09 | — | Nacen las tres clases y la multi-clasificación. |
| 2026-06-17 | — | Las cinco reglas operativas (vocabulario único, booking ≠ clase, reserva en triple, inferida se marca, old-school = FS). |
| 2026-08-01 | s17 | **Silencio editorial**: lo no mencionado no existe; *"mid"* sin clase es lectura completa. |
| 2026-08-26 | s52 | **Coronas**: Feeling Crown (FS+WE) e Instant Classic Crown (las tres). Derivadas, nunca declaradas. |
| 2026-08-26 | s54 | **WE+**: escalón sobre WE, sí toca la jerarquía. Una pieza lleva WE o WE+, nunca las dos. |
| 2026-09-03 | s59 | **Coronas+**: FC+ e ICC+ cuando el entertainment es WE+. Cody/Randy 28/8 sube a WE+. "WS" ratificado como WE. |
| 2026-09-05 | s62 | **PERFECT declarado** sobre Roode & Aries vs Chavo & Hernandez — **mecánica pendiente de ratificación** (sección 4). |

---

## 11. Checklist de auditoría rápida

Antes de dar por buena una ficha, verificar:

- [ ] `clases_vehemiurgo` usa solo slugs válidos; no hay WE y WE+ juntas.
- [ ] Cada clase escrita **tiene su frase en el verbatim** que la
      justifica. Si no la tiene → o es inferida (y está marcada) o es
      error.
- [ ] Si hay reserva declarada, está en `calificacion_vehemiurgo` y en
      el blockquote-lead.
- [ ] Si la clase fue a una persona, el destinatario está anotado.
- [ ] **No hay campo de corona en frontmatter.**
- [ ] El blockquote-lead nombra la clase/corona (o dice *"sin clase"*).
- [ ] `bin/index_add.py <ficha>` corrió después de tocar el frontmatter
      (los índices se regeneran; nunca se editan a mano).
- [ ] `bin/lint_archivo.py --pre-commit` → 0 errores.
