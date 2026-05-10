# Notebook — Bitácora del Vehemiurgo

Cuaderno de campo. Cronológico. Acá viven los **volcados crudos del
Vehemiurgo**: takes editoriales, opiniones, observaciones de show,
preguntas abiertas, delegaciones de research. Cada sesión donde el
Vehemiurgo descarga material editorial genera un archivo nuevo.

> "Quiero poder ingresar mis notas editoriales y de opinión sobre
> distintos temas y tu me ayudas a organizarlas y tener secciones de
> investigaciones pendientes y las sub-investigaciones que te delego
> también." — El Vehemiurgo, 9 may 2026.

---

## Cómo funciona

### Cuando el Vehemiurgo suelta un volcado

Yo abro un nuevo archivo en `notebook/YYYY-MM-DD-<slug>.md` con la fecha
de la sesión y un slug descriptivo (ej.
`2026-05-09-takes-rivalidades-vigentes.md`). Dentro:

1. **Takes editoriales** — uno por tópico. Donde tenga sentido, **cito
   verbatim** al Vehemiurgo entre comillas; donde haga falta organización
   o contexto, parafraseo marcado.
2. **Investigaciones a delegar** — lo que el Vehemiurgo pide se busque
   profundamente. Cada delegación se replica en
   `research/pending.md` para tracking.
3. **Próximos pasos** — qué quedó abierto, qué se distribuye a
   fact-sheets, qué genera dossier o editorial.

### Cuando los takes maduran

Los takes del notebook se **distribuyen** a fact-sheets cuando hay masa
crítica:

- Takes sobre **una persona** → `archive/people/<slug>.md` sección
  *Notas editoriales del Vehemiurgo*.
- Takes sobre **un tema cross-cutting** (gimmick, faction, contract
  reset, era) → `archive/topics/<slug>.md`.
- Takes sobre **una promotion** → `archive/promotions/<slug>.md`
  sección editorial.

El notebook **no se borra ni reescribe** después de la distribución —
queda como registro cronológico fiel del pensamiento del Vehemiurgo.
Es el cuaderno de campo; los fact-sheets son el archivo organizado.

### Cuando hay masa crítica para una pieza

Cuando la sección *Notas editoriales del Vehemiurgo* de un fact-sheet
acumula suficiente material y el Vehemiurgo decide que es momento de
escribir, **ese fact-sheet es la materia prima** del editorial /
dossier que abrimos en `editorials/` o `dossiers/`.

---

## Naming convention

`YYYY-MM-DD-<slug-descriptivo>.md`

- Si hay más de un volcado en el mismo día, sufijo `-1`, `-2`.
- Slug descriptivo de los tópicos centrales (`takes-nxt-2026`,
  `reaction-mania-42`, `dossier-budget-tko`, etc.).

## Estructura de un entry

```yaml
---
fecha: YYYY-MM-DD
sesion: ""
topicos: []
research_delegado: []
ultima_actualizacion: YYYY-MM-DD
---

# Notebook YYYY-MM-DD — <título>

## Contexto
<una frase>

## Takes editoriales

### 1. <título del tópico>
- Persona/tema: ...
- Cita verbatim del Vehemiurgo:
  > "..."
- Notas mías:
- Distribución sugerida: → `archive/people/<x>.md` o `archive/topics/<x>.md`

(repetir por tópico)

## Research a delegar
<entradas con cross-link a research/pending.md>

## Próximos pasos
- [ ] Distribuir takes a fact-sheets X, Y, Z
- [ ] Lanzar sub-agente para investigación A
- [ ] Verificar pista B contra fuente
```

---

## Lo que el notebook no es

- No es editorial. Es la materia prima.
- No es archivo definitivo de nada. Es cronológico, no organizado por
  persona ni por tema.
- No se publica. Es interno.
