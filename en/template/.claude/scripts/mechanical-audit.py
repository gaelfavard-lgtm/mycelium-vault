#!/usr/bin/env python3
"""
mechanical-audit.py — the scriptable part of the filing audit
(3-Resources/methods/filing-method.md §4).                    (OPTIONAL)

This is NOT a hook: the AI (or you) runs it at audit time.
"An AI is not a linter": these checks are deterministic, they do not
need a model. The script MODIFIES NOTHING — text report on the output.

Usage:  python mechanical-audit.py <vault-path>      (default: current folder)

Checks:
  1. root          — files stagnating at the root of the vault
  2. stubs         — empty .md notes (0 bytes)
  3. wikilinks     — broken [[links]], or ambiguous ones (more than 2 targets with the same name)
  4. paths         — `cited/paths.md` between backticks that do not exist on disk
                     (the most profitable check: notes lie about paths)
  5. duplicates    — same file name in several places
  6. freshness     — in MEMORY.md and the project cards (up to "end of card"),
                     a line that announces a STATE (in progress, pending…) without a date
  7. sync          — conflict copies "note (1).md" left by the sync tool
  8. hidden memory — Claude Code's private memory for this vault
                     (~/.claude/projects/<vault>/memory/) must stay empty: otherwise facts
                     live outside the vault, invisible to other AIs

Pitfalls avoided (seen in other vaults or in use):
  - excluding ALL "." folders would make every `.claude/…` path look like a
    ghost: the exclusion list is explicit;
  - a [[link]] cited as an example between backticks is not a link: code is removed
    before the wikilinks pass (but NOT before the paths pass, which needs the backticks);
  - `.claude/worktrees/` and `.trash/` are excluded: walking them drowns the report in
    thousands of false positives.
"""
import os, re, sys, unicodedata
from collections import defaultdict

EXCLUDE_DIRS = {".obsidian", ".git", "__pycache__", "to-delete", "node_modules",
                "session-logs", "worktrees", ".trash"}
ROOT_ALLOW = {"AGENTS.md", "CLAUDE.md", "LOGBOOK.md", "README.md", "START-HERE.md", "_test_claude.txt"}
JOURNAL_SKIP = {"LOGBOOK.md"}                 # history may cite paths that no longer exist
REPEATED_NAMES = {"readme.md", "skill.md", ".gitkeep"}   # repeated by convention
PLACEHOLDERS = {"name", "name|text"}          # [[name]] cited as an example in the notes

STATE = re.compile(r"\b(in progress|pending|to do|to watch|to decide|to be decided|waiting"
                   r"|nothing (?:ordered|bought|published|built|written)|unresolved|active|decided|status)\b", re.I)
DATE = re.compile(r"\d{1,2}/\d{1,2}|\d{4}-\d{2}-\d{2}|\b20\d\d\b|\b(january|february|march|april|may"
                  r"|june|july|august|september|october|november|december)\b", re.I)
SYNC = re.compile(r" \(\d+\)(\.[^.]+)?$")
WIKILINK = re.compile(r"\[\[([^\]|#]+?)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")
PATHREF = re.compile(r"`([^`\n]*?[/\\][^`\n]*?\.[A-Za-z0-9]{1,5})`")
FENCE = re.compile(r"^```.*?^```", re.S | re.M)
INLINE_CODE = re.compile(r"`[^`\n]*`")


def norm(s):
    return unicodedata.normalize("NFC", s)


def strip_code(text):
    """Code blocks and inline code removed: an example between backticks is not a link."""
    return INLINE_CODE.sub(" ", FENCE.sub(" ", text))


def read(full):
    with open(full, encoding="utf-8", errors="ignore") as f:
        return f.read()


