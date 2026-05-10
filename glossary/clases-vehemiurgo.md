# Las Clases del Vehemiurgo

Sistema editorial propio del Vehemiurgo para clasificar matches y
segmentos memorables de su lista personal. **No es un sistema de
estrellas**. La escuela Meltzer / WON usa estrellas porque mide
*match-as-art independiente del draw* — es la escuela editorial
opuesta del proyecto. Ver
[`CLAUDE.md`](../CLAUDE.md) §5 sobre la jerarquía Cornette-school
en este proyecto.

Las clases del Vehemiurgo miden **qué tipo de oficio se cumple
bien** en un match o segmento. Es categoría doctrinal, no
calificación numérica.

> "Quiero implementar un sistema de rank, pero no de estrellas ni
> eso, sino de clases de luchas o segmentos memorables que pongo en
> mi lista." — El Vehemiurgo, 2026-05-09.

---

## Las tres clases

> **NOTA EDITORIAL — borrador en discusión 2026-05-09**: las
> definiciones siguientes son **propuestas iniciales**. El
> Vehemiurgo eligió "discutamos matiz por clase" — las
> definiciones se refinarán en sesiones siguientes. Cuando se
> cierre el canon de una clase, se removerá esta nota para esa
> sección.

### 1. Perfect Wrestling Class

**Borrador de definición** *(en discusión)*:

Matches o segmentos donde **todos los ejes del oficio funcionan al
unísono**. Booking con causa, draw construido, heat genuino,
gimmicks coherentes, intención clara, consecuencia respetada,
ejecución in-ring solo cuando sirve a la historia. Es la clase de
**liturgia completa cumplida** — la trinidad promotor / luchador /
fan opera sin fricción.

**Criterios tentativos** que un Perfect Wrestling cumple:
- Causa narrativa visible (no es match dream sin sustancia).
- Heat o draw demostrable.
- Gimmick coherente con el rol (face / heel / tweener vehemiurgia).
- Finish con peso.
- Consecuencia post-match — el match dejó algo encendido.
- Ejecución in-ring al servicio de la historia.

**Candidatos tentativos desde la lista personal** (a confirmar):
- Christian vs Chris Jericho — WrestleMania XX.
- AJ Styles vs Gunther — WWE Royal Rumble 31.01.2026.
- CM Punk vs Roman Reigns — WrestleMania 42 Día 2.

### 2. Fighting Spirit Class

**Borrador de definición** *(en discusión)*:

Matches o segmentos donde el eje **combate-intensidad-corazón** es
el motor. La rama strong style / king's road / catch puro. Stiff
strikes, struggle, near-falls ganados con sufrimiento, finishers
que escalan. Se mide más por **la guerra que por la coreografía**.

**Criterios tentativos** que un Fighting Spirit cumple:
- Stiff work documentable (golpes con contacto real).
- Struggle por encima de spotfest — la pelea se siente ganada,
  no coreografiada.
- Drama de near-falls construido sobre escalada de daño, no
  sobre cantidad.
- Heart / corazón visible — el wrestler vende que la pelea le
  cuesta.
- El match honra la tradición catch, strong style, king's road,
  o equivalente.

**Candidatos tentativos desde la lista personal** (a confirmar):
- Bret Hart vs Steve Austin — WWF Live Event Germany abril 1996.
- MCMG vs Ikuto Hidaka & Minoru Fujita — ZERO1-MAX 25.08.2006.
- Bradshaw & Barry Windham vs Steve Williams & Gary Albright —
  AJPW 23.11.1997.
- Owen Hart vs Bret Hart — WrestleMania X.
- Dragon Lee vs Taiji Ishimori — NJPW Wrestling Dontaku 2019.

### 3. Wrestling Entertainment Class

**Borrador de definición** *(en discusión)*:

Matches o segmentos donde el eje
**performance-character-promo-spectacle** es el motor. Carny puro,
gimmick ejecutado bien, charisma sobre execution, theatricality
old-school o moderna que respeta la liturgia. Sports entertainment
**cuando se hace con oficio** (no cuando se hace por reflejo
corporativo).

**Criterios tentativos** que un Wrestling Entertainment cumple:
- Performance / character work al frente — la pieza se sostiene
  por la presencia, no por la mecánica.
- Promo o segmento con carga editorial real (heel justificado,
  babyface con causa, comedy carny no chistecito).
- Theatricality que respeta la liturgia carny — no rompe el rito,
  lo amplifica.
- Charisma sobre execution — el público responde al gimmick antes
  que al moveset.

