# Kit de arranque — Claude Code satélite (TikTok)

> **Arquitectura**: VEHEMIURGIA (este repo) es el **centro de
> conocimiento** — la fragua. El satélite es OTRO Claude Code, en
> tu PC, con su propio repo y su propia doctrina de contenido
> (estilo, formatos, cadencia: todo eso se define ALLÁ). El puente
> entre ambos es **git**: el satélite clona VEHEMIURGIA al lado y
> hace `git pull` en cada arranque de sesión — siempre bebe de la
> última versión.

## El contrato (las 3 reglas)

1. **VEHEMIURGIA es la fuente de verdad y es READ-ONLY para el
   satélite.** El satélite lee doctrina, fichas, clases, panteón,
   listas, notebooks — pero **nunca escribe** en El-Vehemiurgo.
2. **Todo conocimiento nuevo entra por acá.** Si haciendo
   contenido surge un take, un dato o una corrección, se dicta en
   ESTA sesión (pipeline `/volcado`) — nunca se edita el archivo
   desde el satélite. Un solo escritor = cero conflictos.
3. **La lista negra rige también el contenido.** El satélite
   respeta `glossary/blacklist.md` y el léxico de
   `glossary/carny-lexicon.md` en todo lo que produzca.

## Pasos en tu PC (una sola vez)

```bash
# 1. Instalar Claude Code si no lo tenés (https://claude.com/claude-code)

# 2. Carpeta madre + clonar VEHEMIURGIA
mkdir -p ~/vehemiurgia && cd ~/vehemiurgia
git clone https://github.com/elvehemiurgo/El-Vehemiurgo.git
cd El-Vehemiurgo
git checkout claude/wrestling-history-platform-KYaB6   # ver nota de branch abajo
cd ..

# 3. Crear el repo del satélite AL LADO (hermanos, misma carpeta madre)
mkdir vehemiurgo-tiktok && cd vehemiurgo-tiktok
git init

# 4. Copiar los archivos semilla desde El-Vehemiurgo/satelite-tiktok/
cp ../El-Vehemiurgo/satelite-tiktok/CLAUDE-template.md ./CLAUDE.md
mkdir -p .claude
cp ../El-Vehemiurgo/satelite-tiktok/settings-template.json ./.claude/settings.json
cp ../El-Vehemiurgo/satelite-tiktok/bio-statement.md ./assets-semilla/bio-statement.md 2>/dev/null || \
  (mkdir -p assets-semilla && cp ../El-Vehemiurgo/satelite-tiktok/bio-statement.md assets-semilla/)

# 5. Arrancar el satélite
claude
```

Desde ahí, la primera conversación en el satélite es para definir
SU doctrina: estilo TikTok, formatos, cadencia. El template de
CLAUDE.md ya trae el contrato con VEHEMIURGIA y deja esas
secciones en blanco para que las dictes allá.

## Nota de branch (importante)

Hoy todo el archivo vive en la branch
`claude/wrestling-history-platform-KYaB6`. El satélite debe
pullear ESA branch (el hook del template ya lo hace con la branch
activa del clone). Cuando decidas mergear a `main`, avisá acá y el
satélite solo necesita `git checkout main` una vez.

## Cómo se mantiene "en tiempo real"

- **Satélite → siempre fresco**: el hook `SessionStart` del
  template corre `git -C ../El-Vehemiurgo pull --ff-only` en cada
  arranque y te muestra el último commit + último notebook. Si
  querés refrescar a mitad de sesión, en el satélite decís
  "refrescá VEHEMIURGIA" y corre el pull de nuevo.
- **Esta sesión → siempre publica**: acá cada volcado termina en
  commit + push (ya es parte del pipeline), así que lo que dictás
  acá está disponible para el satélite minutos después.

## Mapa de lectura para el satélite

| Qué busca | Dónde |
|---|---|
| Doctrina completa (qué es y qué no es wrestling) | `CLAUDE.md` |
| Léxico carny + lista negra | `glossary/carny-lexicon.md` · `glossary/blacklist.md` |
| Sistema de clases (PW·FS·WE) | `glossary/clases-vehemiurgo.md` |
| Nombres canónicos | `glossary/nombres-canonicos.md` |
| Panteón (45 héroes, 3 tiers) | `archive/topics/heroes-fundamentales-vehemiurgia.md` |
| THE FUTURE in 2026 | `archive/topics/the-future-in-2026.md` |
| RUNNER UPS | `archive/topics/runner-ups.md` |
| Matches con juicio editorial | `archive/matches/index.md` → fichas |
| Segments/promos | `archive/segments/index.md` → fichas |
| Fichas de talents | `archive/people/` |
| Takes crudos verbatim (la voz pura) | `notebook/` |
| Dossiers de research con fuentes | `dossiers/` |
| Voz larga de referencia | `editorials/draft-manifiesto-vehemiurgia.md` |
