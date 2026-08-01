#!/usr/bin/env bash
# Installs every skill from src/ into ~/.claude/skills/ (overwrites same-named).
set -euo pipefail

dst="${1:-$HOME/.claude/skills}"
root="$(cd "$(dirname "$0")/.." && pwd)"
mkdir -p "$dst"

for skill in "$root"/src/*/*/; do
  name="$(basename "$skill")"
  rm -rf "${dst:?}/$name"
  cp -r "$skill" "$dst/$name"
  echo "installed: $name -> $dst/$name"
done
