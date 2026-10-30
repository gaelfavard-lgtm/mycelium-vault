# 8. Ouvrir avant d'affirmer

En relisant le carnet pour écrire ce récit, un motif revient plus que tous les autres. **La plupart de
mes erreurs ne sont pas des erreurs de calcul ou de connaissance. Ce sont des affirmations que je n'ai
pas vérifiées alors que la vérification était à portée de main.** J'ai déduit au lieu de regarder.

Le 7 septembre, trois affirmations de ce genre dans la même journée. La parade tient en une ligne :
**ouvrir avant d'affirmer.** Voici à quoi ça ressemble concrètement.

## Déduire au lieu de regarder

- **Des prix de mémoire.** Le 10 août, j'ai donné trois fourchettes de prix pour du matériel
  informatique. Les trois étaient fausses. Règle : **aucune décision d'achat sur un prix que je n'ai
  pas vérifié dans la session**, avec la source et la date.
- **Un lien d'après les résultats de recherche.** J'ai donné un lien vers une boutique en ligne sans
  ouvrir la page. La boutique était fermée. Règle : ne donner un lien qu'après avoir ouvert la page.
- **Le contenu d'une colonne d'après son nom.** Dans une base de données, j'ai affirmé ce que
  contenait une colonne en lisant son intitulé, sans ouvrir la table.
- **Des images d'après leur nom de fichier.** J'ai créé des fiches d'articles en me fiant aux noms des
  photos, sans les regarder. Les noms ne correspondaient pas au contenu.
- **Un appareil d'après sa notice.** « La documentation ne décrit pas cette fonction, donc l'appareil
  ne l'a pas. » C'était faux.

## Croire un document plus vieux que la réalité

- **Une transcription prise pour la situation actuelle.** Le 11 septembre, j'ai annoncé qu'un mail
  « n'était jamais parti » en lisant l'extrait d'une ancienne session. Il était parti, et il avait même
  reçu une réponse. Règle ajoutée : **une transcription dit ce qui s'est dit, pas ce qui s'est fait.**
- **Des tickets périmés.** Le 8 septembre, trois fois dans la journée, ce qu'un ticket annonçait ne
  correspondait plus à la réalité : des fichiers à renommer qui n'existaient pas, un élément « à
  créer » qui existait déjà, une automatisation « jamais publiée » qui tournait. **Un ticket dit ce
  qu'il fallait faire au moment où il a été écrit, pas ce qu'il reste à faire.**
- **Un indicateur mal lu.** Pour cette même automatisation, un champ vide dans la réponse de l'outil
  m'avait fait conclure qu'elle n'avait jamais été publiée. En réalité, ce champ vide voulait dire
  « la version publiée est identique au brouillon ». Et même bien lu, il ne disait rien de ce que
  contenait ce brouillon, qui était une version cassée. **Un statut dit l'état de la publication, pas
  ce qui est publié.**
- **Une fiche qui ment.** Pendant trois semaines, une fiche a demandé de supprimer des données de test
  qui l'avaient déjà été : le carnet l'avait noté, la fiche n'avait pas été mise à jour. Et le
  12 septembre, une question marquée « à clarifier » dans une fiche avait sa réponse **dans la boîte
  mail de Gaël depuis cinq semaines.**

C'est de là que vient la règle du coffre : **le carnet garde l'histoire, la fiche garde le présent.**
Toute décision doit remonter dans la fiche concernée dans la même session. Et **ce qui tourne
vraiment** (une automatisation, une appli) **se vérifie à la source**, pas dans la fiche qui en parle.

## Un contrôle qui n'a rien contrôlé

Ce sont les erreurs les plus traîtres, parce qu'elles ont l'air d'une vérification :
- **La liste filtrée.** Le 5 septembre, j'ai vérifié qu'un article n'existait pas dans une liste… qui
  était filtrée. Il existait. J'ai créé un doublon. *Conclure « ça n'existe pas » d'une liste filtrée,
  c'est conclure de rien.*
- **Le mauvais champ.** Le lendemain, un contrôle de doublons a répondu « aucun doublon » sur 464
  articles. Il lisait le mauvais champ dans la réponse de l'outil : il a comparé 464 noms **vides**.
  Règle : **vérifier qu'un contrôle a bien vu des données avant de croire son verdict.**
- **Trop tôt.** J'ai jugé un test d'automatisation au bout d'une seconde. L'automatisation met environ
  une minute à se déclencher. *Un contrôle lancé trop tôt ne prouve rien, dans un sens comme dans
  l'autre.*
- **Le correctif pas relancé.** Le 1er septembre, j'ai corrigé le script d'audit du coffre pour
  supprimer huit fausses alertes. Je ne l'ai relancé qu'après : il en produisait sept nouvelles. **Un
  correctif non relancé n'est pas un correctif.**
- **Le premier message d'erreur.** J'ai déclaré un PDF « illisible » au premier échec. Il échouait avec
  une option ; sans cette option, il se lisait très bien. *Un outil qui échoue avec une option n'a pas
  échoué tout court.*

Et une règle simple pour les cas où je ne trouve rien : **« je n'ai pas trouvé » ne veut pas dire « ça
n'existe pas ». La seule conclusion honnête est « je ne sais pas ».**

## Imposer mes mots

Une variante moins visible. Pour classer le stock d'une activité artisanale, j'ai choisi un mot pour un
type d'article, et je l'ai installé partout : dans une consigne, dans une table, à la fin de noms de
fichiers. **Sans demander à Gaël quel mot il employait.** Ce qu'il m'a reproché n'était pas le mot,
mais de l'avoir installé sans lui demander. Il a fallu quatre arbitrages en trois jours pour revenir
au terme de départ.

Règle : **demander le mot avant de le graver.** Un mot installé dans les fichiers et les scripts coûte
très cher à retirer.

## Donner des leçons à quelqu'un qui connaît son métier

Dernière forme du même défaut : supposer ce dont l'autre a besoin. Gaël est artisan. Il travaille avec
des machines, de l'électricité, du feu. J'ai longtemps ajouté des avertissements de sécurité et des
« je te recommande de » qu'il n'avait pas demandés. Le 25 août, sur le dessin d'un conduit de poêle,
j'ai ajouté d'office une zone de sécurité. Sa réponse : *« ça c'est mon problème, toi tu dessines. »*

La consigne actuelle est nette : **pas d'avertissement ni de conseil de prudence sans demande.** Un
fait chiffré reste bienvenu (une cote, une distance, une valeur de fiche technique) : c'est de la
donnée. Ce qui est banni, c'est ce qui vient après le chiffre : le jugement, l'avertissement, la
solution recommandée. **Donner la mesure, et se taire.**

## Le point commun

Toutes ces erreurs ont la même forme : **une information plausible a pris la place d'une information
vérifiée**, alors que la vérification coûtait presque toujours moins cher que l'erreur. Le relevé fait
foi, pas la déduction.

---
[← Chapitre 7](07-mesurer-la-confiance.md) · [Sommaire](../README.md) · [Chapitre 9 →](09-pieges-de-claude-code.md)
