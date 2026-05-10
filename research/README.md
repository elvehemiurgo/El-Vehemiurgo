# Research — Investigaciones delegadas

Carpeta operativa de **investigaciones delegadas a sub-agentes**. Acá vive
el dashboard único de qué se está investigando, qué volvió, qué quedó
sin cerrar.

> "Quiero […] tener secciones de investigaciones pendientes y las
> sub-investigaciones que te delego también, y poder estar los dos bien
> al día y sincronizados." — El Vehemiurgo, 9 may 2026.

---

## Estructura

- **`pending.md`** — dashboard activo de toda investigación abierta
  (en cola, en curso, completada pero pendiente de integrar).
- **`closed.md`** — archivo de investigaciones completadas e
  integradas, con cross-link al archivo donde el material vive ahora.

## Estados de una investigación

- **`pendiente`** — declarada, no lanzada todavía.
- **`en-curso`** — sub-agente lanzado, esperando dossier.
- **`completada-sin-integrar`** — sub-agente devolvió dossier, no se
  ha distribuido a archivos finales.
- **`integrada`** — material distribuido al/los archivo(s)
  correspondiente(s); fila se mueve a `closed.md`.
- **`bloqueada`** — sub-agente devolvió pero quedaron pendientes que
  requieren acceso humano (paywall, audio sin transcripción, video).

## Cómo entra una investigación al dashboard

Cuando el Vehemiurgo en chat dice algo como:

> "Quisiera delegar una investigación sobre [X]."

Yo:
1. Sumo entrada a `pending.md` con id, fecha, alcance, dónde irá el
   material cuando termine.
2. Si es momento de lanzar, abro sub-agente con prompt
   self-contained y briefing Cornette-school.
3. Si necesita aprobación previa, lo dejo en `pendiente` y se lo
   muestro al Vehemiurgo.
4. Cuando el sub-agente vuelve, marco
   **`completada-sin-integrar`** y aviso al Vehemiurgo.
5. Cuando se integra, se mueve a `closed.md` con cross-link al
   archivo final.

## Naming de id

`<slug-corto>-YYYY-MM` (ej. `tko-contracts-2025-2026`,
`zaria-debut-monster-heel`).

## Lo que research/ no es

- No es archivo de citas. Las citas viven en los fact-sheets / matches
  / segments con su atribución.
- No es bitácora de pensamiento del Vehemiurgo. Eso vive en
  `notebook/`.
- Es solo **dashboard de delegaciones de research** y status.
