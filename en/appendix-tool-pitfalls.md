# Appendix: tool pitfalls

*Translated from the French original; the French version is the reference.*

What we learned about the tools around the vault, often by breaking something. A large part comes
from running a small craft business: an **Airtable** base (an online database that looks like a
spreadsheet) for tracking items and orders, and a **Softr** application (web pages built on Airtable,
without code) for the team.

## Airtable

**Automations**
- **Deleting a field switches off the automations that watch it.** Restoring it does not switch them
  back on.
- **Undoing a deletion (Ctrl+Z) gives the field back its original identifier**; recreating it gives it
  a new one, and the scripts that used the old one break.
- **Testing an automation from the editor does not switch it on.** We had an automation "tested OK
  live" that had never been activated.
- **The API can create a script automation, but not modify an existing one**: once the script is
  pasted in, trigger, name and deletion are set in the interface.
- **Forty rows created at once launch forty simultaneous executions** of the same automation, which
  trample on each other. You need a guard ("only work if I am the last one"), tolerant deletions, a
  final deduplication — **and a reread after each generation**, because the guard can give way.
- **A naming automation does not necessarily watch the field you have just changed**: to retrigger
  it, clear then reset a field it really does watch.
- **An item's name may be calculated, not written**: writing it by hand gives the illusion of success,
  until the next recalculation.
- **Ceiling of 50 automations per base.** We had to merge several scripts into one. The check after
  merging found eight points to correct.
- **Under heavy load, a trigger can miss records.** Check by looking for what should have changed.
- **Refer to tables, fields and options by their identifier in scripts**, with the readable name as a
  comment. A script that looks up a field by its name breaks **without a word** the day someone
  renames it.
- **No silent fallback value in a script.** A wrong but well-formed name went unnoticed. Now the
  default value applies **and** the log says so.
- **A comment in a script does not make the setting it describes.** An hour lost on a comment that
  described a setting to be made elsewhere. Write "TO BE SET IN..." instead.

**Structure**
- **An empty table does not show its broken fields**: no cell to display the error in.
- **The API deletes no field**, and does not create form pages.
- **Deleting a table turns the links to it into frozen text.**
- **A row grouping ("group by") set by the API in an interface page can no longer be removed in the
  editor**, and the "Group" menu of a published page only offers the displayed fields.
- **A condition whose dynamic value is empty is ignored**: an empty field does not filter on
  "nothing", it lets everything through.
- **Merging two records** is done through the links, which are symmetrical: add the children to the
  row to keep, then delete the other. One write, no child touched.
- **Renaming to a name that already exists is merging without saying so**: first check that the
  target name is free.
- **Attachment URLs are signed and expire**: yesterday's export no longer downloads anything. In
  return, you copy an attachment from one record to another by rewriting the field with the signed
  URL.
- **Entering a model in an order locks it**: its variants are no longer renamed automatically, and a
  correction on a component no longer propagates — it has to be redone on the rows.
- **To audit without pagination**: analysing a table grouped by field gives the duplicate names in one
  call, the "empty" / "among" filters replace page-by-page walks, and a temporary summary field
  answers in a few dozen reads instead of hundreds.

**Interfaces**
- **Publishing an interface publishes every pending draft**, including those of other sessions.
- **"Auto" on an element's size does not mean "fits the content"**: it is a short, fixed height. You
  enlarge through the appearance settings, not by dragging a handle.
- **A grid has no field-by-field editing**: to enter data in place, you need a record detail page. The
  API reads this setting without being able to write it — handy for checking a page.
- **There is no version history for interfaces.** A vanished page is rebuilt by hand.
- **A never-published page is deleted with no way back.** Never delete one without asking whether
  someone has touched it up by hand.

**Deletions made by the human**
- We asked Gaël to delete a field by giving its name. Two fields had similar names: **he deleted the
  wrong one.** First remedy: give the field's identifier. The remedy adopted afterwards comes from
  Gaël: *"Rename it 'to delete' on top, then I can't get it wrong."* We first rename the field
  **"TO DELETE — reason"**, with the explanation in its description, then ask for the deletion. *A
  name you read on screen is worth more than an identifier you have to compare.*

**Working as a pair**
- **The human modifies the base while the AI is working.** The counts move during the session. Never
  reuse a count taken earlier in the same session.

## Softr

- **Softr links fields by their name.** Renaming a field in Airtable breaks the corresponding block,
  without a message.
- **After publishing, the cache delays the display.** Wait before looking for a fault.
- **Records deleted in Airtable stay displayed.** Softr synchronises through "webhooks" (addresses
  that receive the changes), limited to two per base. We found a webhook forgotten by an old Make
  scenario, which may have been taking up a slot; it was deleted. The problem is not solved: email
  sent to support.
- **Several useful features are paid**, and you discover them along the way (for example, installing
  the app on the phone). Workaround: a shortcut on the home screen.
- **Restricting access to the data in Airtable protects everywhere**; restricting it only in the Softr
  pages requires the paid plan.
- **The general theme does not set the fill of buttons**: that is done block by block, and some blocks
  (the login page, for example) have no setting at all.
