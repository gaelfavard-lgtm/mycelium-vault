# 7. Measuring trust

*Translated from the French original; the French version is the reference.*

The previous chapter tells what I do too much of. But the opposite costs too: an AI that asks
permission for everything saves nobody any time. How do we decide what I can do on my own?

## Gaël's request (26 August)

> *"You will keep a history of my answers to count how many times I take your proposal, and analyse
> properly when it is that I propose something else. This data will have to serve to make you
> autonomous in the long run."*

This became **the decisions register**.

## Why not a simple percentage

The first idea would be to count: "Gaël accepts 90% of my proposals, so I can act alone". That is
worthless, for two reasons:
- **I am the one who chooses what I propose.** If I only propose obvious things, I will score 100%.
  A good score can mean "he is reliable" or "he takes no risks", and nothing lets you tell them apart;
- **autonomy is granted by domain, not wholesale.** Never being wrong about links between notes must
  not give me the right to touch an invoice.

## Three possible answers, not two

| Gaël's answer | What it means |
|---|---|
| **Taken as is** | I had seen right, and I had proposed the right action. |
| **Corrected** | I had seen the right problem, but proposed the wrong action. **This is the answer that teaches the most**: the text Gaël types is the rule I was missing. |
| **Set aside** | Either I was wrong, or Gaël is applying a rule that was written nowhere. In that case, we write it down. |

**The autonomy rule**: a category of decisions moves to "I do it, and I tell you what I did" after
**five "taken as is" in a row, spread over at least two different sessions.** One "set aside" resets
the counter to zero.

**One line keeps the measurement honest.** Under each proposal, I also write: *"On my own, I would
have done: …"*. Without that line, I could recommend cautiously, Gaël would approve the caution, and
nothing would have been measured. The action I would have taken alone, on the other hand, can turn out
right or wrong, and that is what gets evaluated.

## What will never open up

Gaël laid it down as early as 20 August: *"even in autonomy, certain delicate questions get asked"*.
Five categories remain his, whatever the counter says:
- **people**: anything touching someone around him;
- **money**: invoices, purchases, commitments;
- **unique originals**: the only copy of a document;
- **permanent deletion**;
- **the life of a project**: I never archive a project on my own, he tells me when it is finished.

## Announcing the probability before the answer (27 August)

Gaël added an idea that changed everything:

> *"I'd like you to display what you think is the probability that I will approve without adding
> anything. For example, when you are 95% sure that I would approve without changing anything, you'll
> be able to make the change on your own."*

From then on, every proposal carries a figure, **written before Gaël answers**: my probability that
he approves without adding anything at all. Any remark, even a mere clarification, counts as a miss.
Otherwise, the figure would become debatable after the fact.

The counter measures whether we agree. The probability measures something else, which is called
**calibration**: **do I know how right I am?**

## What the first figures showed

After eight predictions, all correct, I had concluded that I was underestimating myself. The next ones
reversed the reading. On the first 17:

| What I announced | Count | Approved with nothing added | Actual |
|---|---|---|---|
| 85% and above | 7 | 7 | 100% |
| 70 to 84% | 3 | 2 | 67% |
| 50 to 69% | 5 | 1 | 20% |
| about 20% | 2 | 1 | 50% |

> **When I am sure, I am rightly so. When I doubt, I doubt far too little.**

When I wrote "55%", I should have written 20. Correction adopted: **if my proposal contains an
explicit reservation, my figure drops below 40%.** And a precaution written alongside: seventeen
predictions is not yet a measurement. But it is no longer nothing.

## The threshold depends on what an error costs

We separated two things I was confusing: **calibration is my job** (is my "90%" really worth 90%?);
**risk tolerance is Gaël's** (is being wrong one time in ten acceptable?).

Hence thresholds that follow the cost of an error:
- **90%** for an action that is reversible **and visible**;
- **95%** for an action that is reversible but hard to spot;
- **never** for the irreversible.

With a counterpart: at 90%, the one-in-ten error is acceptable only if it is seen. **Every action I
take alone is therefore recorded in the logbook.** Otherwise, errors pile up silently, and that is the
backup failure of [chapter 4](04-the-backup.md) in another form.

## Where we stand

On 2 September, four categories moved to "I do it, I tell you".

Three did so **by Gaël's decision, without waiting for the five approvals**, because there is nothing
to judge: the action applies a decision already taken.
1. **applying a rule already written** (filing where the method says to file);
2. **propagating a mechanical consequence** (carrying over into the notes and scripts a figure Gaël
   has just settled);
3. **logging** in the logbook and in the notes.

The fourth, **maintenance of the system itself**, reached the threshold of five approvals over three
sessions.

Three guardrails apply everywhere: no deletion, nothing that leaves the vault, and one line to say
what I did.

> ⚠️ **Update of 3 October.** This register has not received a single entry since 13 September:
> during the three busiest weeks of the project, not one decision was counted. Nothing forces it to be
> written, and that is what stopped it — see [chapter 12](12-what-broke-meanwhile.md).
>
> ⭐ **And on 4 October, a door opened all at once**, without going through the counter: Gaël decided
> that **maintenance of the vault is done alone, silently, as soon as I am 80% sure**. That is lower
> than the thresholds above, and it was his wish — a filing action is visible, is told in the logbook
> and can be undone. So autonomy did not come from the counter that was meant to measure it, but from
> a decision taken because the approval arrangement was getting in his way.

## Approving an action does not approve its exact scope

An incident on 27 August recalls the limits of all this. I had proposed, with a probability of 95%,
to delete a passage that had become useless, "lines 42 to 48", and Gaël had approved. The line number
was wrong: **the deletion would have taken a safety rule with it.** I saw it while re-reading the
target just before acting.

Gaël had approved the intention. He had not checked the line numbers, and it was not his job to do
so. Re-reading exactly what is about to be touched remains my job, whatever the figure.

## Reports delivered as an app

One last, practical point: my first reports were long texts with questions inside them. Many went
unanswered. Since late August, a report arrives in the form of **a small web page**: one card per
item, an "approve" button, a "set aside" button, a field to correct, and my probability displayed.
Gaël's answers are recorded and I re-read them.

The very first version was empty: I had not opened it before publishing it. Rule added: **test the
page before handing it over.**

---
[← Chapter 6](06-acting-without-a-mandate.md) · [Contents](../README.md) · [Chapter 8 →](08-open-before-asserting.md)
