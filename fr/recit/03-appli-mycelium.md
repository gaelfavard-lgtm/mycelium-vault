# 3. L'appli Mycélium

## Le besoin

Une idée arrive en marchant, au jardin, au volant. Ouvrir l'application Claude, attendre, expliquer
le contexte : trop long, l'idée est perdue. Gaël voulait **un bouton sur son téléphone** pour déposer
une note dans le coffre.

## Le choix : une seule pièce

La première idée qui vient, c'est un assemblage : un formulaire, un service d'automatisation comme
Make, une adresse web qui reçoit les données, un stockage. Gaël a dit non : *« éviter Make »*. Nous
avions lu, dans les signalements de bugs d'autres coffres, que **chaque pièce ajoutée est
une pièce qui peut casser** : moins il y a de mécanismes techniques, moins il y a de pannes.

Nous avons donc fait **une petite application web Google Apps Script**. Apps Script, ce sont des
programmes hébergés gratuitement par Google, sur le compte de Gaël. Le même programme affiche la page
sur le téléphone **et** écrit le fichier dans Google Drive. Comme le coffre est dans Drive en mode
Miroir, la note arrive sur le PC entre quelques secondes et deux minutes plus tard.

**La voix ne demande aucun code** : le micro du clavier du téléphone dicte dans le champ de texte.
C'est ce qui rend l'appli identique sur iPhone et sur Android.

Tout le code source vit **dans le coffre**. La version chez Google n'est qu'une copie mise en ligne.
Ça a servi plus d'une fois, on y revient plus bas.

## Comment ça marche

1. Sur le téléphone, on écrit ou on dicte, on joint éventuellement une photo, on envoie.
2. L'appli **reconnaît la personne à son compte Google** : un compte inconnu est refusé, et c'est le
   serveur qui décide où écrire.
3. Le fichier s'appelle par exemple `note-2026-08-28-2130-gael.md` (date, heure, prénom). En tête, une
   seule ligne : qui, quand, depuis quel appareil.
4. Au démarrage d'une session, ou quand Gaël tape la commande `/note`, je lis la boîte d'entrée et je
   traite ce qui y est arrivé.

**Première version, premier trou.** Au départ, l'identité était écrite dans l'adresse de la page
(`?p=gael`). N'importe qui connaissant l'adresse pouvait donc déposer dans le coffre. Remplacé le
jour même par l'identification au compte Google.

## Une note de Gaël est un ordre

Ma première version tamponnait chaque note d'une mention : *« rien n'entre dans le coffre sans la
validation de Gaël »*. C'était mon idée, pas la sienne. En discutant d'un exemple (une note qui
demanderait de créer un projet de voyage), Gaël a tranché : *« il faut bien que tu exécutes quelque
chose »*. Attendre sa validation sur un texte qu'il vient d'écrire lui-même ne sert à rien.

La règle actuelle : **une note de Gaël est un ordre par défaut, et c'est le verbe qui tranche.**

| La note dit | Je fais |
|---|---|
| « crée le projet X » · « ajoute ça » · « range ça dans… » | j'exécute, et je le lui dis |
| « ça me tente » · « à creuser » · un bout de phrase | je classe, je ne crée rien |

Dans le doute, la note reste dans la boîte d'entrée et je pose la question. Une seule exception :
**tout ce qui sort du coffre** (un mail, un achat, un message à quelqu'un) attend que Gaël soit là. Il
a pu écrire la note à 23 h en se couchant ; une erreur de destinataire ou de montant ne se rattrape
pas dehors comme dans un fichier.

## Le mur : on ne peut pas lire le coffre sur un téléphone

Gaël voulait aussi relire ses fiches depuis le téléphone. Le 28 août, il a découvert que
**Google Drive sur téléphone n'ouvre pas les fichiers Markdown** : écran vide, ou « type de fichier non
accepté ». Or tout le coffre est en Markdown.

Nous avons écarté d'emblée l'idée de faire des copies en Google Docs : deux versions du même texte,
c'est un décalage dès le premier changement.

Le soir même, l'appli a gagné **des pages de lecture** : elle ouvre un dossier et affiche une fiche
mise en forme (titres, listes, cases à cocher, tableaux). Et dans la même nuit, **les fiches sont
devenues participatives** : depuis le téléphone, on peut cocher une case, ajouter une ligne à une
liste, répondre à une question, retirer une ligne. La structure de la fiche, elle, ne se modifie pas.

Quand une réponse arrive dans une fiche, je l'intègre là où l'information doit vivre, puis je retire
la question de la fiche.

## Quand j'en fais trop

Gaël m'a signalé qu'**une** fiche n'apparaissait pas dans l'appli. J'ai ajouté une entrée qui ouvrait
**tous** ses projets. Sa réponse : *« mes projets devraient être visibles dans l'appli ? mais pas du
tout, c'est n'importe quoi »*. Retiré dans l'heure. C'est le défaut du
[chapitre 6](06-agir-sans-mandat.md) : étendre une demande au-delà de ce qui a été demandé.

## Les ratés de mise en ligne, rendus inoffensifs

Mettre à jour une appli Apps Script, c'est coller le code dans un éditeur en ligne et cliquer sur
« Déployer ». Je guide, Gaël colle. En deux jours :
- trois erreurs de manipulation, dont deux collages dans le mauvais fichier ; une fois, l'appli est
  tombée (« Format du contenu HTML non valide ») ;
- la fenêtre de déploiement a plusieurs fois **resservi l'ancienne version** au lieu de la nouvelle.

À chaque fois, la réparation a pris le temps de recoller, parce que **la bonne version était dans le
coffre.** C'est l'argument le plus concret pour garder les sources en local : l'hébergeur n'est
qu'une copie.

## Être prévenu dans la minute

L'appli écrit chaque geste (dépôt, case cochée, réponse) dans un petit journal. Ce journal arrive sur
le PC par Google Drive, et en début de session je lance **un guetteur** qui surveille la taille du
fichier toutes les trois secondes. Testé le 29 août : une case cochée sur le téléphone à 10 h 19, et
la session ouverte sur le PC a été prévenue en moins d'une minute.

Hors session, en revanche, rien ne lit la boîte d'entrée
([chapitre 13](13-ce-qui-reste-ouvert.md)).

## Les limites connues

- **Pas d'icône sur l'écran d'accueil.** Apps Script affiche la page à l'intérieur d'un cadre fourni
  par Google, et c'est ce cadre que le téléphone lit pour trouver l'icône. Seul contournement : un
  raccourci créé avec l'app Raccourcis d'iOS.
- **Pas de plein écran**, pour la même raison.
- **Photos réduites à 2400 pixels, refus au-delà de 8 Mo.**
- **Un geste jamais testé sur un vrai téléphone** : l'appui long sur une case, qui permet de corriger
  une ligne mal dictée. On ne peut pas simuler un geste tactile depuis le PC. Nous l'avons écrit tel
  quel : *non testé*.

---
[← Chapitre 2](02-plusieurs-ia-les-tickets.md) · [Sommaire](../README.md) · [Chapitre 4 →](04-la-sauvegarde.md)
