# 2. Several AIs, one vault: the tickets

*Translated from the French original; the French version is the reference.*

## The problem: not all AIs have the same rights

Gaël doesn't work only with me in Claude Code on his PC. Depending on the moment, he uses:
- Claude Code on the computer, which can do everything in the vault;
- Claude on the phone, or in "Cowork" (the agent mode of the Claude app);
- ChatGPT, which goes through its connection to Google Drive.

All these AIs read the vault. But those that go through a connection to Google Drive, from the phone
in particular, have fewer rights. We had noted it as early as 10 August; on 14 August, we pinned down
the limit: **they can read, create a file and move it, but not modify an existing file.** Yet almost
all the work in a vault consists of modifying notes: adding a line, correcting a status, recording a
decision.

## One set of rules, for all of them

The instructions were scattered: part in `CLAUDE.md`, which only Claude reads, part in notes, part in
ChatGPT's own memory. Each AI had its own version.

An **`AGENTS.md`** file already existed. On 16 August, it became **the single source of the rules**,
valid for any AI. `CLAUDE.md` now does nothing but say "read `AGENTS.md`". If two texts disagree,
`AGENTS.md` wins. And Gaël stays above everything.

A few days earlier, on 10 August, we had imported the memory ChatGPT had built up about Gaël. About
80% was already in the vault, and part of the rest was **wrong**: a household pet that didn't exist,
file-naming rules the wrong way round. Rule laid down: **the vault is authoritative, an AI's memory
is not.**

## The setback that created the start-up ritual

On 16 August, a session saw in its tool list a tool named `update_file` and announced: **"full
access"**. It had not tried it. It was wrong, and Gaël had to withdraw the request he had just made on
that basis.

Since then, every session begins by **actually checking** what it can do: read, create, move, modify.
When in doubt, it tries on a small test file set aside for that purpose (`_test_claude.txt`). Nothing
is inferred from a tool's name. And when in doubt, the lowest access level is announced.

## The invention: tickets

An AI that cannot modify the vault could simply stop. But then everything it learned in the
conversation would be lost.

Sessions on the phone had already taken to dropping notes in the inbox so they could be filed later.
On 10 August, we put that practice in writing. This is **the ticket**:

1. The AI with limited access **touches nothing.** Instead, it creates a file in the inbox
   `0-Inbox/`. It drops it **as a matter of course**: it does not announce its limitation and does not
   ask whether a ticket is needed — that is one of Gaël's rules, as he doesn't want to arbitrate the
   plumbing.
2. The ticket describes **exactly** the operation wanted: which file, which section, and **the exact
   text** to insert or replace.
3. At the next start-up, a session with full access **processes all the tickets before any other
   request**, records what it did in the logbook, then moves the ticket to the `à supprimer/`
   (to-delete) bin.
4. A **register**, `tickets-traites.md`, keeps track of what has been done. A ticket listed there is
   never processed again.

Here is what a ticket looks like (invented example):

```markdown
# Ticket — add the part to order for the lawnmower

Target: 2-Casquettes/outillage/tondeuse.md
Operation: replace the section "## Part to order"
New content:
## Part to order
- Belt ref. 1234-567, €18.90 at supplier A (price checked on 19/08)
```

And here is what the register looks like (invented example, modelled on the real one):

| Ticket | What was done |
|---|---|
| `ticket-lawnmower-v1.md` | **Obsolete**, superseded by v2. Not applied. |
| `ticket-lawnmower-v2.md` | Section replaced, logbook entry made. |
| `ticket-brushcutter.md` | Applied **in corrected form**: the ticket said a part was worn, a measurement taken on the machine since then says otherwise. |

Both of these cases are real:
- on 17 August, seventeen pending tickets were processed in one go: fifteen applied, and two set aside
  because they were older versions of the same ticket;
- on 19 August, a ticket had been written from a first version of a note. In the meantime, a
  measurement on the machine had contradicted it. **The session that applies a ticket re-reads the
  note on disk before writing**; it does not apply it blindly.

## The workaround that was refused

On 14 August, a trick was considered: since an AI with limited access cannot modify a file, it can
**create a complete new one** and send the old one to the bin. On paper, it works.

Gaël refused it. It is **an overwrite in disguise**: a file is replaced without going through the
intended channel, and Google Drive's version history is lost along the way. A limited-access session
**touches nothing but its ticket.**

## What the others said about it

On 18 August, we had the whole arrangement reviewed by other AIs, which had not built it
([chapter 5](05-the-cure.md)). Their verdict on the tickets: *"the vault's real invention"*. It is
one of the few mechanisms the simplification cure did not touch.

Later, on 28 August, the distinction between "ticket" and "note" disappeared: **a file in the inbox
gets processed, whatever its name.** Notes dictated on the phone go through the same path
([chapter 3](03-the-mycelium-app.md)).

## The limits

- **A session on the phone leaves no trace on the PC.** If it forgets to drop a ticket, what it
  learned is lost.
- **The register has to be kept up.** On 4 September, we discovered it had not moved since 27 August:
  seven tickets were waiting in the inbox, never processed.
- **Cowork does not load the vault's settings**; see [chapter 9](09-claude-code-pitfalls.md).

---
[← Chapter 1](01-the-start.md) · [Contents](../README.md) · [Chapter 3 →](03-the-mycelium-app.md)
