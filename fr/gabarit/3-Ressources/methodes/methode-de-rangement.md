# Méthode de rangement

**Référence unique du classement.** Toute nouvelle règle de rangement s'écrit ici, pas ailleurs.
Test pour chaque ligne : **« si on la retire, quelle erreur revient ? »** Pas de réponse → elle sort.

## 1. Les zones

Classement par **actionnabilité**, pas par thème. La question qui tranche : **« dans quel contexte
est-ce que j'aimerais retomber sur ce fichier ? »** Un fichier = une idée.

| Zone | Question filtre |
|---|---|
| `0-Inbox` | Le sas + la file des tickets. Rien n'y stagne. |
| `1-Projets` | Un début et une fin. « Ça fait avancer un livrable ? » Fiche obligatoire, objectif et statut. |
| `2-Casquettes` | Responsabilité continue. Fiche de tête obligatoire. |
| `3-Ressources` | « Utile un jour ? » Sous-dossiers thématiques permis à l'intérieur. |
| `4-Archives` | « Terminé mais à conserver ? » Nom du dossier = le lieu ou le bien. |
| `_contexte` | Décrit le système, pas le travail. |
| `_prompts` | Les procédures répétables, lisibles par toute IA. |
| `a-supprimer` | La corbeille que seul l'humain vide. |

## 2. Les critères d'arbitrage

1. **Qui s'en sert aujourd'hui ?** L'usage vivant décide, pas l'étiquette.
2. **Ranger pour le déménagement suivant** : un chantier = un dossier qui part en archives d'un bloc.
3. **Qu'est-ce que la correction fait gagner ?** Si la réponse est « ça respecte la règle », ce
   n'est pas un écart.
4. **Un fichier à deux places possibles** : un emplacement + des wikilinks. Ni dupliquer, ni déplacer.
5. **Doublons** : repérage par nom + taille, **comparaison avant tout retrait**, jamais à l'œil.
6. **Nommage** : parlant ; proscrits en zone active : `IMG_*`, `Sans titre`. Après tout renommage :
   grep des occurrences, dans le même geste. Ne rien renommer dans `4-Archives`.
7. **Suppression : jamais en direct** — déplacer vers `a-supprimer/`.
8. **Une tâche sans échéance** = une ligne dans une liste, pas un projet, pas un dossier.

## 3. Pourquoi les fiches mentent — les règles anti-dérive

Le disque est la vérité ; une description se périme.
1. **N'écrire au présent que ce qui existe** — le prévu va dans « À faire ».
2. **Un déplacement n'est fini qu'après le grep** des fiches qui citent l'ancien chemin.
3. **Ne jamais recopier un nom de fichier** depuis une mémoire : lire le disque.
4. **Toute action a deux moitiés** : consigner le nouveau, retirer ce qui devient faux.
5. **Une certification se date** (« vérifié le … ») ou se retire.
6. **Ce qui entre sans passer par l'humain se signe** — la signature est un drapeau : « ceci n'a
   pas été soumis ».
7. **Une observation se date dans le texte** — l'horodatage d'un fichier se réécrit à la moindre
   copie, et les photos perdent souvent leur date en route.
8. **Un état porte sa date** : « en cours (15/01) ». Un fait est intemporel, daté, ou renvoyé à sa
   source vivante.

## 4. L'audit

**Mécanique** (script `.claude/scripts/audit-mecanique.py`, rapport seul) : chemins cités vs
disque, wikilinks cassés ou ambigus, racine qui stagne, fichiers vides, doublons de nom, doublons
de synchronisation (`x (1).md`), états non datés, mémoire cachée de Claude Code.
**Jugement** (une passe IA) : le prévu et le fait qui cohabitent, fiches fourre-tout (> ~300
lignes), fiches qui se contredisent, projets qui dorment (3 mois pour un petit, 1 an pour un gros :
la question est « où en es-tu ? », pas « faut-il archiver ? »).
Fréquence suggérée : courant chaque semaine, de fond chaque mois. Ce que chaque audit apprend va au
carnet.

## 5. Anti-inflation

1. **Budget de démarrage : 300 lignes** (AGENTS + CLAUDE + MEMORY + les 2 fiches de profil).
   Toute règle qui veut y entrer en fait sortir une autre.
2. **Une erreur ne devient une règle qu'à la deuxième occurrence.**
3. **Comment on coupe : 70 / 30.** L'IA garde les 70 % qu'elle juge intouchables, et présente les
   30 % restants **par blocs de sens**, chacun avec ce que sa disparition ferait perdre. L'humain
   tranche bloc par bloc. Rendre 30 % au hasard, c'est lui rendre le problème entier.
4. **On pose des règles, pas des cas** : le carnet garde le cas, la méthode garde la règle.
