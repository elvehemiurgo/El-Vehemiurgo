---
name: panteon
description: Mutaciones del panteón de héroes fundamentales (altas, bajas, movidas de número, cambios de tier, consultas). Usar cuando el Vehemiurgo declara héroes/dioses, mueve posiciones, descarta candidatos o pregunta por el panteón.
---

# /panteon — gestión del panteón

**Source of truth**: `archive/topics/heroes-fundamentales-vehemiurgia.md`.
Estructura (actualizada 2026-08-01 s23): **Tier 0 — Indie Wrestling
Gods** (sin orden interno, jerárquicamente IGUAL al Tier 1 — cumbre
gemela, "la sombra de los 7 dioses"; puede recibir ascensos desde
Tier 2/3, slots de origen se preservan sin renumerar) · Tier 1 — Los
7 Dioses del Wrestling #1-7 (orden REAL) · Tier 2 — The Pillars of
Wrestling #8-25 (orden interno sin confirmar) · Tier 3 — Los
Fundamentales #26+ (sin orden, slot de registro).

## Alta / movida / baja — protocolo atómico (un solo commit)

1. **Tabla del SoT**: aplicar el cambio + fila en "Notas de la
   reorganización" con fecha y verbatim del Vehemiurgo.
2. **Corrimientos**: si la movida desplaza números, listar TODOS
   los desplazamientos en la nota (patrón: "X #a→#b, Y #b→#c…").
3. **Marcadores en fichas**: TODA ficha afectada actualiza su
   blockquote-lead en el MISMO commit. Etiquetas exactas:
   - Tier 0 → `Indie Wrestling God (Tier 0) del Vehemiurgo`
   - Tier 1 → `DIOS DEL WRESTLING #N (Tier 1) del Vehemiurgo`
   - Tier 2 → `Pillar of Wrestling #N del Vehemiurgo`
   - Tier 3 (#26+) → `Héroe Fundamental #N del Vehemiurgo`
4. **Fichas sin abrir**: fila queda `_(ficha pendiente)_`; NO abrir
   stubs masivos por alta al panteón (se abren a demanda).
5. **Descartes**: registrarlos en la sección "Candidatos /
   descartes" con fecha (precedentes: Volk Han, Tamura, Johnny
   Saint — descartados 2026-06-17 pero figuras de archivo).
6. Dobles presencias legales (individual + tag): Kyle O'Reilly #12
   + reDRagon #44; Dynamite Kid #6 + British Bulldogs #42; Kay Lee
   Ray #33 + Filthy Generation #27. Documentar siempre el patrón.
7. `python3 bin/lint_archivo.py` valida los links del SoT.

## Consultas

"¿quién está en el panteón?" → tabla del SoT tal cual (respetando
tiers). "¿X está?" → responder con tier + número + fecha de
declaración, o su estado de candidato/descartado.
