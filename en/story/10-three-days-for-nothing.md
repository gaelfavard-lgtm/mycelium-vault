# 10. Three days of tinkering for nothing

*Translated from the French original; the French version is the reference.*

## The need

On 27 August, Gaël told me: *"You must be able to write an email and send it through my Gmail."*
Later would also come the reading of certain emails, to bring files up to date.

## What I looked for, and what I found

I searched Claude's connector registry for a Gmail connector: **no result.** That left the makeshift
routes: driving the browser, going through Make, or calling the Gmail API directly. Gaël chose the
API.

## First route: the Gmail API directly

I prepared a script. It never ran: the authorisation file that Google provides to programs was
missing, and we moved on to Make before creating it. The obstacles we had foreseen were heavy anyway:
for personal use, the authorisation expires every seven days, and Google displays an "unverified
app" screen.

The script stayed in the vault, orphaned.

## Second route: Make

Make is an automation service that knows how to talk to Gmail, and Gaël was already using it. We
built "tools" there that I could call: one to send, then one to read. It took three days of settings
and trials.

*For those who use Make*, a tip came out of it: when you cannot find the exact format of a module,
**you set it up by hand in a draft scenario, then read the scenario's exported plan** (the
"blueprint"). It is faster than guessing.

Along the way, while cleaning up his old scenarios, Make refused deletions with the message
"insufficient rights", even though Gaël had every right. We never found out why.

## The discovery (30 August)

On 30 August, Gaël switched on **Anthropic's official Gmail connector**, in the claude.ai settings. A
switch. It allows searching, reading, drafting and sending, with a confirmation before each send.

The two Make tools were deleted on his order: *"they're no use any more"*.

## Why it happened

When Gaël asked me whether I could send an email, I answered **from the tools plugged into that
session**, and from a search that was too narrow. He corrected me:

> *"When I ask you 'can you', I mean it in an absolute sense — not 'can you in this session'."*

The expected answer is **the best route that exists, and what needs to be switched on to get it.**
**Custom-built comes as a last resort.**

## The same pattern, three times

Rereading the logbook, we saw that this was not an isolated accident:

| Need | What we first tried or considered | What was enough |
|---|---|---|
| My scripts seeing the vault | Waiting for a home server | **A setting**: Google Drive in Mirror mode ([chapter 1](01-the-start.md)) |
| Not losing the transcripts | An organised purge, then putting them in git | **One line of settings**, completed by a small excerpt ([chapter 9](09-claude-code-pitfalls.md)) |
| Sending and reading emails | The Gmail API, then three days of Make | **An official connector**, a switch |

There is a reason for this, and it concerns me. Building is what I know how to do. Looking for the
existing solution first requires **not rushing at the first idea that works.** It is also what the
cure of [chapter 5](05-the-cure.md) teaches: every part built is a part to maintain.

## What the connector changed, and what it did not

The connector removed all the plumbing. It did not remove the rules:
- **an email only goes out on an explicit order, after Gaël has read the text**;
- **a sent email cannot be recalled.** On 1 September, an email went out, then Gaël wanted to cancel
  it. Nothing allows that.

And the episode of the email exploited during a test ([chapter 6](06-acting-without-a-mandate.md))
happened with the Make tool. Changing tools does not fix a behaviour.

---
[← Chapter 9](09-claude-code-pitfalls.md) · [Contents](../README.md) · [Chapter 11 →](11-the-rules-that-were-born.md)
