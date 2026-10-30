# AGENTS.md — Règles communes à toutes les IA

Valable pour **toute IA** (Claude, ChatGPT, autre) qui travaille avec ce coffre. **Source unique
des consignes** : toute règle s'écrit ici ou dans un fichier pointé d'ici — jamais ailleurs.
En cas de divergence, AGENTS.md prime. L'utilisateur garde la main au-dessus de tout.

> *Gabarit — à adapter.* Remplacez `<Prénom>` par le prénom de la personne qui tient le coffre,
> et `<IA>` par le nom de l'assistant (Claude, ChatGPT…). Retirez cette note ensuite.

## 1. Le coffre

Ce coffre est **la seule référence**. Méthode IPCRA : `0-Inbox` / `1-Projets` / `2-Casquettes` /
`3-Ressources` / `4-Archives` + couche `_contexte`. **Tout ce qui concerne le rangement** (zones,
critères, doublons, nommage, audit) : `3-Ressources/methodes/methode-de-rangement.md`, référence
unique — ne rien décider de rangement sans l'avoir lue.

## 2. Démarrage de session

a) **Vérifie factuellement ton niveau d'accès** (lire / créer / déplacer / **modifier un fichier
   existant**) — teste sur `_test_claude.txt` en cas de doute ; n'annonce jamais un accès par
   déduction du nom d'un outil. Sans la capacité « modifier », la session est **à accès limité** :
   elle dépose des tickets et s'arrête (voir §5).
b) **Lis, et rien de plus** : ce fichier · `_contexte/MEMORY.md` (l'index) ·
   `_contexte/profil/consignes-de-travail.md` (des **consignes**, pas des notes) ·
   `_contexte/profil/profil.md` · les 2-3 dernières entrées de `CARNET-DE-BORD.md`.
   **Le reste s'ouvre quand le sujet arrive** — `MEMORY.md` dit quoi ouvrir et quand.
c) **Relève le sas `0-Inbox/`** (comparé au registre `_contexte/tickets-traites.md`). En accès
   complet, traite ce qui s'y trouve avant toute autre demande (§5). Une note de <Prénom> déposée
   là est un **ordre**. **Tout fichier là depuis plus de 3 jours se signale en tête.**
d) **Rends la main en 5 lignes max** : accès, tickets en attente, en cours, blocages.

## 3. Sécurité — NON NÉGOCIABLE

- **Rien ne se crée, ne se renomme, ne s'écrase ni ne se supprime sans ORDRE EXPLICITE.**
  **Une intention n'est pas une autorisation** : « on va faire X », une question, une réponse
  technique ne sont pas des ordres. **Présenter le plan puis se taire** — ne pas demander
  « je le fais ? » : la question fabrique l'ambiguïté, toute réponse adjacente se lisant comme un
  accord. <Prénom> dit « vas-y » de lui-même. Seule exception : **consigner** (§4), demandé une
  fois pour toutes.
- **Supprimer = déplacer vers `a-supprimer/`** ; <Prénom> vide. Définitif = ordre ciblé, sans
  ambiguïté ; au moindre doute sur la cible, s'arrêter et confirmer.
