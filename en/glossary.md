# Glossary

*Translated from the French original; the French version is the reference.*

**`AGENTS.md`** — The vault's working-rules file, valid for every AI.

**Agent / sub-agent** — An AI to which another AI entrusts a precise task (for example reading part of
the vault), and which returns its result.

**Airtable** — An online database that looks like a spreadsheet.

**API** — The door that a service (Gmail, Airtable...) opens to programs, so that they can read or
modify data without going through the screen.

**Apps Script** — A free Google service for writing small programs hosted on one's Google account,
able to read from and write to Drive.

**Area** (*casquette*) — In the IPCRA method, a responsibility that lasts (paperwork, the garden, the
vehicles), as opposed to a project, which comes to an end.

**Artifact** — A small web page that Claude publishes, hosted by Anthropic (a plan, a form, a decision
app).

**Audit** — An inspection of the whole vault to find what is misfiled, broken or stale.

**BOM** — An invisible mark at the start of a text file, indicating its encoding.

**Calibration** — The fact that an announced probability matches reality: out of a hundred things
announced "at 90%", about ninety must turn out to be true.

**Claude Code** — Claude installed on the computer, able to read and modify files and run commands in
a folder.

**Connector (MCP)** — A link between Claude and an external service (Gmail, Google Drive, Airtable).
MCP is the name of the protocol used.

**Cowork** — The agent mode of the Claude app, which can work on a connected folder.

**CRLF** — The way Windows marks the end of a line in a text file. Linux uses a different mark.

**Git** — A free tool that keeps every successive version of a folder and lets you go back to any of
them.

**Holistic memory** — The name we give the vault: a memory where the domains are not separated (the
machines, the garden, health, the business), as opposed to the library of notes usually called a
"second brain".

**Hook** — A small program that Claude Code runs automatically at a precise moment: before a tool is
used, at the end of a response, at the end of a session.

**Inbox** — The folder where notes and tickets arrive before being processed.

**IPCRA** — The vault's filing method, named after the French folder names: Inbox, Projets
(projects), Casquettes (areas), Ressources (resources), Archives.

**`.jsonl`** — The format of the files in which Claude Code records its sessions: text, one line per
event.

**Logbook** — The file `CARNET-DE-BORD.md`: the dated history of the vault, written by each session
for the next.

**Make** — An online automation service that links applications together.

**Markdown** — A simple text format, readable as is, where `**bold**` is written with asterisks and
`# Title` with a hash sign.

**`MEMORY.md`** — The vault's index: one line per subject, read by Claude at every startup.

**Mirror (Google Drive)** — A Google Drive mode where the folder exists in full on the computer
**and** in the cloud, permanently synchronised in both directions.

**Note** (*fiche*) — A text file of the vault, on one subject: a project, a machine, a rule.

**Obsidian** — A free piece of software for reading and linking Markdown files.

**PARA** — A filing method created by Tiago Forte (Projects, Areas, Resources, Archives), of which
IPCRA is an adaptation.

**Sandbox** — The isolated environment where the AI runs its commands, with no access to the rest of
the computer except what it is allowed.

**Session** — A conversation with Claude, from start to finish. Each session starts from scratch.

**Skill / command** — A reusable instruction. A skill triggers when its subject comes up; a command
is launched by typing its name (`/note`).

**Snapshot** — A file written before a mass modification, containing the state before and the way
back. It replaces undo, which an API does not offer.

**Softr** — A service that builds web pages from an Airtable base, without code.

**Task Scheduler** — The Windows tool that launches a program at a fixed time or on an event (logging
on, for example).

**Ticket** — A file dropped in the inbox by an AI that is not allowed to modify the vault, describing
exactly the change to make.

**Token** — The unit in which an AI reads and writes text (about three quarters of a word). Everything
it reads has a cost in tokens.

**Transcript** — The complete record of a session: messages, tools called, results.

**Vault** (*coffre*) — The folder of text files that contains the whole system.

**Webhook** — A web address that automatically receives data when something happens elsewhere.

---
[← Contents](README.md)
