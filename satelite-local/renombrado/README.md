# Renombrado de mediateca — kit del satélite LOCAL

> Ejecuta las **tablas de renombrado** de las guías `vehemiurgia/`
> sobre los archivos reales del disco. Formato de destino, siempre:
> **`YYYY MM DD Nombre del Show`** + la extensión original.

Este entorno (el Claude del repo) **no ve el disco del Vehemiurgo**:
acá vive el mapa canónico y la herramienta; el renombrado lo corre el
satélite local o el Vehemiurgo en su PC.

## Qué hay acá

| Archivo | Qué es |
|---|---|
| [`renombrar.py`](./renombrar.py) | El renombrador. Genérico: lo maneja el mapa, no el código. |
| [`mapas/ecw-hardcore-tv-1997.tsv`](./mapas/ecw-hardcore-tv-1997.tsv) | Los 52 programas #193–#244, derivados de [`vehemiurgia/ecw-hardcore-tv-1997.md`](../../vehemiurgia/ecw-hardcore-tv-1997.md) §1. |
| [`mapas/ecw-supercards-y-ppv-1997.tsv`](./mapas/ecw-supercards-y-ppv-1997.tsv) | Los 3 PPVs + 12 supercards de 1997, y las 4 trampas de corpus ajeno. |

## Cómo se corre

```bash
# 1. SIEMPRE primero en seco. No toca un solo archivo.
python3 renombrar.py --carpeta "D:\VEHEWRES\ECW 1997" \
  --mapa mapas/ecw-hardcore-tv-1997.tsv \
  --mapa mapas/ecw-supercards-y-ppv-1997.tsv \
  --informe informe-ecw-1997.md

# 2. Leer el informe. Resolver a mano lo que quedó AMBIGUO.

# 3. Recién ahí:
python3 renombrar.py --carpeta "D:\VEHEWRES\ECW 1997" \
  --mapa mapas/ecw-hardcore-tv-1997.tsv \
  --mapa mapas/ecw-supercards-y-ppv-1997.tsv --aplicar
```

Opciones: `--recursivo` (baja a subcarpetas), `--informe X.md`
(vuelca el informe a archivo), `--todas-las-extensiones` (por defecto
solo mira extensiones de video).

**Sin Python en la PC**: no hace falta. El mapa `.tsv` se lee solo —
el satélite local puede hacer el mapeo leyendo el TSV y la lista de
archivos, y proponer la tabla antes de tocar nada, que es su
procedimiento declarado igual.

## Las tres reglas duras

1. **Dry-run por defecto.** Renombra únicamente con `--aplicar`.
2. **Nunca borra y nunca sobrescribe.** Si el destino ya existe, o si
   dos archivos reclaman el mismo nombre, lo reporta como
   `CONFLICTO` y sigue de largo.
3. **Lo dudoso no se toca.** Lo que no resuelve sin ambigüedad sale
   en la tabla "Sin resolver" para ojo humano. Preferimos 3 archivos
   sin renombrar que 1 renombrado mal.

## Cómo decide

En orden de autoridad:

1. **Nº de programa** (`#193`, `ep196`, `Hardcore TV 235`). Manda
   sobre todo lo demás: la fecha solo corrobora, porque medio corpus
   circula fechado por taping o con día y mes dados vuelta.
2. **Fecha de emisión** — la canónica, una por programa.
3. **Fecha de taping** — última opción, y **solo resuelve si es
   única**: hay 5 tapings que alimentan dos programas o más (el 20/9
   alimenta cuatro), y ahí sin nº no hay nada que hacer.
4. **Título** — solo para PPVs y supercards, que no tienen nº.

Además: un archivo que se anuncia como *Hardcore TV* **nunca** se
renombra como supercard aunque comparta la fecha del taping. Esa es
justamente la trampa 1 de la guía.

### Estados del informe

| Estado | Qué significa |
|---|---|
| *(a renombrar)* | resuelto sin ambigüedad |
| *(ya correctos)* | el archivo ya lleva el nombre canónico |
| `AMBIGUO` | la evidencia apunta a más de un programa, o el nº y la fecha se contradicen |
| `SIN MATCH` | ni nº, ni fecha, ni título reconocibles |
| `CONFLICTO` | el nombre de destino ya está ocupado |
| `FUERA DE CORPUS` | show de otro año mal clasificado en la carpeta (trampa 5) |

## Formato del mapa (para escribir mapas nuevos)

TSV de 5 columnas, `#` para comentarios:

```
numero	nombre_canonico	fecha_emision	fecha_taping	nota
193	1997 01 02 ECW Hardcore TV 193	1997-01-02		taping de dic. 1996
	1997 04 13 Barely Legal	1997-04-13	1997-04-13	PPV
	!Big Ass Extreme Bash			es de 1996
```

- `numero` vacío = pieza sin nº (PPV, supercard): se matchea por
  fecha y título.
- `nombre_canonico` con **`!`** delante = **no pertenece al corpus**;
  si aparece en la carpeta se reporta como `FUERA DE CORPUS` y no se
  renombra nada.
- Las fechas van ISO (`YYYY-MM-DD`) aunque el nombre de destino use
  espacios.

**El mapa se deriva de la guía, no al revés.** Si el visionado
corrige una fecha, se corrige la guía `vehemiurgia/` y después el
mapa — nunca solo el TSV.

## Estado de prueba

`renombrar.py` se probó contra una carpeta simulada de 14 archivos
con nombres de rip reales mezclando las cuatro convenciones (ISO,
`mm-dd-yy`, `dd-mm-yyyy`, nº suelto), más un PPV, un show de 1996 mal
clasificado y dos casos irresolubles a propósito: **14/14
clasificados bien**, renombrado aplicado y verificado idempotente.
**No se probó en Windows** — el entorno del repo es Linux. Si aparece
algo raro con rutas o acentos, el satélite local lo ajusta.
