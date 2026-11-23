#!/bin/sh
set -e
here=$(cd "$(dirname "$0")" && pwd)

link() {
  mkdir -p "$(dirname "$2")"
  [ -L "$2" ] || [ ! -e "$2" ] || { echo "skip (exists, not a symlink): $2" >&2; return; }
  ln -sfn "$1" "$2"
}

skills() {
  dir=$1; shift
  if [ $# -eq 0 ]; then
    for p in "$here"/skills/*/; do set -- "$@" "$(basename "$p")"; done
  fi
  for s in "$@"; do link "$here/skills/$s" "$dir/$s"; done
  for l in "$dir"/*; do
    [ -L "$l" ] && [ ! -e "$l" ] && case "$(readlink "$l")" in "$here"/skills/*) rm "$l";; esac
  done
  return 0
}

skills ~/.claude/skills
skills ~/.codex/skills

link "$here/AGENTS.md" ~/.claude/CLAUDE.md
link "$here/AGENTS.md" ~/.codex/AGENTS.md

python3 "$here/configure-codex.py" "$HOME/.codex/config.toml" "$HOME/.codex/skills/.system"
