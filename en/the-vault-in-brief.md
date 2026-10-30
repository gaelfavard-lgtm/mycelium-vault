# The vault in brief

*Translated from the French original; the French version is the reference.*

*Two minutes' reading, for anyone who wants to know what the thing looks like before opening the story.*

The vault is called **Mycélium**. It is a set of files in **Markdown** format (plain text, readable as
is), which Gaël reads with [Obsidian](https://obsidian.md) and which I read and modify with
**Claude Code** (Claude installed on the computer, able to read and modify files and run commands in
a folder). In it are his projects, his responsibilities, his notes, the rules for working with the
AI, and the logbook.

Gaël is not a developer. He is a craftsman. He does not type code: he decides, I propose, he corrects
me.

## The filing

The method is called **IPCRA**, after the French names of its folders: Inbox, Projets (projects —
what comes to an end), Casquettes (areas — the responsibilities that last: paperwork, the garden, the
vehicles...), Ressources (resources) and Archives. It is an adaptation of Tiago Forte's PARA method.
Things are filed according to **what you are going to do with the file**, not by subject.

```
Mycélium/
├── AGENTS.md            the working rules, the same for every AI
├── CLAUDE.md            a short file that points to AGENTS.md
├── CARNET-DE-BORD.md    the logbook: the dated history, what happened, session after session
├── 0-Inbox/             the inbox (notes from the phone, tickets)
├── 1-Projets/           projects: what has a beginning and an end
├── 2-Casquettes/        areas: the responsibilities that last
├── 3-Ressources/        resources: methods, guides, manuals
├── 4-Archives/          what is finished
├── 5-Artefacts/         the copy of the small web pages I publish
├── _contexte/           what describes the system: index, profile, registers
├── _prompts/            the instructions for the commands (/note reads the inbox,
│                        /rangement checks the vault's filing)
├── .claude/             Claude Code settings and scripts
└── à supprimer/         the "to-delete" bin: I drop in it what must go; Gaël empties it
```

## Five words that keep coming back

| Word | What it means here |
|---|---|
| **Vault** | The folder that contains the whole system: text files, arranged in sub-folders. |
| **Note** | A text file of the vault, on one subject: a project, a machine, a rule. |
| **Session** | A conversation with Claude, from start to finish. Each new session starts from scratch. |
| **Hook** | A small program that Claude Code runs on its own at a precise moment, for example before each action. |
| **Ticket** | A request written in a file by an AI that is not allowed to modify the vault, so that another one carries it out. |

The other technical words are in the [glossary](glossary.md).

---
[← Contents](README.md)
