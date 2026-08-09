#!/usr/bin/env bash
set -euo pipefail

usage() {
  echo "Usage: ./install.sh <codex|claude|both>"
  exit 1
}

install_skill() {
  local source_dir="$1"
  local target_dir="$2"

  if [[ -e "$target_dir" ]]; then
    echo "Refusing to overwrite existing skill: $target_dir"
    echo "Remove or rename it first, then run this command again."
    exit 1
  fi

  mkdir -p "$(dirname "$target_dir")"
  cp -R "$source_dir" "$target_dir"
  echo "Installed: $target_dir"
}

case "${1:-}" in
  codex)
    install_skill "$(pwd)/codex" "$HOME/.codex/skills/figma-flutter-implementation"
    ;;
  claude)
    install_skill "$(pwd)/claude-code" "$HOME/.claude/skills/figma-flutter-implementation"
    ;;
  both)
    install_skill "$(pwd)/codex" "$HOME/.codex/skills/figma-flutter-implementation"
    install_skill "$(pwd)/claude-code" "$HOME/.claude/skills/figma-flutter-implementation"
    ;;
  *)
    usage
    ;;
esac