def main(vault):
    vault = os.path.abspath(vault)
    md_files, all_names, all_relpaths = [], defaultdict(list), set()
    for dirpath, dirnames, filenames in os.walk(vault):
        dirnames[:] = [d for d in dirnames if norm(d) not in EXCLUDE_DIRS]
        for f in filenames:
            full = os.path.join(dirpath, f)
            rel = norm(os.path.relpath(full, vault)).replace("\\", "/")
            all_relpaths.add(rel.lower())
            all_names[norm(f).lower()].append(rel)
            if f.lower().endswith(".md"):
                md_files.append((full, rel))

    issues = defaultdict(list)

    # 1. Root: nothing stagnates
    for f in os.listdir(vault):
        if os.path.isfile(os.path.join(vault, f)) and norm(f) not in ROOT_ALLOW:
            issues["root"].append(f)

    # 2. Empty stubs
    for full, rel in md_files:
        if os.path.getsize(full) == 0:
            issues["stubs"].append(rel)

    # 3. Broken / ambiguous wikilinks (Obsidian only resolves a link without extension to a .md)
    stems = defaultdict(list)
    for name, paths in all_names.items():
        stems[name.rsplit(".", 1)[0]].extend(paths)
    for full, rel in md_files:
        if os.path.basename(rel) in JOURNAL_SKIP:
            continue
        for m in WIKILINK.finditer(strip_code(read(full))):
            target = norm(m.group(1).strip()).lower()
            if target in PLACEHOLDERS:
                continue
            hits = ([p for p in stems.get(target, []) if p.lower().endswith(".md")]
                    or all_names.get(target) or all_names.get(target + ".md") or [])
            if not hits:
                issues["broken wikilinks"].append(f"{rel} → [[{m.group(1)}]]")
            elif len(set(hits)) > 2:
                issues["ambiguous wikilinks"].append(f"{rel} → [[{m.group(1)}]] ({len(set(hits))} targets)")

    # 4. Cited paths vs disk
    for full, rel in md_files:
        if os.path.basename(rel) in JOURNAL_SKIP:
            continue
        for m in PATHREF.finditer(read(full)):
            raw = norm(m.group(1).strip()).replace("\\", "/")
            if raw.startswith(("/home", "/etc", "/usr", "/var", "/opt", "/tmp")):
                continue                     # absolute paths from another machine
            p = raw.strip("/")
            if re.match(r"^[A-Za-z]:", p) or p.startswith(("http", "www", "~", "<", "...", "@", "$")):
                continue
            if p.startswith(("../", "./")):  # relative to the note
                p = os.path.normpath(os.path.join(os.path.dirname(rel), p)).replace("\\", "/")
            if any(c in p for c in "*<>@") or " / " in p:
                continue                     # pattern, template or notation, not a path
            if re.search(r"\.[A-Za-z0-9]{1,5}/\.[A-Za-z0-9]{1,5}$", p):
                continue                     # extension notation: "x.skp/.skb"
            pl = p.lower()
            if pl not in all_relpaths and not any(rp.endswith("/" + pl) for rp in all_relpaths):
                issues["ghost paths"].append(f"{rel} → `{m.group(1)}`")

    # 5. Duplicate names (outside the .claude/ machinery and names repeated by convention)
    for name, paths in all_names.items():
        if name in REPEATED_NAMES:
            continue
        content = [p for p in paths if not p.lower().startswith(".claude/")]
        if len(content) > 1 and name.endswith((".md", ".pdf", ".jpg", ".jpeg", ".png", ".xlsx")):
            issues["duplicate names"].append(f"{name}: " + " | ".join(sorted(content)))

    # 6. Freshness: all of MEMORY.md, project cards up to "end of card"
    for full, rel in md_files:
        lines = read(full).splitlines()
        if rel == "_context/MEMORY.md":
            zone = lines
        elif rel.startswith(("1-Projects/", "2-Areas/")) and \
                os.path.basename(rel).lower() not in REPEATED_NAMES:
            ends = [i for i, l in enumerate(lines) if "end of card" in l.lower() and i > 3]
            if not ends:
                continue
            zone = lines[:ends[0]]
        else:
            continue
        # a bullet and its continuation lines form ONE item: the date may be on the next line
        items = []
        for i, l in enumerate(zone):
            s = l.strip()
            if not s or s.startswith(("-", "*", "|", ">")) or re.match(r"\d+\.", s):
                items.append([i + 1, s])
            elif s.startswith("#"):
                items.append([i + 1, ""])   # a heading is not a state
            elif items:
                items[-1][1] += " " + s
        for n, item in items:
            t = WIKILINK.sub(" ", strip_code(item))
            if STATE.search(t) and not DATE.search(t):
                issues["undated states"].append(f"{rel}:{n} — {item[:90]}")

    # 7. Sync duplicates: "x (1).md", or a copy whose original sits next to it
    for name, paths in all_names.items():
        if not SYNC.search(name):
            continue
        for p in paths:
            original = SYNC.sub(lambda m: m.group(1) or "", p).lower()
            if p.lower().endswith(".md") or original in all_relpaths:
                issues["sync duplicates"].append(p)

    # 8. Claude Code's hidden memory for THIS vault
    #    (the project folder is the vault's path, special characters replaced by "-")
    key = re.sub(r"[^A-Za-z0-9]", "-", vault).lower()
    projects = os.path.join(os.path.expanduser("~"), ".claude", "projects")
    if os.path.isdir(projects):
        for d in os.listdir(projects):
            mem = os.path.join(projects, d, "memory")
            if d.lower() == key and os.path.isdir(mem) and os.listdir(mem):
                issues["hidden memory"].append(f"{mem}: " + ", ".join(sorted(os.listdir(mem))))

    # Report
    total = sum(len(v) for v in issues.values())
    print(f"MECHANICAL AUDIT — {len(md_files)} notes, {len(all_relpaths)} files — {total} finding(s)\n")
    for k in ["root", "stubs", "broken wikilinks", "ambiguous wikilinks", "ghost paths",
              "duplicate names", "sync duplicates", "hidden memory", "undated states"]:
        if issues[k]:
            print(f"### {k} ({len(issues[k])})")
            for line in sorted(issues[k]):
                print(f"  - {line}")
            print()
    if total == 0:
        print("No mechanical discrepancy.")
    print("Reminder: report only — nothing has been modified. The judgement checks remain the AI's.")


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")   # Windows console in cp1252: "→" used to crash
    except Exception:
        pass
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
