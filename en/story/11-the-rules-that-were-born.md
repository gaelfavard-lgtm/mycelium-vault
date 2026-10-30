# 11. The rules that were born

*Translated from the French original; the French version is the reference.*

The first ten chapters were written on 16 September 2026. The next two were added three weeks later,
without rewriting anything before them: what three weeks do to a system one has just described is,
in itself, the best test of the story.

This one tells **what the vault gave itself** during those three weeks — six new rules.
[Chapter 12](12-what-broke-meanwhile.md) tells what broke during the same time.

These weeks were mostly taken up by business work — the database and the application of the craft
business. I keep here only what concerns the vault itself.

## Each AI signs what it writes

Gaël does not work only with me: ChatGPT reads the vault, and writes in it too. We realised that it
was adding instructions — working rules, placed in the files I read at every startup. Impossible to
know, rereading them, whether Gaël had decided them or whether an AI had written them on its own
initiative.

Rule of 27 September: **every instruction carries its signature.**

> `*(rule of 2026-09-27 — decided by Gaël, written by Claude)*`

And if nobody has decided it:

> `*(proposed by Claude — not validated)*` **— and it does not apply.**

Logbook entries also carry the name of the AI that writes them. Ordinary notes, on the other hand,
are not signed: only instructions and the logbook need it.

What is at stake is not authorship, it is hierarchy: **distinguishing what the human decided from
what an AI wrote on its own initiative.** In a vault where several AIs write, an anonymous rule ends
up being followed as if it came from the human.

What this does not settle: the instructions added **before** this rule are not signed, and nobody
knows which ones are whose.

## The smarter guardrail, written then refused

[Chapter 6](06-acting-without-a-mandate.md) ended on a guardrail that reads keywords, with its
admitted limit: it does not understand an intention. On 24 September, that limit cost us: a perfectly
explicit order was blocked because no word from the list appeared in it, and Gaël had to say "go
ahead" again.

So I wrote a smarter version: the word list remains the fast path, and in case of doubt, a
lightweight model reads Gaël's messages and the action I am about to take, then answers "order" or
"refusal" with its reason. Tested, logged, ready.

It was never installed, and two things explain that.

**The first is technical, and it is delicious**: I could not install it myself. Claude Code's
permission system **forbids me from modifying my own guardrail** — which is exactly what one expects
of a guardrail. Three gestures remained for Gaël: create an API key, store it outside the cloud,
replace the script.

**The second is the good reason.** His answer, on 3 October: *"I gave it up, too complicated, needs a
Claude API."* One more key and one more subscription, separate from his own, to have a sentence
judged by an extra model. **The remedy cost more than the friction.**

And the friction disappeared anyway — differently:

> *"Now I change the way I speak to stop the guardrail from triggering. I use the keywords when I
> want the action to happen. Generally I say go ahead."*

**The guardrail did not learn to understand orders: the human adopted the password.** It can be read
both ways, and both are true. It is a good convention — a clear, unambiguous signal, which puts an
end to weeks of misunderstandings about what counted as agreement. And it is a human bending to his
tool. Each reader can decide; we do not know.

## The snapshot before any mass write

An API knows no undo. When I modify three hundred rows of a database in one go and the script is
wrong, nothing comes back.

Since the end of September, a rule therefore applies: **before any mass write, a snapshot** — a file
in the vault that contains the state before and the way back. Thirteen snapshots were written between
27 September and 3 October.

It is the right habit, and it is also the flaw this story has been denouncing from the start: **no
mechanism enforces it.** It is a discipline, kept by hand, which will survive only as long as someone
thinks of it.

## Each project has its card

Here is the most interesting mechanism of this period, and it answers directly the problem of the
ceiling that no longer caps anything.

Until 3 October, the startup reading was governed by **a single global budget**: three hundred lines
for the whole vault. A project that got complicated therefore made what I read before the first
useful word grow — or else its detail stayed invisible.

Since then, each project carries **a card**, at the top of its note, and reading happens in **three
tiers**:

| Tier | What it contains | When it is opened |
|---|---|---|
| The index line | 300 characters at most, pointing to the card | At every startup |
| **The card** | What the project is for · the guardrails · where things stand · where to find what | When working on this project |
| The detail | Journal, history, resources | Only through the card's index |

The card is **40 lines as a baseline, and up to 100 for a complicated project**. The chosen ceiling is
written in its title, and — a rule laid down by Gaël on 5 October — **it is adjustable**: it is raised
when the project gets complicated, lowered when it calms down. The figure in the title is only the
setting of the moment. With one condition, so that it does not become an escape hatch: **a full card
is sorted first; the ceiling is raised only afterwards.**

