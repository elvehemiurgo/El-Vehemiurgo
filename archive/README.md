# Archive — Expedientes vivos

El archivo del Vehemiurgo. Cada archivo acá es un **fact-sheet vivo**: se
abre cuando una pieza lo demanda, se va llenando con cada nueva
investigación, y queda como referencia compartida para no repetir trabajo.

Esto **no es Wikipedia**. No buscamos cobertura completa: buscamos lo que
sirve para escribir editorial old-school. Datos duros (fechas, gates,
contratos, cifras), contexto financiero y de poder, anécdotas backstage
documentadas, hilos de podcast on-record, vínculos familiares, citas con
fuente.

## Categorías

| Carpeta | Qué guarda |
|---|---|
| `people/` | Luchadores, promotores, bookers, comentaristas, ejecutivos, periodistas. |
| `promotions/` | Empresas: WWE/WWF, NWA, AWA, AJPW, NJPW, AAA, CMLL, ROH, AEW, TNA, ECW, los territorios, las indies relevantes. |
| `programs/` | Programas TV: Raw, SmackDown, Nitro, Thunder, Dynamite, Collision, Saturday Night's Main Event, World of Sport, AJPW Saturday, etc. |
| `events/` | PPVs, supershows, eventos clave individuales (WrestleMania III, Starrcade '83, Tokyo Dome 1/4, etc.). |
| `eras/` | Periodos definidos: Era de los Territorios, Rock 'n' Wrestling, Monday Night Wars, Attitude Era, Ruthless Aggression, era PG, Reality Era, era post-COVID, etc. |
| `families/` | Familias de wrestling (Hart, Anoa'i, Funk, Guerrero, Von Erich, Brisco, Briscoe, Rhodes, Dynamite/Roddy lineages, etc.). |
| `contracts/` | Contratos relevantes documentados, modelos contractuales (downside guarantees, independent contractor, AEW vs WWE, NJPW). |
| `interviews/` | Entrevistas históricas relevantes con cita y resumen. |
| `podcasts/` | Episodios de podcast con material on-record útil (Cornette, Conrad Thompson, Ross, POST, WON, Talk Is Jericho, etc.). |
| `matches/` | Registro personal del Vehemiurgo: matches vistos, con storyline, datos financieros, planes de booking, *look-backs* y review propia. Plantilla y workflow en `matches/README.md`. |
| `segments/` | Registro personal del Vehemiurgo: segmentos / promos / momentos puntuales (no matches enteros), con líneas textuales, contexto del storyline, voces y review propia. Plantilla y workflow en `segments/README.md`. |

## Naming

`<categoria>/<slug>.md` en kebab-case, sin acentos.

Ejemplos:
- `archive/people/jim-cornette.md`
- `archive/promotions/jim-crockett-promotions.md`
- `archive/eras/era-territorios-nwa.md`
- `archive/events/starrcade-1983.md`
- `archive/podcasts/jim-cornette-experience.md`

## Plantilla

Todo fact-sheet usa `templates/fact-sheet.md` como punto de partida y se
adapta a la categoría.

## Cómo crece

- Cada pieza nueva (editorial, review, dossier) **actualiza el archivo**
  con los datos verificados que aportó.
- Si una pieza usó una entrevista o un podcast como fuente, queda
  registrado en `interviews/` o `podcasts/` con cita.
- Si una pieza descubrió un dato contractual o financiero, queda en
  `contracts/` o en el fact-sheet de la persona/empresa.
- Si una afirmación quedó marcada como rumor, se registra como tal con la
  fuente original. **No subimos rumor a hecho** sin nueva evidencia.

## Lo que el archivo no es

- No es enciclopedia exhaustiva.
- No es wiki para fans.
- No es lista de logros / records (eso lo tienen Cagematch y Wikipedia y
  no vamos a competir ahí).
- Es **memoria operativa de un periodista old-school**: lo que necesito a
  mano para escribir bien la próxima pieza.
