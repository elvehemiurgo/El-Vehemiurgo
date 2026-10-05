# Informe — claude/barrido-hija-6 (lotes 16, 17, 18)

Sesión hija del barrido de datos duros `barrido-datos-duros-2026-10`.
Procesó `lote-16.md` (CZW), `lote-17.md` (AEW) y `lote-18.md` (AEW), en
ese orden, vía sub-agentes de research con WebSearch. Tres commits —
uno por lote — más un commit intermedio de progreso en lote 16 (ver
nota de proceso al final). Todo en la rama `claude/barrido-hija-6`,
empujada a `origin`.

## Conteos por lote

| Lote | Empresa / periodo | Fichas en el lote | Fichas editadas | Ítems de dato duro cerrados | Discrepancias | WebSearch usadas |
|---|---|---|---|---|---|---|
| 16 | CZW, 2017-09-09 a 2019-04-13 | 36 | 5 | 4 (finish ×3, recinto ×2) | 1 | 20 |
| 17 | AEW, 2021-11-13 a 2026-05-24 | 44 | 44 | ciudad/recinto en casi todas; duración/finish/ganador en la mayoría | 4 | 35 |
| 18 | AEW, 2026-05-27 a 2026-07-08 | 46 | 46 | ciudad/recinto en todas; duración/finish/ganador donde la fuente lo permitió | 2 | 19 |
| **Total** | | **126** | **95** | | **7** | **74** |

El lote 16 (CZW indie 2017-2019) resultó muy pobre en cobertura
secundaria: la mayoría de los shows no tienen recaps con play-by-play
disponibles vía WebSearch, a diferencia de AEW (lotes 17-18), donde
Fightful/PWTorch/Wrestling Inc./POST Wrestling/Cageside Seats/F4WOnline
documentan casi toda la card con tiempos.

## Discrepancias (7)

Ninguna se resolvió reescribiendo el hecho que la ficha afirma — todas
quedaron anotadas en `## Pendientes` con el prefijo **Discrepancia
(research 2026-10-05)**, para research dedicado o verificación contra
video, como indica la regla 5 del README.

1. **`archive/matches/2017-12-09-tag-titles-4-way-the-rep-gana-czw-cage-of-death-19.md`**
   (lote 16) — la ficha registra una "corrección de research" previa
   que da el cuarto equipo como Alex Reynolds & Matt Palmer; una fuente
   agregada vía WebSearch (profightdb/Cagematch, Fightful) lo da como
   Alex Reynolds & **Dan Barry** — coincidiendo con el dictado original
   del Vehemiurgo, no con la "corrección".
2. **`archive/segments/2026-04-01-mjf-vs-speedball-contract-signing-aew-dynamite.md`**
   (lote 17) — la ficha la registra como firma MJF vs Bailey; los
   recaps dicen que el segmento de apertura fue la firma MJF vs Kenny
   Omega para Dynasty, con el cruce de Bailey dentro del mismo segmento.
3. **`archive/matches/2026-04-08-united-empire-showcase-aew-dynamite.md`**
   (lote 17) — research identifica esta lucha como el main event
   8-man tag (United Empire vs Death Riders), no un "showcase" menor.
4. **`archive/matches/2026-05-13-darby-allin-vs-takeshita-aew-dynamite.md`**
   y **`archive/segments/2026-05-13-mjf-darby-contract-signing-aew-dynamite.md`**
   (lote 17) — ciudad/recinto discrepante entre fuentes para el mismo
   show del 13/5: North Charleston Coliseum (SC) vs Harrah's Cherokee
   Center (Asheville, NC). No resuelto.
5. **`archive/matches/2026-05-24-cope-cage-vs-ftr-aew-double-or-nothing.md`**
   (lote 17) — la ficha (verbatim del Vehemiurgo) dice "Street Fight";
   varias fuentes describen oficialmente el match como "Tag Team 'I
   Quit' Match". No se tocó `estipulacion`.
6. **`archive/matches/2026-05-30-hazuki-vs-maya-world-aew-collision.md`**
   (lote 18) — la ficha registra victoria de Maya World; Wrestling Inc.
   registra lo contrario: Hazuki ganó en 10:20.
7. **`archive/matches/2026-06-06-dogs-vs-guns-rematch-aew-collision.md`**
   y su segmento asociado (lote 18) — la ficha registra un tag team
   rematch; las fuentes no listan ese match en la card del 6/6 —
   registran un singles Clark Connors (The Guns) derrota a Juice
   Robinson (The Dogs) en 13:10, con interferencia de Finlay.

## Lo que quedó sin cubrir y por qué

- **`referee`**: no se cerró en prácticamente ninguna de las 126
  fichas de los tres lotes. Ni los recaps indie de CZW ni los de AEW
  (Fightful, PWTorch, Wrestling Inc., POST Wrestling, etc.) reportan
  nombres de árbitro de forma rutinaria — es un dato que casi nunca
  aparece en cobertura textual, solo sería verificable contra video.
- **`duracion`** de la mayoría de los *segments*/promos: los recaps
  dan tiempos de matches, casi nunca de segmentos no competitivos.
- **CZW (lote 16) en general**: 31 de 36 fichas no se tocaron porque
  WebSearch no devolvió recaps con datos duros confiables para esos
  shows indie de 2017-2019 (PWPonderings, OWW, Fightful y Gerweck
  fueron las únicas fuentes que aportaron algo, y solo para 4
  fichas). El resto de los placeholders de duración/referee/finish de
  ese lote siguen abiertos — no por falta de intento, sino por
  ausencia real de fuente secundaria indexada.
- Varios *finish* exactos en lote 17/18 cuando la fuente confirmaba
  ganador y duración pero no el movimiento final (ej. Cope & Cage vs
  FTR, Darby vs Takeshita 13/5) — quedaron marcados `[parcial]` o con
  nota de "mecanismo no detallado en las fuentes".
- Rosters completos de multi-man matches (Forbidden Door 6v6,
  gauntlet de Beach Break) — solo se confirmaron participantes
  parciales vía los shows que los armaron, no el orden/entrada
  completo.
- `linea_textual` de promos (fuera de alcance: no es un campo de
  "dato duro" según el README, así que no se persiguió activamente).

## Nota de proceso

Un hook local (`~/.claude/stop-hook-git-check.sh`) bloquea el fin de
turno si hay cambios sin commitear. Como los sub-agentes de research
corren en background y van editando fichas mientras la sesión
principal espera su resultado, el hook disparó una vez a mitad del
lote 16 con una sola ficha ya editada; se hizo un commit intermedio
("barrido datos duros lote 16 (parcial)") para no perder el trabajo,
y luego el commit final de cierre del lote con el resumen completo.
Lotes 17 y 18 cerraron en un solo commit cada uno. No afecta el
contenido ni la integridad de los datos, solo la cantidad de commits
del lote 16 (2 en vez de 1).

En cada reanudación también apareció sistemáticamente un diff
cosmético en `bin/__pycache__/archivo_lib.cpython-311.pyc` (bytecode
compilado al correr `bin/lint_archivo.py`); se descartó con `git
checkout --` en cada ocasión y nunca se commiteó.

## Verificación

`python3 bin/lint_archivo.py --pre-commit` → 0 errores en los tres
commits de cierre (15 warnings preexistentes, no relacionados con este
barrido).
