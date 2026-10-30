#!/usr/bin/env python3
"""
audit-mecanique.py — la partie scriptable de l'audit de rangement
(3-Ressources/methodes/methode-de-rangement.md §4).          (FACULTATIF)

Ce n'est PAS un hook : l'IA (ou vous) le lance au moment d'un audit.
« Une IA n'est pas un linter » : ces contrôles sont déterministes, ils n'ont pas
besoin d'un modèle. Le script NE MODIFIE RIEN — rapport texte sur la sortie.

Usage :  python audit-mecanique.py <chemin-du-coffre>      (défaut : dossier courant)

Contrôles :
  1. racine        — fichiers qui stagnent à la racine du coffre
  2. stubs         — fiches .md vides (0 octet)
  3. wikilinks     — [[liens]] cassés, ou ambigus (plus de 2 cibles du même nom)
  4. chemins       — `chemins/cités.md` entre backticks qui n'existent pas sur le disque
                     (le contrôle le plus rentable : les fiches mentent sur les chemins)
  5. doublons      — même nom de fichier à plusieurs endroits
  6. fraîcheur     — dans MEMORY.md et les cartes de projet (jusqu'à « fin de carte »),
                     une ligne qui annonce un ÉTAT (en cours, en attente…) sans date
  7. synchro       — copies de conflit « fiche (1).md » laissées par l'outil de synchro
  8. mémoire cachée— la mémoire privée de Claude Code pour ce coffre
                     (~/.claude/projects/<coffre>/memory/) doit rester vide : sinon des
                     faits vivent hors du coffre, invisibles aux autres IA

Pièges évités (vus chez d'autres coffres ou à l'usage) :
  - exclure TOUS les dossiers « . » ferait passer chaque chemin `.claude/…` pour
    fantôme : la liste d'exclusion est explicite ;
  - un [[lien]] cité en exemple entre backticks n'est pas un lien : le code est retiré
    avant la passe wikilinks (mais PAS avant la passe chemins, qui a besoin des backticks) ;
  - `.claude/worktrees/` et `.trash/` sont exclus : les parcourir noie le rapport sous
    des milliers de faux positifs.
"""
import os, re, sys, unicodedata
from collections import defaultdict

EXCLUDE_DIRS = {".obsidian", ".git", "__pycache__", "a-supprimer", "node_modules",
                "journal-sessions", "worktrees", ".trash"}
ROOT_ALLOW = {"AGENTS.md", "CLAUDE.md", "CARNET-DE-BORD.md", "README.md", "DEMARRER-ICI.md", "_test_claude.txt"}
JOURNAL_SKIP = {"CARNET-DE-BORD.md"}          # l'histoire peut citer des chemins disparus
NOMS_REPETES = {"_lisez-moi.md", "skill.md", ".gitkeep"}   # répétés par convention
PLACEHOLDERS = {"nom", "nom|texte"}           # [[nom]] cité comme exemple dans les fiches

ETAT = re.compile(r"\b(en cours|en attente|à faire|à surveiller|à trancher"
                  r"|rien (?:commandé|acheté|publié|monté|écrit)|non résolu|actif|décidée?|statut)\b", re.I)
DATE = re.compile(r"\d{1,2}/\d{1,2}|\d{4}-\d{2}-\d{2}|\b20\d\d\b|\b(janvier|février|mars|avril|mai"
                  r"|juin|juillet|août|septembre|octobre|novembre|décembre)\b", re.I)
SYNCHRO = re.compile(r" \(\d+\)(\.[^.]+)?$")
WIKILINK = re.compile(r"\[\[([^\]|#]+?)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")
PATHREF = re.compile(r"`([^`\n]*?[/\\][^`\n]*?\.[A-Za-z0-9]{1,5})`")
FENCE = re.compile(r"^```.*?^```", re.S | re.M)
INLINE_CODE = re.compile(r"`[^`\n]*`")


def norm(s):
    return unicodedata.normalize("NFC", s)


def strip_code(text):
    """Blocs de code et code inline retirés : un exemple entre backticks n'est pas un lien."""
    return INLINE_CODE.sub(" ", FENCE.sub(" ", text))


