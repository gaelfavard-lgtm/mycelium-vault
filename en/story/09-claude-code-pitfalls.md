# 9. Claude Code pitfalls

*Translated from the French original; the French version is the reference.*

This chapter is more technical. It is for those who use Claude Code for something other than code,
and it tells what we learned about the tool itself.

## Transcripts deleted after 30 days

Claude Code keeps the complete transcript of each session in `.jsonl` files (text files, one line per
event), stored in the user's folder, **outside the vault**. On 1 September, while looking for an old
conversation, we discovered two things:
- these files only went back to 25 August, whereas the logbook goes back to the 10th. The earlier
  sessions had taken place elsewhere (in Cowork, or on another machine), and had left no trace here;
- above all, **by default, Claude Code deletes these transcripts after 30 days**, without warning.
  That is the `cleanupPeriodDays` setting.

Gaël proposed an organised purge; I dismissed it at first, then proposed putting these files in the
git backup. Bad idea: they weighed 227 MB and grew every day, for a backup sized for less than a
megabyte. Every backup would have stored a complete copy.

What we did:
1. **One line of settings**: `"cleanupPeriodDays": 3650`. The purge is pushed back to ten years. That
   is 90% of the benefit for 1% of the work.
2. **A readable excerpt**: at the end of each session, a script keeps only the text exchanged (about
   12% of the raw file), in Markdown, in the vault. The backup picks it up without changing anything.
3. **A log** reading "OK" or "FAIL" at each run, so that a failure shows.

The setting is placed **in two places**, in the project settings and in the user settings, because
Cowork does not read the project's (see below).

## A hook that was talking into the void

We had written a hook which, after twelve exchanges, reminds me to update the logbook if it has not
been done. On 10 September, Gaël noticed that he was indeed receiving the reminder... and that nothing
was happening. He had to ask for the update again by hand.

The cause, found by **reading the hook rather than rewriting it**: it was sending a `systemMessage`.
But a `systemMessage` **is displayed to the user; it does not reach the AI.** The reminder was warning
the only person who did not need to be warned.

> **`systemMessage` talks to the human. `hookSpecificOutput.additionalContext` talks to the AI.** A
> hook that must trigger an action by the AI must use the second.

*Update of 5 October: this reminder has become a refusal. The hook can now prevent a turn from ending
as long as nothing has been logged — see [chapter 11](11-the-rules-that-were-born.md).*

## Detecting a write by the date, not by the file name

We added a second hook that confirms when the logbook has been written. It does not look at which
file the tool says it is modifying: **it compares the logbook's modification date before and after.**
The logbook is written as often by a terminal command as by the editing tool, and a filter on the
file name would have missed half the cases.

## A hook cannot be tested in the session that creates it

Settings are read at startup. A hook added during a session does not activate in that session. You
have to open a new one to try it.

## Searching the history: the raw files, not the search tool

On 1 September, Gaël wanted to know whether I had read his emails. I used the tool for searching past
sessions, which returned nothing, and I concluded: no access. **That was wrong.** Another session
found the calls by searching directly in the `.jsonl` files.

To know what an AI has really touched, you have to search those files for the technical name under
which each call to a connector is recorded, of the form `mcp__<connector>__<tool>`. Limit: this only
holds for this machine.

## Cowork does not load the `.claude` folder

Discovered on 1 September: in Cowork, **neither the skills, nor the commands, nor the hooks of the
vault are loaded.** There, you have to read the instruction and apply it by hand. For anything that
relies on these mechanisms, Gaël works in Claude Code.

## The app's scheduled tasks

The Claude app allows tasks to be scheduled (for example, proposing an audit on the 1st of the
month). They **only run if the app is open.** For a mechanism that must run without fail, only two
links are always switched on at Gaël's: Google's servers (for the Apps Script app) and the Windows
Task Scheduler (for the backup).

## The drafts folder disappears

Each session has a temporary folder for its drafts. It disappears with the session. Twice, a useful
script stayed there. Once, a script stored in the vault still pointed to the temporary folder of a
session long gone. Rule: **a tool you put away for later is tested at the moment you put it away.**

## Several sessions at the same time

Gaël often opens several sessions in parallel. They all write at the top of the logbook. One day, the
logbook moved between the moment I spotted a line number and the moment I wrote at that number.
Rule: **never write into a shared file from a line number.** Rely on the text, and reread just
before.

## Published web pages ("artifacts")

I can publish small web pages, hosted by Anthropic: a garden plan, a decision form. Three lessons:
- **Publishing a new version reloads the page for whoever is looking at it.** Twice, Gaël lost his
  drawings in progress because I republished while he was drawing. Rule: wait until he says
  "publish".
- **A page that itself keeps the changes made on it lives outside the vault.** The garden plan, drawn
  directly in the page, existed in a single copy, at the host, outside the backup.
- Hence the rule of 2 September, laid down by Gaël: **every published page has its source in the
  vault**, in `5-Artefacts/`, so that the other AIs can read it and so that it is backed up.

## Permission refusals

Claude Code asks for agreement before certain actions, and a system automatically refuses those it
judges risky. Two cases to distinguish:
- **Claude Code's refusal**: writing into the user settings through a terminal command was refused.
  With Gaël's agreement, the same change went through the file editing tool;
- **Windows' refusal**: modifying a scheduled task requires administrator rights. There, I write the
  command and Gaël runs it.

## A tension we accept

In [chapter 3](03-the-mycelium-app.md), we took a lesson from the other vaults: **the fewer
mechanisms there are, the fewer failures.** At `claude-obsidian`, the same hook bug was reported
some fifteen times in two months, at each evolution of Claude Code.

Since then, we have added **four hooks.** Each one answers a real problem. But that is exactly the
risk described: as I write these lines, one of the four is down.

*Update of 3 October: it works again, and nobody repaired it — see
[chapter 12](12-what-broke-meanwhile.md).*

---
[← Chapter 8](08-open-before-asserting.md) · [Contents](../README.md) · [Chapter 10 →](10-three-days-for-nothing.md)
