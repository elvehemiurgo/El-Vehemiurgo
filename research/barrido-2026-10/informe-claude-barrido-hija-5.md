# Informe — claude/barrido-hija-5

Sesión hija del research `barrido-datos-duros-2026-10`. Lotes
asignados: `lote-13.md` (TNA, 12 shows feb–abr 2026), `lote-14.md`
(TNA, 2 shows abr 2026), `lote-15.md` (CZW, 7 shows 2013–2017).

Método: un sub-agente de research por show (o par de shows
contiguos) vía WebSearch, editando directamente las fichas
asignadas bajo las reglas estrictas del `README.md` del barrido.
Tres commits, uno por lote, en ese orden. Push a
`claude/barrido-hija-5`. No se abrió pull request.

## Conteos por lote

| Lote | Fichas en el lote | Fichas con al menos un cambio | Items de Pendientes cerrados | Discrepancias |
|---|---|---|---|---|
| 13 | 35 | 35 | 44 | 7 |
| 14 | 11 | 1 | 1 | 0 |
| 15 | 24 | 24 | 26 | 0 |
| **Total** | **70** | **60** | **71** | **7** |

Nota sobre "fichas con al menos un cambio": en el lote 13 cuento
35 porque toda ficha tocada recibió como mínimo el cierre de
`ciudad`/`recinto` por cruce con el taping, aunque algunas no
cerraron `referee`/`finish`/`duracion`. Diez fichas del lote 14
quedaron sin ningún cambio (ver abajo, presupuesto agotado).

## Discrepancias (7, todas en lote 13 — lote 14 y 15 sin discrepancias)

1. **`archive/matches/2026-03-19-brian-myers-vs-moose-first-time-ever-tna-impact.md`**
   — la ficha data el match el 19/2/2026, pero la card completa y
   confirmada de ese episodio (Nashville, The Pinnacle) no incluye
   a Myers vs Moose. El match con el setup descrito por el
   Vehemiurgo (veto de Santino a The System del ringside,
   spear-squash) corresponde al TNA Impact del **19/3/2026**
   (Gateway Center Arena, College Park, GA). No se reescribió la
   fecha ni los campos de frontmatter; se dejó anotado en
   Pendientes como discrepancia para que el Vehemiurgo decida si
   renombrar/reubicar la ficha (fuera del alcance de este barrido:
   la regla 4 del README prohíbe tocar slugs/nombres de archivo).
2. **`archive/matches/2026-04-02-arianna-grace-vs-xia-brookside-tna-impact.md`**
   — `estipulacion: "standard"` en la ficha, pero PWTorch,
   Fightful, Slam Wrestling, WrestleView y Wrestling Inc coinciden
   en que fue defensa titular del **TNA Knockouts World
   Championship**. No se reescribió `estipulacion` (no era
   placeholder de datos duros); queda anotado en Pendientes.
3. **`archive/matches/2026-03-26-six-woman-tag-tessa-myla-grace-hudson-tna-impact.md`**
   — la ficha agrupaba a Tessa Blanchard junto a Myla Grace y
   Harley Hudson. Las fuentes (ewrestling, rajah, wrestlinginc)
   confirman que Tessa integraba el trío **ganador** (con Mila
   Moore y Victoria Crawford) **enfrentando** a Jody Threat, Myla
   Grace y Harley Hudson — no acompañándolas. No se tocó el campo
   `participantes`; discrepancia anotada en Pendientes.
4. **`archive/matches/2026-04-11-hardys-vs-the-system-tag-title-tna-rebellion.md`**,
5. **`archive/matches/2026-04-11-mike-santana-vs-eddie-edwards-tna-world-title-rebellion.md`**,
6. **`archive/matches/2026-04-11-mustafa-ali-vs-trey-miguel-international-tna-rebellion.md`**,
7. **`archive/segments/2026-04-11-eric-young-promo-regreso-ec3-tna-rebellion.md`**
   — las cuatro fichas de TNA Rebellion 2026 traían
   `attendance_anunciada: "2.969 [una fuente]"`. Wikipedia reporta
   **3.929** pagados para el evento; una base de datos secundaria
   (profightdb) coincide con 2.969. Dos fuentes contra una, sin
   resolver — anotado como discrepancia idéntica en las cuatro
   fichas, sin tocar el campo.

