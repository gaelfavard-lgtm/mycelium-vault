#!/usr/bin/env python3
"""
backup.py — backup of the vault, text only, into a local git repository
placed OUTSIDE any synced folder (Google Drive, OneDrive, Dropbox, iCloud).
                                                              (OPTIONAL)
This is NOT a hook: run it by hand, or from the task scheduler
(Windows) / cron (macOS, Linux), for example once a day.

WHY OUTSIDE THE SYNCED FOLDER
  A git repository inside a synced folder gets corrupted: the sync tool
  copies the .git files one by one while git is writing. And sync
  is not a backup: a deletion or a corruption syncs
  too. You need a separate copy, with history.

Usage:
    python backup.py
    python backup.py --vault <path> --repo <path>

What the script does:
  1. copies the vault's text files (EXTENSIONS) to the repository;
  2. removes from the repository what no longer exists in the vault (git history keeps it);
  3. creates a restore point (commit) if there is a change;
  4. ALWAYS writes a line in <repo>/backup-log.txt, OK or FAILURE.
     A safety net that goes quiet is worse than no net: have a look at
     this log from time to time.

Restore without an AI: open the repository, `git log` to pick a point,
`git checkout <point> -- <file>` to recover a file.

Rule: no AI writes to the backup repository (one forgotten git lock
is enough to block every following backup).
"""
import os, sys, time, shutil, subprocess, datetime, argparse, platform

EXTENSIONS = {".md", ".txt", ".json", ".py", ".sh", ".bat", ".html", ".css", ".js", ".csv"}
IGNORE = {".git", ".obsidian", "node_modules", "__pycache__", ".trash", "worktrees"}
LOG = "backup-log.txt"


def git(repo, *args):
    return subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True)


def copy(vault, repo):
    """Copies the vault's text files to the repository, and removes what has disappeared."""
    copied = expected = 0
    for root, dirs, files in os.walk(vault):
        dirs[:] = [d for d in dirs if d not in IGNORE]
        for f in files:
            if os.path.splitext(f)[1].lower() not in EXTENSIONS:
                continue
            src = os.path.join(root, f)
            rel = os.path.relpath(src, vault)
            dst = os.path.join(repo, rel)
            expected += 1
            try:
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                if (not os.path.exists(dst) or os.path.getmtime(src) > os.path.getmtime(dst)
                        or os.path.getsize(src) != os.path.getsize(dst)):
                    shutil.copy2(src, dst)
                    copied += 1
            except Exception as e:
                print(f"  ! cannot copy {rel}: {e}")
    # Remove from the repository what no longer exists in the vault (recoverable through git).
    removed = 0
    for root, dirs, files in os.walk(repo):
        dirs[:] = [d for d in dirs if d not in IGNORE]
        for f in files:
            if f == LOG:
                continue
            dst = os.path.join(root, f)
            rel = os.path.relpath(dst, repo)
            if not os.path.exists(os.path.join(vault, rel)):
                os.remove(dst)
                removed += 1
    return copied, removed, expected


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    p = argparse.ArgumentParser(description="Text backup of the vault into a local git repository.")
    p.add_argument("--vault", default=os.path.abspath(os.path.join(here, "..", "..")))
    p.add_argument("--repo", default=os.path.join(os.path.expanduser("~"), "vault-backup"))
    a = p.parse_args()
    vault, repo = os.path.abspath(a.vault), os.path.abspath(a.repo)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"\n  Vault  : {vault}\n  Backup : {repo}\n")

    if not os.path.isdir(vault):
        print(f"  [FAILURE] vault not found: {vault}")
        return 1
    if os.path.commonpath([vault, repo]) == vault:
        print("  [FAILURE] the backup repository must not be INSIDE the vault.")
        return 1
    if shutil.which("git") is None:
        print("  [FAILURE] git is not installed — https://git-scm.com/downloads")
        return 1

    os.makedirs(repo, exist_ok=True)
    if not os.path.isdir(os.path.join(repo, ".git")):
        print("  First backup — creating the local repository...")
        git(repo, "init", "-q")
        git(repo, "config", "user.name", "Vault backup")
        git(repo, "config", "user.email", "backup@localhost")

    copied, removed, expected = copy(vault, repo)
    print(f"  {expected} text files — {copied} copied, {removed} removed")
    machine = os.environ.get("COMPUTERNAME") or platform.node() or "?"

    # A forgotten git lock (interruption) makes ALL following commits fail,
    # and git only says so on stderr. We remove those older than 5 minutes.
    for lock in ("HEAD.lock", "index.lock"):
        path = os.path.join(repo, ".git", lock)
        if os.path.exists(path) and time.time() - os.path.getmtime(path) > 300:
            try:
                os.remove(path)
                print(f"  Stale git lock removed: {lock}")
            except Exception as e:
                print(f"  ! lock {lock} cannot be removed: {e}")

    git(repo, "add", "-A")
    changed = git(repo, "diff", "--cached", "--quiet").returncode != 0
    verdict = "OK"
    if changed:
        r = git(repo, "commit", "-q", "-m", f"Backup {timestamp} - {machine}")
        if r.returncode == 0:
            status = "new point"
            print("\n  [OK] New restore point recorded.")
        else:
            # NEVER write "OK" when git refused: a log that lies is
            # worse than no log.
            verdict = "FAILURE"
            cause = (r.stderr or r.stdout).strip().replace("\n", " ")
            status = "FAILURE commit: " + cause[:120]
            print(f"\n  [FAILURE] git commit refused: {cause}")
    else:
        status = "nothing new"
        print("\n  [OK] No change since the last backup.")

    points = git(repo, "rev-list", "--count", "HEAD").stdout.strip() or "0"
    tracked = len([l for l in git(repo, "ls-files").stdout.splitlines() if l])
    with open(os.path.join(repo, LOG), "a", encoding="utf-8") as j:
        j.write(f"{timestamp}  {verdict}  {status}  ({tracked} files, {points} points)  [{machine}]\n")
    print(f"\n  Restore points : {points}\n  Files backed up: {tracked}\n")
    return 0 if verdict == "OK" else 1


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    sys.exit(main())
