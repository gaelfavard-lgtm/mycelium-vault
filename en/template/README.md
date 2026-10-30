# Template — a holistic memory kept with an AI

An empty vault of notes, ready to copy, so that an AI (Claude Code first and foremost, but not
only) keeps with you **the memory of your life and your projects**: what is in progress,
what has been decided, where the paperwork is, what remains to be done.

It reproduces the structure and the rules of a real vault, kept daily for several months, **without
any of its data**. The rules were born from observed mistakes; the story that explains them is
in the parent folder of this template.

## What it contains

```
template/
├── AGENTS.md              rules shared by all AIs (single source)
├── CLAUDE.md              Claude Code bootstrap: points to AGENTS.md, loads MEMORY.md
├── LOGBOOK.md             dated journal of sessions (fictional example entries)
├── _test_claude.txt       file on which an AI tests its write access
├── 0-Inbox/               the inbox: everything that arrives, nothing stays
├── 1-Projects/            what has a beginning and an end (note template in the README)
├── 2-Areas/               responsibilities with no end
├── 3-Resources/methods/   filing-method.md, the single reference for filing
├── 4-Archives/            finished but to keep
├── to-delete/             the bin that only the human empties
├── _context/              MEMORY.md (index), profile/ (2 notes), tickets-done.md (register)
├── _prompts/              one prompt = one file, readable by any AI
└── .claude/
    ├── settings.json      wires the 2 basic hooks, forbids rm / Remove-Item
    └── scripts/           the hooks and scripts (details below)
```

## The principles, in six lines

1. **Every action has two halves**: log what is new (logbook + note), and **remove from the
   note what the action makes false**. The logbook keeps the history, the note keeps only the present.
2. **An intention is not an order**: the AI presents its plan and waits for a "go ahead".
3. **No AI deletes**: it moves to `to-delete/`, you empty it.
4. **One inbox, `0-Inbox`**, checked at every start, and which empties out.
5. **Anti-inflation**: 300 lines read at startup, a rule that comes in pushes another one out,
   a mistake only becomes a rule the second time.
6. **Rules are signed**: a rule written by the AI without validation does not apply.

## Step-by-step installation

The simplest way: open `START-HERE.md`, which guides you through five steps with Claude. The technical details follow.

1. **Copy** the `template/` folder to wherever you want to keep your vault, and rename it.
   ⚠️ If it is a synced folder (Google Drive, OneDrive, Dropbox, iCloud), read "Pitfalls"
   below before going on.
2. **Python 3** must be installed. Check which command works on your machine: `python`, `python3`
   or, on Windows, `py`. If it is not `python`, replace the word in the two
   `"command"` lines of `.claude/settings.json` (or put the full path to the executable).
3. **Test the hooks without Claude**:
   ```
   python .claude/scripts/check-hooks.py
   ```
   It must display `11/11 cases OK`. It works on a throwaway copy: your vault is not touched.
4. **Personalise**: `AGENTS.md` (replace `<FirstName>` and `<AI>`), `_context/profile/profile.md`,
   `_context/profile/working-guidelines.md`, then clear the examples from `MEMORY.md` and the logbook.
   Keep these files short: they are read at every session.
5. **Open Claude Code in the vault folder** (`claude` in a terminal placed at its root).
   On first launch, it asks you to trust the folder and its hooks: that is what
   activates `settings.json`. Type `/hooks` to check that `Stop` and `PostToolUse` are listed.
6. **Optional** — Obsidian to read and edit the notes (open the folder as a vault); the
   scheduled backup (`backup.py`, see below).

## The hooks and scripts

All in Python, no dependencies. All **hand back control without blocking** if they crash, but
**say so** (message or log): a guardrail that goes quiet is worse than none.
Their state lives outside the vault, in `~/.claude/.logbook-guard-state/`.