**Candidatos tentativos desde la lista personal** (a confirmar):
- Fatal Influence debut — WWE SmackDown 24.04.2026 *("the
  greatest act in WWE now in the big leagues, the whole act is
  here")*.
- Kazarian Elvis "Bear with me" promo — TNA Impact 18.12.2025.
- Kit Wilson Poetry Slam — WWE SmackDown 20.03.2026.
- Christian Coalition backstage segments — TNA 2007.
- Steve Austin vs The Rock — WWF In Your House 12.07.1997.
- Randy Savage vs DDP — WCW Great American Bash 15.06.1997.

---

## Multi-clasificación

**Decisión editorial del Vehemiurgo (2026-05-09)**: una entrada
**puede pertenecer a más de una clase**. No son mutuamente
excluyentes.

Esto refleja la realidad del oficio: un match puede ser **Perfect
Wrestling y Fighting Spirit al mismo tiempo** (booking impecable +
guerra brutal), o **Fighting Spirit y Wrestling Entertainment**
(combate intenso + performance excepcional), o **las tres**
simultáneamente cuando la pieza alcanza algo raro.

**Una entrada sin clasificar** lleva el campo vacío. **No es
defecto**: es estado. La lista del Vehemiurgo va a tener muchas
entradas sin clase asignada por mucho tiempo — la asignación
ocurre cuando el Vehemiurgo revisa la entrada con voluntad
editorial, no por barrido bulk.

---

## Schema operativo

### Campo en frontmatter

`templates/match.md` y `templates/segment.md` llevan el campo:

```yaml
clases_vehemiurgo: []
# o cuando se asignan:
clases_vehemiurgo:
  - perfect-wrestling
  - fighting-spirit
```

**Valores válidos**:
- `perfect-wrestling`
- `fighting-spirit`
- `wrestling-entertainment`
- `[]` (lista vacía = sin clasificar)

### Triggers de chat

El Vehemiurgo en chat:

- **"Esto es Perfect Wrestling"** / *"Esto es Fighting Spirit"* /
  *"Esto es Wrestling Entertainment"* — agrego la clase al match o
  segmento de contexto. Si el archivo no existe, lo abro como
  stub.

- **"Es Perfect Wrestling y Fighting Spirit"** (multi) — agrego
  ambas.

- **"Sumá Wrestling Entertainment a [X]"** — agrego clase a
  archivo existente, sin tocar las que ya están.

- **"Quitá [clase] de [X]"** — remuevo del listado.

- **"¿Qué tengo en Perfect Wrestling Class?"** — grepo todos los
  archivos que llevan `perfect-wrestling` y devuelvo lista
  ordenada.

- **"¿Cuántas Fighting Spirit tengo?"** — count.

- **"Mostrame los matches con dos o más clases"** — busco entradas
  con `len(clases_vehemiurgo) >= 2`.

### Cómo se agrega a entradas existentes

Cuando una entrada del notebook
[`2026-05-09-2-lista-personal-completa.md`](../notebook/2026-05-09-2-lista-personal-completa.md)
se procesa y el Vehemiurgo le asigna clase, **se actualiza el
archivo de match/segment correspondiente**. Las entradas que ya
existen en `archive/` (los 18 fact-sheets de la sesión anterior)
**se editan agregando el campo** cuando se les asigne clase, no
antes. Bulk no.

### Cómo se actualiza la doctrina

Cuando el Vehemiurgo refina la definición de una clase, este
archivo se actualiza:
- Definición canónica reemplaza el borrador.
- Se remueve la nota *"borrador en discusión"* de esa sección.
- Se sumar criterios o ejemplos confirmados.

---

## Por qué este sistema y no estrellas

Cornette-school doctrine. Las estrellas son métrica de la escuela
Meltzer / WON: *match-as-art independiente del draw*. La doctrina
del Vehemiurgo declarada en
[`CLAUDE.md`](../CLAUDE.md) §3 y §5 es **booking-first,
draw-first**. Por lo tanto:

- Una **clasificación numérica única** (estrellas) es
  reduccionismo: aplana ejes diversos del oficio en una sola
  línea.
- Una **clasificación por categoría con multi-clasificación**
  refleja que el wrestling tiene **distintos modos de cumplir el
  oficio**, y que un match excepcional cumple varios a la vez.

Las clases **no compiten entre sí** en jerarquía. Perfect Wrestling
no es "mejor que" Fighting Spirit ni que Wrestling Entertainment.
**Son distintos modos del oficio** que el Vehemiurgo reconoce y
nombra.

---

*Las clases del Vehemiurgo son lectura editorial, no veredicto.
Cuando un match recibe una clase, no se está afirmando que sea
"mejor" — se está afirmando que **cumple un modo del oficio que
vale la pena nombrar**.*
