#!/usr/bin/env python3
"""
garde-carnet.py — ne pas rendre la main sans avoir consigné la séance.

Branché sur le hook « Stop » de Claude Code (.claude/settings.json), donc lancé
à CHAQUE fin de tour. Il doit rester muet et rapide : il ne parle qu'une fois
par session.

CE QU'IL FAIT
  1. Contrôle du carnet. Si, depuis le début de la séance,
       - un fichier du coffre a été modifié,
       - ou la séance a atteint SEUIL_TOURS échanges,
     et que CARNET-DE-BORD.md n'a PAS bougé, il refuse UNE fois la fin de tour :
     l'IA doit consigner (AGENTS.md §4), ou dire en une phrase pourquoi il n'y a
     rien à consigner.
  2. Contrôle du sas. Tout fichier de 0-Inbox dont le nom figure au registre
     _contexte/tickets-traites.md (donc traité) mais qui est encore là fait
     refuser UNE fois la fin de tour (AGENTS.md §5). La section « Gardés exprès »
     du registre est ignorée.

  Il n'écrit RIEN dans le coffre : écrire demande du jugement, c'est le travail
  de l'IA. Il automatise seulement le CONTRÔLE.

RÈGLES DE CONCEPTION
  - Un seul refus par session et par contrôle (drapeau posé AVANT de répondre :
    jamais de boucle, même si l'écriture échoue ensuite).
  - Jamais de refus si le carnet a bougé depuis le début de la séance.
  - L'état vit HORS du coffre (dossier personnel), pour ne pas polluer la
    synchronisation ni la sauvegarde.
  - Parcours du coffre plafonné à TEMPS_MAX secondes : sur un dossier cloud lent,
    mieux vaut un contrôle incomplet qu'un hook qui dépasse son délai.
  - En cas d'erreur : jamais de blocage (sortie 0), MAIS un message visible et
    une ligne dans un journal. Un garde-fou qui s'éteint en silence est pire que
    pas de garde-fou : on cesse de vérifier.

COMMENT REVENIR EN ARRIÈRE, SANS IA
  1. Garder le rappel, couper le refus — créer un fichier vide nommé
     .garde-carnet-sans-blocage dans le dossier d'état (voir ETAT ci-dessous) :
         Git Bash / macOS / Linux : touch ~/.claude/.etat-garde-carnet/.garde-carnet-sans-blocage
         PowerShell : New-Item -ItemType File "$HOME\\.claude\\.etat-garde-carnet\\.garde-carnet-sans-blocage"
     Supprimer ce fichier réactive le refus.
  2. Tout couper — retirer le bloc "Stop" de .claude/settings.json.
  (Un hook ne se teste pas dans la session qui le modifie : l'effet se voit à la
  session suivante. Pour le tester sans Claude : .claude/scripts/verifier-hooks.py)

RÉGLAGES (variables d'environnement facultatives)
  MEMOIRE_COFFRE  chemin du coffre (par défaut : deux dossiers au-dessus de ce script)
  MEMOIRE_ETAT    dossier d'état (par défaut : ~/.claude/.etat-garde-carnet)
"""
import sys, json, os, re, time, pathlib, datetime, traceback

# --- Réglages -----------------------------------------------------------------
SEUIL_TOURS = 5          # nombre d'échanges qui déclenche le contrôle même sans écriture
TEMPS_MAX = 3.0          # secondes max pour parcourir le coffre
SUFFIXES_AUTEUR = ()     # ex. ("alex", "sam") si vos notes se nomment note-<date>-alex.md

ICI = pathlib.Path(__file__).resolve()
COFFRE = pathlib.Path(os.environ.get("MEMOIRE_COFFRE") or ICI.parents[2])
CARNET = COFFRE / "CARNET-DE-BORD.md"
INBOX = COFFRE / "0-Inbox"
REGISTRE = COFFRE / "_contexte" / "tickets-traites.md"
ETAT = pathlib.Path(os.environ.get("MEMOIRE_ETAT")
                    or pathlib.Path.home() / ".claude" / ".etat-garde-carnet")