## Qué quedó sin cubrir y por qué

### Lote 14 — cobertura mínima por agotamiento de presupuesto WebSearch

El sub-agente de TNA Impact 23/4 y 30/4 reportó que el presupuesto
de WebSearch de la sesión (~200, compartido entre los 10
sub-agentes lanzados en paralelo para los tres lotes) se agotó tras
apenas ~5 búsquedas efectivas, casi al inicio de su tanda. Solo se
cerró `duracion` de **Matt Hardy vs Dutch** (23/4). Quedan
**intactos, sin haber sido buscados**:

- `referee` de bear-bronson-vs-nic-nemeth, mike-santana-vs-rich-swann
  (world title), mustafa-ali-vs-adam-brooks, vincent-vs-jeff-hardy,
  y el propio matt-hardy-vs-dutch.
- `duracion` de los 6 segmentos del 23/4 y 30/4 (ec3-promo-trial-by-combat,
  kazarian-burla-elijah-guitar-strap, rich-swann-promo-pre-titular,
  the-system-promo-parking-lot, tomas-backstage-swann-santana,
  kazarian-promo-guitar-strap-match).
- El show completo del **30/4** no llegó a tener ninguna búsqueda
  dedicada (solo el cruce de recinto no aplicó porque no se buscó
  nada de ese show).

Esto no es "buscado y sin hallazgo" sino **no buscado** — el
sub-agente lo marca explícitamente así para distinguirlo del resto
del barrido, donde "sin cobertura" sí implica búsqueda fallida.
Recomendación para una sesión de seguimiento: relanzar este tramo
con presupuesto de WebSearch fresco.

### Lote 13 — referees y algunos datos puntuales sin cobertura de prensa

Patrón consistente en casi todos los shows de TNA Impact/Rebellion/
Sacrifice 2026: **los recaps de prensa (PWTorch, Fightful, Wrestling
Inc, PostWrestling, F4WOnline, Cageside Seats, 411mania, etc.) casi
nunca nombran al réferi** salvo que haya un spot explícito de
réferi (bump, distracción con nombre propio — como el caso resuelto
de "Alice Lane" en Mike Santana vs Eddie Edwards). Quedan `referee:
"[verif]"` intactos en la gran mayoría de fichas de este lote: las
5 de TNA Rebellion 11/4, ambas de Impact 16/4, Hometown Man vs
Kazarian, Elijah vs AJ Francis, Moose vs Cedric Alexander, las 6 de
Sacrifice 27/3 (salvo Moose vs Eddie Edwards, resuelto), las 3 de
Impact 26/3, y las de Impact 2/4 y 9/4.

Casos puntuales sin cobertura por agotamiento parcial de
presupuesto (no solo falta de fuente):

- **`archive/matches/2026-04-09-dani-luna-tna-impact.md`** — el
  sub-agente llegó a este match con el presupuesto casi agotado;
  solo cerró `ciudad`/`recinto` por cruce de taping. Rival,
  estipulación, finish, ganador, referee y duración **no se
  llegaron a buscar**.
- **`archive/matches/2026-04-09-hardys-vs-righteous-tna-impact.md`**
  — mismo caso, el único placeholder (`referee`) no se llegó a
  buscar puntualmente.
- **`archive/matches/2026-04-09-mustafa-ali-vs-trey-miguel-tna-impact.md`**
  y **`archive/matches/2026-04-09-myla-grace-vs-elayna-black-tna-impact.md`**
  — solo `ciudad`/`recinto` cerrados por cruce; el resto de
  placeholders no se buscó.
