#!/usr/bin/env bash
# Estado de sesión — corre en SessionStart (hook de Claude Code).
# Imprime el contexto operativo del archivo + activa el pre-commit hook.
cd "$(dirname "$0")/.." || exit 0

# pre-commit hook idempotente
git config core.hooksPath bin/githooks 2>/dev/null

echo "=== EL VEHEMIURGO — estado de sesión ==="
echo "branch: $(git branch --show-current) | último commit: $(git log -1 --format='%h %s' | cut -c1-80)"
echo "fichas: $(ls archive/matches/*.md 2>/dev/null | grep -vc 'index\|README') matches · $(ls archive/segments/*.md 2>/dev/null | grep -vc 'index\|README') segments · $(ls archive/people/*.md 2>/dev/null | wc -l) people · $(ls archive/topics/*.md 2>/dev/null | wc -l) topics"
ULTIMO_NB=$(ls -t notebook/2026-*.md 2>/dev/null | head -1)
echo "último notebook: ${ULTIMO_NB#notebook/}"
ACTIVAS=$(sed -n '/## Activas/,/## En cola/p' research/pending.md | grep -c '^| `')
echo "research activo: ${ACTIVAS} investigación(es)"
PEND=$(grep -c '^- (✓)' notebook/2026-05-09-2-lista-personal-completa.md 2>/dev/null)
TOTAL=$(grep -c '^- ' notebook/2026-05-09-2-lista-personal-completa.md 2>/dev/null)
echo "lista personal: ${PEND} de ${TOTAL} bullets reconciliados (✓)"
LINT=$(python3 bin/lint_archivo.py --pre-commit 2>/dev/null | tail -1)
echo "lint: ${LINT}"
echo "skills: /volcado /clase /panteon /future /research /donde-quede /pista — doctrina en CLAUDE.md"
