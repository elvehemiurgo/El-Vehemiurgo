# Index — Matches del Vehemiurgo

Tabla viva. Una fila por match registrado en `archive/matches/`. Se ordena
por fecha del match (más reciente arriba). Se actualiza con cada alta y
con cada cambio de estado.

| Fecha | Match | Empresa / Programa | Estado | Veces visto | Archivo |
|---|---|---|---|---|---|
| 2005-04-25 | Christian (w/ Triple H) vs Batista | WWE / Raw (NEC Birmingham) | en-investigacion | — | [→](2005-04-25-christian-cage-vs-batista-raw.md) |
| 1995-07-23 | 1-2-3 Kid vs The Roadie | WWF / In Your House 2 (Nashville) | en-investigacion | — | [→](1995-07-23-123-kid-vs-the-roadie-in-your-house-2.md) |

---

## Leyenda

- **Estado**: `stub` (recién creado), `en-investigacion`, `verificado`, `vivo`.
- **Veces visto**: campo `veces_visto_vehemiurgo` del frontmatter. `—` si no
  se ha registrado todavía.

## Cómo se mantiene

- Cada alta de match agrega una fila.
- Cuando cambia el estado o el rewatch count, se actualiza la fila
  correspondiente.
- Ordenado por fecha del match, no por fecha de alta.
- Si la fecha está pendiente (`YYYY-XX-XX`), va al lugar aproximado del
  año o se agrupa al final del año.
