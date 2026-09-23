#!/usr/bin/env bash
# Installs skills from src/ into ~/.claude/skills/ (overwrites same-named).
#
# A directory is a skill only if it contains SKILL.md directly, so reference
# material such as src/references/ is never installed.
#
# Usage:
#   install.sh [dest]            install into dest (default ~/.claude/skills)
#   install.sh --check [dest]    compare only, exit 1 if anything differs
set -euo pipefail

mode="install"
if [ "${1:-}" = "--check" ] || [ "${1:-}" = "-c" ]; then
  mode="check"
  shift
fi

dst="${1:-$HOME/.claude/skills}"
root="$(cd "$(dirname "$0")/.." && pwd)"

# Collect skill directories: src/*/*/ that hold a SKILL.md.
skills=()
for candidate in "$root"/src/*/*/; do
  [ -f "${candidate}SKILL.md" ] || continue
  skills+=("${candidate%/}")
done

if [ "${#skills[@]}" -eq 0 ]; then
  echo "no skills found under $root/src (expected src/<group>/<skill>/SKILL.md)" >&2
  exit 1
fi

if [ "$mode" = "install" ]; then
  mkdir -p "$dst"
  for skill in "${skills[@]}"; do
    name="$(basename "$skill")"
    rm -rf "${dst:?}/$name"
    cp -r "$skill" "$dst/$name"
    echo "installed: $name -> $dst/$name"
  done
  echo "total: ${#skills[@]} skill(s) installed into $dst"
  exit 0
fi

# --check: report differences, never write anything.
if [ ! -d "$dst" ]; then
  echo "missing destination: $dst"
  echo "check FAILED: destination does not exist"
  exit 1
fi

problems=0
for skill in "${skills[@]}"; do
  name="$(basename "$skill")"
  if [ ! -d "$dst/$name" ]; then
    echo "MISSING:  $name (not installed in $dst)"
    problems=$((problems + 1))
  elif ! diff -r -q --strip-trailing-cr "$skill" "$dst/$name" >/dev/null 2>&1; then
    echo "DIFFERS:  $name"
    { diff -r -q --strip-trailing-cr "$skill" "$dst/$name" 2>&1 || true; } |
      sed 's/^/            /'
    problems=$((problems + 1))
  else
    echo "ok:       $name"
  fi
done

# Extra directories in dst are reported, but are not a failure.
for installed in "$dst"/*/; do
  [ -d "$installed" ] || continue
  name="$(basename "$installed")"
  found=0
  for skill in "${skills[@]}"; do
    if [ "$(basename "$skill")" = "$name" ]; then
      found=1
      break
    fi
  done
  if [ "$found" -eq 0 ]; then
    echo "foreign:  $name (not from ai_tools)"
  fi
done

if [ "$problems" -gt 0 ]; then
  echo "check FAILED: $problems of ${#skills[@]} ai_tools skill(s) differ from src"
  exit 1
fi
echo "check OK: all ${#skills[@]} ai_tools skill(s) match src"
