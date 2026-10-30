# Gabarit — une mémoire holistique tenue avec une IA

Un coffre de notes vide, prêt à copier, pour qu'une IA (Claude Code en premier lieu, mais pas
seulement) tienne avec toi **la mémoire de ta vie et de tes projets** : ce qui est en cours,
ce qui a été décidé, où sont les papiers, ce qu'il reste à faire.

Il reprend la structure et les règles d'un coffre réel, tenu au quotidien plusieurs mois, **sans
aucune de ses données**. Les règles sont nées d'erreurs constatées ; le récit qui les explique est
dans le dossier parent de ce gabarit.

## Ce qu'il contient

```
gabarit/
├── AGENTS.md              règles communes à toutes les IA (source unique)
├── CLAUDE.md              amorçage Claude Code : pointe vers AGENTS.md, charge MEMORY.md
├── CARNET-DE-BORD.md      journal daté des séances (entrées d'exemple fictives)
├── _test_claude.txt       fichier sur lequel une IA teste son accès en écriture
├── 0-Inbox/               le sas : tout ce qui arrive, rien n'y stagne
├── 1-Projets/             ce qui a un début et une fin (modèle de fiche dans le LISEZ-MOI)
├── 2-Casquettes/          les responsabilités sans fin
├── 3-Ressources/methodes/ methode-de-rangement.md, référence unique du classement
├── 4-Archives/            terminé mais à conserver
├── a-supprimer/           la corbeille que seul l'humain vide
├── _contexte/             MEMORY.md (index), profil/ (2 fiches), tickets-traites.md (registre)
├── _prompts/              un prompt = un fichier, lisible par toute IA
└── .claude/
    ├── settings.json      branche les 2 hooks de base, interdit rm / Remove-Item
    └── scripts/           les hooks et scripts (détail plus bas)
```

## Les principes, en six lignes

1. **Toute action a deux moitiés** : consigner le nouveau (carnet + fiche), et **retirer de la
   fiche ce que l'action rend faux**. Le carnet garde l'histoire, la fiche ne garde que le présent.
2. **Une intention n'est pas un ordre** : l'IA présente son plan et attend un « vas-y ».
3. **Aucune IA ne supprime** : elle déplace vers `a-supprimer/`, tu vides.
4. **Un sas, `0-Inbox`**, relevé à chaque démarrage, et qui se vide.
5. **Anti-inflation** : 300 lignes lues au démarrage, une règle qui entre en fait sortir une
   autre, une erreur ne devient règle qu'à la deuxième fois.
6. **Les règles se signent** : une règle écrite par l'IA sans validation ne s'applique pas.

## Installation pas à pas

Le plus simple : ouvre `DEMARRER-ICI.md`, qui te guide en cinq étapes avec Claude. Le détail technique suit.

1. **Copie** le dossier `gabarit/` où tu veux tenir ton coffre, et renomme-le.
   ⚠️ Si c'est un dossier synchronisé (Google Drive, OneDrive, Dropbox, iCloud), lis « Pièges »
   plus bas avant de continuer.
