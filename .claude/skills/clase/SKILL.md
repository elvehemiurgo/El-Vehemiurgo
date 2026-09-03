---
name: clase
description: Asignar, ratificar o consultar clases Vehemiurgia (perfect-wrestling / fighting-spirit / wrestling-entertainment) sobre matches y segments. Usar cuando el Vehemiurgo declara "ponle X class", "se merece todas las clases", "¿qué tengo en Perfect Wrestling?", o ratifica una clase asignada por lectura.
---

# /clase — gestión de clases Vehemiurgia

Doctrina completa: `glossary/clases-vehemiurgo.md` + CLAUDE.md §4.
Vocabulario ÚNICO en frontmatter: `perfect-wrestling`,
`fighting-spirit`, `wrestling-entertainment`,
`wrestling-entertainment-plus` (slugs; en índices PW·FS·WE·WE+).

**WE+** es un escalón por encima de WE (ley s54): *"segmentos
simplemente demasiado buenos que definen el entertainment y el
wrestling booking inteligente"*. **Una pieza lleva WE o WE+, nunca las
dos.** A diferencia de las coronas, WE+ SÍ toca la jerarquía.

**Coronas — NO se escriben, se derivan.** Cuatro vigentes:

| Combinación | Corona |
|---|---|
| `FS + WE` | **Feeling Crown (FC)** |
| `FS + WE+` | **Feeling Crown+ (FC+)** |
| `PW + FS + WE` | **Instant Classic Crown (ICC)** |
| `PW + FS + WE+` | **Instant Classic Crown+ (ICC+)** |

Las variantes `+` son ley s59: *"WE+ entra en las coronas pero sería
una Corona+"*. **No son coronas nuevas** — misma corona, marcada con
`+` cuando el entertainment es WE+ en vez de WE.

Todas salen solas de `clases_vehemiurgo` vía
`bin/archivo_lib.py: Ficha.corona` y aparecen en la columna *Corona*
de los índices. **Nunca agregar un campo de corona al frontmatter** —
sería estado duplicado. Se nombran en prosa (blockquote-lead) cuando
corresponde.

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
