# Informe — barrido datos duros 2026-10, sesión `claude-barrido-hija-1`

Rama: `claude/barrido-hija-1`. Tres lotes procesados en orden, un commit
por lote, research vía WebSearch (WebFetch bloqueado por el proxy en
Cagematch/Wikipedia/wikis en este environment — se trabajó con
snippets en todos los casos). Presupuesto de WebSearch usado: ~45
búsquedas de las ~200 disponibles para la sesión; no se agotó el
presupuesto, el barrido se cerró porque los tres lotes quedaron
procesados.

## Conteos por lote

| Lote | Fichas tocadas | Ítems de pendientes cerrados (aprox.) | Discrepancias nuevas |
|---|---|---|---|
| 01 (OTROS) | 11 | 13 | 2 (Cody/Omega G1 Special: fecha + título en disputa) |
| 02 (WWE, 1984–2026-04) | 39 | ~45 | 1 (Bret Hart vs The Mountie: ciudad) |
| 03 (WWE, 2026-06/07) | 16 | ~18 | 1 (Fénix/Vikingo: nombre del finisher) |
| **Total** | **66** | **~76** | **4** |

Todas las fichas pasaron `bin/lint_archivo.py --pre-commit` con 0
errores antes de cada commit.

## Discrepancias documentadas (requieren atención editorial)

1. **`archive/matches/2018-06-30-cody-rhodes-vs-kenny-omega-njpw-g1-special-san-francisco.md`**
   — la ficha fecha el show el 2018-06-30; las fuentes consultadas
   (F4WOnline, Cageside Seats, Wrestleview) lo fechan el 2018-07-07.
   Además, la ficha describe la estipulación como IWGP US Heavyweight
   Championship, pero las fuentes indican que ese match específico
   fue por el IWGP Heavyweight Championship (el título de EE.UU. se
   disputó aparte, Juice Robinson vs Jay White, el mismo show).
   **No se tocó `estipulacion`/`tipo_match`** — son discrepancias de
   hecho, no placeholders de este lote. Verificar contra NJPW
   primario.

2. **`archive/matches/1992-10-26-bret-hart-vs-the-mountie-wwf.md`**
   — las fuentes consultadas ubican un WWF Title dark match Bret Hart
   vs The Mountie el 26 oct 1992 en el Prairie Capitol Convention
   Center, Springfield, IL (TV taping de Survivor Series Showdown),
   lo que contradice la ciudad ya registrada en la ficha (Saskatoon,
   Saskatchewan). No se tocó el campo `ciudad` (no es placeholder de
   este lote). Verificar Saskatoon vs Springfield IL contra fuente
   primaria.

3. **`archive/matches/2026-07-03-rey-fenix-vs-hijo-del-vikingo-wwe-smackdown.md`**
   — 411mania describe el movimiento final como "Black Fire Driver
   (Spinning Sitout Kinniku Buster)", distinto del "Mexican Muscle
   Buster" que registraba el research previo (2026-08-01). No se
   sobreescribió `finish` — ambas versiones quedan anotadas en
   pendientes hasta verificar contra video.

4. (Menor, no crítica) **`archive/matches/1984-04-01-paul-orndorff-vs-jimmy-jackson.md`**
   — se halló un Orndorff vs Jimmy Jackson homónimo en WWF All Star
   Wrestling, 21 ene 1984, Hamburg PA, pero no se pudo confirmar que
   sea la misma fecha que la ficha (1 abr 1984); queda anotado sin
   aplicarse.

## Correcciones de hecho sin reescritura retroactiva (fuera de alcance)

- **AJ Styles vs Homicide (IWC 2004)**: la fecha real del evento es
  2004-04-17 ("A Gangsta's Retribution"), no 2004-01-01 (placeholder).
  No se tocó el campo `fecha` — anotado en pendientes para que la
  sesión principal lo corrija.
