#!/usr/bin/env python3
"""
garde-accord.py — pas d'action qui modifie quelque chose HORS du coffre sans un
accord explicite dans le message de l'utilisateur.        (FACULTATIF)

Branché sur le hook « PreToolUse » (.claude/settings.json), avec un « matcher »
qui ne vise que les outils qui ÉCRIVENT ailleurs : envoi de mail, écriture dans
une base en ligne, clic ou saisie dans un navigateur… Les lectures ne doivent
pas passer par ici (réglez le matcher), ou sont laissées passer ci-dessous.

POURQUOI
  « Ne pas agir sans accord explicite » écrit dans les consignes se transgresse :
  une IA lit volontiers une intention (« il faudrait… ») comme un ordre. Ce
  hook en fait un mécanisme : si le tour en cours ne contient aucun mot d'accord,
  l'outil est refusé et l'IA doit présenter son plan puis attendre.

RÈGLE
  Les messages de l'utilisateur du tour en cours (celui qui l'a ouvert, plus
  ceux envoyés pendant que l'IA travaillait) doivent contenir un accord :
  « vas-y », « fais-le », « oui » en tête, ou un verbe d'ordre (crée, envoie…).
  Liste ACCORDS ci-dessous, à ajuster à votre façon de parler.

LIMITES — à connaître avant de l'installer
  - Un mot-clé ne lit pas l'intention : un accord peut être raté (faux refus) ou
    mal lu (« ne l'envoie pas » contient « envoie »).
  - Un ordre sur UN point laisse passer toute l'action suivante dans le même
    tour. Le hook ne sait pas si le plan d'ensemble est validé.
  - Bash/PowerShell ne sont pas surveillés (trop larges).
  - Retour d'usage : ce qui a le mieux marché n'est pas d'enrichir la liste,
    c'est que l'humain prenne l'habitude d'un mot net (« vas-y ») quand il veut
    que l'action se fasse.
  - En cas d'erreur du script : l'outil passe (un garde-fou cassé ne doit pas
    bloquer la séance), MAIS un message visible le signale.
"""
import sys, json, re, unicodedata, tempfile

ACCORDS = [
    r"vas? y", r"fai[st] (le|la|les|ce que|ca)", r"tu peux y aller", r"\bgo\b",
    r"c est parti", r"feu vert", r"je valide", r"\bvalide\b", r"\bok fais", r"^oui\b",
    r"\bcree[sz]?\b", r"\bcreer\b", r"\bsupprime[sz]?\b", r"\brenomme\b", r"\bconsigne\b",
    r"\bpublie\b", r"\benvoie\b", r"\bcorrige\b", r"\binstalle\b", r"\bapplique\b",
    r"\bajoute\b", r"\bmodifie\b", r"\bactive\b", r"\bdesactive\b", r"\bremplace\b",
    r"\blance\b", r"\bexecute[rsz]?\b", r"\bmets\b", r"\bconstrui[st]\b", r"\bcontinue[sz]?\b",
]

# Actions de navigateur qui ne font que regarder.
LECTURE_NAV = {"screenshot", "zoom", "scroll", "scroll_to", "wait", "hover"}
LECTURE_BATCH = {"find", "read_page", "get_page_text", "navigate", "tabs_context",
                 "read_console_messages", "read_network_requests"}
# Un JavaScript qui contient l'un de ces motifs ÉCRIT (clic, DOM, requête) : refusé.
ECRITURES_JS = (
    "click(", "setvalue(", "submit(", "dispatchevent(", "execcommand(", "focus(",
    "innerhtml", "outerhtml", "insertadjacent", "appendchild", "removechild",
    "createelement", "document.write", "localstorage.setitem", "sessionstorage.setitem",
    "clipboard.write", "xmlhttprequest", "websocket",
    '"post"', "'post'", '"patch"', "'patch'", '"put"', "'put'", '"delete"', "'delete'",
)

REFUS = ("Accord explicite absent. Présente le plan en une phrase (où · quoi · résultat) "
         "et attends que l'utilisateur dise de l'exécuter.")


