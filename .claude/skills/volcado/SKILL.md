---
name: volcado
description: Distribuir un volcado/take editorial del Vehemiurgo (match, segmento, promo, declaración de clase, alta a listas) al archivo completo — notebook, match-stub, fact-sheets, índices, marcas (✓), cross-links y commit. Usar ante cualquier take sobre wrestling visto ("estoy viendo X...", "el match Y se merece...", "sumá...").
---

# /volcado — pipeline de distribución de un take

Ejecutar los pasos EN ORDEN. Fuente de doctrina: CLAUDE.md §§4-6.

## 0. Pre-checks (siempre, antes de escribir)

1. **Nombres — identificación obligatoria por show+fecha**:
   consultar `glossary/nombres-canonicos.md` (tabla + "Método de
   identificación"). Ante nombre parcial/dudoso: (a) ubicar show y
   fecha dictados, (b) contrastar con resultados y rosters reales
   del periodo, (c) grep en el archivo por si ya existe bajo otra
   grafía — nunca duplicar identidad, (d) solo si no resuelve →
   `[verif]` con candidatos. **(e) El contexto dictado es verdad de
   tablas**: afiliaciones, alineaciones y resultados que el
   Vehemiurgo declara para la fecha del show prevalecen sobre
   hipótesis previas del archivo — corregir el archivo, nunca
   forzar el dictado a encajar (precedente Connors/The Dogs, s47).
   Confirmar con data real de buenas fuentes (rosters, linajes,
   resultados). El verbatim del Vehemiurgo se preserva con typos;
   TODO lo demás (slugs, títulos, prosa, tags) usa el canónico
   completo.
2. **Duplicados**: grep en `notebook/2026-05-09-2-lista-personal-completa.md`
   y en `archive/matches/index.md` + `archive/segments/index.md`
   por fecha + participantes. Si el match YA tiene ficha, esto es
   una **elaboración** → actualizar in-place (nueva cita verbatim +
   sección de lectura), NO crear archivo nuevo (precedente: Moose
   vs Cedric Street Fight, sesiones #15-#16).
3. **Fichas existentes**: `ls archive/people/` por cada talent
   mencionado. Existente → append de bloque `### Sesión` (formato B
   de `templates/fact-sheet-sesion.md`). Inexistente → stub solo si
   el talent recibió take individual (no abrir stubs por mención de
   pasada).

## 1. Notebook

Crear `notebook/YYYY-MM-DD-sNN-<slug>.md` con **fecha real de hoy**
y NN = siguiente número zero-padded de la serie del día (s01, s02…).
Contenido: contexto (2-4 líneas), **cita verbatim completa**, takes
por tópico con distribuciones declaradas, próximos pasos.

## 2. Match/segment stub

Usar `templates/match-stub.md` (o el formato de segment análogo).
Reglas de clase (doctrina CLAUDE.md §4):
- Clase SOLO si el Vehemiurgo la declaró ("se merece todas las
  clases", "ponle FS"). Slugs únicamente.
- Si yo la infiero por lectura → asignarla PERO anotar en el campo
  calificacion y en "Lectura": *"asignada por lectura, pendiente de
  ratificación"*.
- "El booking estuvo genial" ≠ clase (booking y clase son ejes
  distintos).
- Triple clase admite reserva técnica puntual si el Vehemiurgo la
  dio junto al elogio.

## 3. Índices — vía script, nunca a mano

```
python3 bin/index_add.py archive/matches/<nuevo>.md
```
(Sirve también para actualizar la fila si cambió clase/estado.)

## 4. Marca (✓) en la lista personal

Si el take corresponde a un bullet de la lista maestra: reescribir
esa línea como `- (✓) **<texto verbatim intacto>** → [link] (nota
corta)`. Si hay duda de a qué bullet corresponde, correr
`python3 bin/reconciliar_lista.py` (dry-run) y aplicar solo
propuestas correctas.

## 5. Cross-links y listas

- Bidireccionales: match ↔ fichas ↔ topics del cluster.
- Altas a **THE FUTURE in 2026** o al **panteón** → usar las skills
  `/future` y `/panteon` (mantienen numeración + marcadores).
- Research pedido/autorizado → skill `/research`.

## 6. Validar + commit + push

```
python3 bin/lint_archivo.py --pre-commit   # (el hook lo repite)
git add -A && git commit && git push -u origin <branch>
```
Mensaje de commit: 1 línea de qué se registró + clases declaradas +
archivos clave. No repetir el checklist entero (el notebook ya lo
tiene).

## Anti-patrones (no hacer)

- Editar tablas de índice posicionalmente con Edit.
- Inventar clase no declarada sin marcar "por lectura".
- Abrir fichas masivas por menciones de pasada.
- Reescribir el notebook viejo (verbatim sagrado; solo marcas ✓).
- Anclar Edits en frontmatter multilínea — preferir anclas de una
  línea o scripts.
