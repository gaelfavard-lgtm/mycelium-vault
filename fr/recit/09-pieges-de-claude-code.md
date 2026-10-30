# 9. Les pièges de Claude Code

Ce chapitre est plus technique. Il s'adresse à ceux qui utilisent Claude Code pour autre chose que du
code, et il raconte ce que nous avons appris sur l'outil lui-même.

## Les transcriptions effacées au bout de 30 jours

Claude Code garde la transcription complète de chaque session dans des fichiers `.jsonl` (des
fichiers texte, une ligne par événement), rangés dans le dossier de l'utilisateur, **en dehors du
coffre**. Le 1er septembre, en cherchant une vieille conversation, nous avons découvert deux choses :
- ces fichiers ne remontaient qu'au 25 août, alors que le carnet remonte au 10. Les sessions d'avant
  s'étaient tenues ailleurs (dans Cowork, ou sur une autre machine), et n'avaient laissé aucune trace
  ici ;
- surtout, **par défaut, Claude Code supprime ces transcriptions au bout de 30 jours**, sans prévenir.
  C'est le réglage `cleanupPeriodDays`.

Gaël a proposé une purge organisée ; je l'ai d'abord écartée, puis j'ai proposé de mettre ces fichiers
dans la sauvegarde git. Mauvaise idée : ils pesaient 227 Mo et grossissaient chaque jour, pour une
sauvegarde dimensionnée pour moins d'un mégaoctet. Chaque sauvegarde en aurait stocké une copie
complète.

Ce que nous avons fait :
1. **Une ligne de réglage** : `"cleanupPeriodDays": 3650`. La purge est repoussée à dix ans. C'est
   90 % du bénéfice pour 1 % du travail.
2. **Un extrait lisible** : à la fin de chaque session, un script garde seulement le texte échangé
   (environ 12 % du fichier brut), en Markdown, dans le coffre. La sauvegarde le ramasse sans rien
   changer.
3. **Un journal** « OK » ou « ECHEC » à chaque passage, pour qu'une panne se voie.

Le réglage est posé **à deux endroits**, dans les réglages du projet et dans ceux de l'utilisateur,
parce que Cowork ne lit pas ceux du projet (voir plus bas).

## Un hook qui parlait dans le vide

Nous avions écrit un hook qui, après douze échanges, rappelle de mettre à jour le carnet si ce n'est
pas fait. Le 10 septembre, Gaël a remarqué qu'il recevait bien le rappel… et que rien ne se passait. Il
devait redemander la mise à jour à la main.

La cause, trouvée en **lisant le hook plutôt qu'en le réécrivant** : il envoyait un `systemMessage`.
Or un `systemMessage` **s'affiche à l'utilisateur, il n'arrive pas jusqu'à l'IA.** Le rappel prévenait
la seule personne qui n'avait pas besoin d'être prévenue.

> **`systemMessage` parle à l'humain. `hookSpecificOutput.additionalContext` parle à l'IA.** Un hook qui
> doit déclencher une action de l'IA doit utiliser le second.

*Mise à jour du 5 octobre : ce rappel est devenu un refus. Le hook peut maintenant empêcher la fin
d'un tour tant que rien n'est consigné — voir le [chapitre 11](11-les-regles-qui-sont-nees.md).*

## Détecter une écriture par la date, pas par le nom du fichier

Nous avons ajouté un second hook qui confirme quand le carnet a été écrit. Il ne regarde pas quel
fichier l'outil dit modifier : **il compare la date de modification du carnet avant et après.** Le
carnet s'écrit aussi souvent par une commande du terminal que par l'outil d'édition, et un filtre sur
le nom de fichier aurait raté la moitié des cas.

## Un hook ne se teste pas dans la session qui le crée

Les réglages sont lus au démarrage. Un hook ajouté pendant une session ne s'active pas dans cette
session. Il faut en ouvrir une nouvelle pour l'essayer.

## Chercher dans l'historique : les fichiers bruts, pas l'outil de recherche

Le 1er septembre, Gaël a voulu savoir si j'avais lu ses mails. J'ai utilisé l'outil de recherche dans
les sessions passées, qui n'a rien renvoyé, et j'ai conclu : aucun accès. **C'était faux.** Une autre
session a trouvé les appels en cherchant directement dans les fichiers `.jsonl`.

