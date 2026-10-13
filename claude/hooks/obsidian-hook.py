#!/usr/bin/env python3
"""Hooks do cofre do Obsidian (~/Obsidian/Claude).

  obsidian-hook.py pretool  PreToolUse de Edit/Write/NotebookEdit/AskUserQuestion: nega se o
                            turno ainda não consultou o cofre (edição dentro do cofre é livre).
  obsidian-hook.py stop     Stop: bloqueia uma vez se o turno usou ferramentas e não gravou nada
                            no cofre; stop_hook_active libera, então não entra em loop.

"Turno" = tudo desde o último prompt real do usuário. Qualquer erro: sai 0 sem bloquear.
"""
import json
import re
import sys

VAULT = "Obsidian"
EDIT_TOOLS = ("Write", "Edit", "NotebookEdit")
LOOKUP_TOOLS = ("Read", "Grep", "Glob")
# Bash conta como escrita no cofre se cita Obsidian (direto ou via cd) e tem redirecionamento
# real (não 2>/dev/null nem >/dev/null) ou comando que escreve.
BASH_WRITE = re.compile(r"(?<![0-9&])>>?\s*(?!/dev/null)\S|\b(cp|mv|tee|touch|mkdir|sed\s+-i)\b")

STOP_REASON = (
    "Antes de encerrar, registre no cofre ~/Obsidian/Claude todo conhecimento novo deste turno, "
    "seguindo ~/.claude/OBSIDIAN.md. Para cada item, crie a nota se não existir ou edite a existente:\n"
    "- pessoa nova ou contexto novo sobre alguém -> Pessoas/<Nome>.md\n"
    "- decisão tomada -> Decisions/YYYY-MM-DD-<slug>.md + link em Projects/<repo>.md\n"
    "- comando, snippet, config ou gotcha reusável -> Reference/<tema>.md\n"
    "- arquitetura, convenção, gotcha ou trabalho do projeto -> Projects/<repo>.md (## Histórico)\n"
    "- preferência ou correção do usuário -> memory/\n"
    "- não cabe em nenhuma -> crie a pasta ou subpasta que fizer sentido\n"
    "Se não houve nada novo, apenas encerre sem gravar e sem comentar este aviso."
)

PRETOOL_REASON = {
    "AskUserQuestion": (
        "Antes de perguntar ao usuário, busque no cofre ~/Obsidian/Claude se essa dúvida já foi "
        "respondida antes (grep pelo tema em Projects/, Decisions/, Reference/, Pessoas/, memory/). "
        "Se a resposta estiver lá, use-a e não pergunte. Se não estiver, pergunte normalmente."
    ),
    "edit": (
        "Antes de implementar ou editar, consulte o cofre ~/Obsidian/Claude: leia "
        "Projects/<repo>.md, as Decisions/ ligadas a ela e busque (grep) o tema em Reference/ e "
        "memory/. Respeite decisões e gotchas já registrados. Depois refaça a edição."
    ),
}


def is_real_prompt(row):
    if row.get("type") != "user" or row.get("isMeta"):
        return False
    content = (row.get("message") or {}).get("content")
    if isinstance(content, str):
        return True
    return isinstance(content, list) and not any(
        isinstance(b, dict) and b.get("type") == "tool_result" for b in content
    )


def turn_tool_uses(transcript_path):
    rows = []
    with open(transcript_path, encoding="utf-8") as f:
        for line in f:
            try:
                rows.append(json.loads(line))
            except ValueError:
                continue
    start = max((i for i, r in enumerate(rows) if is_real_prompt(r)), default=-1)
    uses = []
    for row in rows[start + 1:]:
        if row.get("type") != "assistant":
            continue
        for block in (row.get("message") or {}).get("content") or []:
            if isinstance(block, dict) and block.get("type") == "tool_use":
                uses.append(block)
    return uses


def touches_vault(tool_input):
    return VAULT in json.dumps(tool_input or {}, ensure_ascii=False)


def looked_up_vault(use):
    name, tool_input = use.get("name"), use.get("input") or {}
    if name in LOOKUP_TOOLS or name == "Bash":
        return touches_vault(tool_input)
    return False


def wrote_to_vault(use):
    name, tool_input = use.get("name"), use.get("input") or {}
    if name in EDIT_TOOLS:
        return VAULT in str(tool_input.get("file_path", ""))
    if name == "Bash":
        command = str(tool_input.get("command", ""))
        return VAULT in command and bool(BASH_WRITE.search(command))
    return False


def stop(data):
    if data.get("stop_hook_active"):
        return None
    uses = turn_tool_uses(data["transcript_path"])
    if not uses or any(wrote_to_vault(u) for u in uses):
        return None
    return {"decision": "block", "reason": STOP_REASON}


def pretool(data):
    tool = data.get("tool_name")
    tool_input = data.get("tool_input") or {}
    if tool in EDIT_TOOLS:
        if VAULT in str(tool_input.get("file_path", "")):
            return None
        reason = PRETOOL_REASON["edit"]
    elif tool == "AskUserQuestion":
        reason = PRETOOL_REASON["AskUserQuestion"]
    else:
        return None
    uses = turn_tool_uses(data["transcript_path"])
    if any(looked_up_vault(u) for u in uses):
        return None
    return {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }
    }


def main():
    try:
        handler = {"stop": stop, "pretool": pretool}[sys.argv[1]]
        result = handler(json.load(sys.stdin))
    except Exception:
        return
    if result:
        print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
