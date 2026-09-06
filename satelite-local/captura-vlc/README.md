# Captura de takes desde VLC — kit del satélite LOCAL

> **Pregunta del Vehemiurgo (2026-09-06)**: *"hay forma de que sepas
> qué archivo estoy viendo en VLC y cuando presione una combinación de
> teclas pueda ingresar [...] cada segmento y lucha como siempre"*.
>
> **Respuesta corta**: desde la sesión cloud de VEHEMIURGIA, no — ese
> Claude no ve tu PC. **Desde tu PC, sí**: VLC expone por HTTP qué
> archivo suena y en qué segundo, y un script de AutoHotkey convierte
> una combinación de teclas en "pausá, decime el take, anotalo con
> show y minuto". El borrador que sale se pega tal cual en la sesión
> de VEHEMIURGIA y entra por `/volcado` como siempre — con una mejora:
> **cada take llega con su `[HH:MM:SS]`**, que es la ubicación en el
> show que las fichas y los guiones siempre dejaban en `[verif]`.

## Cómo funciona

```
VLC (reproduciendo 2013 02 14 Impact Wrestling.mp4, min 00:23:41)
        │  interfaz web: http://127.0.0.1:8080/requests/status.json
        ▼
vehemiurgo-captura.ahk  ── Ctrl+Alt+V ──►  pausa VLC, abre ventanita
        │                                   "▶ 2013 02 14 Impact Wrestling  ⏱ 00:23:41"
        │                                   escribís el take, Enter
        ▼
E:\VEHEWRES\borradores\2026-09-06-borrador.md
        ## 2013 02 14 Impact Wrestling
        - **[00:23:41]** Roode y Aries abren con la promo... WE
        - **[00:41:05]** el tag titular se merece las 3 clases...
        │
        ▼  (al terminar el visionado: copiar y pegar en VEHEMIURGIA)
sesión cloud → /volcado → fichas con fecha, show y ubicación en el show
```

El archivo tiene que estar nombrado con el formato de la mediateca
(`YYYY MM DD Nombre del Show.ext`) — el script toma el nombre del
archivo sin extensión como nombre del show. Si la mediateca ya está
renombrada con las guías `vehemiurgia/`, no hay nada que hacer.

## Instalación (una sola vez)

### 1. Activar la interfaz web de VLC

1. VLC → **Herramientas → Preferencias** (Ctrl+P).
2. Abajo a la izquierda, **Mostrar ajustes: Todo**.
3. **Interfaz → Interfaces principales** → marcar **Web**.
4. **Interfaz → Interfaces principales → Lua** → en **HTTP de Lua →
   Contraseña** poner la misma que va en `VLC_PASSWORD` del script
   (por defecto `vehemiurgo`).
5. Guardar y **reiniciar VLC**. La primera vez Windows pregunta por el
   firewall: alcanza con permitir redes privadas (solo escucha en la
   propia PC).
6. Probar en el navegador: `http://127.0.0.1:8080/requests/status.json`
   — usuario en blanco, la contraseña de arriba. Tiene que devolver un
   JSON con `"time"` y `"filename"`.

### 2. AutoHotkey v2

Instalar **AutoHotkey v2** (https://www.autohotkey.com — la v1 no
corre este script). Copiar `vehemiurgo-captura.ahk` al repo del
satélite (`vehemiurgo-local/captura-vlc/`) y editar el bloque
`CONFIG`: contraseña y carpeta de borradores.

Doble clic en el `.ahk` para arrancarlo (queda en la bandeja). Para
que arranque con Windows: acceso directo en `shell:startup`.

### 3. Teclas

| Combinación | Qué hace |
|---|---|
| **Ctrl+Alt+V** | Pausa VLC, muestra show + minuto, abre el cuadro del **take**. Enter guarda, Ctrl+Enter salto de línea, Esc cancela. Al cerrar, VLC sigue. |
| **Ctrl+Alt+M** | **Marca** rápida: solo minuto + etiqueta corta (*"arranca el main event"*, *"ref bump"*). Para fijar tiempos sin detenerse a opinar. |
| **Ctrl+Alt+B** | Abre el **borrador del día** en tu editor. |

Se cambian en la sección `HOTKEYS` del script (`^` Ctrl, `!` Alt,
`+` Shift, `#` Win).

## El borrador

Un archivo por día: `BORRADOR_DIR\YYYY-MM-DD-borrador.md`. Un
encabezado `## YYYY MM DD Nombre del Show` cada vez que cambia el
archivo que suena, y debajo una línea por take:

```markdown
# Borrador de visionado — 2026-09-06

## 2013 02 14 Impact Wrestling

- **[00:04:12]** _(marca)_ arranca el show, Hogan en el ring
- **[00:23:41]** Roode y Aries backstage. Dirty Heels otra vez WE, el
  timing de Aries es de otro planeta
- **[00:41:05]** tag titular vs Chavo y Hernandez, se merece las 3
  clases, el walk-out de Roode es la definición de wrestling

## 2013 02 21 Impact Wrestling

- **[00:12:30]** ...
```

**Es un borrador, no el registro.** El registro nace en VEHEMIURGIA:
al terminar, copiar el contenido y pegarlo en la sesión cloud. Allá
el pipeline `/volcado` lee el encabezado como fecha + show de cada
ficha y el `[HH:MM:SS]` como `ubicacion_en_show` (y alimenta las
tablas de timestamps de los guiones). Tus palabras se preservan
verbatim, typos incluidos, como siempre.

## Qué NO hace (a propósito)

- **No escribe en El-Vehemiurgo.** Contrato del satélite, regla 1. El
  borrador vive en tu disco; el archivo se escribe desde la sesión
  cloud.
- **No reconoce luchadores ni segmentos** en el video. Sabe archivo y
  minuto — la identificación de nombres, resultados y roles sigue
  siendo la ley de sub-agentes del centro (CLAUDE.md §4).
- **No adivina el show** si el archivo no está renombrado
  `YYYY MM DD Nombre del Show`; anota el nombre que tenga el archivo.

## Si algo falla

- *"No encuentro nada sonando en VLC"* con VLC abierto → la interfaz
  web no está activa o la contraseña no coincide. Verificar el paso 1
  en el navegador. Sin interfaz web el script cae a leer el título de
  la ventana: da el show pero **no el minuto** (lo anota como `sin
  timestamp`).
- Error de sintaxis al arrancar → casi seguro AutoHotkey **v1**
  instalado en vez de v2.
- Cualquier otra cosa: pegarle el error al **satélite LOCAL** — el
  script es suyo, lo puede ajustar. Este kit se escribió desde el
  entorno cloud, **sin poder ejecutarlo**: la primera corrida puede
  necesitar un retoque.
