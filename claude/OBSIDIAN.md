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

Tudo numa pasta só por tipo, sem subpasta por empresa. Nome do projeto = nome da pasta do repositório (ex.: `Renov-Home`).

## Ler antes de começar

No início de qualquer tarefa num projeto, ANTES de agir: ler `Projects/<nome-projeto>.md` (se existir), as `Decisions/` linkadas nela e dar uma olhada em `Reference/` por tema relevante. Se a tarefa envolve alguém, ler `Pessoas/<nome>.md`. Objetivo: não repetir erro/decisão já documentada nem redescobrir gotcha conhecido. Se nota não existir, seguir normal.

## Quando salvar

Não pedir permissão, é rotina.

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
