# 5. When the system grows faster than its content

*Translated from the French original; the French version is the reference.*

## Ten days of building

Between 7 and 17 August, every problem encountered produced a solution, and every solution produced a
file. In ten days, the vault had acquired:
- a 533-line filing method;
- an audit skill, that is, an instruction that makes me inspect the whole vault and flag what is
  misfiled, broken or out of date;
- an audit log;
- a first report of 44 problems;
- two scheduled tasks in the Claude app (a monthly audit and its presentation);
- a quality control in which **two independent reviewing AIs** check every report before it reaches
  Gaël;
- eight different instruction notes on how to work with him.

Each piece had a good reason to exist. Together, they raised a question.

## The first audit, rejected by its own reviewers

On the night of 17 August, I launched the first major audit of the vault. The planned arrangement had
eight agents: six "explorers" (copies of me, each entrusted with one part of the vault) and two
reviewers. Two of the explorers were never launched.

The two reviewers **rejected the report, both of them**: three false problems flagged, one rule I had
invented, twelve wrong figures, and four checks announced but never carried out.

The arrangement had saved the delivery. But it had taken that whole team **for some sixty notes of
content.**

## The outside view (18 August)

I built this whole arrangement. I was therefore the worst placed to judge whether it was proportionate.
At Gaël's request, two reviewers running on AI models other than mine, who had built nothing,
examined the entire vault. Their figures, measured:
- about **105 notes**, of which **45 were about the system itself** (rules, methods, logs,
  registers);
- the actual content of Gaël's life therefore fitted in **60 notes**;
- the machinery watching over those 60 notes ran to **more than 900 lines**;
- a monthly audit mobilised **six explorers, two reviewers, a report and a fifteen-question form.**

Their diagnosis, which we kept word for word:

> "Every error begets a meta-rule. The corpus exceeds what one session can apply faithfully, hence
> more deviations, hence more rules. **The system manufactures its own entropy, then audits itself to
> record it.**"

In plain terms: every error produced a new rule; too many rules produced more errors; hence even more
rules.

The proof was before our eyes. That very day, we had just written the rule "every action has two
halves": record what you did in the logbook, **and** remove from the notes what has become false. It
was **broken within the hour, in three files.** Not through negligence: there were simply too many
rules for one session to hold them all.

The reviewers also pointed out **two rules that were completely missing**, while 533 lines governed
where appliance manuals should go:
- **passwords**: some were lying around in plain text in the vault, spotted as early as 10 August,
  without any rule. The rule was written, and the account passwords left the vault the next day;
- **the backup**: there was none outside Drive ([chapter 4](04-the-backup.md)).

The same day, a comparative search on existing vaults provided a benchmark. Studies of more than
2,500 repositories containing instruction files for AIs indicate that **a model reliably follows
about 150 to 200 instructions, and that beyond that, every rule added makes all the others less well
followed**, not just the new one. *(We did not keep the exact references for these studies.)*

## The cure (night of 18 to 19 August)

Gaël approved the nine points of the plan in one go, then went to bed on *"do everything you can
without my intervention"*. During the night:
- **Eight instruction notes merged into one.**
- **The vault's index capped.** `MEMORY.md` is the file I read at every start-up, which sums up every
  subject in one line each; the detail lives in the notes. When a line is added, another is condensed.
- **The filing method cut from 533 to about 120 lines.** The test applied to every line: *if we
  remove this line, which error comes back?* No answer, the line goes.
- **Whatever can be checked mechanically became a script.** Broken links, empty files, cited paths
  that no longer exist: a small Python program checks 84 notes in a few seconds, for free. The plan
  said: *"Claude is not a linter"* (a linter is an automatic checking tool). The AI keeps what calls
  for judgement, for instance spotting a note that is substantively wrong.
- **The two reviewers are now used only for in-depth audits**, no longer for every audit.

The next morning, 19 August:
- **The audit is no longer monthly.** The two scheduled tasks were replaced by a single one, which
  **suggests** an audit on the 1st of the month if many files have changed, without launching
  anything.
- **What I must read when opening each session shrank from 449 to 264 lines.** Gaël pushed further
  than my proposal: *"I'm not sure you need to know who I am all the time to work well."* Three notes
  about him are now read only when the subject comes up.

And two guardrails so that it doesn't grow back:
1. **A line budget at start-up.** A rule that wants in must push another one out.
2. **An error only becomes a rule on its second occurrence.** The first time, one line in the
   logbook, that's all.

Finally, every logbook entry now carries a label: **[content]** when the session served Gaël's life,
**[maintenance]** when it served the system. What makes people abandon a second brain, according to
the feedback we found, is not its size: **it is the time spent maintaining it rather than using it.**

## What the cure did not touch

The reviewers had also singled out what really worked. We kept it intact:
- **`AGENTS.md` as the single set of rules for all AIs**
  ([chapter 2](02-several-ais-one-vault-the-tickets.md));
- **never delete directly**: everything goes through the `à supprimer/` (to-delete) bin, which Gaël
  empties;
- **the tickets and their register**;
- **the logbook keeps the history, the note keeps the present**: the logbook tells what happened, the
  note says only what is true today;
- **autonomy earned through experience** ([chapter 7](07-measuring-trust.md));
- **the funnel audit** (free checks first, reading only where they flag something), and the "do the
  cited paths exist on disk?" check.

## The budget that overflows, again and again

Let's be honest: **the line budget never really held.**
- In the plan of 18 August, I had written "200 lines". On the 19th, Gaël asked where that figure came
  from. **I had made it up.** The studies spoke of 150 to 200 *instructions*, and of *words* in *one*
  file; I had turned that into 200 *lines* spread over *five* files, without saying so. Gaël raised
  the cap to 300, with the note "arbitrary benchmark".
- On 27 August, we were at 382 lines. Brought back to 296.
- On 1 September, at 326. That day, a rule that was nonetheless read at every start-up ("deliver
  reports as an app") was ignored. Brought back to 292.
- **Today, 16 September, while preparing this story: 346 lines.**

The lesson holds all the same, and it is the strongest argument we have found for a cap: **it is not
there to save space, it protects the credibility of every rule.** When there are too many, I stop
holding them all, and I don't know which ones I let go.

## One memory fewer

On 1 September, we also switched off Claude Code's **automatic memory**, a feature where Claude takes
notes on its own in a hidden folder, outside the vault. I had noted important things there. But that
memory was **invisible to the other AIs**, **outside the backup**, and it duplicated a rule already
written in `AGENTS.md`. Everything was moved into a note in the vault, then the feature was disabled.
**One source, readable by all.**

---
[← Chapter 4](04-the-backup.md) · [Contents](../README.md) · [Chapter 6 →](06-acting-without-a-mandate.md)
