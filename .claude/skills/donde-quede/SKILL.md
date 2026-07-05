---
name: donde-quede
description: Responder "¿en qué me quedé?" — último episodio visto de un programa, qué está pendiente de ver, estado de listas y research. Usar ante preguntas de continuidad del visionado ("¿en qué episodio de X me quedé?", "¿qué tengo pendiente?", "¿está registrado Y?").
---

# /donde-quede — consultas de continuidad

Fuentes, en este orden (todas derivadas — si el hook de sesión
avisó staleness, advertirlo en la respuesta):

1. **Último visto de un programa**: filtrar
   `archive/matches/index.md` + `archive/segments/index.md` por
   empresa/programa, tomar la fecha más reciente. Distinguir
   semanal (Impact, Dynamite, Raw…) de PPV/specials.
2. **Pendientes de ver**: `archive/topics/eventos-watch-list-vehemiurgo.md`
   (cards agrupadas + sueltos, moderno primero).
3. **¿Está registrado X?**: grep por fecha+nombres en ambos índices
   (usar variantes del registro canónico al buscar: el Vehemiurgo
   puede haberlo dictado como "Lion Slather"); si no está en
   índices, grep en la lista personal
   (`notebook/2026-05-09-2-lista-personal-completa.md`) para
   distinguir "declarado sin ficha" de "no registrado".
4. **Listas**: panteón (SoT), THE FUTURE, conocer-más, research
   (pending.md).

Formato de respuesta: directo — el dato primero (fecha/estado),
después el detalle en tabla corta si hay varios items. Ofrecer
abrir el stub si el item no existe ("¿lo registro?" solo si el
Vehemiurgo no dio ya el take completo — si lo dio, registrar
directamente vía /volcado).
