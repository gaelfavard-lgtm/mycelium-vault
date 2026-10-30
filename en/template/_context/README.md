# `_context/` — what describes the system, not the work

Lives alongside IPCRA. Here you find:
- `MEMORY.md` — the index read at every startup (cap ~60 lines);
- `profile/` — the 2 notes read at startup (`profile.md`, `working-guidelines.md`), plus
  those that are only opened on request;
- `tickets-done.md` — the register of files taken out of `0-Inbox` (read by `logbook-guard.py`);
- `session-logs/` — created by the optional hook `session-extract.py`. **Authoritative on nothing.**

The startup budget (300 lines, `AGENTS.md` §7) counts `MEMORY.md` and the 2 profile notes.
