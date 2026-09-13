# Plugins do Claude Code

Instalados automaticamente pelo `install.sh`: `i-have-adhd@i-have-adhd`, `ponytail@ponytail` e
`superpowers@claude-plugins-official`. A regra de brainstorm antes de mudanças grandes está no `CLAUDE.md`.
O modo sempre ligado vem de `~/.claude/.i-have-adhd-always` e de `claude/ponytail.json` (`ultra`).

# Plugins do Codex

Os conteúdos de plugins não são copiados: são dependências de terceiros e ficam no cache.
Reinstale-os a partir das fontes oficiais:

```bash
codex plugin marketplace add https://github.com/ayghri/i-have-adhd.git --ref main
codex plugin marketplace add https://github.com/affaan-m/ECC.git
codex plugin marketplace add https://github.com/obra/superpowers.git
codex plugin add i-have-adhd@i-have-adhd
codex plugin add ecc@ecc
codex plugin add superpowers@superpowers-dev
```

O arquivo `codex/config.toml` registra os nomes resolvidos dos marketplaces e plugins.