INTERRUPTEUR = ETAT / ".garde-carnet-sans-blocage"
JOURNAL_ERREURS = ETAT / "erreurs.log"

# Machinerie ou bruit : une écriture là-dedans ne vaut pas une consignation.
# (worktrees et .trash : d'autres coffres ont vu leurs contrôles noyés de faux positifs.)
IGNORES = {".obsidian", ".git", "__pycache__", "journal-sessions", "worktrees", ".trash",
           "node_modules"}

# --- Messages -----------------------------------------------------------------
MESSAGE = (
    "Rappel du garde-fou : {cause}, et CARNET-DE-BORD.md n'a pas bougé. "
    "AGENTS.md §4 : toute action a deux moitiés. Consigner avant de fermer."
)
MESSAGE_BLOCAGE = (
    "Garde-fou du carnet : fin de tour refusée une fois ({cause}, rien au carnet). "
    "L'IA doit consigner, ou dire pourquoi il n'y a rien à consigner."
)
CONSIGNE = (
    "Le garde-fou du carnet signale que cette séance n'a rien consigné ({cause}). "
    "Applique AGENTS.md §4 avant de rendre la main : entrée datée au CARNET-DE-BORD.md "
    "(marqueur [contenu] ou [entretien], signée), mise à jour de la fiche de référence "
    "concernée, et retrait de ce que l'action rend faux. Si la séance ne mérite vraiment "
    "pas d'entrée — une question, une lecture, rien de décidé — dis-le en une phrase "
    "plutôt que de l'ignorer."
)
CONSIGNE_INBOX = (
    "Garde-fou du sas : ces fichiers de 0-Inbox figurent au registre tickets-traites.md, "
    "donc sont traités, mais n'ont pas été sortis : {liste}. AGENTS.md §5 : un fichier "
    "traité ne reste jamais dans 0-Inbox — range-le à sa place s'il a une valeur propre, "
    "sinon vers a-supprimer/. S'il doit rester exprès, c'est à l'utilisateur de le dire : "
    "l'inscrire alors sous « Gardés exprès » dans le registre."
)


def coffre_touche(depuis):
    """Chemin relatif du premier fichier modifié depuis `depuis`, ou None.
    S'arrête dès qu'il en trouve un, ou au bout de TEMPS_MAX secondes."""
    carnet = str(CARNET).lower()
    limite = time.time() + TEMPS_MAX
    for racine, dossiers, fichiers in os.walk(COFFRE):
        dossiers[:] = [d for d in dossiers if d not in IGNORES]
        if time.time() > limite:
            return None
        for f in fichiers:
            chemin = os.path.join(racine, f)
            if chemin.lower() == carnet:
                continue
            try:
                if os.path.getmtime(chemin) > depuis:
                    return os.path.relpath(chemin, COFFRE)
            except OSError:
                continue
    return None


def _cle(nom):
    """note-2026-01-15-1346-3.jpg -> note-2026-01-15-1346
    (sans extension, sans « (1) » de synchro, sans suffixe -N de pièce jointe)."""
    base = os.path.splitext(nom)[0]
    base = re.sub(r" \(\d+\)$", "", base)
    base = re.sub(r"-\d$", "", base)
    return base


def sas_oublies():
    """Fichiers de 0-Inbox dont le nom figure au registre, hors « Gardés exprès »."""
    if not INBOX.is_dir() or not REGISTRE.is_file():
        return []
    texte = REGISTRE.read_text(encoding="utf-8", errors="replace")
    texte = re.sub(r"(?ims)^##[^\n]*gard[ée]s expr[èe]s.*?(?=^## |\Z)", "", texte)
    oublies = []
    for f in sorted(os.listdir(INBOX)):
        if f.startswith((".", "_")) or f.lower() == "desktop.ini":
            continue
        if not (INBOX / f).is_file():
            continue
        cle = _cle(f)
        candidates = {cle}
        if SUFFIXES_AUTEUR:
            candidates.add(re.sub(r"-(%s)$" % "|".join(map(re.escape, SUFFIXES_AUTEUR)), "", cle))
        # longueur minimale : éviter qu'un nom court (« note ») ne matche n'importe quoi
        if any(len(c) >= 10 and c in texte for c in candidates):
            oublies.append(f)
    return oublies


