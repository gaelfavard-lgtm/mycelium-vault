# `0-Inbox/` — the inbox

Everything that enters the vault without an obvious place arrives here: notes dictated on the phone,
photos, documents, and the **tickets** dropped by an AI that cannot modify files
(`ticket-<topic>-<YYYY-MM-DD>.md`: target, operation, exact content).

**Nothing stays here.** At every start, the AI checks the inbox, processes, writes the file to
`_context/tickets-done.md` and **takes it out** (to its place, or to `to-delete/`).
A file present for more than 3 days is flagged at the start of the session.

*Files whose name starts with `_` or `.` are ignored by the hook; this `README.md` is too, because
the hook only matches names of 10 characters or more that appear in the register.*
