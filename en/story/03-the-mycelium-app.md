# 3. The Mycelium app

*Translated from the French original; the French version is the reference.*

## The need

An idea comes while walking, in the garden, at the wheel. Opening the Claude app, waiting, explaining
the context: too long, the idea is lost. Gaël wanted **a button on his phone** to drop a note into
the vault.

## The choice: a single part

The first idea that comes to mind is an assembly: a form, an automation service such as Make, a web
address that receives the data, some storage. Gaël said no: *"avoid Make"*. We had read, in the bug
reports of other vaults, that **every part added is a part that can break**: the fewer technical
mechanisms, the fewer failures.

So we made **a small Google Apps Script web app**. Apps Script is a set of programs hosted for free
by Google, on Gaël's account. The same program displays the page on the phone **and** writes the file
to Google Drive. Since the vault is in Drive in Mirror mode, the note reaches the PC between a few
seconds and two minutes later.

**Voice needs no code**: the phone keyboard's microphone dictates into the text field. That is what
makes the app identical on iPhone and on Android.

All the source code lives **in the vault**. The version at Google is only a copy put online. That has
come in handy more than once; we come back to it below.

## How it works

1. On the phone, you type or dictate, optionally attach a photo, and send.
2. The app **recognises the person by their Google account**: an unknown account is refused, and it
   is the server that decides where to write.
3. The file is named, for example, `note-2026-08-28-2130-gael.md` (date, time, first name). At the
   top, a single line: who, when, from which device.
4. At the start of a session, or when Gaël types the `/note` command, I read the inbox and process
   what has arrived there.

**First version, first hole.** At the outset, the identity was written in the page's address
(`?p=gael`). Anyone who knew the address could therefore drop something into the vault. Replaced the
same day by identification through the Google account.

## A note from Gaël is an order

My first version stamped every note with a mention: *"nothing enters the vault without Gaël's
validation"*. That was my idea, not his. While discussing an example (a note asking to create a
travel project), Gaël settled it: *"you do have to execute something"*. Waiting for his validation on
a text he has just written himself serves no purpose.

The current rule: **a note from Gaël is an order by default, and the verb decides.**

| The note says | What I do |
|---|---|
| "create project X" · "add this" · "file this under…" | I execute, and I tell him |
| "I'm tempted" · "to dig into" · a fragment of a sentence | I file it, I create nothing |

When in doubt, the note stays in the inbox and I ask the question. One exception only: **anything
that leaves the vault** (an email, a purchase, a message to someone) waits until Gaël is there. He
may have written the note at 11 pm on his way to bed; a wrong recipient or a wrong amount cannot be
undone outside the way it can in a file.

## The wall: you can't read the vault on a phone

Gaël also wanted to re-read his notes from his phone. On 28 August, he discovered that **Google Drive
on a phone does not open Markdown files**: blank screen, or "file type not supported". Yet the whole
vault is in Markdown.

We ruled out from the start the idea of making copies as Google Docs: two versions of the same text
means a discrepancy from the first change onwards.

That same evening, the app gained **reading pages**: it opens a folder and displays a formatted note
(headings, lists, checkboxes, tables). And in the same night, **the notes became participatory**:
from the phone, you can tick a box, add a line to a list, answer a question, remove a line. The
structure of the note, however, cannot be changed.

When an answer arrives in a note, I integrate it where the information should live, then I remove the
question from the note.

## When I overdo it

Gaël pointed out to me that **one** note did not appear in the app. I added an entry that opened
**all** his projects. His reply: *"my projects should be visible in the app? not at all, that's
nonsense"*. Removed within the hour. This is the flaw of [chapter 6](06-acting-without-a-mandate.md):
extending a request beyond what was asked.

## Deployment mishaps, made harmless

Updating an Apps Script app means pasting the code into an online editor and clicking "Deploy". I
guide, Gaël pastes. In two days:
- three handling errors, including two pastes into the wrong file; once, the app went down ("Invalid
  HTML content format");
- the deployment window several times **served up the old version** instead of the new one.

Each time, the repair took only as long as pasting again, because **the right version was in the
vault.** It is the most concrete argument for keeping the sources locally: the host is only a copy.

## Being notified within the minute

The app writes every action (a drop, a ticked box, an answer) to a small log. That log reaches the PC
through Google Drive, and at the start of a session I launch **a watcher** that monitors the file's
size every three seconds. Tested on 29 August: a box ticked on the phone at 10:19, and the session
open on the PC was notified in under a minute.

Outside a session, on the other hand, nothing reads the inbox
([chapter 13](13-what-remains-open.md)).

## Known limits

- **No icon on the home screen.** Apps Script displays the page inside a frame supplied by Google,
  and it is that frame the phone reads to find the icon. The only workaround: a shortcut created with
  the iOS Shortcuts app.
- **No full screen**, for the same reason.
- **Photos reduced to 2,400 pixels, refused above 8 MB.**
- **One gesture never tested on a real phone**: the long press on a checkbox, which lets you correct
  a badly dictated line. A touch gesture cannot be simulated from the PC. We wrote it as it is: *not
  tested*.

---
[← Chapter 2](02-several-ais-one-vault-the-tickets.md) · [Contents](../README.md) · [Chapter 4 →](04-the-backup.md)
