# AI Configs

Configurações pessoais reproduzíveis para Claude Code e Codex CLI.

## Conteúdo

- `CLAUDE.md`: regras globais do Claude Code.
- `AGENTS.md` e `CODEX.md`: regras globais e entrada de documentação do Codex.
- `claude/` e `codex/`: RTK, hooks, settings, permissões e skills próprias.
- `plugins.md`: marketplaces e plugins instalados, sem copiar caches de terceiros.
- `install.sh`: instalação local com backup dos arquivos existentes.

Credenciais, históricos, sessões, caches, caminhos confiáveis e hashes locais não são versionados.
O `codex/config.toml` é uma versão portátil e sanitizada; ele não é aplicado automaticamente
para não apagar configurações locais específicas de cada máquina.

## Inicialização

```bash
gh repo clone berbraga/ai-configs ~/ai-configs
cd ~/ai-configs
./install.sh
```

O script instala o rtk, os plugins do Claude Code (incluindo superpowers), o graphify e o Obsidian sozinho.
Ao abrir o Claude Code num repositório git sem `graphify-out/graph.json`, um hook cria o grafo em
segundo plano (só código, local, sem custo de API) e coloca `graphify-out/` no `.git/info/exclude`. Os plugins do Codex
estão em `plugins.md`. Depois, reinicie o Claude Code/Codex.

## Memória do Claude

A memória fica no cofre do Obsidian em `~/Obsidian/Claude/memory` (repositório privado
`berbraga/obsidian`, clonado pelo `install.sh`). Os hooks do `claude/settings.json` fazem
`git pull` ao abrir uma sessão e commit + push ao fechar.

## Mudei algo numa máquina

```bash
cd ~/ai-configs && git pull && ./install.sh
```

Para levar uma mudança local para o repositório: `cp ~/.claude/settings.json claude/`, depois
`git commit -am "..." && git push`.

## Atualização

Edite os arquivos neste repositório e execute `./install.sh` novamente. O instalador cria
um backup com timestamp antes de substituir uma configuração existente.
