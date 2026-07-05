---
name: research
description: Ciclo completo de investigación delegada a sub-agentes (lanzar, integrar, consultar estado). Usar cuando el Vehemiurgo autoriza sub-agentes, pide "investigá X", "confírmame la carrera de X", o pregunta qué research hay abierto.
---

# /research — ciclo de investigación delegada

Dashboard: `research/pending.md` (activas) + `research/closed.md`
(cerradas). Regla de oro: **una investigación nunca queda a medias
entre los dos archivos** (anti-zombie; precedente: tko-contracts).

## Lanzar (requiere autorización del Vehemiurgo — CLAUDE.md §5)

1. Fila en la tabla "Activas" de pending.md: id-kebab, estado
   en-curso, fecha, alcance 1 línea, origen (link al notebook),
   destino del material.
2. Lanzar sub-agente background con prompt auto-contenido:
   objetivo + entregables numerados + jerarquía de fuentes
   (CLAUDE.md §5) + regla de honestidad ("[no confirmado] antes
   que dato fabricado") + **advertencia 403**: Cagematch/Wikipedia/
   wikis devuelven HTTP 403 vía WebFetch en este environment — que
   trabaje con snippets de WebSearch y lo declare.
3. NO escribe archivos del repo: devuelve dossier en su mensaje
   final (excepción: regeneración de vistas derivadas, que sí
   escribe solo esas).

## Integrar (cuando vuelve el dossier)

1. Distribuir el material a fichas/matches/topics destino
   (citando "Sub-agente <id> (research YYYY-MM-DD, closed)" en
   fuentes_principales).
2. **Mover** la entrada: borrar de pending.md (tabla Y detalle si
   lo hubiera) + fila en closed.md.
3. Formato closed.md: celda "Notas" **máx ~500 caracteres** —
   síntesis + correcciones clave. El dossier completo NO va en la
   celda (anti-precedente: celdas de 7.900 chars ilegibles). Si el
   dossier merece preservarse íntegro → `dossiers/`.
4. Commit único de integración.

## Estado

"¿qué tengo abierto?" → tabla Activas de pending.md + En cola +
Bloqueadas, tal cual.