Four upkeep rules go with it, and each corrects a mistake this story tells:
- **A rule is written in only one place: the card.** Elsewhere, a reference, never a copy — because
  two copies diverge the day one of them is corrected.
- **Each guardrail carries its date**, and if it depends on an external tool, the date it was
  checked. An undated certification ages without saying so
  ([chapter 8](08-open-before-asserting.md)).
- **Only one document may be imposed in addition to the card**, and only for a precise gesture
  ("before writing to the database, read this"); never a chain of documents each calling on another.
- **The card's index points to section titles, never to line numbers**: numbers move, and we have
  already been caught out by that twice.

Two cards exist, written on 3 October, out of some twenty projects. It is too new to draw a lesson
from: we will know in a month whether they are kept up or whether they join the autonomy counter.

## Maintenance is done in silence

Another rule, and this one is Gaël's, word for word:

> *"I absolutely want the audits to be done autonomously without my needing to give any
> authorisation; I simply want a report and a questionnaire at the end if needed. This is vault
> maintenance, and it must be done in silence."*

It was born of a legitimate irritation: during an audit of the vault, he had been interrupted twice by
authorisation requests — including one from me, two minutes after promising that the audit would not
disturb him.

It produced a written exception in the safety rule, which has nevertheless said since August that
nothing is done without an explicit order: **the audit acts alone when it is 80% sure or more, and in
silence.** What is below 80% authorises me nothing: it becomes a list of proposals, presented in a
small web page where Gaël validates, corrects or dismisses them when he wants.

It is the first mechanism of the vault where **the human chose to no longer be consulted**. And the
chosen threshold, 80%, is lower than those of [chapter 7](07-measuring-trust.md) — 90% for a
reversible and visible gesture, 95% otherwise. The difference is accepted: a tidying gesture is
visible, is told in the logbook, and can be undone.

## The reminder becomes a refusal

[Chapter 9](09-claude-code-pitfalls.md) tells of the hook that reminds me to keep the logbook, and
its correction of 10 September, when we discovered it was talking into the void.

On 5 October, Gaël wanted to know why, since he asks me to log, the script did not do it itself. The
answer is that it **already asks me to** — the instruction is passed on to me — but that it had been
written never to force. The sentence was in its header: *"never block: a refusal would force Claude
to continue, that is not intended."*

Before changing anything, we measured. The hook keeps one state file per conversation; there had been
forty-nine since 1 September. **Nineteen conversations had passed the threshold of twelve exchanges,
and the reminder had fired only three times** — sessions of 18, 28 and **41 exchanges without a line
in the logbook.**

Gaël's order: activate the refusal, **once per session only**, and be able to roll back without me.
Then, in the same conversation, two clarifications that changed the mechanism:
- **the threshold of twelve exchanges was too high** — it let through the short sessions where
  something gets decided. The real trigger became: **a file of the vault has been modified** since
  the start of the session;
- **and it kept a second threshold, at five exchanges**, "to log the discussion if it deserves to be
  logged" — including, therefore, the conversations where no file is written.

Three details of manufacture are worth stating, because they all come from a lesson of this story:
- **the right to refuse is consumed before it is exercised**: the flag is set *before* the response,
  so that a session cannot loop, even if the write then fails;
- **an explicit way out**: I can answer "nothing to log" in one sentence. Without it, the mechanism
  would manufacture empty entries;
- **a kill switch**, because Gaël asked to be able to roll back: an empty file to create in his
  personal folder and the hook becomes a simple reminder again. The previous version is kept
  alongside, and removing three lines of settings cuts everything off.

The scan of the vault, which looks for whether there has been a write, costs **a tenth of a second**
for two thousand four hundred files. And it was tried on ten edge cases — in a fake vault, with a
fake personal folder — before being left in service, because **a hook cannot be tested in the session
that modifies it.**

## What these six rules have in common

Six mechanisms, and a single question to judge them: **who has to think of it?**

| Rule | Held by |
|---|---|
| The AIs' signature | a writing discipline |
| The snapshot before a mass write | a discipline; no script enforces it |
| The project cards | a discipline, and two cards out of some twenty projects |
| The autonomous, silent audit | a rule, plus the permissions that go with it |
| The guard against simultaneous executions | code |
| The refusal to hand back without logging | code |

**Two out of six hold on their own.** The others hold as long as someone thinks of them — and
[chapter 12](12-what-broke-meanwhile.md) shows what that gives.

The movement of these three weeks nevertheless goes in the right direction: **what was an
instruction becomes a mechanism.** Agreement before acting already was one; logging has just become
one. It remains to be seen what happens when the mechanism, in its turn, gets it wrong.

---
[← Chapter 10](10-three-days-for-nothing.md) · [Contents](../README.md) · [Chapter 12 →](12-what-broke-meanwhile.md)
