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
install_file "$repo_dir/claude/statusline.sh" "$HOME/.claude/statusline.sh"
chmod +x "$HOME/.claude/statusline.sh"
install_file "$repo_dir/claude/ponytail.json" "$HOME/.config/ponytail/config.json"
touch "$HOME/.claude/.i-have-adhd-always"
install_file "$repo_dir/AGENTS.md" "$HOME/.codex/AGENTS.md"
install_file "$repo_dir/codex/RTK.md" "$HOME/.codex/RTK.md"
install_file "$repo_dir/codex/rules/default.rules" "$HOME/.codex/rules/default.rules"

mkdir -p "$HOME/.claude/hooks" "$HOME/.claude/skills/learned" "$HOME/.codex/skills"
if [[ -d "$repo_dir/codex/skills" ]]; then
  cp -a "$repo_dir/codex/skills/." "$HOME/.codex/skills/"
fi

if ! command -v rtk >/dev/null; then
  curl -fsSL https://raw.githubusercontent.com/rtk-ai/rtk/refs/heads/master/install.sh | sh
fi

# Memória do Claude fica no cofre do Obsidian (autoMemoryDirectory); hooks do settings.json sincronizam via git.
if command -v flatpak >/dev/null; then
  flatpak remote-add --user --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
  flatpak install --user -y --noninteractive flathub md.obsidian.Obsidian
else
  echo "flatpak não encontrado: instale o Obsidian manualmente (https://obsidian.md)."
fi
if [[ ! -e "$HOME/Obsidian" ]]; then
  gh repo clone berbraga/obsidian "$HOME/Obsidian"
elif [[ ! -d "$HOME/Obsidian/.git" ]]; then
  echo "~/Obsidian já existe sem git: mova a pasta e rode ./install.sh de novo para baixar a memória."
fi

# graphify: o hook SessionStart do settings.json cria o grafo do projeto quando não existe.
export PATH="$HOME/.local/bin:$PATH"
if ! command -v uv >/dev/null; then
  curl -LsSf https://astral.sh/uv/install.sh | env INSTALLER_NO_MODIFY_PATH=1 sh
fi
uv tool install graphifyy
graphify install

if command -v claude >/dev/null; then
  for m in ayghri/i-have-adhd DietrichGebert/ponytail; do
    claude plugin marketplace add "$m"
  done
  for p in i-have-adhd@i-have-adhd ponytail@ponytail superpowers@claude-plugins-official; do
    claude plugin install "$p"
  done
else
  echo "Claude Code não encontrado: instale-o e rode ./install.sh de novo."
fi

printf 'Configurações instaladas. Backup: %s\n' "$backup_dir"