2. **Python 3** doit être installé. Vérifie quelle commande marche chez toi : `python`, `python3`
   ou, sous Windows, `py`. Si ce n'est pas `python`, remplace le mot dans les deux lignes
   `"command"` de `.claude/settings.json` (ou mets le chemin complet de l'exécutable).
3. **Teste les hooks sans Claude** :
   ```
   python .claude/scripts/verifier-hooks.py
   ```
   Il doit afficher `11/11 cas OK`. Il travaille sur une copie jetable : ton coffre n'est pas touché.
4. **Personnalise** : `AGENTS.md` (remplace `<Prénom>` et `<IA>`), `_contexte/profil/profil.md`,
   `_contexte/profil/consignes-de-travail.md`, puis vide les exemples de `MEMORY.md` et du carnet.
   Garde ces fichiers courts : ils sont lus à chaque séance.
5. **Ouvre Claude Code dans le dossier du coffre** (`claude` dans un terminal placé à sa racine).
   Au premier lancement, il demande de faire confiance au dossier et à ses hooks : c'est ce qui
   active `settings.json`. Tape `/hooks` pour vérifier que `Stop` et `PostToolUse` sont listés.
6. **Facultatif** — Obsidian pour lire et éditer les notes (ouvrir le dossier comme coffre) ; la
   sauvegarde planifiée (`sauvegarde.py`, voir plus bas).

## Les hooks et scripts

Tous en Python, sans dépendance. Tous **rendent la main sans bloquer** s'ils plantent, mais
**le disent** (message ou journal) : un garde-fou qui s'éteint en silence est pire que rien.
Leur état vit hors du coffre, dans `~/.claude/.etat-garde-carnet/`.

| Script | Branché sur | Ce qu'il fait |
|---|---|---|
| `garde-carnet.py` | `Stop` (fin de tour) — **installé** | Refuse **une fois par séance** de rendre la main si un fichier du coffre a changé (ou 5 échanges ont eu lieu) sans que `CARNET-DE-BORD.md` ait bougé : l'IA doit consigner ou dire pourquoi il n'y a rien à consigner. Refuse aussi une fois si un fichier inscrit au registre `tickets-traites.md` traîne encore dans `0-Inbox`. |
| `notif-consignation.py` | `PostToolUse` — **installé** | Affiche « Consignation faite » la première fois que le carnet change dans la séance. |
| `garde-accord.py` | `PreToolUse` — *facultatif* | Refuse les outils qui agissent **hors du coffre** (mail, base en ligne, navigateur) si ton message ne contient pas un mot d'accord (« vas-y », « envoie », « crée »…). Lis ses limites en tête du fichier. |
| `extrait-session.py` | `SessionEnd` — *facultatif* | Dépose un extrait texte de chaque séance dans `_contexte/journal-sessions/`. ⚠️ Tout ce qui s'est dit entre alors dans le coffre. |
| `audit-mecanique.py` | à la main | Rapport d'écarts : liens cassés, chemins cités qui n'existent pas, doublons, copies de synchro, états non datés. Ne modifie rien. `python .claude/scripts/audit-mecanique.py .` |
| `sauvegarde.py` | planificateur de tâches | Copie le texte du coffre dans un dépôt git **hors du dossier synchronisé** et y crée un point de restauration ; journal OK/ÉCHEC à chaque passage. |
| `verifier-hooks.py` | à la main | Teste `garde-carnet` et `notif-consignation` sur une copie jetable. À relancer après chaque mise à jour de Claude Code. |

**Couper un hook** : retirer son bloc de `.claude/settings.json`. **Garder le rappel du carnet sans
le refus** : créer un fichier vide `~/.claude/.etat-garde-carnet/.garde-carnet-sans-blocage`.

**Brancher les hooks facultatifs** — ajouter dans `"hooks"` de `settings.json` :

```json
"SessionEnd": [
  { "hooks": [ { "type": "command", "timeout": 120,
    "command": "python \"$CLAUDE_PROJECT_DIR/.claude/scripts/extrait-session.py\"" } ] }
],
"PreToolUse": [
  { "matcher": "^mcp__.*__(send|reply|forward|create|update|delete|trash).*$",
    "hooks": [ { "type": "command", "timeout": 10,
      "command": "python \"$CLAUDE_PROJECT_DIR/.claude/scripts/garde-accord.py\"" } ] }
]
```

Le `matcher` de `garde-accord` est un exemple : il vise les outils de connecteurs (MCP) dont le
nom contient un verbe d'écriture. Adapte-le aux connecteurs que tu branches — et laisse-en
les lectures dehors.

## Pièges — ce qui casse chez les autres coffres

Tirés des signalements publics d'autres coffres tenus par IA, et de l'usage de celui-ci :

- **Le filet qui s'éteint en silence.** Une sauvegarde automatique qui cesse de tourner sans
  rien dire, pendant des semaines. → Ici chaque script écrit OK ou ÉCHEC ; lis
  `journal-sauvegarde.txt` de temps en temps.
- **La synchronisation cloud n'est pas une sauvegarde**, et elle corrompt un dépôt git placé dans
  le dossier synchronisé. → Dépôt de sauvegarde **hors** du dossier synchronisé ; état des hooks
  hors du coffre. Évite qu'une IA fasse des écritures en masse pendant que la synchro travaille.
- **Les copies de conflit** (`fiche (1).md`) quand deux machines écrivent. → L'audit les signale.
- **La plomberie casse à chaque mise à jour de l'outil.** → Peu de hooks, un script de test,
  et des règles écrites en texte dans `AGENTS.md` qui restent valables même si un hook tombe.
- **Les hooks qui dépassent leur délai** sur Windows ou sur un dossier cloud lent. →
  `garde-carnet` plafonne son parcours du coffre à 3 secondes.
- **Trop de commandes, trop de taxonomie.** Ceux qui tiennent dans la durée utilisent 3 à 5
  commandes, pas 25, et un découpage grossier. → Le gabarit n'en livre aucune : ajoute-les
  à la deuxième fois que le besoin revient.
- **La mémoire cachée.** Claude Code peut garder une mémoire privée hors du coffre, invisible aux
  autres IA. → Désactive-la si tu veux que tout vive dans le coffre (`"autoMemoryEnabled": false`
  dans `settings.json`) ; l'audit vérifie qu'elle reste vide.
- **Certains environnements ne chargent pas `.claude/`** (selon l'application ou le mode
  utilisé) : ni hooks, ni skills. Vérifie avec `/hooks`, et ne compte pas sur un hook pour une
  règle vitale — elle doit aussi être écrite dans `AGENTS.md`.

## Confidentialité

Le coffre contiendra ta vie : ne le publie pas, et réfléchis à ce que tu y mets
(`AGENTS.md` §3 : aucun secret par défaut). Si tu partages un jour une partie de ta
configuration, pars de **ce** gabarit plutôt que de ton coffre.