- **Aucun secret dans le coffre** (mots de passe, clés d'API, jetons). Si <Prénom> en décide
  autrement, ils vivent dans **un seul fichier** désigné par lui, jamais dans un dossier partagé.
  En croiser un ailleurs : le signaler.
- **Opérations de masse** (10+ fichiers) : toujours réversibles, via `a-supprimer/`.
- **Hors du coffre** (messagerie, bases en ligne, navigateur) : on discute, puis <Prénom> dit
  d'exécuter. **Un ordre sur un point ne valide pas le plan entier.**
- En cas de doute : demander avant d'agir.

## 4. Consigner — toute action a deux moitiés

1. **Consigner le nouveau** : entrée datée au `CARNET-DE-BORD.md` (marqueur **[contenu]** ou
   **[entretien]**) **et** mise à jour de la fiche de référence concernée, dans la même session.
2. **Retirer de la fiche ce que l'action rend faux.** Le carnet garde l'histoire, la fiche ne
   garde que le présent — c'est ce qui rend l'effacement sûr. Une action n'est finie qu'après.
   **Une correction se cherche dans tout le coffre** (un grep de l'ancienne affirmation) : marquer
   `~~…~~ *(ancien — remplacé le JJ/MM : …)*` ce qui est rapide, et dire au carnet ce qui a été
   corrigé — l'audit rattrape le reste.
3. **N'écrire au présent que ce qui existe** ; dater toute certification ; après un renommage, grep
   des occurrences dans le même geste ; ne jamais recopier un nom de fichier sans lire le disque.
4. **Un journal de session ne fait foi sur rien** : il dit ce qui s'est dit, jamais ce qui s'est
   fait après. L'état d'une affaire se lit dans sa fiche.
5. **Si aucune fiche ne porte l'affaire, la créer fait partie de l'action** — sauf si <Prénom> dit
   qu'elle n'a pas à vivre dans le coffre.
6. **Signer** : toute consigne ajoutée à ce fichier, aux consignes ou à la méthode porte
   `*(règle du AAAA-MM-JJ — décidée par <Prénom>, écrite par <IA>)*`, sinon
   `*(proposée par <IA> — non validée)*` — et alors **elle ne s'applique pas**.
   Carnet : `[contenu] [<IA>]`. Fiches ordinaires : rien.

Le marqueur du carnet est la mesure : **[contenu]** = le coffre a servi la vie réelle (un projet,
un achat, une décision) ; **[entretien]** = le coffre s'est occupé de lui-même. Si l'entretien
dépasse le contenu pendant des semaines, le système travaille pour lui, pas pour vous.

## 4bis. Diagnostiquer

**Quand une correction échoue deux fois, arrêter de corriger et aller chercher le fait manquant**
(lire le journal, l'erreur exacte, la doc officielle) plutôt que d'essayer une troisième variante.

## 5. Tickets `0-Inbox` — écritures différées

**Accès limité** (une IA qui sait lire mais pas modifier) : elle dépose un ticket dans `0-Inbox`
(`ticket-<sujet>-<AAAA-MM-JJ>.md` : cible, opération, contenu exact), rien d'autre — d'office,
sans demander s'il en faut un. **Accès complet** : traiter, consigner, inscrire le **nom complet
du fichier** à `_contexte/tickets-traites.md` (qui fait foi : ne jamais retraiter ce qui y est)
**et** sortir le fichier du sas — rangé à sa place s'il a une valeur propre (photo, document),
sinon vers `a-supprimer/`. **Un fichier traité ne reste jamais dans `0-Inbox`.** Ce qui attend une
validation part tout de suite à sa place ; la question va dans la fiche, section « À préciser ».
Le hook de fin de tour (`garde-carnet.py`) refuse de rendre la main si un fichier inscrit au
registre est encore dans le sas ; exception : section « Gardés exprès » du registre.

## 6. Style de réponse

**Court et direct**, répondre puis s'arrêter, pas de relance ; dire « je ne sais pas ». Le reste
(décider, contredire, chercher avant de demander) est dans `consignes-de-travail.md`.

## 7. Anti-inflation

- **Budget de démarrage : 300 lignes** (ce fichier + `CLAUDE.md` + `MEMORY.md` + les 2 fiches de
  profil). **Une règle qui entre en fait sortir une autre.**
- **Une erreur ne devient une règle qu'à la deuxième occurrence.** La première : une ligne au carnet.
- **Peu de mécanismes** : chaque hook, script ou skill ajouté est une pièce qui peut casser en
  silence à la prochaine mise à jour de l'outil. On n'en ajoute un qu'après avoir constaté le
  besoin deux fois.
- **Sauvegarde** : hors du dossier synchronisé, **aucune IA n'écrit dans le dépôt de sauvegarde**.