- **`archive/matches/2026-02-13-elegance-brand-vs-brookside-hartwell-tna-no-surrender.md`**
  — `referee`, único placeholder, sin cobertura tras búsqueda
  real (PWTorch, POST Wrestling, Fightful, Diva Dirt, Cagematch,
  SEScoops consultados).
- **`archive/matches/2026-04-16-aj-francis-vs-kc-navarro-tna-impact.md`**
  — el nombre del finisher de AJ Francis sigue sin resolverse del
  todo: una segunda fuente (Blog of Doom/eWrestling) corrobora
  "chokeslam" sobre "Down Payment", pero no hay cruce perfecto; la
  duración quedó como rango "~7:01–7:05 [2 fuentes, sin cruce
  exacto]". `referee` sin cobertura.
- **`archive/matches/2026-03-27-moose-vs-eddie-edwards-tna-sacrifice.md`**
  — se identificó que *Alice Lane* fue la réferi reconocida del
  show de Sacrifice 2026 (por su manejo de la lesión de Maclin en
  el main event), pero ninguna fuente confirma que haya sido
  específicamente la réferi de este match (una fuente incluso se
  contradecía a sí misma); por la regla de no inventar, el
  placeholder quedó intacto.

### Lote 15 — referees de CZW casi sin cobertura; algunos finishes sin confirmar

Cagematch, la fuente habitual para réferis de shows indie como CZW,
es inalcanzable vía WebFetch (bloqueado por el proxy en todos los
dominios) y los recaps de prensa indie (Wrestleview,
wrestlingrecaps.com, 411mania, PWTorch) rara vez nombran árbitros.
Excepción: para **CZW Down with the Sickness (9/14/2013)** se halló
vía snippet de IMDb que **Kris Levin** fue el único réferi
acreditado en el cast de esa taping, y se aplicó a las 6 fichas de
ese show. Para **CZW Cerebral (10/12/2013)** IMDb acredita **dos**
réferis (Kris Levin y Nick Papagiorgio) sin forma de atribuir cuál
trabajó cada lucha específica — ahí el placeholder quedó intacto en
4 de las 6 fichas (las otras 2 ya tenían réferi especial declarado
en el cuerpo: DJ Hyde, o se resolvió `finish`).

`referee` sin cobertura en el resto del lote: **todas** las fichas
de Cage of Death XV (2013-12-14), High Stakes 5 (2014-03-08),
Awakening (2017-01-14), Sacrifices (2017-05-13), Evilution
(2017-07-08) y Once in a Lifetime (2017-08-05).

`finish` sin cobertura (mecanismo exacto del pin/sumisión no
reportado por ninguna fuente): la mayoría de los matches de Cage
of Death XV, varios de High Stakes 5, Private Party vs Dub Boys y
Shane Strickland vs Sami Callihan (Sacrifices), MJF vs Trevor Lee y
The Rep vs Private Party (Evilution), MJF vs John Silver y Shane
Strickland vs Masada (Once in a Lifetime).

`duracion` sin cobertura en los segmentos backstage/promo de todo
el lote (Jake Crist/OI4K, MJF in-ring Awakening, promos de
Callihan/cierre en Evilution, booking CCK/The Rep y promo
Rush/Janela en Once in a Lifetime) — ningún recap documenta
duración de segmentos no competitivos.

## Verificación

`python3 bin/lint_archivo.py --pre-commit` → **0 errores** en los
tres commits (17 warnings, mismos preexistentes — variantes de
nombre en citas verbatim/`calificacion_vehemiurgo` que no se tocan
por regla, no introducidas por este barrido).

## Commits

- `barrido datos duros lote 13: 35 fichas TNA (12 shows feb-abr 2026), 44 items cerrados, 7 discrepancias`
- `barrido datos duros lote 14: 1 ficha cerrada de 11 (presupuesto WebSearch agotado), 0 discrepancias`
- `barrido datos duros lote 15: 24 fichas CZW (7 shows 2013-2017), 26 items cerrados, 0 discrepancias`

Rama: `claude/barrido-hija-5`, push a `origin/claude/barrido-hija-5`.
Sin pull request.
