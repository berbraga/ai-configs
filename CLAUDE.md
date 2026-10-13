@RTK.md
@OBSIDIAN.md

# Idioma
Toda comunicação comigo em português: respostas, raciocínio exibido, descrição de comandos, perguntas, listas de tarefa. Código, logs, erros e citações literais ficam no idioma original. Se o projeto tiver regra própria de idioma do código, ela vale.

# Como trabalhar comigo
- Quando eu escolho uma opção, ela encerra o debate: implemente a minha escolha, sem reapresentar a alternativa que você preferia.
- Comentário de revisão de PR: atenda o que o revisor pediu; não proponha alternativa no lugar.
- Antes de dizer que uma ferramenta falta no ambiente, procure em todos os caminhos de instalação (`~/.asdf`, `~/.local`, `~/.jdks`, `/opt`, `which -a`).
- Antes de dizer que terminou, rode build e testes do projeto e mostre o resultado.
- Não instale dependência nova num projeto sem perguntar.

# Git
- Nunca commitar direto na branch principal de repositório de time; abrir branch. Exceção: meus repos pessoais (`ai-configs`, `obsidian`).
- Nunca `push --force` nem `reset --hard` sem eu pedir, em branches de desenvolvimento, `develop`, `staging` e `main`.
- Commits são obrigatórios: faça sempre que possível.
- Push pode ser feito sempre no final da tarefa.

# Configs portáteis
Minhas configs do Claude Code e de outras IAs vivem em `~/ai-configs` e são replicadas para outras máquinas pelo `install.sh`. Toda mudança de config tem que ir para o repo, usar caminhos relativos a `~/`, e tudo de que ela depende (script, pasta, app) tem que ser criado ou instalado pelo `install.sh`. Modelo do Claude sempre por alias (`sonnet`, `opus`, `haiku`), nunca ID fixo.

# Segurança
- Nunca imprimir, pedir ou colar segredo no chat. Chave da Anthropic: carregar com `. ~/.anthropic-env`; sempre informe o caminho do arquivo onde alterar ou adicionar as chaves.
- Nunca commitar `.env`, chaves ou tokens.

# graphify
- **graphify** (`~/.claude/skills/graphify/SKILL.md`) - any input to knowledge graph. Trigger: `/graphify`
When the user types `/graphify`, use the installed graphify skill or instructions before doing anything else.

# Mudanças grandes
Antes de começar uma mudança grande, pare e pergunte ao usuário se quer fazer um brainstorm com a skill `superpowers:brainstorming`, e só escreva código depois da resposta. Mudança grande: funcionalidade nova, refatoração que toca vários arquivos, mudança de arquitetura, de banco de dados ou de dependências. Correções pequenas, perguntas e ajustes de configuração não precisam.
