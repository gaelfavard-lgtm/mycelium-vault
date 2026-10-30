# 4. La sauvegarde : le filet qui ne tenait pas

## Ce qu'on voulait

Tout le coffre vit dans Google Drive, en mode Miroir : une copie sur le PC, une copie dans le cloud,
synchronisées en permanence. On pourrait croire que c'est une sauvegarde. **Ça n'en est pas une.** Si
Gaël supprime une fiche par erreur, ou si j'en abîme une, l'erreur est recopiée partout en quelques
secondes. Le Miroir protège d'un disque qui meurt, pas d'une erreur.

Le 18 août, les relecteurs extérieurs l'ont écrit noir sur blanc ([chapitre 5](05-la-cure.md)) :
plusieurs IA écrivaient dans le coffre, et **il n'existait aucune sauvegarde en dehors de Drive.**

Nous avons choisi **git**, l'outil des développeurs pour garder toutes les versions d'un dossier. Il
est libre, gratuit, et n'appartient à personne : si Anthropic ou Google disparaissaient demain, la
sauvegarde resterait lisible. Trois décisions :
- **le dépôt git est en dehors de Drive**, parce qu'un historique git dans un dossier synchronisé
  finit par se corrompre : c'est documenté chez d'autres coffres ;
- **on ne sauvegarde que le texte** (moins d'un mégaoctet), pas les photos et les PDF, que git
  recopierait en entier à chaque version ;
- **c'est Windows qui lance la sauvegarde**, avec son Planificateur de tâches, et **pas l'IA**. La
  sauvegarde doit marcher même sans Claude, sans abonnement, sans session ouverte. Nous avons aussi
  écrit un guide pour que Gaël puisse **restaurer sans moi**.

## Premier déboire : six corrections pour rien (19 août, matin)

Le script de sauvegarde (un fichier `.bat`, le format de script le plus simple de Windows) se
bloquait. J'ai proposé une correction, puis une autre : **six essais, six échecs.** À chaque fois une
hypothèse plausible, jamais la recherche de la vraie cause. Les vraies causes, trouvées à la fin :
- le fichier avait été enregistré avec des **fins de ligne au format Linux**, que Windows lit de
  travers : il mange un caractère par ligne, en silence. Résultat, l'historique git s'est créé **dans
  le coffre**, ce que je venais moi-même d'interdire ;
- une **pause en fin de script** attendait qu'on appuie sur une touche. Lancé automatiquement, le
  script attendait donc pour toujours ;
- j'avais demandé à Gaël de vérifier si Python était installé, puis j'étais passé à autre chose sans
  la réponse. Deux fois.

Et c'est Gaël qui a remis le diagnostic sur ses rails, deux fois : *« la sauvegarde manuelle a
marché »* (donc le script est bon, cherche ailleurs), puis *« ça se bloque aussi en déclenchement
manuel »* (donc le déclencheur n'y est pour rien, alors que je proposais justement de le changer).

Nous en avons tiré **la règle des deux échecs** :

> Quand une correction échoue deux fois, on arrête de corriger. On va chercher le fait qui manque :
> un numéro de version, un message d'erreur, un journal. Et on attend la réponse.

## Deuxième déboire : le journal qui mentait (19 août, fin de matinée)

À 10 h 31, Gaël a lancé la sauvegarde à la main : elle a réussi. **Le script fonctionnait.**

À 10 h 56, j'ai lancé moi-même la sauvegarde depuis mon bac à sable, sur son vrai dépôt. J'y ai laissé
un petit fichier de verrouillage, et à partir de là git a refusé **tous** les enregistrements : les
miens, les siens, ceux de la tâche automatique. J'ai ensuite passé une heure à chercher pourquoi « ça
ne marchait pas ». **C'était ma faute.**

Pire : **le journal de la sauvegarde écrivait « OK » à chaque passage**, parce que le script ne
vérifiait pas si git avait réussi. J'avais construit exactement l'instrument qui cachait ma propre
erreur.

Bilan honnête, écrit au carnet ce jour-là : le premier script avait peut-être fonctionné depuis le
début. Gaël ne voyait pas qu'il se terminait, parce que l'écran du Planificateur ne se rafraîchit pas
tout seul (il faut appuyer sur F5).

Ce qui a changé :
- le script a été réécrit en Python. Il lit la réponse de git et écrit **« ECHEC » avec la raison**
  quand ça ne passe pas, et il retire lui-même un verrou oublié depuis plus de cinq minutes. Au
  passage, le Planificateur coupe la commande au premier espace, et le chemin de Python n'en contient
  pas ;
- Gaël a tranché : **aucune IA ne touche plus au dépôt de sauvegarde.** C'est sa sauvegarde, pas un
  terrain d'essai ;
- la sauvegarde a été vérifiée **en ouvrant le dépôt et en relisant les fichiers**, pas en croyant le
  message à l'écran.

Nous l'avons résumé ainsi : **un journal qui ment est pire que pas de journal.**

## Troisième déboire : six jours sans sauvegarde, sans que personne le sache

Le 27 août, lors d'un audit, nous avons lu le journal de sauvegarde : quatre lignes le 19 août, huit
le 26… **et rien entre les deux.** Du 20 au 25 août, pas un seul point de restauration.

La cause était banale :
- la tâche démarrait **à l'ouverture de la session Windows**, puis se répétait toutes les heures tant
  que cette session restait ouverte ;
- or le portable de Gaël **se met en veille**. Pendant la veille, les échéances passent sans que rien
  ne se lance ;
- et la case **« exécuter la tâche dès que possible après un démarrage planifié manqué »** était
  décochée. Rien n'était jamais rattrapé.

Réparation le 27 août : la case de rattrapage cochée, et un deuxième déclencheur quotidien. Le
29 août, Gaël a fixé les horaires actuels : **à l'ouverture de session, à 10 h et à 21 h.** Une
vérification de dix secondes est écrite dans le guide : dans le Planificateur, la colonne « Prochaine
exécution » ne doit jamais être vide. Avant la réparation, elle l'était.

Un détail qui dit bien la répartition des rôles : **je ne peux pas modifier une tâche planifiée**,
Windows exige les droits administrateur. J'ai écrit la commande, Gaël l'a lancée.

## Ce que ça nous a appris

Le 19 août, le jour même où nous avons installé la sauvegarde, nous avions lu les signalements ouverts
sur un projet voisin, `claude-obsidian`. La panne la plus grave qu'on y trouvait : **le filet de
sécurité qui s'éteint sans bruit.** Chez eux, un mécanisme échouait sur Mac, et par ricochet la
sauvegarde git automatique s'arrêtait sans rien dire. Un utilisateur pouvait travailler des jours en
se croyant protégé.

Nous l'avions lu. Nous l'avions écrit dans le coffre. **Et notre sauvegarde s'est arrêtée dès le
lendemain, sans que nous le voyions pendant une semaine.**

C'est peut-être la leçon la plus importante de ce récit : **une leçon écrite ne protège de rien.** Ce
qui protège, c'est un mécanisme qui la tient, et une trace visible à chaque passage, réussi ou raté.
Un filet qui peut s'éteindre en silence est pire que pas de filet, parce qu'on arrête de vérifier.

## Ce qui n'est toujours pas fait

**Les fichiers lourds** (photos, PDF, plans) n'ont aucune copie sur un disque externe.

---
[← Chapitre 3](03-appli-mycelium.md) · [Sommaire](../README.md) · [Chapitre 5 →](05-la-cure.md)
