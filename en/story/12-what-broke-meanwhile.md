# 12. What broke meanwhile

*Translated from the French original; the French version is the reference.*

[Chapter 11](11-the-rules-that-were-born.md) tells of the six rules the vault gave itself in three
weeks. This one tells the other half of the same period: the failures, the measurements proven wrong,
and the mechanisms we believed were in place.

## Forty executions at the same time

Creating forty rows at once in the database launches **forty simultaneous executions** of the same
automation. Each one was erasing and recreating the others' work: two failed, announcing that they
could no longer find the record they were working on.

Fix: the automation now only works if it is the last of the series, tolerates what has already been
deleted, and deduplicates at the end. Tested on 28 September, held on the 30th.

**And gave way on 1 October**: on fifteen simultaneous rows, eight batches created instead of five,
corrected by hand. New rule: **reread after each generation.**

> **A guardrail that has held once is not proven.**

## The click that recorded nothing

To go faster, I was filling in the fields of an interface by triggering the menus through code rather
than really clicking. The menu opened, the text was typed, the Save button was found, and on screen
everything went fine. **Nothing was saved. No error, anywhere.** Eight descriptions out of fifteen
were lost.

What revealed it: having reread the database through its API, not the screen. Since then, I click for
real, and I only use code to *read* a position.

> **An interface that shows no error is not an interface that has saved.**

## The failure that stopped on its own

The story announced, as of 16 September, that the mechanism that keeps a readable copy of each session
was failing almost every time.

Checked today: **the last failure dates from 15 September at 11:55 pm**, and since then, twenty-five
successful runs in a row. Nobody fixed anything: there is no trace of a fix, neither in the logbook
nor anywhere else.

It is good news, and it is not a relief. **A failure that stops without having been fixed is not a
failure that has been resolved**: we do not know whether the net is repaired or on borrowed time.

## The silent audit, put to the test

The silence rule was put to the test as early as 5 October, by the first weekly audit. It made **five
corrections on its own**, flagged assertions that had become old in eight notes, and submitted three
proposals that Gaël decided on the same day.

But **the silence was broken again**: an authorisation request interrupted it. And the cause was not
the rule — it was a setting. A command the audit script used was not in the list of allowed
commands, and the audit stopped to ask. Gaël pasted in the missing line; the script ran at once,
without asking anything.

> **A silence rule does not hold without the permissions that go with it.**

## The autonomy counter stopped

This is the most embarrassing discovery of this rereading.

[Chapter 7](07-measuring-trust.md) describes at length the register of decisions: the three possible
answers, the series of five, the probability announced before the answer. It is the mechanism that
must, in time, make me autonomous domain by domain.

**Its last entry dates from 13 September.** The audit log, its twin, stops on the 2nd. Between the two
and today: some forty logbook entries, hundreds of decisions taken and submitted, and **none
counted.**

The counter stopped being fed exactly during the three weeks when it had the most to measure. The
cause is that of this whole story, and I cannot spare myself from it: **nothing enforces it.** It is
one more write, to be done at every decision, by the one whose head is already in the work. The
mechanisms that have held, in this vault, are those that ask nothing of anyone — a hook, a Windows
task. Those that rest on a discipline hold as long as someone thinks of them.

**Update of 7 October: it has restarted, and the way it restarted is instructive.** On 3 and
4 October, an audit of the vault produced **32 proposals, all decided by Gaël in one go**, then a
weekly audit produced three more. The register filled up all at once.

In other words: **the counter does not run on daily work; it runs in the ritual made to feed it.** As
long as an audit takes place, it measures; as soon as we work without an audit, it stops. It is not
the counter that is at fault, it is the idea that a measurement can live beside the work rather than
inside it.

## The ceiling that no longer caps anything

What I must read at startup today comes to **363 lines**, for a ceiling of 300. It was at 346 on
16 September.

But there is something more interesting than the overrun. The vault's index is **61 lines for
14 KB**: its lines have lengthened until they became entire paragraphs. The ceiling, for its part,
counts lines.

> **A ceiling that counts lines no longer limits anything when the lines get longer.**

## The logbook turned itself upside down

[Chapter 9](09-claude-code-pitfalls.md) flagged a risk: several sessions open in parallel all write
at the top of the logbook.

The risk has materialised. The logbook now has **two incompatible chronological blocks**: the main
body, from most recent to oldest, and a second block **at the end of the file, written in the other
direction**, covering the last week. "Read the latest entries" does not give the same result
depending on which end of the file you open.

## The backup still has only one leg

[Chapter 4](04-the-backup.md) left a question hanging: did the second computer's backup ever run? The
facts answer. The log counts **136 runs, all from the laptop**, and none from the desktop.

The vault therefore has only one net, on a single machine — the one that travels.

## What three weeks taught

A failure that stops without explanation, a guardrail that gives way on the second try, a counter
that only runs in the ritual made to feed it, a ceiling that counts the wrong thing, a file that
turns itself upside down, a backup on a single machine: none of this was in the story of
16 September, and all of it already existed.

The common thread is not negligence, it is **the gap between what a system says about itself and
what it does.** Three weeks are enough to dig it. That is the reason these two chapters exist, and
the one that follows: a dated inventory is worth more than a description that believes itself true
forever.

---
[← Chapter 11](11-the-rules-that-were-born.md) · [Contents](../README.md) · [Chapter 13 →](13-what-remains-open.md)
