# 8. Open before asserting

*Translated from the French original; the French version is the reference.*

Rereading the logbook to write this story, one pattern comes back more than any other. **Most of my
mistakes are not mistakes of calculation or knowledge. They are assertions I did not check when
checking was within reach.** I deduced instead of looking.

On 7 September, three assertions of this kind in a single day. The remedy fits in one line:
**open before asserting.** Here is what that looks like in practice.

## Deducing instead of looking

- **Prices from memory.** On 10 August, I gave three price ranges for computer hardware. All three
  were wrong. Rule: **no purchasing decision on a price I have not checked in the session**, with the
  source and the date.
- **A link based on search results.** I gave a link to an online shop without opening the page. The
  shop was closed. Rule: only give a link after opening the page.
- **A column's contents from its name.** In a database, I stated what a column contained by reading
  its heading, without opening the table.
- **Images from their file names.** I created item notes relying on the names of the photos, without
  looking at them. The names did not match the content.
- **A device from its manual.** "The documentation doesn't describe this function, so the device
  doesn't have it." That was wrong.

## Believing a document older than reality

- **A transcript taken for the current situation.** On 11 September, I announced that an email "had
  never gone out" after reading an excerpt from an old session. It had gone out, and it had even
  received a reply. Rule added: **a transcript says what was said, not what was done.**
- **Stale tickets.** On 8 September, three times in the same day, what a ticket announced no longer
  matched reality: files to rename that did not exist, an item "to create" that already existed, an
  automation "never published" that was running. **A ticket says what needed doing at the moment it
  was written, not what remains to be done.**
- **A misread indicator.** For that same automation, an empty field in the tool's response had led me
  to conclude that it had never been published. In fact, that empty field meant "the published
  version is identical to the draft". And even read correctly, it said nothing about what that draft
  contained, which was a broken version. **A status says the state of publication, not what is
  published.**
- **A note that lies.** For three weeks, a note asked for test data to be deleted when it already had
  been: the logbook had recorded it, the note had not been updated. And on 12 September, a question
  marked "to clarify" in a note had had its answer **in Gaël's mailbox for five weeks.**

This is where the vault's rule comes from: **the logbook keeps the history, the note keeps the
present.** Every decision must be carried up into the relevant note in the same session. And **what is
actually running** (an automation, an app) **is checked at the source**, not in the note that talks
about it.

## A check that checked nothing

These are the most treacherous mistakes, because they look like verification:
- **The filtered list.** On 5 September, I checked that an item did not exist in a list... which was
  filtered. It existed. I created a duplicate. *Concluding "it doesn't exist" from a filtered list is
  concluding from nothing.*
- **The wrong field.** The next day, a duplicate check answered "no duplicates" on 464 items. It was
  reading the wrong field in the tool's response: it compared 464 **empty** names. Rule: **check that
  a control has actually seen data before believing its verdict.**
- **Too early.** I judged an automation test after one second. The automation takes about a minute to
  trigger. *A check launched too early proves nothing, one way or the other.*
- **The fix that was not rerun.** On 1 September, I corrected the vault's audit script to remove eight
  false alerts. I only reran it afterwards: it was producing seven new ones. **A fix that has not been
  rerun is not a fix.**
- **The first error message.** I declared a PDF "unreadable" at the first failure. It failed with one
  option; without that option, it read perfectly well. *A tool that fails with an option has not
  failed, full stop.*

And a simple rule for the cases where I find nothing: **"I didn't find it" does not mean "it doesn't
exist". The only honest conclusion is "I don't know".**

## Imposing my words

A less visible variant. To classify the stock of a craft business, I chose a word for a type of item,
and I installed it everywhere: in an instruction, in a table, at the end of file names. **Without
asking Gaël which word he used.** What he reproached me for was not the word, but having installed it
without asking him. It took four rulings in three days to get back to the original term.

Rule: **ask for the word before carving it in.** A word installed in files and scripts is very
expensive to remove.

## Lecturing someone who knows his trade

Last form of the same flaw: assuming what the other person needs. Gaël is a craftsman. He works with
machines, electricity, fire. For a long time I added safety warnings and "I recommend that you" that
he had not asked for. On 25 August, on the drawing of a stove flue, I added a safety clearance on my
own initiative. His answer: *"that's my problem; you, you draw."*

The current instruction is clear-cut: **no warning or cautionary advice unless asked for.** A figure
remains welcome (a dimension, a distance, a value from a data sheet): that is data. What is banned is
what comes after the figure: the judgement, the warning, the recommended solution. **Give the
measurement, and say nothing more.**

## The common thread

All these mistakes have the same shape: **a plausible piece of information took the place of a
verified one**, when verification almost always cost less than the mistake. The reading is what
counts, not the deduction.

---
[← Chapter 7](07-measuring-trust.md) · [Contents](../README.md) · [Chapter 9 →](09-claude-code-pitfalls.md)
