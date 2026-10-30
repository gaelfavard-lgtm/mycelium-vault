# Filing method

**Single reference for filing.** Every new filing rule is written here, not elsewhere.
Test for each line: **"if we remove it, which mistake comes back?"** No answer → it goes.

## 1. The zones

Filing by **actionability**, not by theme. The deciding question: **"in which context
would I like to come across this file again?"** One file = one idea.

| Zone | Filter question |
|---|---|
| `0-Inbox` | The inbox + the ticket queue. Nothing stays. |
| `1-Projects` | A beginning and an end. "Does it move a deliverable forward?" Mandatory note, goal and status. |
| `2-Areas` | Continuous responsibility. Mandatory head note. |
| `3-Resources` | "Useful some day?" Thematic sub-folders allowed inside. |
| `4-Archives` | "Finished but to keep?" Folder name = the place or the asset. |
| `_context` | Describes the system, not the work. |
| `_prompts` | Repeatable procedures, readable by any AI. |
| `to-delete` | The bin that only the human empties. |

## 2. The arbitration criteria

1. **Who uses it today?** Living use decides, not the label.
2. **File for the next move**: one worksite = one folder that goes to the archives as a single block.
3. **What does the correction gain?** If the answer is "it respects the rule", it
   is not a discrepancy.
4. **A file with two possible places**: one location + wikilinks. Neither duplicate nor move.
5. **Duplicates**: detection by name + size, **comparison before any removal**, never by eye.
6. **Naming**: meaningful; banned in active zones: `IMG_*`, `Untitled`. After any rename:
   grep the occurrences, in the same move. Rename nothing in `4-Archives`.
7. **Deletion: never direct** — move to `to-delete/`.
8. **A task with no deadline** = one line in a list, not a project, not a folder.

## 3. Why notes lie — the anti-drift rules

The disk is the truth; a description goes stale.
1. **Write in the present tense only what exists** — what is planned goes under "To do".
2. **A move is only finished after the grep** of the notes that cite the old path.
3. **Never copy a file name** from memory: read the disk.
4. **Every action has two halves**: log what is new, remove what becomes false.
5. **A certification is dated** ("checked on …") or removed.
6. **What enters without going through the human is signed** — the signature is a flag: "this has
   not been submitted".
7. **An observation is dated in the text** — a file's timestamp is rewritten at the slightest
   copy, and photos often lose their date along the way.
8. **A state carries its date**: "in progress (15/01)". A fact is timeless, dated, or referred to its
   living source.

## 4. The audit

**Mechanical** (script `.claude/scripts/mechanical-audit.py`, report only): cited paths vs
disk, broken or ambiguous wikilinks, root that stagnates, empty files, duplicate names, sync
duplicates (`x (1).md`), undated states, Claude Code's hidden memory.
**Judgement** (one AI pass): the planned and the done living side by side, catch-all notes (> ~300
lines), notes that contradict each other, sleeping projects (3 months for a small one, 1 year for a big one:
the question is "where are you with it?", not "should it be archived?").
Suggested frequency: light every week, deep every month. What each audit teaches goes to the
logbook.

## 5. Anti-inflation

1. **Startup budget: 300 lines** (AGENTS + CLAUDE + MEMORY + the 2 profile notes).
   Any rule that wants in pushes another one out.
2. **A mistake only becomes a rule on its second occurrence.**
3. **How to cut: 70 / 30.** The AI keeps the 70% it judges untouchable, and presents the
   remaining 30% **in blocks of meaning**, each with what its disappearance would lose. The human
   decides block by block. Handing back 30% at random is handing them the whole problem.
4. **We set rules, not cases**: the logbook keeps the case, the method keeps the rule.
