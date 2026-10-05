# Informe — claude/barrido-hija-4 (lotes 10, 11, 12)

Sesión hija del research `barrido-datos-duros-2026-10`. Procesé los
lotes 10 (AAA), 11 (TNA 2007 / TNA enero 2013) y 12 (TNA enero-febrero
2013 + TNA 2025-2026), en ese orden, cada uno vía research delegado a
un sub-agente con las reglas estrictas de `README.md`, revisión de
diff, `bin/lint_archivo.py --pre-commit` y commit/push propios.

Ninguna ficha de los tres lotes fue saltada por la regla de
`fuentes_principales` ya cubierto ("pendientes-fichas-sep26",
"research 2026-09-30", "research 2026-10-0"): ninguna de las 85
fichas de los lotes llevaba esas marcas.

## Conteos por lote

| Lote | Fichas en el lote | Fichas editadas | Ítems de dato duro cerrados | Discrepancias |
|---|---|---|---|---|
| 10 (AAA) | 30 | 9 | 9 | 0 |
| 11 (TNA 2007 / ene 2013) | 49 | 49 | ~45 (ver detalle) | 1 |
| 12 (TNA ene-feb 2013 + 2025-26) | 45 | 27 | 23 | 4 |
| **Total** | **124** | **85** | **~77** | **5** |

(El lote 11 tocó las 49 fichas porque casi todas solo necesitaban
ciudad/recinto, resuelto de una vez al confirmar sede por show.)

## Discrepancias encontradas (no se reescribió ningún hecho — quedaron como ítem en Pendientes de cada ficha)

1. **`archive/segments/2007-06-21-beer-money-formation-tna-impact.md`**
   (lote 11): la ficha registra la formación de Beer Money el
   21/6/2007. Bleacher Report ubica un primer teaming informal
   Storm/Roode ya en junio de 2007; la página de Wikipedia dedicada a
   "Beer Money, Inc." fija el debut televisado formal el 12/6/2008.
   No se pudo reconciliar con las fuentes disponibles — queda para
   revisión editorial del Vehemiurgo.
2. **`archive/matches/2013-02-07-bully-ray-sting-vs-devon-doc-tables-tna-impact.md`**
   (lote 12): mecanismo del finish en disputa entre recaps —
   *"chokeslammed"* (Bleacher Report, pwmania) vs **uranage/urinage**
   (otra fuente). Se reportaron ambos valores, sin elegir uno.
3. **`archive/matches/2025-11-14-the-system-vs-the-rascalz-tna-turning-point.md`**
   (lote 12): la ficha lista un posible tag/trios (Eddie Edwards,
   Brian Myers, Bronson vs Trey Miguel, Zachary Wentz); las fuentes
   (PWTorch, Fightful) reportan un eight-man tag distinto — The
   System = Moose, Eddie Edwards, Brian Myers, JDC; The Rascalz =
   Dezmond Xavier, Trey Miguel, Zachary Wentz, Myron Reed. Bronson no
   aparece en los recaps consultados.
4. **`archive/matches/2026-01-17-mustafa-ali-vs-elias-tna-genesis.md`**
   (lote 12): la ficha nombra al rival como "Elias"; el competidor
   real en TNA usa el ring name "Elijah" (Jeffrey Scuillo, el "Elias"
   de WWE, se renombró tras su salida de WWE en 2023 y debutó en TNA
   en febrero de 2025 bajo ese nombre).
5. **`archive/matches/2026-02-03-zaruca-vs-elegance-brand-nxt.md`**
   (lote 12): la secuencia del finish reportada por Fightful incluye
   a "Ash by Elegance" interviniendo (tira a Sol Ruca contra las
   escaleras del ring) — tercera integrante no listada en
   `participantes` de la ficha (que solo trae a M by Elegance y
   Heather by Elegance).

## Qué quedó sin cubrir y por qué

- **Referee**: es el dato duro con peor tasa de resolución en los tres
  lotes. Para TV tapings de AAA 2026 y TNA 2013/2007, ningún outlet
  consultado (POST Wrestling, Cageside Seats, Pro Wrestling Dot Net,
  Fightful, 411mania, PWTorch/Caldwell, Bleacher Report, sacnilk.com,
  Wikipedia, Cagematch vía snippets) acredita el nombre del árbitro
  salvo en los casos donde el árbitro es parte explícita del ángulo
  (p. ej. Taryn Terrell en Gail Kim vs Velvet Sky y en el gauntlet de
  Genesis 2013; Alice Lane en Mustafa Ali vs Elijah). El agente del
  lote 10 descartó deliberadamente dos respuestas de búsqueda que
  atribuían nombres de réferi sin poder verificarlas contra texto
  citado — preferimos dejarlo `[verif]` antes que arriesgar un dato
  inventado.
- **Duración de segments** (promos, videos de recap, backstage,
  entrevistas, firmas de contrato): la prensa de lucha solo cronometra
  matches, no segmentos puntuales. Ningún segmento de los tres lotes
  tiene fuente accesible para este dato — quedaron todos sin cambio en
  ese campo.
- **Attendance/gate de PPV 2007** (Sacrifice, Victory Road): TNA no
  publicaba gate ni boletería tradicional para shows grabados en el
  Impact Zone; se usó la cifra estándar reportada para esos PPV (900)
  como estimación marcada, sin fuente de gate real.
- **Casos puntuales específicos sin resolver**: nombre real del
  finisher de Daga (7/25 AAA, variante "Dagge Double Stomp" sin
  segunda fuente); secuencia completa Penta vs Bronco Nima (8/22 AAA);
  duración total del gauntlet femenino (8/30 AAA); finish de Zema Ion
  vs Kenny King (10/1/2013 TNA, ninguna cobertura accesible lo
  detalla); duración de Samoa Joe vs Kurt Angle y etiqueta exacta del
  resultado (no contest vs double DQ, 14/2/2013); segunda fuente de
  duración para Gail Kim/Tara/Jesse vs Party Marty/Blossom Twins y
  para Bad Influence/Dirty Heels vs Chavo/Hernandez/Storm/Park
  (21/2/2013).

## Presupuesto de research

Los tres sub-agentes usaron WebSearch agrupado por show (1-2
búsquedas reutilizadas por card, más algunas de verificación cruzada
puntual cuando una respuesta sonaba poco confiable). WebFetch/curl no
se usaron — bloqueados por el proxy del environment en prácticamente
todos los sitios relevantes (Cagematch, Wikipedia, dirt sheets),
según lo previsto en el README.

## Commits

- `0b0ed40` — lote 10: 9 fichas, 9 ítems cerrados, 0 discrepancias.
- `14436e7` — lote 12: 27 fichas, 23 ítems cerrados, 4 discrepancias.
- `fdacead` — lote 11: 49 fichas, 1 discrepancia.

Rama: `claude/barrido-hija-4`, pusheada a `origin` tras cada commit.
