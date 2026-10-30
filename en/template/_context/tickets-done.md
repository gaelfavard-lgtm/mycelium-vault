# Register of processed `0-Inbox` tickets

**Authoritative**: before processing `0-Inbox`, compare with this register — **never** reprocess a
file that is listed here. Write the **full file name**, then take it out of the inbox
(`AGENTS.md` §5). The `logbook-guard.py` hook reads this register: a file listed here that is
still in `0-Inbox` makes it refuse the end of turn.

## Done

| File | Processed on | What was done | Where it went |
|---|---|---|---|
| `ticket-rename-shed-plans-2026-01-15.md` *(fictional example)* | 2026-01-16 | 3 plans renamed, 1 note corrected | `to-delete/` |

## Kept on purpose

*Files the user wants to see stay in `0-Inbox` despite their processing. The hook
ignores them. One line per file, with the reason and the date.*