def lire(full):
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

    # 1. Racine : rien ne stagne
    for f in os.listdir(vault):
        if os.path.isfile(os.path.join(vault, f)) and norm(f) not in ROOT_ALLOW:
            issues["racine"].append(f)

    # 2. Stubs vides
    for full, rel in md_files:
        if os.path.getsize(full) == 0:
            issues["stubs"].append(rel)

    # 3. Wikilinks cassés / ambigus (Obsidian ne résout un lien sans extension que vers un .md)
    stems = defaultdict(list)
    for name, paths in all_names.items():
        stems[name.rsplit(".", 1)[0]].extend(paths)
    for full, rel in md_files:
        if os.path.basename(rel) in JOURNAL_SKIP:
            continue
        for m in WIKILINK.finditer(strip_code(lire(full))):
            target = norm(m.group(1).strip()).lower()
            if target in PLACEHOLDERS:
                continue
            hits = ([p for p in stems.get(target, []) if p.lower().endswith(".md")]
                    or all_names.get(target) or all_names.get(target + ".md") or [])
            if not hits:
                issues["wikilinks cassés"].append(f"{rel} → [[{m.group(1)}]]")
            elif len(set(hits)) > 2:
                issues["wikilinks ambigus"].append(f"{rel} → [[{m.group(1)}]] ({len(set(hits))} cibles)")

    # 4. Chemins cités vs disque
    for full, rel in md_files:
        if os.path.basename(rel) in JOURNAL_SKIP:
            continue
        for m in PATHREF.finditer(lire(full)):
            raw = norm(m.group(1).strip()).replace("\\", "/")
            if raw.startswith(("/home", "/etc", "/usr", "/var", "/opt", "/tmp")):
                continue                     # chemins absolus d'une autre machine
            p = raw.strip("/")
            if re.match(r"^[A-Za-z]:", p) or p.startswith(("http", "www", "~", "<", "...", "@", "$")):
                continue
            if p.startswith(("../", "./")):  # relatif à la fiche
                p = os.path.normpath(os.path.join(os.path.dirname(rel), p)).replace("\\", "/")
            if any(c in p for c in "*<>@") or " / " in p:
                continue                     # motif, gabarit ou notation, pas un chemin
            if re.search(r"\.[A-Za-z0-9]{1,5}/\.[A-Za-z0-9]{1,5}$", p):
                continue                     # notation d'extensions : « x.skp/.skb »
            pl = p.lower()
            if pl not in all_relpaths and not any(rp.endswith("/" + pl) for rp in all_relpaths):
                issues["chemins fantômes"].append(f"{rel} → `{m.group(1)}`")

    # 5. Doublons de nom (hors machinerie .claude/ et noms répétés par convention)
    for name, paths in all_names.items():
        if name in NOMS_REPETES:
            continue
        contenu = [p for p in paths if not p.lower().startswith(".claude/")]
        if len(contenu) > 1 and name.endswith((".md", ".pdf", ".jpg", ".jpeg", ".png", ".xlsx")):
            issues["noms en double"].append(f"{name} : " + " | ".join(sorted(contenu)))

    # 6. Fraîcheur : MEMORY.md entier, cartes de projet jusqu'à « fin de carte »
    for full, rel in md_files:
        lines = lire(full).splitlines()
        if rel == "_contexte/MEMORY.md":
            zone = lines
        elif rel.startswith(("1-Projets/", "2-Casquettes/")) and \
                os.path.basename(rel).lower() not in NOMS_REPETES:
            fins = [i for i, l in enumerate(lines) if "fin de carte" in l.lower() and i > 3]
            if not fins:
                continue
            zone = lines[:fins[0]]
        else:
            continue
        # une puce et ses lignes de suite forment UN item : la date peut être à la ligne d'après
        items = []
        for i, l in enumerate(zone):
            s = l.strip()
            if not s or s.startswith(("-", "*", "|", ">")) or re.match(r"\d+\.", s):
                items.append([i + 1, s])
            elif s.startswith("#"):
                items.append([i + 1, ""])   # un titre n'est pas un état
            elif items:
                items[-1][1] += " " + s
        for n, item in items:
            t = WIKILINK.sub(" ", strip_code(item))
            if ETAT.search(t) and not DATE.search(t):
                issues["états non datés"].append(f"{rel}:{n} — {item[:90]}")

    # 7. Doublons de synchro : « x (1).md », ou une copie dont l'original est à côté
    for name, paths in all_names.items():
        if not SYNCHRO.search(name):
            continue
        for p in paths:
            original = SYNCHRO.sub(lambda m: m.group(1) or "", p).lower()
            if p.lower().endswith(".md") or original in all_relpaths:
                issues["doublons de synchro"].append(p)

    # 8. Mémoire cachée de Claude Code pour CE coffre
    #    (le dossier de projet est le chemin du coffre, caractères spéciaux remplacés par « - »)
    cle = re.sub(r"[^A-Za-z0-9]", "-", vault).lower()
    projets = os.path.join(os.path.expanduser("~"), ".claude", "projects")
    if os.path.isdir(projets):
        for d in os.listdir(projets):
            mem = os.path.join(projets, d, "memory")
            if d.lower() == cle and os.path.isdir(mem) and os.listdir(mem):
                issues["mémoire cachée"].append(f"{mem} : " + ", ".join(sorted(os.listdir(mem))))

    # Rapport
    total = sum(len(v) for v in issues.values())
    print(f"AUDIT MÉCANIQUE — {len(md_files)} fiches, {len(all_relpaths)} fichiers — {total} signalement(s)\n")
    for k in ["racine", "stubs", "wikilinks cassés", "wikilinks ambigus", "chemins fantômes",
              "noms en double", "doublons de synchro", "mémoire cachée", "états non datés"]:
        if issues[k]:
            print(f"### {k} ({len(issues[k])})")
            for line in sorted(issues[k]):
                print(f"  - {line}")
            print()
    if total == 0:
        print("Aucun écart mécanique.")
    print("Rappel : rapport seul — rien n'a été modifié. Les contrôles de jugement restent à l'IA.")


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")   # console Windows en cp1252 : « → » plantait
    except Exception:
        pass
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
