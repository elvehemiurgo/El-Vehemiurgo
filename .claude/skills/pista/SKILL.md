---
name: pista
description: >-
  Tracking de los luchadores de THE FUTURE in 2026 y RUNNER UPS:
  qué luchas/segments tienen registrados en el archivo, cuál fue la
  última lectura editorial del Vehemiurgo sobre cada uno, y en qué
  están siendo bookeados. Usar cuando el Vehemiurgo pide "seguirle
  la pista" a alguien, "¿en qué anda X?", "¿cómo van los del
  FUTURE?", "dame el estado de los RUNNER UPS", o el reporte
  completo de ambas listas.
---

# /pista — tracking de THE FUTURE y RUNNER UPS

Origen: pedido del Vehemiurgo 2026-07-11 s03 (*"quiero una skill
para que a todos los luchadores de el futuro del wrestling y
runner ups, pueda ver sus luchas y en que están siendo bookeados"*).

## 1. Resolver el roster a trackear

- **THE FUTURE in 2026**: leer `archive/topics/the-future-in-2026.md`
  — miembros = las secciones `### #N — <nombre>`. Ignorar la tabla
  "Considerados y descartados".
- **RUNNER UPS**: leer `archive/topics/runner-ups.md` — casos
  fundantes + altas numeradas.
- Si el Vehemiurgo nombra a UN talent ("seguile la pista a X"),
  limitar el reporte a ese talent (aunque no esté en las listas —
  en ese caso marcarlo "fuera de listas").

## 2. Recolectar por talent (todo local, sin red)

Para cada miembro:

1. **Ficha**: `archive/people/<slug>.md` — del frontmatter:
   `estado`, `ultima_actualizacion`; del cuerpo: el ÚLTIMO bloque
   `### Sesión` / `### Research` (la lectura editorial más
   reciente) y los pendientes abiertos clave.
2. **Matches/segments**: grep del nombre canónico en
   `archive/matches/index.md` y `archive/segments/index.md`
   (columna match/segmento) — no editar nada, solo leer. Ordenar
   por fecha; quedarse con fecha + pieza + clase (PW·FS·WE) + link.
3. **Booking actual**: la entrada MÁS RECIENTE por fecha de show
   (no de captura) + lo que la ficha diga de storyline vigente.
   Todo lo no registrado en el archivo es **[no registrado]** —
   nunca rellenar de memoria.

## 3. Formato del reporte

Una sección por lista, tabla por talent:

```
## THE FUTURE in 2026

### #4 — Myla Grace
| | |
|---|---|
| Último show registrado | 2026-04-09 vs Elayna Black (sin clase) [→](link) |
| Piezas en archivo | N matches · N segments (con clases si tienen) |
| Última lectura | "me impresiona más cada vez" (2026-07-11 s03) |
| Booking actual | <storyline vigente según archivo o [no registrado]> |
| Alertas | pendientes clave / riesgos declarados (ej. "tour América") |
```

Cerrar con un bloque **"Huecos de tracking"**: talents sin
registro nuevo desde hace más tiempo (fecha de show más reciente
más vieja primero) — ahí está lo que el Vehemiurgo tiene que
ponerse al día o delegar a research.

## 4. Booking actual fuera del archivo (opcional)

Si el Vehemiurgo quiere el booking REAL más allá de lo registrado
(cards próximas, resultados no vistos), eso es research delegado:
proponer `/research` con briefing por talent (advertencia 403
incluida). NO lanzar sub-agentes sin autorización (CLAUDE.md §5).

## Reglas

- Solo lectura: `/pista` NO escribe fichas, índices ni marcas.
- Nombres canónicos siempre (`glossary/nombres-canonicos.md`).
- Dato no archivado = "[no registrado]", nunca inventado.
- Si una lista cambió (altas/bajas), el reporte refleja el archivo
  tal cual está — las mutaciones van por `/future` y las altas
  RUNNER UPS por `/volcado`.