- **Pinch-to-zoom on Android** was blocked by a modal window, not by the page: in full page, it works.
- **The editor is driven by searching for an element, not by coordinates**: they change with the tab's
  zoom.

## Google Drive

- **Claude's Drive connector cannot hand out rights as you want**: it never shares as "anyone with the
  link". And it displayed "owner only" on folders that were really shared. The log of a script that
  shares is what counts, not the connector.
- **A file created through the API without a parent folder lands at the root of Drive.** Better to
  write to the disk and let the synchronisation do the rest.
- **Sending a file through the connector is very expensive**: the file goes through encoded as text,
  about 460,000 tokens for 1.3 MB. Copying the file into the local Drive folder is free.
- **Google Drive on the phone does not open Markdown files.**
- **Mirror mode synchronisation can run several minutes late.**
- **Drive's preview paginates and ignores CSS backgrounds**: coloured dots were showing up white. What
  must be seen must not depend on a background — we replaced them with images. The pagination margins
  cannot be removed: you compensate by enlarging.
- **The Gmail connector does not return attachments**: an invoice received as a PDF stays unreadable.

## Google Apps Script

- **The page is served inside a frame provided by Google.** Consequences: no home-screen icon, no full
  screen (the Apple tags are refused and crash the page), and no simulation of touch gestures from
  the computer.
- **`ScriptApp.getService().getUrl()` is not reliable** depending on the context: the app's address
  must be hard-coded.
- **All internal links must carry `target="_top"`**, otherwise they open inside the frame and are
  blocked.
- **`location.reload()` gives a blank page.** Update the page by replacing its content.
- **HTML templates already escape variables**: `<?= JSON.stringify(x) ?>` adds extra quotation marks.
  Write `<?= x ?>`.
- **Deployment can serve the old version again.** Check the number announced in the confirmation
  window.
- **Check which file is open before pasting the code.**

## Windows

- **A `.bat` file must have Windows line endings (CRLF).** Otherwise Windows eats one character per
  line, in silence.
- **No pause and no waiting for input in a script launched automatically**: it would wait forever.
- **The Task Scheduler cuts the command at the first space.** Put the executable alone in "Program",
  and the script's path in quotation marks in "Arguments".
- **On a laptop that goes to sleep, a task launched "at log on" then repeated every hour stops
  repeating**, and nothing is caught up. Set several triggers, and tick "run task as soon as possible
  after a scheduled start is missed".
- **The Task Scheduler's "Running tasks" screen does not refresh on its own**: press F5. The proof that
  a task has run is its log, not the display.
- **Modifying a scheduled task requires administrator rights.**
- **The `python` command may be only a shortcut to the Microsoft Store**; it is `py` that launches
  Python.
- **PowerShell 5.1 misreads the accents of a script saved without a BOM** (an invisible mark at the
  start of the file indicating its encoding): save as UTF-8 with BOM.
- **In PowerShell, `$Out` and `$out` are the same variable**: capitals do not count. A script thus
  overwrote one of its own variables — and the same fault came back with `$V` and `$v`, where an inner
  loop overwrote the outer loop's list, for a result wrong by a factor of six. **Name collections with
  a whole word.**
- **`perl -i` with a wide escape notation (`\x{...}`) on an accented file re-encodes the whole file**:
  2,354 lines out of 3,773 double-encoded for a one-line correction. The reverse conversion
  (`iconv -f UTF-8 -t LATIN1`) undoes exactly that damage. **It was the command's own output that
  betrayed the error** — it has to be read.
- **A script that writes a non-Latin alphabet must be saved as UTF-8 with BOM**, otherwise
  PowerShell 5.1 damages it.
- **To produce a PDF without installing anything**: the browser in headless mode
  (`msedge --headless --print-to-pdf`) on the local HTML file.
- **A web-page retrieval script overwrote 252 result files**, because we had planned where it read but
  not where it wrote. Write results as you go, with resumption.
- **Windows' "Storage Sense" and OneDrive** turn files into "online-only" ghosts. Pin the files and
  turn off the automatic purge.
- **iPhone photos (HEIC)** convert without additional software, with the components already present
  in Windows.

## Claude Code

*[Chapter 9](story/09-claude-code-pitfalls.md) tells the essentials; here is what has been added
since.*

- **The permission system forbids Claude from modifying its own guardrail.** This is the expected
  behaviour, but you need to know it: installing a guardrail remains a human gesture.
- **Republishing a web page from another file path creates a second page** instead of updating the
  first: you have to pass the address of the existing page.
- **Tool results are not always written to disk**: it is then impossible to build a script from them.
  Workaround: write by hand, in batches with a constant prefix, where an error leaps to the eye.

## Miscellaneous

- **Transmitted photos lose their date data (EXIF)**, whatever the channel. The date survives only in
  the file name.
- **A straight apostrophe in a JavaScript string** killed an entire page. Use the typographic
  apostrophe in texts.
- **ChatGPT invents plausible names** when asked to identify objects in photos from a closed catalogue
  of 28 types: three invented names out of fifteen. The closed list must be imposed on it, not
  offered.
- **Merchant sites often refuse automated reading.** Code 402: suspended Shopify store; 404: page
  deleted; 403: live site, but automated reading blocked.

---
[← Contents](README.md)
