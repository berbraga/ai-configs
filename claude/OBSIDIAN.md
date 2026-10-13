# Obsidian Notes

Vault: `~/Obsidian/Claude` (sincronizado via git pelos hooks SessionStart/SessionEnd).

## Estrutura

```
~/Obsidian/Claude/
├── memory/      # memória nativa do Claude (autoMemoryDirectory) — não escrever aqui por estas regras
├── Projects/    # uma nota por projeto: <nome-projeto>.md
├── Decisions/   # uma nota por decisão: YYYY-MM-DD-<slug>.md
├── Reference/   # referência técnica reusável: <tema>.md
└── Pessoas/     # uma nota por pessoa: <Nome Sobrenome>.md
```

Essas são as pastas base. **Pode criar pasta nova à vontade** — na raiz (novo tipo de nota que não cabe nas existentes, ex.: `Clientes/`, `Incidentes/`, `Estudos/`) ou subpasta dentro de uma existente (ex.: `Reference/Cloudflare/`) quando um tema crescer. Antes de criar, checar se já existe pasta com o mesmo propósito para não duplicar. Ao criar pasta nova na raiz, adicionar uma linha nesta árvore. Nunca escrever em `memory/` por estas regras.

Nome do projeto = nome da pasta do repositório (ex.: `Renov-Home`).

## Consultar antes de perguntar ou editar

- **Antes de tirar qualquer dúvida com o usuário**: buscar no cofre (grep pelo tema em `Projects/`, `Decisions/`, `Reference/`, `Pessoas/`, `memory/`) se ela já foi respondida. Se a resposta estiver lá, usar e não perguntar.
- **Antes de cada implementação ou edição**: ler `Projects/<repo>.md`, as `Decisions/` ligadas e buscar o tema em `Reference/` e `memory/`. Respeitar decisões e gotchas registrados.

O PreToolUse hook (`~/.claude/hooks/obsidian-hook.py pretool`) nega `AskUserQuestion`, `Edit`, `Write` e `NotebookEdit` enquanto o turno não tiver consultado o cofre. Pergunta em texto livre não passa pelo hook — a regra vale igual.

## Ler antes de começar

No início de qualquer tarefa num projeto, ANTES de agir: ler `Projects/<nome-projeto>.md` (se existir), as `Decisions/` linkadas nela e dar uma olhada em `Reference/` por tema relevante. Se a tarefa envolve alguém, ler `Pessoas/<nome>.md`. Objetivo: não repetir erro/decisão já documentada nem redescobrir gotcha conhecido. Se nota não existir, seguir normal.

## Quando salvar

Não pedir permissão, é rotina. **Todo conhecimento novo vira nota na hora** — pessoa nova, decisão, gotcha, config, convenção: criar a nota se não existir, editar se já existir. Não esperar o fim da sessão. O Stop hook (`~/.claude/hooks/obsidian-hook.py stop`) cobra isso em toda resposta que usou ferramentas e não gravou nada no cofre.

- **Toda sessão com trabalho real** (não trivial: mais que pergunta rápida, typo ou comando simples): no fim, adicionar entrada no `## Histórico` de `Projects/<nome-projeto>.md` — criar a nota se não existir.
- **Decisão tomada** (arquitetura, lib, abordagem escolhida entre alternativas, incluindo decisão do usuário que encerrou debate): criar nota em `Decisions/` e linkar no projeto.
- **Conhecimento reusável entre projetos** (comando, snippet, config, gotcha de ferramenta): criar ou editar `Reference/<tema>.md`.
- **Pessoa relevante** (quem é dono de quê, papel, como prefere receber review, contexto de trabalho): criar ou editar `Pessoas/<nome>.md`. Só contexto profissional — nada de dado pessoal sensível (saúde, família, opinião sobre a pessoa). Usar they/them se o pronome não foi dito.

Editar nota existente (append) em vez de recriar. Não duplicar o que já está no código, no git ou em `memory/`.

## Formatos

### Projects/<nome-projeto>.md

```markdown
# <nome-projeto>

Repo: <url ou caminho> · Stack: <...>

## Arquitetura
...

## Convenções
...

## Gotchas
- ...

## Decisões
- [[YYYY-MM-DD-slug]] — resumo de uma linha

## Histórico
### YYYY-MM-DD — <tópico>
- Feito: ...
- Pendente: ...
```

### Decisions/YYYY-MM-DD-<slug>.md

```markdown
# <decisão em uma frase>

Data: YYYY-MM-DD · Projeto: [[<nome-projeto>]] · Status: aceita | substituída por [[...]]

## Contexto
## Opções consideradas
## Decisão e porquê
## Consequências
```

### Reference/<tema>.md

```markdown
# <tema>

Atualizado: YYYY-MM-DD

## <subtópico>
...
```

### Pessoas/<Nome Sobrenome>.md

```markdown
# <Nome Sobrenome>

Papel: ... · Time/empresa: ... · Projetos: [[...]]

## Contexto
- YYYY-MM-DD: ...
```

## Links

Sempre linkar com `[[nome-da-nota]]`: projeto ↔ decisões ↔ pessoas ↔ referências. Link pra nota que ainda não existe é ok — marca algo a escrever.
