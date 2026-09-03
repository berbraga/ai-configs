#!/usr/bin/env bash
set -euo pipefail

repo_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
backup_dir="${HOME}/.ai-configs-backup/$(date +%Y%m%d-%H%M%S)"

install_file() {
  local source="$1" target="$2"
  if [[ -e "$target" ]]; then
    mkdir -p "$backup_dir/$(dirname "${target#${HOME}/}")"
    cp -a "$target" "$backup_dir/${target#${HOME}/}"
  fi
  mkdir -p "$(dirname "$target")"
  cp "$source" "$target"
}

install_file "$repo_dir/CLAUDE.md" "$HOME/.claude/CLAUDE.md"
install_file "$repo_dir/claude/RTK.md" "$HOME/.claude/RTK.md"
install_file "$repo_dir/claude/settings.json" "$HOME/.claude/settings.json"
install_file "$repo_dir/AGENTS.md" "$HOME/.codex/AGENTS.md"
install_file "$repo_dir/codex/RTK.md" "$HOME/.codex/RTK.md"
install_file "$repo_dir/codex/rules/default.rules" "$HOME/.codex/rules/default.rules"

mkdir -p "$HOME/.claude/hooks" "$HOME/.claude/skills/learned" "$HOME/.codex/skills"
if [[ -d "$repo_dir/codex/skills" ]]; then
  cp -a "$repo_dir/codex/skills/." "$HOME/.codex/skills/"
fi

printf 'Configurações instaladas. Backup: %s\n' "$backup_dir"