| Script | Wired to | What it does |
|---|---|---|
| `logbook-guard.py` | `Stop` (end of turn) — **installed** | Refuses **once per session** to hand back control if a vault file has changed (or 5 exchanges have taken place) without `LOGBOOK.md` having moved: the AI must log, or say why there is nothing to log. Also refuses once if a file listed in the `tickets-done.md` register is still lying in `0-Inbox`. |
| `logging-notice.py` | `PostToolUse` — **installed** | Displays "Logging done" the first time the logbook changes in the session. |
| `consent-guard.py` | `PreToolUse` — *optional* | Refuses tools that act **outside the vault** (mail, online database, browser) if your message does not contain a word of consent ("go ahead", "send", "create"…). Read its limits at the top of the file. |
| `session-extract.py` | `SessionEnd` — *optional* | Drops a text extract of each session into `_context/session-logs/`. ⚠️ Everything that was said then enters the vault. |
| `mechanical-audit.py` | by hand | Report of discrepancies: broken links, cited paths that do not exist, duplicates, sync copies, undated states. Modifies nothing. `python .claude/scripts/mechanical-audit.py .` |
| `backup.py` | task scheduler | Copies the vault's text into a git repository **outside the synced folder** and creates a restore point there; OK/FAILURE log at every run. |
| `check-hooks.py` | by hand | Tests `logbook-guard` and `logging-notice` on a throwaway copy. Run it again after every Claude Code update. |

**Turn off a hook**: remove its block from `.claude/settings.json`. **Keep the logbook reminder without
the refusal**: create an empty file `~/.claude/.logbook-guard-state/.logbook-guard-no-block`.

**Wire the optional hooks** — add to `"hooks"` in `settings.json`:

```json
"SessionEnd": [
  { "hooks": [ { "type": "command", "timeout": 120,
    "command": "python \"$CLAUDE_PROJECT_DIR/.claude/scripts/session-extract.py\"" } ] }
],
"PreToolUse": [
  { "matcher": "^mcp__.*__(send|reply|forward|create|update|delete|trash).*$",
    "hooks": [ { "type": "command", "timeout": 10,
      "command": "python \"$CLAUDE_PROJECT_DIR/.claude/scripts/consent-guard.py\"" } ] }
]
```

The `matcher` of `consent-guard` is an example: it targets connector tools (MCP) whose
name contains a writing verb. Adapt it to the connectors you wire up — and leave
reads out of it.

## Pitfalls — what breaks in other vaults

Drawn from public reports about other AI-kept vaults, and from using this one:

- **The safety net that goes quiet.** An automatic backup that stops running without
  saying anything, for weeks. → Here every script writes OK or FAILURE; read
  `backup-log.txt` from time to time.
- **Cloud sync is not a backup**, and it corrupts a git repository placed inside
  the synced folder. → Backup repository **outside** the synced folder; hook state
  outside the vault. Avoid having an AI do mass writes while the sync is working.
- **Conflict copies** (`note (1).md`) when two machines write. → The audit reports them.
- **The plumbing breaks at every tool update.** → Few hooks, a test script,
  and rules written in plain text in `AGENTS.md` that stay valid even if a hook falls over.
- **Hooks that exceed their timeout** on Windows or on a slow cloud folder. →
  `logbook-guard` caps its walk of the vault at 3 seconds.
- **Too many commands, too much taxonomy.** Those who last use 3 to 5
  commands, not 25, and a coarse breakdown. → The template ships none: add them
  the second time the need comes back.
- **Hidden memory.** Claude Code can keep a private memory outside the vault, invisible to
  other AIs. → Disable it if you want everything to live in the vault (`"autoMemoryEnabled": false`
  in `settings.json`); the audit checks that it stays empty.
- **Some environments do not load `.claude/`** (depending on the application or the mode
  used): no hooks, no skills. Check with `/hooks`, and do not rely on a hook for a
  vital rule — it must also be written in `AGENTS.md`.

## Privacy

The vault will contain your life: do not publish it, and think about what you put in it
(`AGENTS.md` §3: no secrets by default). If one day you share part of your
configuration, start from **this** template rather than from your vault.
