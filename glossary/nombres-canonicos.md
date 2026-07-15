# Registro de nombres canónicos

> **Ley operativa**: el `notebook/` preserva los typos **verbatim**
> (registro fiel). Todo lo demás — `archive/`, slugs, filenames,
> índices, vistas derivadas — usa el **canónico**. Antes de crear
> cualquier ficha o slug nuevo, consultar esta tabla.
>
> Este archivo es **leído por `bin/lint_archivo.py`** (sección
> "Variantes prohibidas") y por `bin/reconciliar_lista.py` (mapa de
> equivalencias para el matching). Mantener el formato de tabla.

## Variantes prohibidas (lint: warning fuera de notebook/)

| Canónico | Variantes prohibidas |
|---|---|
| Mickie James | Mickey James |
| Leon Slater | Lion Slater, Leon Slather, Lion Slather |
| Arianna Grace | Ariana Grace |
| Jodi Threat | Jody Threat, Jody Thread |
| Thekla | Tekhla, Teklah, Tehkla |
| Saquon Shugars | Saquan Sugars, Saquoan Suggars, Saquan Shugars |
| JD McDonagh | JD McDona, JD Mcdonna, JD MCDONA |
| Indi Hartwell | Indy Hartwell |
| Mark Rocco | Marc Rocko, Mark Rocko |
| Kelani Jordan | Kelany Jordan |
| Jada Stone | Jaida Stone |
| Candice LeRae | Candace Lerae, Candace LeRae |

## Atención — contexto-dependientes (no linteados)

| Nombre | Regla |
|---|---|
| **Elijah / Elias** | *Elijah* = ring name TNA 2025+ (canónico actual). *Elias* = era WWE 2017-2023. En slugs nuevos usar `elijah`. El slug `...-vs-elias-tna-genesis` quedó como legado. |
| **Kazarian / Frankie Kazarian** | Ambas formas OK en prosa. Slug único: `frankie-kazarian`. |
| **"Xia Lee" (dictado)** | Sin correspondencia real — mezcla auditiva de "Lei Ying" + "Xia" (Brookside, mencionada en el mismo take). Resuelve a **Lei Ying Lee** por contexto (gimmick "chinese warrior", crítica de promos en idioma no inglés). NO agregar como variante ciega: "Xia" también refiere legítimamente a Xia Brookside en otros contextos. |
| **Kira (CMLL) / Kira Summer (TJPW) / Keyra (AAA-CMLL)** | Tres talents distintos. Desambiguación en `archive/people/kira.md` y `keyra.md`. |
| **Myla Grace / Mila Moore** | Dos talents distintas (TNA Knockouts). No unificar. |
| **Bear Bronson / Bear Boulder** | Distintos (ex-Bear Country ambos). |

## Cómo se agrega una entrada

Cuando el Vehemiurgo dicta un nombre que suena a variante:
1. Verificar la grafía canónica (cobertura oficial de la empresa).
2. Si es typo recurrente → fila en "Variantes prohibidas".
3. Si es ambigüedad real → fila en "Atención".
4. La ficha del talent glosa la variante (*"el Vehemiurgo a veces
   lo escribe X"*) — la glosa en la ficha es legítima y el lint la
   ignora (líneas de quote `>` quedan exentas).
