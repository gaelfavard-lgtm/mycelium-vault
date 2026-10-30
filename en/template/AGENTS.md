# AGENTS.md — Rules shared by all AIs

Applies to **any AI** (Claude, ChatGPT, other) that works with this vault. **Single source
of guidelines**: every rule is written here or in a file pointed to from here — never elsewhere.
In case of divergence, AGENTS.md prevails. The user keeps the final say over everything.

> *Template — adapt it.* Replace `<FirstName>` with the first name of the person who keeps the vault,
> and `<AI>` with the assistant's name (Claude, ChatGPT…). Then remove this note.

## 1. The vault

This vault is **the only reference**. IPCRA method: `0-Inbox` / `1-Projects` / `2-Areas` /
`3-Resources` / `4-Archives` + the `_context` layer. **Everything about filing** (zones,
criteria, duplicates, naming, audit): `3-Resources/methods/filing-method.md`, single
reference — decide nothing about filing without having read it.

## 2. Session start

a) **Factually check your access level** (read / create / move / **modify an existing
   file**) — test on `_test_claude.txt` if in doubt; never announce an access level by
   inferring it from a tool's name. Without the "modify" capability, the session is **limited-access**:
   it drops tickets and stops (see §5).
b) **Read this, and nothing more**: this file · `_context/MEMORY.md` (the index) ·
   `_context/profile/working-guidelines.md` (**guidelines**, not notes) ·
   `_context/profile/profile.md` · the last 2-3 entries of `LOGBOOK.md`.
   **The rest is opened when the topic comes up** — `MEMORY.md` says what to open and when.
c) **Check the inbox `0-Inbox/`** (compared with the register `_context/tickets-done.md`). With
   full access, process what is there before any other request (§5). A note from <FirstName> dropped
   there is an **order**. **Any file there for more than 3 days is flagged up front.**
d) **Hand back control in 5 lines max**: access, pending tickets, in progress, blockers.

## 3. Safety — NON-NEGOTIABLE

- **Nothing is created, renamed, overwritten or deleted without an EXPLICIT ORDER.**
  **An intention is not an authorisation**: "we're going to do X", a question, a technical
  answer are not orders. **Present the plan, then stay silent** — do not ask
  "shall I do it?": the question manufactures ambiguity, since any adjacent answer reads as
  consent. <FirstName> says "go ahead" on their own. Only exception: **logging** (§4), requested
  once and for all.
- **Delete = move to `to-delete/`**; <FirstName> empties it. Permanent = a targeted order, without
  ambiguity; at the slightest doubt about the target, stop and confirm.
- **No secrets in the vault** (passwords, API keys, tokens). If <FirstName> decides
  otherwise, they live in **a single file** they designate, never in a shared folder.
  Come across one elsewhere: report it.
- **Mass operations** (10+ files): always reversible, via `to-delete/`.
- **Outside the vault** (email, online databases, browser): we discuss, then <FirstName> says
  to execute. **An order on one point does not validate the whole plan.**
- When in doubt: ask before acting.

## 4. Logging — every action has two halves

1. **Log what is new**: dated entry in `LOGBOOK.md` (marker **[content]** or
   **[maintenance]**) **and** update of the relevant reference note, in the same session.
2. **Remove from the note what the action makes false.** The logbook keeps the history, the note
   keeps only the present — that is what makes erasing safe. An action is only finished after this.
   **A correction is searched for across the whole vault** (a grep of the old statement): mark
   `~~…~~ *(old — replaced on DD/MM: …)*` what is quick, and tell the logbook what was
   corrected — the audit catches the rest.
3. **Write in the present tense only what exists**; date every certification; after a rename, grep
   the occurrences in the same move; never copy a file name without reading the disk.
4. **A session log is authoritative on nothing**: it says what was said, never what was
   done afterwards. The state of a matter is read in its note.
5. **If no note carries the matter, creating it is part of the action** — unless <FirstName> says
   it does not need to live in the vault.
6. **Sign**: every guideline added to this file, to the guidelines or to the method carries
   `*(rule of YYYY-MM-DD — decided by <FirstName>, written by <AI>)*`, otherwise
   `*(proposed by <AI> — not validated)*` — and then **it does not apply**.
   Logbook: `[content] [<AI>]`. Ordinary notes: nothing.

The logbook marker is the measure: **[content]** = the vault served real life (a project,
a purchase, a decision); **[maintenance]** = the vault looked after itself. If maintenance
exceeds content for weeks, the system is working for itself, not for you.

## 4bis. Diagnosing

**When a fix fails twice, stop fixing and go find the missing fact**
(read the log, the exact error, the official docs) rather than trying a third variant.

## 5. `0-Inbox` tickets — deferred writes

**Limited access** (an AI that can read but not modify): it drops a ticket in `0-Inbox`
(`ticket-<topic>-<YYYY-MM-DD>.md`: target, operation, exact content), nothing else — by default,
without asking whether one is needed. **Full access**: process, log, write the **full
file name** to `_context/tickets-done.md` (which is authoritative: never reprocess what is there)
**and** take the file out of the inbox — filed in its place if it has value of its own (photo, document),
otherwise to `to-delete/`. **A processed file never stays in `0-Inbox`.** What awaits a
validation goes straight to its place; the question goes in the note, section "To clarify".
The end-of-turn hook (`logbook-guard.py`) refuses to hand back control if a file listed in the
register is still in the inbox; exception: section "Kept on purpose" of the register.

## 6. Answer style

**Short and direct**, answer then stop, no follow-up prompting; say "I don't know". The rest
(deciding, contradicting, searching before asking) is in `working-guidelines.md`.

## 7. Anti-inflation

- **Startup budget: 300 lines** (this file + `CLAUDE.md` + `MEMORY.md` + the 2 profile
  notes). **A rule that comes in pushes another one out.**
- **A mistake only becomes a rule on its second occurrence.** The first: one line in the logbook.
- **Few mechanisms**: every hook, script or skill added is a part that can break
  silently at the tool's next update. One is only added after the need has been observed
  twice.
- **Backup**: outside the synced folder, **no AI writes to the backup repository**.
