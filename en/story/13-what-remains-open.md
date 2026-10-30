# 13. What remains open

*Translated from the French original; the French version is the reference.*

A story that only speaks of solved problems gives a false picture. Here is what does not work, or not
yet, **as of 3 October 2026**. Several of these points were discovered while preparing this story,
then while rereading it three weeks later.

## What has been settled since 16 September

To be fair, let us start there:
- **The session excerpts work again** — but nobody repaired them
  ([chapter 12](12-what-broke-meanwhile.md)).
- **All four hooks are running.** As of 16 September, one was down; that is no longer the case.
- **The question of the second computer's backup is settled**, and the answer is no: none of the
  136 recorded runs comes from it.
- **Test data is no longer indistinguishable from the real thing**: a naming convention
  ("to-delete") and an up-to-date register say what is fictitious and how to purge it. It is not a
  mechanism, it is a written discipline — but the hole is no longer bare.
- **The guardrail that reads words and not intentions** received a remedy, written and tested. It
  was **refused** for its cost, and the friction dissolved because Gaël changed the way he speaks.

## Mechanisms that rest on discipline alone

- **The autonomy counter only runs in audits.** Stopped from 13 September to 3 October, it filled up
  all at once when an audit submitted 32 proposals. It is the pivot of
  [chapter 7](07-measuring-trust.md), and it measures nothing of ordinary work.
- **The snapshot before a mass write** is kept by hand, with no script to require it.
- **Instructions written before the signature rule are not signed**: nobody knows which come from
  Gaël and which from an AI.

## Incomplete nets

- **A single computer backs up the vault**, and it is the laptop.
- **Heavy files** (photos, PDFs, plans) **have no copy outside Drive**: the backup covers 513 text
  files; the vault weighs several gigabytes.
- **Sessions done elsewhere** (phone, Cowork, claude.ai) **leave no trace on the PC**
  ([chapter 2](02-several-ais-one-vault-the-tickets.md)).
- **This story itself is in no backup**: the folder that contains it is outside the vault and is not
  yet a git repository. Seventeen days since this was flagged.
- **A device label password is still in plain text in the logbook**, flagged on 16 September, still
  there.

## Problems without a mechanism

- **Nothing signals that a note no longer tells the truth.** The audit script finds broken links,
  not a note that lies on substance. The note of the refused guardrail announced for seventeen days
  an installation that would never come.
- **A ceiling that counts lines no longer limits anything** when the lines get longer: 363 lines at
  startup for a ceiling of 300, and a 61-line index weighing 14 KB. The **project cards**
  ([chapter 11](11-the-rules-that-were-born.md)) are the answer to this problem: a ceiling per
  project, adjustable, instead of a global budget. Two cards out of some twenty projects — too early
  to say whether the measure holds.
- **Nothing reads the inboxes when no session is running.**
- **Several sessions write to the same file without any lock** — the logbook bears the trace, with
  its two chronological orders.
- **A guardrail proven once is not proven**: the one protecting against simultaneous executions held
  twice, then gave way.
- **A failure that stops without explanation** does not say whether the net is repaired or on
  borrowed time.

## Tensions we do not know how to settle

- **Mechanisms.** The other vaults taught us that fewer mechanisms means fewer failures. We have
  five, plus four human disciplines, and it is the disciplines that give way. The latest-born — the
  refusal to hand back without having logged — is precisely a discipline converted into code: we
  will see whether it holds, and what it costs when it gets it wrong.
- **Rules.** Every incident makes one want to write a rule. Every rule added makes the others less
  well followed. The budget overflows anyway.
- **Autonomy.** Four categories are open, and Gaël decides everything else. That is intended. But the
  counter that was supposed to open others no longer runs.

## The question of duration

This vault is **eight weeks old.** Looking for accounts of experience, we found almost no story of
prolonged use of this kind of system. The most detailed testimony
([on DEV.to](https://dev.to/huy_tieu/i-finally-built-a-second-brain-that-i-actually-use-6th-attempt-4075))
described a sixth system, after several abandonments, which had held for three months; three weeks
later, its author had entirely reorganised it.

We do not know whether Mycélium will hold. A holistic memory has no value of its own: it is only
worth as much as it is kept up, and the day nobody writes in it any more, it is a folder of stale
files. **The only indicator we follow** is the [content] or [maintenance] label of each logbook entry
([chapter 5](05-the-cure.md)). If the [maintenance] entries end up dominating, the vault will have
become what it was meant to avoid.

This chapter will be completed. Chapters [11](11-the-rules-that-were-born.md) and
[12](12-what-broke-meanwhile.md) were born that way.

---
[← Chapter 12](12-what-broke-meanwhile.md) · [Contents](../README.md) · [The lessons →](../lessons.md)
