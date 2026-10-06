# Informe — sesión hija claude/barrido-hija-3

Lotes asignados: `lote-07.md`, `lote-08.md`, `lote-09.md` (en ese
orden). Los tres quedaron procesados por completo. Tres commits, uno
por lote, empujados a `claude/barrido-hija-3`.

## Conteos por lote

| Lote | Alcance | Fichas tocadas | Ítems cerrados | Discrepancias |
|---|---|---|---|---|
| 07 | WWE, shows 25/8–4/9/2026 | 2 | 2 | 0 |
| 08 | WWE, shows 6/9–21/9/2026 | 2 | 2 | 0 |
| 09 | AAA, 2006–18/7/2026 | 27 (23 matches + 4 segments) | ~35 | 3 |
| **Total** | | **31** | **~39** | **3** |

Commits:
- `0b8620d` — lote 07.
- `c949f71` — lote 08.
- `9f352a8` — lote 09.

## Por qué el rendimiento es tan distinto entre lotes

Lote 07 y 08 (WWE semanal 2026) tenían mayoría de pendientes de
**referee** (matches) y **duración exacta de segmentos**. Ninguno de
los dos tipos de dato se reporta casi nunca en dirt sheets/recaps —
los referees de WWE solo se nombran cuando hay un bump o un spot de
árbitro que dispara una nota específica (y aun así, a veces ni
entonces), y la duración de un segmento no-match (promo, backstage,
video) no figura en ningún agregador. El research cerró lo que pudo
(2 ítems por lote) y dejó el resto correctamente abierto — esto no es
un vacío del barrido sino un límite estructural de la fuente.

Lote 09 (AAA) rindió mucho más porque sus pendientes eran
mayoritariamente **finish + ganador + ciudad/recinto + roster**, datos
que sí se reportan en los recaps estándar de AAA on FOX/Worldwide
(Fightful, F4W/WON, POST Wrestling, Pro Wrestling Dot Net, PWMania,
WWE.com). Además varios shows de 2026 comparten taping block (misma
grabación emitida en semanas sucesivas), así que una sola búsqueda por
fecha de grabación resolvía ciudad/recinto para varias fichas a la
vez.

## Discrepancias (ficha + detalle)

1. **`archive/matches/2026-05-02-hijo-del-vikingo-vs-mini-vikingo-aaa-worldwide.md`**
   — la ficha registra como hecho que **gana Hijo del Vikingo** con
   Phoenix 630. Múltiples fuentes de research (F4W/WON, Pro Wrestling
   Dot Net, Fightful) coinciden en lo contrario: **gana Mini
   Vikingo**, descrito como uno de los upsets más grandes de la
   historia de la lucha libre — Vikingo powerbombea a Mini (que
   kickea out), va a usar una silla, **Dr. Wagner Jr. interviene con
   un Wagner Driver sobre Vikingo** (no sobre Mini), y Mini remata con
   **630 sobre Vikingo**. El research invierte ganador, quién recibe
   la intervención de Wagner y quién ejecuta el movimiento final. No
   se reescribió el frontmatter — contradice un visionado directo
   declarado verbatim por el Vehemiurgo — solo se agregó la nota
   completa en `## Pendientes` para que decida.

2. **`archive/matches/2026-04-18-dinamico-hiedra-vs-iguana-lola-aaa-worldwide.md`**
   — la ficha afirma explícitamente que la "Lola" de este match **no
   es Lola Vice** y linkea a una ficha separada (`lola-aaa.md`).
   Múltiples fuentes (F4W/WON, Fightful, Pro Wrestling Dot Net, POST
   Wrestling, Cagematch) identifican sin ambigüedad a la compañera de
   Mr. Iguana como **Lola Vice** — la misma campeona cross-promotion
   NXT/AAA que aparece en otras fichas de este mismo barrido (p. ej.
   `2026-03-28-money-machine-hiedra-vs-fenix-lola-iguana...md`). Se
   registró la discrepancia sin tocar la identidad declarada ni la
   ficha `lola-aaa.md`.

3. **`archive/matches/2026-03-21-money-machine-hiedra-vs-fenix-lola-iguana-aaa-rey-de-reyes-week-2.md`**
   — el dictado fecha el show el **28/3/2026**, pero WWE.com/Cagematch
   registran "Rey de Reyes Week 2" (AAA on FOX #10, Part 2) como
   transmitida/tapeada el **21/3/2026**. No se reescribió `fecha` sin
   una segunda fuente que confirme a qué corte semanal correspondió lo
   que vio el Vehemiurgo.

Las tres quedaron como ítems de `## Pendientes` en sus fichas, con
`[ ]` (no `[x]`), para que el Vehemiurgo las resuelva con autoridad
editorial.

## Qué quedó sin cubrir y por qué

- **Referees de WWE y AAA sin bump/spot notable** (la gran mayoría de
  los pendientes de `referee` en los tres lotes): no se reportan en
  ningún recap/dirt sheet accesible vía WebSearch. Patrón consistente
  en decenas de intentos — a partir de lote 08 se dejó de insistir más
  de una búsqueda por show en este tipo de dato específico para no
  gastar presupuesto sin rendimiento.
- **Duración exacta de segmentos no-match** (promos, backstage,
  videos de hype): mismo problema estructural — ningún agregador
  cronometra segmentos.
- **2026-06-13 `los-vipers-vs-fiscal-octagon-parka-aaa-worldwide.md`**:
  pendiente editorial previo pedía desambiguar la sede de grabación
  (Arena Monterrey 31/5 vs Gimnasio Juan de la Barrera CDMX, fuentes
  en conflicto). El research de esta sesión no encontró una fuente que
  resuelva el conflicto; queda igual que antes.
- **2026-06-20 segmentos** (`dominik-mysterio-promo`,
  `promo-video-fenix-vs-laredo`): solo faltaba `duracion`, no
  encontrada (caso general arriba).
- **2026-07-11 y 2026-07-18** (Money Machine vs Noisy Boy/Epydemius
  Jr.; La Hiedra/Laredo Kid vs Wilde/Apache; Texano/Wagner/Abismo):
  ya estaban extensamente investigadas por research previo
  (2026-08-01); esta sesión solo pudo confirmar lo ya registrado y no
  halló referee ni, en un caso, duración exacta.

## Notas de método

- Presupuesto de WebSearch usado con moderación: una o dos búsquedas
  por show, reutilizadas para todas las fichas de esa fecha cuando fue
  posible (patrón explícito del README). No se gastó presupuesto en
  sub-agentes — todo el research se hizo directo en esta sesión,
  dado el volumen manejable de fichas por lote.
- Cuando una fuente única parecía dudosa (p. ej. una duración de
  3:19 para Zilla Fatu vs Tristan Angels que no cuadraba con el rango
  9:27–9:39 ya registrado) se descartó en vez de registrarla como
  tercera fuente en desacuerdo, por tratarse casi con certeza de un
  error de resumen del buscador y no de una fuente real adicional.
- Todas las fichas tocadas pasan `bin/lint_archivo.py --pre-commit`
  con 0 errores (15 warnings basales, preexistentes, no relacionados
  con este barrido).