def ecrire(marqueur, etat):
    marqueur.write_text(json.dumps(etat), encoding="utf-8")


def main():
    brut = sys.stdin.buffer.read().decode("utf-8-sig", "replace").strip()
    hook = json.loads(brut) if brut else {}
    sid = re.sub(r"[^A-Za-z0-9_-]", "", hook.get("session_id") or "inconnue")[:16]

    # Déjà relancé par un refus : ne jamais enchaîner deux refus.
    if hook.get("stop_hook_active"):
        return

    ETAT.mkdir(parents=True, exist_ok=True)
    marqueur = ETAT / (sid + ".json")
    mtime = CARNET.stat().st_mtime if CARNET.is_file() else 0.0

    if marqueur.is_file():
        etat = json.loads(marqueur.read_text(encoding="utf-8"))
    else:
        # Début de séance : l'heure de création du transcript fait foi, sinon
        # maintenant (les écritures du premier tour seraient alors ratées).
        depart = time.time()
        t = hook.get("transcript_path")
        if t:
            try:
                depart = os.path.getctime(t)
            except OSError:
                pass
        etat = {"mtime_depart": mtime, "t_depart": depart, "tours": 0, "averti": False}
        # Carnet modifié pendant ce premier tour : il a bougé.
        if mtime > depart:
            etat["mtime_depart"] = -1.0

    etat["tours"] += 1
    ecrire(marqueur, etat)

    # --- 1. Contrôle du sas, indépendant du carnet (une fois par session) ---
    if not etat.get("averti_inbox"):
        oublies = sas_oublies()
        if oublies:
            etat["averti_inbox"] = True
            ecrire(marqueur, etat)
            liste = ", ".join(oublies[:15]) + (" ..." if len(oublies) > 15 else "")
            texte = CONSIGNE_INBOX.format(liste=liste)
            sortie = {
                "systemMessage": "Garde-fou du sas : %d fichier(s) traité(s) encore dans 0-Inbox."
                                 % len(oublies),
                "hookSpecificOutput": {"hookEventName": "Stop", "additionalContext": texte},
            }
            if not INTERRUPTEUR.exists():
                sortie["decision"] = "block"
                sortie["reason"] = texte
            print(json.dumps(sortie))
            return

    # --- 2. Contrôle du carnet ---
    if etat["averti"]:
        return
    if mtime > etat["mtime_depart"]:
        return  # le carnet a bougé : rien à dire

    fichier = coffre_touche(etat.get("t_depart", 0.0))
    if fichier:
        cause = "le coffre a été modifié (" + fichier + ")"
    elif etat["tours"] >= SEUIL_TOURS:
        cause = "%d échanges" % etat["tours"]
    else:
        return

    # Drapeau posé AVANT de répondre : au pire un seul refus par session.
    etat["averti"] = True
    ecrire(marqueur, etat)

    sortie = {
        "systemMessage": MESSAGE.format(cause=cause),
        "hookSpecificOutput": {"hookEventName": "Stop",
                               "additionalContext": CONSIGNE.format(cause=cause)},
    }
    if not INTERRUPTEUR.exists():
        sortie["decision"] = "block"
        sortie["reason"] = CONSIGNE.format(cause=cause)
        sortie["systemMessage"] = MESSAGE_BLOCAGE.format(cause=cause)
    print(json.dumps(sortie))


def signaler_panne():
    """Jamais de blocage sur panne, mais jamais de silence non plus."""
    try:
        ETAT.mkdir(parents=True, exist_ok=True)
        with JOURNAL_ERREURS.open("a", encoding="utf-8") as j:
            j.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "  "
                    + traceback.format_exc(limit=3).replace("\n", " | ") + "\n")
    except Exception:
        pass
    print(json.dumps({"systemMessage": "garde-carnet.py est en panne (le contrôle du carnet "
                                       "ne tourne pas). Détail : " + str(JOURNAL_ERREURS)}))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        signaler_panne()
    sys.exit(0)
