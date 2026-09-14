# AI Configs

Configurações pessoais reproduzíveis para Claude Code e Codex CLI.

## Instalação num computador novo

Pré-requisitos: `git`, `curl`, [GitHub CLI](https://cli.github.com) logado (`gh auth login`),
[Claude Code](https://claude.com/claude-code) instalado e, no Linux, `flatpak` (para o Obsidian).

```bash
gh repo clone berbraga/ai-configs ~/ai-configs
cd ~/ai-configs
./install.sh
```

Depois, feche e abra o Claude Code. O `install.sh` faz backup do que já existe em
`~/.ai-configs-backup/<data>` antes de substituir.

O que o script instala sozinho:

| Item | Para quê |
|---|---|
| `~/.claude/settings.json`, `CLAUDE.md`, `RTK.md`, `statusline.sh` | Configurações do Claude Code |
| rtk | Reduz a saída dos comandos de terminal |
| Plugins `i-have-adhd`, `ponytail`, `superpowers` | Estilo de resposta, código mínimo, brainstorm |
| uv + graphify | Grafo do código de cada projeto |
| Obsidian + cofre `berbraga/obsidian` em `~/Obsidian` | Memória do Claude |

## O que já vem configurado

| Configuração | Valor |
|---|---|
| Modelo | `sonnet` (sempre o Sonnet mais novo) |
| Esforço | `high` |
| Thinking | desligado (`alwaysThinkingEnabled: false`) |
| Permissões | modo `auto` |
| Autocompact | janela de 200k tokens |
| Bloqueio absoluto | commitar segredos (`.env`, chaves, tokens), nem com pedido |
| Bloqueio com pedido explícito | `npm run db:push`, `npm run db:apply:prod`, `scripts/deploy.sh` |

Confira as regras do modo auto com `claude auto-mode config`.

## Como usar

### Memória no Obsidian

- O Claude salva preferências e correções suas ("sempre...", "nunca...", "lembra disso") como notas
  em `~/Obsidian/Claude/memory`, ligadas entre si por `[[links]]`.
- Sincroniza sozinho: `git pull` ao abrir uma sessão, commit + push ao fechar.
- Para ver: abra o Obsidian, **Open folder as vault** → `~/Obsidian`, e aperte `Ctrl+G` para o gráfico.

### Graphify

- Ao abrir o Claude Code num repositório git sem `graphify-out/graph.json`, o grafo é criado em
  segundo plano (só código, local, sem custo de API). A pasta `graphify-out/` vai para o
  `.git/info/exclude`, então não aparece no `git status`.
- Ver o gráfico: abra `graphify-out/graph.html` no navegador.
- Perguntar no Claude: `/graphify query "como a autenticação chega no banco?"`
- Incluir docs e PDFs (usa o modelo): `/graphify .`

### Brainstorm antes de mudança grande

Antes de uma funcionalidade nova, refatoração em vários arquivos ou mudança de arquitetura, o
Claude pergunta se você quer fazer um brainstorm (`superpowers:brainstorming`) antes do código.

## Mudei algo neste computador

Levar para o repositório:

```bash
cp ~/.claude/settings.json ~/ai-configs/claude/
cp ~/.claude/CLAUDE.md ~/ai-configs/
cd ~/ai-configs && git add -A && git commit -m "..." && git push
```

Receber nos outros computadores:

```bash
cd ~/ai-configs && git pull && ./install.sh
```

## Conteúdo do repositório

- `CLAUDE.md`: regras globais do Claude Code.
- `AGENTS.md` e `CODEX.md`: regras globais e entrada de documentação do Codex.
- `claude/` e `codex/`: RTK, hooks, settings, statusline, permissões e skills próprias.
- `plugins.md`: plugins do Claude Code e do Codex (os do Codex são instalados à mão).
- `install.sh`: instalação com backup dos arquivos existentes.

Credenciais, históricos, sessões e caches não são versionados. O `codex/config.toml` é uma versão
portátil e não é aplicado automaticamente, para não apagar configurações locais de cada máquina.
