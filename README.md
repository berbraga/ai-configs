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
git clone git@github.com:berbraga/ai-configs.git
cd ai-configs
./install.sh
```

Depois, reinstale os plugins listados em `plugins.md` e reinicie o Claude Code/Codex.

## Atualização

Edite os arquivos neste repositório e execute `./install.sh` novamente. O instalador cria
um backup com timestamp antes de substituir uma configuração existente.
