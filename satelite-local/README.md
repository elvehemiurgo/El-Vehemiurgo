# Kit de arranque — Claude Code satélite LOCAL (mediateca / PC del Vehemiurgo)

> **Autorizado 2026-08-01 (s22).** Arquitectura idéntica al satélite
> TikTok: VEHEMIURGIA (este repo) es el **centro de conocimiento** —
> la fragua. El satélite local es OTRO Claude Code corriendo en tu PC,
> **con acceso real a tus carpetas** (`E:\VEHEWRES\...`, la mediateca,
> descargas, lo que le des). El puente entre ambos es **git**: clona
> VEHEMIURGIA al lado y hace `git pull` en cada arranque — siempre
> bebe de la última versión del archivo.

## Para qué sirve este satélite (y el TikTok no)

- **Renombrar y organizar la mediateca** — ejecutar las tablas de
  renombrado de las guías `vehemiurgia/` sobre los archivos reales
  (formato `YYYY MM DD Nombre del Show`).
- **Acompañar los watch parties VEHEMIURGIA en vivo** — con la guía
  del repo abierta y los videos en el disco, puede decirte qué show
  sigue, qué mirar en cada lucha, y el contexto al instante.
- **Cualquier tarea de archivos locales** que este entorno cloud no
  puede tocar.
- (Futuro, si el Vehemiurgo lo activa: acá viviría el "cerebro"
  interactivo — el visor local con reconocimiento de entidades que
  quedó anotado como idea diferida.)

## El contrato (las 3 reglas — idénticas al satélite TikTok)

1. **VEHEMIURGIA es la fuente de verdad y es READ-ONLY para el
   satélite.** Lee doctrina, fichas, guías, listas, notebooks — pero
   **nunca escribe** en El-Vehemiurgo. Ni un typo.
2. **Todo conocimiento nuevo entra por el centro.** Si durante un
   watch party sale un take, se dicta en la sesión de VEHEMIURGIA
   (pipeline `/volcado` de allá). El satélite puede tomar notas
   temporales en SU repo para que no se pierdan, pero el registro
   canónico nace en el centro.
3. **El léxico rige en todo**: `glossary/blacklist.md` y
   `glossary/carny-lexicon.md` aplican también a nombres de archivo,
   notas y cualquier texto que el satélite produzca.

## Pasos en tu PC (una sola vez)

En Windows, con Git instalado (los comandos corren igual en Git Bash;
en PowerShell cambia `mkdir -p` por `mkdir`):

```bash
# 1. Carpeta madre + clonar VEHEMIURGIA (si ya la tenés del satélite
#    TikTok, saltá este paso — se comparte el mismo clon)
mkdir -p ~/vehemiurgia && cd ~/vehemiurgia
git clone https://github.com/elvehemiurgo/El-Vehemiurgo.git
cd El-Vehemiurgo
git checkout claude/wrestling-history-platform-KYaB6
cd ..

# 2. Crear el repo del satélite local AL LADO
mkdir vehemiurgo-local && cd vehemiurgo-local
git init

# 3. Copiar los archivos semilla
cp ../El-Vehemiurgo/satelite-local/CLAUDE-template.md ./CLAUDE.md
mkdir -p .claude
cp ../El-Vehemiurgo/satelite-local/settings-template.json ./.claude/settings.json

# 4. Arrancar
claude
```

Primera conversación en el satélite: presentarle tus carpetas (rutas
de la mediateca, ej. `E:\VEHEWRES`) para que las registre en su
CLAUDE.md, y probar el primer renombrado con la guía
`vehemiurgia/czw-2017-2018.md`.

## Nota de branch

El archivo vive en `claude/wrestling-history-platform-KYaB6` — el
hook del template pullea esa branch. Si el repo migra a `main`,
actualizar el hook allá.

## Diferencia con el satélite TikTok

| | TikTok | Local |
|---|---|---|
| Produce | contenido para el canal | organización de mediateca + soporte de visionado |
| Toca archivos locales | no | **sí — esa es su razón de ser** |
| Escribe en VEHEMIURGIA | nunca | nunca |
| Doctrina propia | estilo/formatos TikTok | rutas de mediateca + preferencias de organización |
