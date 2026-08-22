#!/usr/bin/env bash
# Estado de sesión — corre en SessionStart (hook de Claude Code).
# Imprime el contexto operativo del archivo + activa el pre-commit hook.
# Los conteos con definición no-trivial (fichas, lista personal) los
# posee lint_archivo.py --stats; acá solo queda git/ls/lint.
cd "$(dirname "$0")/.." || exit 0

# pre-commit hook idempotente
git config core.hooksPath bin/githooks 2>/dev/null

echo "=== EL VEHEMIURGO — estado de sesión ==="
echo "branch: $(git branch --show-current) | último commit: $(git log -1 --format='%h %s' | cut -c1-80)"
python3 bin/lint_archivo.py --stats 2>/dev/null
ULTIMO_NB=$(ls -t notebook/2026-*.md 2>/dev/null | head -1)
echo "último notebook: ${ULTIMO_NB#notebook/}"
ACTIVAS=$(sed -n '/## Activas/,/## En cola/p' research/pending.md | grep -c '^| `')
echo "research activo: ${ACTIVAS} investigación(es)"
LINT=$(python3 bin/lint_archivo.py --pre-commit 2>/dev/null | tail -1)
echo "lint: ${LINT}"
echo "skills: /volcado /clase /panteon /future /research /donde-quede /pista — doctrina en CLAUDE.md"
