# Workflow — Cómo trabajamos

Este archivo describe la operación día a día entre el Vehemiurgo y su copiloto.
La doctrina vive en `CLAUDE.md`. Esto es la mecánica.

---

## 1. Cómo pedís trabajo

No hace falta formalismo. El Vehemiurgo escribe natural, en español, en
inglés o mezclando. Yo entiendo y nunca pido traducir el input.

Patrones que ya están normalizados:

- **"Escribime un editorial sobre X"** → arranco borrador en
  `editorials/draft-<slug>.md` con la plantilla, pregunto por ángulo solo si
  es estrictamente ambiguo.
- **"Review del Raw del lunes"** → abro `reviews/<promocion>/<YYYY-MM-DD>-<slug>.md`,
  pido el dato del show (link, fecha, lugar) si no lo tengo, y arranco.
- **"Dossier de Crockett 1985"** → abro `dossiers/<slug>.md` y antes de
  escribir te propongo un esquema breve para que lo apruebes o corrijas.
- **"Investigá X"** → si es acotado, lo hago directo. Si es amplio o paralelo,
  te propongo abrir un sub-agente (ver §3).
- **"Armá fact-sheet de [persona/empresa/programa]"** → abro el archivo en
  `archive/<categoria>/<slug>.md` con la plantilla y lleno lo que tengo
  fuente fiable. Lo que no tenga, lo dejo marcado como "pendiente" en vez
  de inventar.

Para cosas muy abiertas ("hablame de la era de los territorios") yo te
respondo con dos o tres ángulos posibles antes de arrancar a escribir, para
no quemar trabajo.

---

## 2. Investigación y citas

### Jerarquía
1. **Primaria**: contratos, filings (10-K, S-1, 8-K de TKO/WWE histórico),
   gates oficiales, declaraciones on-record con video/audio del protagonista,
   documentos legales.
2. **Secundaria fiable**: WON (Meltzer), Wrestling Observer Live, F4WOnline,
   PWInsider, Pollock & Wai Ting (POST Wrestling), Wade Keller (PWTorch),
   Hornbaker, libros académicos y de historiadores serios.
3. **Terciaria**: dirt sheets sin firma, notas de prensa de las propias
   promociones (sesgadas pero útiles para la versión oficial), redes
   sociales del talento.
4. **Rumor**: foros, Reddit, Twitter sin contexto, podcasts citando "alguien
   me dijo".

### Reglas
- **Siempre cito**. Inline o al pie, formato consistente en la pieza:
  `[Tipo: Autor/medio, Fecha, Link]`.
- **Marcar el nivel**: si es rumor, decirlo. Si es atribuido pero no
  confirmado, decirlo. Si es backstage, decirlo y nombrar al cuentista.
- **Números**:
  - *Gate* y *attendance*: distinguir paid attendance, announced attendance,
    no-shows estimados, gate bruto, gate neto.
  - *PPV buys*: distinguir total buys, buys domésticos, ingresos por buy,
    *streaming subs* (era moderna). Aclarar si es estimado de Meltzer o
    declaración oficial.
  - *Salarios y contratos*: casi siempre rumor o filtración. Marcarlo.
- **Backstage**: nunca hecho consumado salvo confirmación on-record del
  involucrado o documentación legal.

### Podcasts y YouTube como fuente
Son fuente legítima si el protagonista habla on-record. Formato de cita:
`[Podcast: Nombre del show, episodio con [invitado], fecha, timestamp si es relevante, link]`.

Si yo no puedo ver/escuchar el material directamente, te lo digo y te pido
el resumen o el extracto, en vez de inventar lo que dijo el invitado.

---

## 3. Delegación a sub-agentes

Cuando la investigación requiere búsquedas amplias o paralelas, te propongo
abrir un sub-agente. Patrón:

> "Para esta pieza necesito mapear: (a) gates de Mid-South Wrestling 1982–1986,
> (b) menciones backstage de Bill Watts post-2010 en podcasts, (c) historial
> documentado del double-cross con Magnum TA. ¿Te abro un sub-agente que
> devuelva un dossier consolidado y lo integro?"

Vos decidís y lo lanzo. El sub-agente vuelve con un reporte; yo lo integro
en la pieza con citas. **No lanzo sub-agentes sin tu aprobación**, salvo que
sea trivial y autocontenido.

Tipos:
- **Explore**: cuando hay que buscar datos puntuales en muchos lados.
- **general-purpose**: cuando es research multi-paso con síntesis.

---

## 4. Ciclo de vida de una pieza

```
draft-<slug>.md   →   <slug>.md (editado)   →   publicado
```

1. **Draft** (`draft-<slug>.md`): primera versión. Frontmatter mínimo. Marca
   explícita de qué falta cubrir.
2. **Edición**: vos lo corregís, yo aplico cambios, recortamos, ajustamos.
   Al pasar el filtro del checklist editorial, se renombra quitando el
   `draft-`.
3. **Publicado**: pieza terminada. Si después la migrás a la web, queda como
   fuente canónica acá.

### Checklist editorial antes de quitar `draft-`
- [ ] Voz consistente con CLAUDE.md (vehemencia, no berrinche).
- [ ] Cero términos de `glossary/blacklist.md`.
- [ ] Términos en inglés del oficio glosados la primera vez si la pieza es
      introductoria.
- [ ] Toda afirmación dura tiene fuente o está marcada como rumor.
- [ ] Datos numéricos con fecha y fuente.
- [ ] Sin generalidades de relleno; si falta dato, se marca o se corta.
- [ ] Cierre con una idea, no con un resumen de lo dicho.

---

## 5. Convenciones de archivos

### Naming
- Slugs en kebab-case, sin acentos: `manifiesto-vehemiurgia.md`,
  `crockett-promotions-1985.md`, `dynamite-2026-05-07.md`.
- Reviews semanales: `reviews/<promocion>/<YYYY-MM-DD>-<slug>.md`.
  Ejemplo: `reviews/aew/2026-05-07-dynamite-double-or-nothing-go-home.md`.
- Fact-sheets: `archive/<categoria>/<slug>.md`. Categorías base:
  `people/`, `promotions/`, `programs/`, `events/`, `eras/`, `families/`,
  `contracts/`, `interviews/`, `podcasts/`.

### Frontmatter mínimo
```yaml
---
titulo: ""
tipo: editorial | review | dossier | fact-sheet
autor: El Vehemiurgo
fecha: YYYY-MM-DD
estado: draft | editado | publicado
tags: []
fuentes_principales: []
---
```

### Fechas
- Siempre `YYYY-MM-DD` en metadatos.
- En cuerpo, fechas escritas: "el 15 de septiembre de 1992" o "September 15,
  1992" según contexto. Mes en español si la pieza es en español.

---

## 6. Cómo entrego

- Borradores van directos al archivo correspondiente, no al chat.
- En el chat te resumo qué hice, qué supuestos tomé, qué falta verificar y
  qué fuentes faltan.
- Si una pieza arrancó con datos débiles, te lo digo arriba del archivo en un
  bloque `> NOTA EDITORIAL` que removemos al pasar a publicado.

---

## 7. Lo que nunca hago sin pedirte

- Cambiar la doctrina (`CLAUDE.md`).
- Tocar `glossary/blacklist.md` para sumar o sacar términos.
- Crear infraestructura web, branding visual, integraciones externas.
- Postear nada fuera del repo.
- Abrir PRs o pushear sin que me lo pidas explícitamente para esa tanda.
