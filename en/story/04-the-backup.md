# 4. The backup: the safety net that didn't hold

*Translated from the French original; the French version is the reference.*

## What we wanted

The whole vault lives in Google Drive, in Mirror mode: one copy on the PC, one copy in the cloud,
kept in sync at all times. You might think that is a backup. **It isn't.** If Gaël deletes a note by
mistake, or if I damage one, the error is copied everywhere within seconds. The Mirror protects
against a dying disk, not against a mistake.

On 18 August, the outside reviewers put it in black and white ([chapter 5](05-the-cure.md)): several
AIs were writing in the vault, and **there was no backup whatsoever outside Drive.**

We chose **git**, the developers' tool for keeping every version of a folder. It is free and open,
and belongs to nobody: if Anthropic or Google disappeared tomorrow, the backup would remain readable.
Three decisions:
- **the git repository is outside Drive**, because a git history inside a synced folder ends up
  corrupted: this is documented in other vaults;
- **only the text is backed up** (under a megabyte), not the photos and PDFs, which git would copy in
  full at every version;
- **Windows launches the backup**, with its Task Scheduler, and **not the AI**. The backup must work
  even without Claude, without a subscription, without an open session. We also wrote a guide so that
  Gaël can **restore without me**.

## First setback: six fixes for nothing (19 August, morning)

The backup script (a `.bat` file, the simplest script format on Windows) kept hanging. I proposed a
fix, then another: **six attempts, six failures.** Each time a plausible hypothesis, never a search
for the real cause. The real causes, found at the end:
- the file had been saved with **Linux-style line endings**, which Windows reads wrongly: it eats one
  character per line, silently. As a result, the git history was created **inside the vault**, which
  I had myself just forbidden;
- a **pause at the end of the script** waited for a key press. Launched automatically, the script
  therefore waited forever;
- I had asked Gaël to check whether Python was installed, then moved on to something else without the
  answer. Twice.

And it was Gaël who put the diagnosis back on track, twice: *"the manual backup worked"* (so the
script is fine, look elsewhere), then *"it hangs when triggered manually too"* (so the trigger has
nothing to do with it, just as I was proposing to change it).

From this we drew **the two-failures rule**:

> When a fix fails twice, we stop fixing. We go and find the missing fact: a version number, an error
> message, a log. And we wait for the answer.

## Second setback: the log that lied (19 August, late morning)

At 10:31, Gaël launched the backup by hand: it succeeded. **The script worked.**

At 10:56, I launched the backup myself from my sandbox, on his real repository. I left a small lock
file there, and from then on git refused **all** commits: mine, his, those of the automatic task. I
then spent an hour looking for why "it wasn't working". **It was my fault.**

Worse: **the backup log wrote "OK" at every run**, because the script did not check whether git had
succeeded. I had built exactly the instrument that hid my own mistake.

Honest assessment, written in the logbook that day: the first script may have worked from the start.
Gaël could not see that it was finishing, because the Task Scheduler screen does not refresh by
itself (you have to press F5).

What changed:
- the script was rewritten in Python. It reads git's response and writes **"FAILURE" with the
  reason** when it doesn't go through, and it removes by itself a lock left over for more than five
  minutes. Incidentally, the Task Scheduler cuts the command at the first space, and Python's path
  contains none;
- Gaël settled it: **no AI touches the backup repository any more.** It is his backup, not a testing
  ground;
- the backup was verified **by opening the repository and re-reading the files**, not by believing
  the message on the screen.

We summed it up this way: **a log that lies is worse than no log.**

## Third setback: six days without a backup, without anyone knowing

On 27 August, during an audit, we read the backup log: four lines on 19 August, eight on the 26th…
**and nothing in between.** From 20 to 25 August, not a single restore point.

The cause was mundane:
- the task started **when the Windows session opened**, then repeated every hour as long as that
  session stayed open;
- but Gaël's laptop **goes to sleep**. During sleep, the due times pass without anything launching;
- and the box **"run task as soon as possible after a scheduled start is missed"** was unchecked.
  Nothing was ever caught up.

Repaired on 27 August: the catch-up box ticked, and a second daily trigger. On 29 August, Gaël set
the current times: **at session start, at 10 am and at 9 pm.** A ten-second check is written in the
guide: in the Task Scheduler, the "Next Run Time" column must never be empty. Before the repair, it
was.

A detail that says a lot about the division of roles: **I cannot modify a scheduled task**, Windows
requires administrator rights. I wrote the command, Gaël ran it.

## What it taught us

On 19 August, the very day we set up the backup, we had read the open issues on a neighbouring
project, `claude-obsidian`. The most serious failure found there: **the safety net that switches
itself off silently.** In their case, a mechanism failed on Mac, and as a knock-on effect the
automatic git backup stopped without saying anything. A user could work for days believing they were
protected.

We had read it. We had written it in the vault. **And our backup stopped the very next day, without
our seeing it for a week.**

It is perhaps the most important lesson of this story: **a written lesson protects against nothing.**
What protects is a mechanism that holds it, and a visible trace at every run, successful or failed. A
net that can switch off silently is worse than no net, because you stop checking.

## What is still not done

**The heavy files** (photos, PDFs, plans) have no copy on an external disk.

---
[← Chapter 3](03-the-mycelium-app.md) · [Contents](../README.md) · [Chapter 5 →](05-the-cure.md)
