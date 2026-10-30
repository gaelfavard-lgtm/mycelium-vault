# Start here — setting up the vault

## What you need

- **Claude Code**, installed on your computer.
- **Python 3**, for the automatic checks. If you do not know whether it is installed, Claude
  will check at step 3.
- The template was road-tested on **Windows**. On Mac or Linux it works too, but Claude may
  have to adjust a command.

## Setting up

1. **Copy the `template` folder** to the place where you want to keep your vault, and rename it as
   you like (for example `MyVault`). To begin with, avoid a synced folder (Google Drive,
   OneDrive, iCloud): it is possible, but there are pitfalls, described in the `README.md`.
2. **Open Claude Code in that folder.** On first launch, it asks whether you trust
   the folder: answer yes. That is what activates the automatic checks.
3. **Ask it to install it**, for example:
   *"Read the README.md and install this vault with me: check that Python works, run the test
   of the automatic checks, then help me fill in my profile."*
4. **Fill in your profile with it.** It asks you questions about who you are and how you want
   to work, then fills in the two notes of `_context/profile`. They are read at every
   conversation.
5. **Add your first project**, for example your app: *"Create the note for my application
   project."* From then on, each session starts by reading the index and the logbook:
   no need to explain everything again.

## The three rules to know

- Claude does nothing without your consent: say **"go ahead"** when you want it to act.
- It never deletes: it puts things in `to-delete`, you are the one who empties it.
- After each action, it writes down what it did in the logbook and updates the note.

## Start small, and shape it to yourself

No point filling every folder from the start. Begin with **a single project**, the one you
are working on, and let the vault grow session after session.

The template's rules are mine: a starting point, not a fixed manual. **You are going to
shape them in your own image.** When a way of doing things does not suit you, tell Claude: it
fixes the rule. When a problem comes back a second time, the two of you write the missing rule
together. Rules are added this way, **little by little**, born from your real use, and the vault
ends up looking like you.

## Privacy

Over time, the vault will contain your life or your project in detail. **Do not publish it**, and
put **neither passwords nor access keys** in it: a folder read by an AI is not a safe.

## Going further

To read the files yourself, **Obsidian** (free, obsidian.md) makes them more pleasant:
open the folder as a vault.

The technical details (scripts, settings, pitfalls) are in `README.md`. The story of these rules,
and why they exist, is in the parent folder: start with its `README.md`.