- **Ricky Saints vs Carmelo Hayes, 15/5/2026**: el resultado real de
  ese match es que **ganó Carmelo Hayes** (rollup con las cuerdas),
  no `[verif]` como tenía registrado el archivo. Confirmado contra
  WWE.com, Fandom y Pro Wrestling Dot Net. Anotado en la ficha del
  19/6 (que referenciaba la incertidumbre); la ficha del propio
  15/5 (`archive/matches/2026-05-15-carmelo-hayes-vs-ricky-saints-wwe-smackdown.md`)
  no estaba en mis lotes y no se tocó.

## Lo que quedó sin cubrir y por qué

- **La inmensa mayoría de los pendientes de `referee`** en los tres
  lotes (indies/puroresu de los lotes 01-02, y prácticamente todo el
  lote 03 de TV semanal WWE 2026) quedó sin cerrar. No existe fuente
  pública que documente árbitros de shows de TV semanal o indies de
  décadas pasadas — cerrar esto sin fuente sería fabricar el dato,
  prohibido por las reglas del barrido.
- **Duraciones exactas de segmentos/promos** (no matches) casi nunca
  están cronometradas en recaps de prensa — quedaron pendientes salvo
  donde la propia ficha ya tenía un dato previo que pude confirmar
  (venues/ciudades sí se consiguieron para casi todos los segmentos
  de WWE 2026 vía los previews/resultados oficiales de cada show).
- **1982-09-11 Terry Funk vs Stan Hansen (AJPW)**: no se pudo
  confirmar ciudad/recinto con una fuente directa fiable (un
  resultado de búsqueda sugería Korakuen Hall pero era una síntesis
  del motor de búsqueda sin cita textual verificable) — se descartó
  aplicar para no fabricar con baja confianza.
- **1998-09-21 Volk Han vs Kiyoshi Tamura (RINGS Fighting Integration VI)**
  y **1997-09-26 Volk Han vs Kiyoshi Tamura (RINGS Fighting Extension VII)**:
  duración/referee no documentados en snippets accesibles.
- **MLW Slaughterhouse 2025-10-04**: referee no documentado para
  ninguno de los 5 matches del lote; sí se cerraron los resultados de
  semifinal/final del Opera Cup 2025 (Místico campeón) como contexto
  adicional en las fichas de Místico/Guerrero y el segmento de Aries.
- **Oba Femi vs Dominik Mysterio (Raw 15/6/2026)**: no se halló
  confirmación de duración en las fuentes consultadas (el research
  previo cita un valor de wiki de nivel 3 sin segunda fuente); queda
  como estaba.
- **Jacy Jayne vs Rhea Ripley (SmackDown 24/4/2026)**: no se encontró
  un resultado de pin explícito en las fuentes — consistente con la
  lectura ya registrada en la ficha de que el booking priorizó la
  emboscada de debut sobre un resultado formal. No se forzó un
  ganador.

## Notas de proceso

- Lote 01 contenía material histórico (1963-2019) de alta dificultad
  de research — varias fichas (Rikidōzan/Destroyer 1963, Terry
  Funk/Hansen 1982, RINGS 1997-98) ya tenían trabajo de sub-agentes
  previos muy denso; el barrido solo pudo cerrar los huecos que esos
  sub-agentes habían dejado explícitamente abiertos con `[verif]`.
- Lote 02 y 03 (bloque WWE 2013-2026) tuvieron research mucho más
  productivo — casi todas las fichas de shows WWE 2026 (NXT/Raw/
  SmackDown/PLE) obtuvieron ciudad, recinto, ganador, finish y/o
  duración con 1-2 búsquedas por show, reutilizadas entre todas las
  fichas del mismo card tal como pedía el README.
- Siempre que una ficha ya tenía research de sub-agentes previos
  (2026-08-01, 2026-09-20, etc.) con detalle narrativo rico, el
  barrido se limitó a **confirmar o corregir datos duros puntuales**
  (duración, ciudad/recinto, ganador) sin tocar la prosa editorial,
  las citas verbatim, las clases Vehemiurgia ni los cross-links.
- Ningún dato se escribió sin fuente. Donde solo había una fuente
  débil, se marcó `[una fuente]`. Donde dos fuentes discrepaban, se
  registraron ambas. Donde no había fuente, el placeholder quedó
  intacto.
