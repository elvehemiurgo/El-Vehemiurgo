# Index — Segments del Vehemiurgo

Tabla viva. Una fila por segmento registrado en `archive/segments/`. Se
ordena por fecha del segmento (más reciente arriba). Se actualiza con
cada alta y con cada cambio de estado.

| Fecha | Segmento | Empresa / Programa | Tipo | Estado | Veces visto | Archivo |
|---|---|---|---|---|---|---|
| 2026-04-20 | JD McDonagh & Finn Bálor: video promo dual | WWE / Raw After WM42 (T-Mobile Las Vegas) | vignette dual pre-grabada | en-investigacion | — | [→](2026-04-20-jd-mcdonagh-video-promo-raw.md) |
| 2026-03-24 | Sol Ruca vs Zaria: *"You didn't want a team, you wanted a moment"* | WWE / NXT (Performance Center Orlando) | promo in-ring confrontacional | en-investigacion | — | [→](2026-03-24-sol-ruca-you-didnt-wanted-a-team-nxt.md) |

---

## Leyenda

- **Tipo**: promo, backstage, in-ring confrontation, post-match angle,
  sketch, interview, vignette, entrance, celebration, turn, run-in,
  spot-aislado.
- **Estado**: `stub` (recién creado), `en-investigacion`, `verificado`,
  `vivo`.
- **Veces visto**: campo `veces_visto_vehemiurgo` del frontmatter. `—`
  si no se ha registrado todavía.

## Cómo se mantiene

- Cada alta de segmento agrega una fila.
- Cuando cambia el estado o el rewatch count, se actualiza la fila
  correspondiente.
- Ordenado por fecha del segmento, no por fecha de alta.
- Si la fecha está pendiente (`YYYY-XX-XX`), va al lugar aproximado del
  año o se agrupa al final del año.
