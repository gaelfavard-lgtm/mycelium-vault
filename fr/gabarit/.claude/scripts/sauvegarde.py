#!/usr/bin/env python3
"""
sauvegarde.py — sauvegarde du coffre, texte uniquement, dans un dépôt git local
placé HORS de tout dossier synchronisé (Google Drive, OneDrive, Dropbox, iCloud).
                                                              (FACULTATIF)
Ce n'est PAS un hook : on le lance à la main, ou par le planificateur de tâches
(Windows) / cron (macOS, Linux), par exemple une fois par jour.

POURQUOI HORS DU DOSSIER SYNCHRONISÉ
  Un dépôt git dans un dossier synchronisé se fait corrompre : l'outil de synchro
  recopie les fichiers de .git un par un pendant que git écrit. Et la synchro
  n'est pas une sauvegarde : une suppression ou une corruption se synchronise
  aussi. Il faut une copie séparée, avec historique.

Usage :
    python sauvegarde.py
    python sauvegarde.py --coffre <chemin> --depot <chemin>

Ce que fait le script :
  1. copie les fichiers texte du coffre (EXTENSIONS) vers le dépôt ;
  2. retire du dépôt ce qui n'existe plus dans le coffre (l'historique git le garde) ;
  3. crée un point de restauration (commit) s'il y a du changement ;
  4. écrit TOUJOURS une ligne dans <depot>/journal-sauvegarde.txt, OK ou ÉCHEC.
     Un filet qui s'éteint en silence est pire que pas de filet : jetez un œil à
     ce journal de temps en temps.

Restaurer sans IA : ouvrir le dépôt, `git log` pour choisir un point,
`git checkout <point> -- <fichier>` pour récupérer un fichier.

Règle : aucune IA n'écrit dans le dépôt de sauvegarde (un verrou git oublié
suffit à bloquer toutes les sauvegardes suivantes).
"""
import os, sys, time, shutil, subprocess, datetime, argparse, platform

EXTENSIONS = {".md", ".txt", ".json", ".py", ".sh", ".bat", ".html", ".css", ".js", ".csv"}
IGNORER = {".git", ".obsidian", "node_modules", "__pycache__", ".trash", "worktrees"}
JOURNAL = "journal-sauvegarde.txt"


def git(depot, *args):
    return subprocess.run(["git", "-C", str(depot), *args], capture_output=True, text=True)


def copier(coffre, depot):
    """Copie les fichiers texte du coffre vers le dépôt, et retire ce qui a disparu."""
    copies = attendus = 0
    for racine, dossiers, fichiers in os.walk(coffre):
        dossiers[:] = [d for d in dossiers if d not in IGNORER]
        for f in fichiers:
            if os.path.splitext(f)[1].lower() not in EXTENSIONS:
                continue
            src = os.path.join(racine, f)
            rel = os.path.relpath(src, coffre)
            dst = os.path.join(depot, rel)
            attendus += 1
            try:
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                if (not os.path.exists(dst) or os.path.getmtime(src) > os.path.getmtime(dst)
                        or os.path.getsize(src) != os.path.getsize(dst)):
                    shutil.copy2(src, dst)
                    copies += 1
            except Exception as e:
                print(f"  ! impossible de copier {rel} : {e}")
    # Retirer du dépôt ce qui n'existe plus dans le coffre (récupérable par git).
    retires = 0
    for racine, dossiers, fichiers in os.walk(depot):
        dossiers[:] = [d for d in dossiers if d not in IGNORER]
        for f in fichiers:
            if f == JOURNAL:
                continue
            dst = os.path.join(racine, f)
            rel = os.path.relpath(dst, depot)
            if not os.path.exists(os.path.join(coffre, rel)):
                os.remove(dst)
                retires += 1
    return copies, retires, attendus


def main():
    ici = os.path.dirname(os.path.abspath(__file__))
    p = argparse.ArgumentParser(description="Sauvegarde texte du coffre dans un dépôt git local.")
    p.add_argument("--coffre", default=os.path.abspath(os.path.join(ici, "..", "..")))
    p.add_argument("--depot", default=os.path.join(os.path.expanduser("~"), "Sauvegarde-coffre"))
    a = p.parse_args()
    coffre, depot = os.path.abspath(a.coffre), os.path.abspath(a.depot)
    horodatage = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"\n  Coffre     : {coffre}\n  Sauvegarde : {depot}\n")

    if not os.path.isdir(coffre):
        print(f"  [ECHEC] coffre introuvable : {coffre}")
        return 1
    if os.path.commonpath([coffre, depot]) == coffre:
        print("  [ECHEC] le dépôt de sauvegarde ne doit pas être DANS le coffre.")
        return 1
    if shutil.which("git") is None:
        print("  [ECHEC] git n'est pas installé — https://git-scm.com/downloads")
        return 1

    os.makedirs(depot, exist_ok=True)
    if not os.path.isdir(os.path.join(depot, ".git")):
        print("  Première sauvegarde — création du dépôt local...")
        git(depot, "init", "-q")
        git(depot, "config", "user.name", "Sauvegarde du coffre")
        git(depot, "config", "user.email", "sauvegarde@localhost")

    copies, retires, attendus = copier(coffre, depot)
    print(f"  {attendus} fichiers texte — {copies} copiés, {retires} retirés")
    machine = os.environ.get("COMPUTERNAME") or platform.node() or "?"

    # Un verrou git oublié (interruption) fait échouer TOUS les commits suivants,
    # et git ne le dit que sur stderr. On retire ceux de plus de 5 minutes.
    for verrou in ("HEAD.lock", "index.lock"):
        chemin = os.path.join(depot, ".git", verrou)
        if os.path.exists(chemin) and time.time() - os.path.getmtime(chemin) > 300:
            try:
                os.remove(chemin)
                print(f"  Verrou git périmé retiré : {verrou}")
            except Exception as e:
                print(f"  ! verrou {verrou} impossible à retirer : {e}")

    git(depot, "add", "-A")
    change = git(depot, "diff", "--cached", "--quiet").returncode != 0
    verdict = "OK"
    if change:
        r = git(depot, "commit", "-q", "-m", f"Sauvegarde {horodatage} - {machine}")
        if r.returncode == 0:
            etat = "nouveau point"
            print("\n  [OK] Nouveau point de restauration enregistré.")
        else:
            # Ne JAMAIS écrire « OK » quand git a refusé : un journal qui ment est
            # pire que pas de journal.
            verdict = "ECHEC"
            cause = (r.stderr or r.stdout).strip().replace("\n", " ")
            etat = "ECHEC commit : " + cause[:120]
            print(f"\n  [ECHEC] git commit a refusé : {cause}")
    else:
        etat = "rien de neuf"
        print("\n  [OK] Aucun changement depuis la dernière sauvegarde.")

    points = git(depot, "rev-list", "--count", "HEAD").stdout.strip() or "0"
    suivis = len([l for l in git(depot, "ls-files").stdout.splitlines() if l])
    with open(os.path.join(depot, JOURNAL), "a", encoding="utf-8") as j:
        j.write(f"{horodatage}  {verdict}  {etat}  ({suivis} fichiers, {points} points)  [{machine}]\n")
    print(f"\n  Points de restauration : {points}\n  Fichiers sauvegardés   : {suivis}\n")
    return 0 if verdict == "OK" else 1


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    sys.exit(main())
