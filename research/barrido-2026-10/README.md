# Barrido de datos duros 2026-10 — instrucciones para sesiones hijas

Research `barrido-datos-duros-2026-10` (ver `research/pending.md`).
Cada sesión hija procesa **sus lotes** (`lote-NN.md` de esta carpeta)
y empuja a **su propia rama**; la sesión principal integra.

## Tarea

Cerrar pendientes de **datos duros** (duración, referee, finish/
ganador/resultado, ciudad/recinto) en las fichas de match/segment
listadas en tus lotes. Cada línea: `ruta :: placeholders del
frontmatter :: pendientes abiertos`.

**Saltar** toda ficha cuyo `fuentes_principales` ya contenga
"pendientes-fichas-sep26", "research 2026-09-30" o "research
2026-10-0".

## Research

- **Presupuesto**: la sesión tiene ~200 WebSearch en total (compartidas
  con tus sub-agentes). Sé eficiente: **una o dos búsquedas por show**
  suelen traer la card completa con tiempos; reutilízalas para todas
  las fichas de ese show. Prioriza por show, no por ficha.
- WebFetch y curl están bloqueados por el proxy en casi todos los
  sitios (Cagematch/Wikipedia 403). Trabaja con snippets.
- Nunca inventar. Una sola fuente débil → valor + " [una fuente]".
  Fuentes en desacuerdo → las dos ("12:05 / 12:30 según fuente").
  **No usar conocimiento propio sin fuente** para datos duros.

## Reglas de edición (estrictas)

1. Frontmatter: reemplazar los placeholders de duracion / referee /
   finish / ganador / ciudad / recinto por el valor hallado (mismo
   estilo de comillas). Ningún otro campo, salvo
   `ultima_actualizacion: 2026-10-05` y una línea en
   `fuentes_principales`:
   `  - "Sub-agente barrido-datos-duros-2026-10 (research 2026-10-05) — WebSearch (<sitios>); WebFetch bloqueado por egress"`
   — solo en fichas que cambiaste.
2. `## Pendientes`: "- [ ]" → "- [x] … → <valor> (<fuente>)" en ítems
   de dato duro resueltos; si es parcial, partir en resuelto/abierto.
   No tocar ítems editoriales, de verbatim/video o de fichas de people.
3. Si el cuerpo repite el mismo placeholder, actualizarlo igual.
4. **Nunca** tocar los blockquotes verbatim del Vehemiurgo ("> *\"…"
   y la sección "Cita verbatim"), `clases_vehemiurgo`,
   `calificacion_vehemiurgo`, slugs, nombres de archivo, `index.md`,
   vistas derivadas (`archive/topics/*`), notebooks, ni archivos fuera
   de tus lotes.
5. Si un hallazgo **contradice** lo que la ficha afirma como hecho
   (ganador, fecha, show, participantes), no reescribir: agregar
   "- [ ] **Discrepancia (research 2026-10-05)**: <ficha> vs <fuente>
   (<fuente>)".
6. Prosa en español, concisa.

## Cierre

1. `python3 bin/lint_archivo.py --pre-commit` → 0 errores.
2. Un commit por lote: "barrido datos duros lote NN: X fichas, Y ítems
   cerrados, Z discrepancias", con el trailer de atribución de la
   sesión.
3. `git push -u origin <tu rama>`.
4. Al final, escribe `research/barrido-2026-10/informe-<rama>.md`:
   conteos por lote, lista de discrepancias (ficha + detalle), qué
   quedó sin cubrir y por qué. Commit + push.
