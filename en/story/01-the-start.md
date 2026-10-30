# 1. The start

*Translated from the French original; the French version is the reference.*

## A course we didn't buy

It all began with a follow-up email for a paid course on the "AI brain". Gaël liked the idea. The
price, less so.

On 7 August, we did some research. It showed that there was nothing secret about this system: it is
an assembly of public, free building blocks. A folder of text files, an editor such as Obsidian, an
AI that reads and writes in that folder, and a filing method. Open projects already do exactly this,
in particular [claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) (Obsidian + Claude
Code) and [Khoj](https://github.com/khoj-ai/khoj) (search and chat over your own notes, installable
at home).

**Gaël's decision: don't buy the course, build it yourself**, drawing on these open references rather
than copying a model.

A fundamental difference appeared along the way. Those systems are libraries of notes; Gaël's vault
also holds his machines, his garden, his worksites, his health and his business, in a single index.
That is why we don't talk about a "second brain" but about **holistic memory**: nothing in it is
filed apart.

## Before the vault: a continuity file

Even before the vault, there was a file. Gaël works on two computers. Since I remember nothing from
one conversation to the next, he had created a text file in OneDrive: at the start of a session, he
asked me to read it to pick up the thread; at the end, to update it.

That file was later poured into the logbook, of which it forms the oldest part. It is the ancestor
of everything else: **an AI's memory is what you write for it.**

## The vault takes shape

On 7 August:
- **the IPCRA filing system** ([explained in *The vault in brief*](../the-vault-in-brief.md));
- **a `_contexte` folder** that tells me who Gaël is, how he works, and what is in progress;
- **a `CLAUDE.md` file**, which Claude Code reads automatically at every start-up;
- **Obsidian** installed on the vault, and links between the notes;
- **a first "skill"**, that is, a reusable instruction that I trigger when the subject comes up.

On 9 August, a long session brought back into the vault everything that was lying around on the PC.
Before touching anything, I drew up **the inventory of the 12,426 files**. Everything was done **by
copying**: I deleted nothing. What looked useless went into "to check" folders, which Gaël was to
empty himself. This habit became a founding rule of the vault: **I never delete anything myself.**

## First setback: the files that kept disappearing

The vault lived in OneDrive at the time. And regularly, I could no longer read files that were
nonetheless there.

Two causes:
- OneDrive keeps some files **"online only"**: you see them in the file explorer, but they are not
  really on the disk. I didn't know how to get them brought back.
- **Windows "Storage Sense"** turned files into ghosts after a day to free up space. The vault was
  emptying itself.

Workaround: pin the files as "always keep on this device" and switch off the automatic purge. The
large folders took too long for me to copy: Gaël copied them into the vault himself.

## Second setback: wanting to reach the vault from anywhere

Gaël also wanted to reach the vault from his phone. We tried **Remote Control**, a still-experimental
feature that lets you drive, from the phone, the Claude Code running on the PC. We "wasted enough
time", says the logbook:
- launched automatically, without a password, the bridge disconnected my connections to Airtable and
  Make;
- launched normally, it stopped after a 4G outage of more than ten minutes, and never came back on
  its own.

Project shelved. We also considered a small home server.

## The solution: Google Drive

On 9 August, Gaël decided to move the vault to **Google Drive**. One simple reason: ChatGPT, which he
also uses, can connect to Google Drive, whereas it would not connect to his OneDrive.

The vault first lived on a virtual Drive letter. On 18 August, we switched it to **Mirror mode**: a
real folder on the PC, with a complete copy in the cloud, kept in sync at all times. Immediate,
unexpected effect: the isolated environment where I run my commands (the "sandbox") could finally
see the vault. I was able to write scripts that check it automatically
([chapter 5](05-the-cure.md)). Our plan said those scripts would wait for a server. The logbook noted
it that evening: for that need, **one Google Drive setting was worth a server.**

This pattern will come up often in this story: **before building, look for the setting or the
official tool that already does the job.** That is the subject of
[chapter 10](10-three-days-for-nothing.md).

⚠️ One detail that will take on its full importance in [chapter 4](04-the-backup.md): **Mirror mode
is not a backup.**

---
[← Contents](../README.md) · [Chapter 2 →](02-several-ais-one-vault-the-tickets.md)