Pour savoir ce qu'une IA a réellement touché, il faut chercher dans ces fichiers le nom technique sous
lequel chaque appel à un connecteur est enregistré, de la forme `mcp__<connecteur>__<outil>`. Limite :
ça ne vaut que pour cette machine.

## Cowork ne charge pas le dossier `.claude`

Découvert le 1er septembre : dans Cowork, **ni les skills, ni les commandes, ni les hooks du coffre ne
se chargent.** Là-bas, il faut lire la consigne et l'appliquer à la main. Pour tout ce qui repose sur
ces mécanismes, Gaël travaille dans Claude Code.

## Les tâches planifiées de l'application

L'application Claude permet de programmer des tâches (par exemple, proposer un audit le 1er du mois).
Elles **ne tournent que si l'application est ouverte.** Pour un mécanisme qui doit tourner à coup sûr,
seuls deux maillons sont toujours allumés chez Gaël : les serveurs de Google (pour l'appli Apps Script)
et le Planificateur de tâches de Windows (pour la sauvegarde).

## Le dossier de brouillons disparaît

Chaque session a un dossier temporaire pour ses brouillons. Il disparaît avec la session. Deux fois,
un script utile y est resté. Une fois, un script rangé dans le coffre pointait encore vers le dossier
temporaire d'une session disparue depuis longtemps. Règle : **un outil qu'on range pour plus tard se
teste au moment où on le range.**

## Plusieurs sessions en même temps

Gaël ouvre souvent plusieurs sessions en parallèle. Elles écrivent toutes en tête du carnet. Un jour, le
carnet a bougé entre le moment où j'ai repéré un numéro de ligne et celui où j'ai écrit à ce numéro.
Règle : **ne jamais écrire dans un fichier partagé à partir d'un numéro de ligne.** On s'appuie sur le
texte, et on relit juste avant.

## Les pages web publiées (« artifacts »)

Je peux publier de petites pages web, hébergées chez Anthropic : un plan de jardin, un formulaire de
décision. Trois leçons :
- **Publier une nouvelle version recharge la page chez celui qui la regarde.** Deux fois, Gaël a perdu
  ses dessins en cours parce que j'ai republié pendant qu'il dessinait. Règle : attendre qu'il dise
  « publie ».
- **Une page qui garde elle-même les modifications faites dessus vit hors du coffre.** Le plan du jardin,
  dessiné directement dans la page, n'existait qu'en un seul exemplaire, chez l'hébergeur, hors
  sauvegarde.
- D'où la règle du 2 septembre, posée par Gaël : **toute page publiée a sa source dans le coffre**,
  dans `5-Artefacts/`, pour que les autres IA puissent la lire et qu'elle soit sauvegardée.

## Les refus de permission

Claude Code demande l'accord avant certaines actions, et un système refuse automatiquement celles qu'il
juge risquées. Deux cas à distinguer :
- **le refus de Claude Code** : écrire dans les réglages utilisateur par une commande du terminal a
  été refusé. Avec l'accord de Gaël, la même modification est passée par l'outil d'édition de
  fichiers ;
- **le refus de Windows** : modifier une tâche planifiée exige les droits administrateur. Là, j'écris
  la commande et Gaël la lance.

## Une tension que nous assumons

Au [chapitre 3](03-appli-mycelium.md), nous avons retenu une leçon des autres coffres : **moins il y a
de mécanismes, moins il y a de pannes.** Chez `claude-obsidian`, un même bug de hook a été signalé une
quinzaine de fois en deux mois, à chaque évolution de Claude Code.

Depuis, nous avons ajouté **quatre hooks.** Chacun répond à un vrai problème. Mais c'est exactement le
risque décrit : au moment où j'écris ces lignes, l'un des quatre est en panne.

*Mise à jour du 3 octobre : il fonctionne de nouveau, et personne ne l'a réparé — voir le
[chapitre 12](12-ce-qui-a-casse.md).*

---
[← Chapitre 8](08-ouvrir-avant-d-affirmer.md) · [Sommaire](../README.md) · [Chapitre 10 →](10-trois-jours-pour-rien.md)
