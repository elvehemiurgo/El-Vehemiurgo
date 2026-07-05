---
name: clase
description: Asignar, ratificar o consultar clases Vehemiurgia (perfect-wrestling / fighting-spirit / wrestling-entertainment) sobre matches y segments. Usar cuando el Vehemiurgo declara "ponle X class", "se merece todas las clases", "¿qué tengo en Perfect Wrestling?", o ratifica una clase asignada por lectura.
---

# /clase — gestión de clases Vehemiurgia

Doctrina completa: `glossary/clases-vehemiurgo.md` + CLAUDE.md §4.
Vocabulario ÚNICO en frontmatter: `perfect-wrestling`,
`fighting-spirit`, `wrestling-entertainment` (slugs; en índices
PW·FS·WE).

## Asignar / ratificar

1. Localizar la ficha (grep en índices por fecha/participantes).
2. Editar frontmatter `clases_vehemiurgo` + `calificacion_vehemiurgo`
   (cita corta del llamado).
3. Estado de la clase — SIEMPRE registrar cuál es:
   - **Declarada explícita**: el Vehemiurgo la nombró.
   - **Asignada por lectura**: yo la inferí — dejar nota "pendiente
     de ratificación".
   - **Ratificada**: era por-lectura y el Vehemiurgo la confirmó
     después → nota "ratificada explícitamente el YYYY-MM-DD"
     (precedente: Cedric vs Moose Street Fight).
4. Actualizar la fila del índice: `python3 bin/index_add.py <ficha>`.
5. Si es triple clase con reserva técnica puntual (ej. "los setups
   del fameasser se ven incómodos pero el resto magistral") — la
   clase VALE, la reserva se documenta (precedente: Slater vs
   Nemeth dream rematch).

## Reglas duras

- **Booking ≠ clase**: elogio al booking/diseño narrativo no da
  clase (precedente: Hometown Man vs Kazarian).
- "Muy buena / genial con limitaciones" ≠ triple clase — respetar
  el matiz del Vehemiurgo, no inflar.
- Old-school class = fighting-spirit (confirmado 2026-05-26). FS
  aplica también a promos.

## Consultar ("¿qué tengo en X class?")

```
grep -l '"perfect-wrestling"' archive/matches/*.md archive/segments/*.md
```
o filtrar la columna Clase de los índices (PW·FS·WE). Responder con
tabla fecha + match + clase.