def normaliser(t):
    t = unicodedata.normalize("NFD", t.lower())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")   # sans accents
    t = re.sub(r"<system-reminder>.*?</system-reminder>", " ", t, flags=re.S)
    return re.sub(r"[’'\-_]", " ", t).strip()


def js_lecture(entree):
    code = str((entree or {}).get("text") or "").lower()
    return bool(code) and not any(m in code for m in ECRITURES_JS)


def lecture_seule(outil, entree):
    """Vrai si l'appel ne fait que lire : on le laisse passer sans accord."""
    if outil.endswith("__computer"):
        return entree.get("action") in LECTURE_NAV
    if outil.endswith("__javascript_tool"):
        return js_lecture(entree)
    if outil.endswith("__browser_batch"):
        for a in entree.get("actions") or []:
            nom = a.get("name", "")
            if nom == "computer":
                if (a.get("input") or {}).get("action") not in LECTURE_NAV:
                    return False
            elif nom == "javascript_tool":
                if not js_lecture(a.get("input") or {}):
                    return False
            elif nom not in LECTURE_BATCH:
                return False
        return True
    if outil in ("Edit", "Write"):
        # brouillons dans le dossier temporaire du système : libres
        chemin = (entree.get("file_path") or "").replace("\\", "/").lower()
        return chemin.startswith(tempfile.gettempdir().replace("\\", "/").lower())
    return False


def messages_du_tour(chemin):
    """Messages de l'utilisateur du tour en cours : celui qui a ouvert le tour,
    plus ceux envoyés pendant que l'IA travaillait (« queued_command »).
    Une précision envoyée en cours de route n'annule donc pas l'ordre donné
    juste avant. Le message suivant ouvre un nouveau tour et remet à zéro.
    ⚠️ Dépend du format interne du transcript de Claude Code : à revérifier
    après une mise à jour (verifier-hooks.py ne teste pas ce point)."""
    tour = None
    with open(chemin, encoding="utf-8") as f:
        for ligne in f:
            if '"user"' not in ligne and "queued_command" not in ligne:
                continue
            try:
                o = json.loads(ligne)
            except ValueError:
                continue
            if o.get("type") == "attachment":
                a = o.get("attachment") or {}
                if (a.get("type") == "queued_command"
                        and (a.get("origin") or {}).get("kind") == "human"
                        and tour and tour[0] == "texte"):
                    tour[1].append(a.get("prompt") or "")
                continue
            if o.get("type") != "user" or o.get("isMeta"):
                continue
            if o.get("isCompactSummary"):
                tour = ("resume", [])
                continue
            c = (o.get("message") or {}).get("content")
            if isinstance(c, list):
                if any(isinstance(b, dict) and b.get("type") == "tool_result" for b in c):
                    continue
                c = " ".join(b.get("text", "") for b in c
                             if isinstance(b, dict) and b.get("type") == "text")
            if not isinstance(c, str):
                continue
            propre = re.sub(r"<system-reminder>.*?</system-reminder>", "", c, flags=re.S).strip()
            if not propre or propre.startswith("<"):
                continue
            tour = ("texte", [propre])   # nouveau tour : on repart de ce message
    return tour


def main():
    brut = sys.stdin.buffer.read().decode("utf-8-sig", "replace").strip()
    hook = json.loads(brut) if brut else {}
    outil = hook.get("tool_name") or ""
    if lecture_seule(outil, hook.get("tool_input") or {}):
        return
    tour = messages_du_tour(hook.get("transcript_path") or "")
    if tour is None or tour[0] == "resume":
        return   # reprise après résumé automatique : l'accord a été donné avant
    for message in tour[1]:
        texte = normaliser(message)
        if any(re.search(p, texte) for p in ACCORDS):
            return
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": REFUS,
    }}, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(json.dumps({"systemMessage": "garde-accord.py en panne, l'outil passe sans "
                                           "contrôle : %s" % type(e).__name__}))
    sys.exit(0)
