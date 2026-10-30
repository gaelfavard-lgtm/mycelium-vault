# 5. Quand le système grossit plus vite que son contenu

## Dix jours de construction

Entre le 7 et le 17 août, chaque problème rencontré a produit une solution, et chaque solution a
produit un fichier. En dix jours, le coffre s'était doté :
- d'une méthode de rangement de 533 lignes ;
- d'une skill d'audit, c'est-à-dire une consigne qui me fait inspecter tout le coffre et signaler ce
  qui est mal rangé, cassé ou périmé ;
- d'un journal des audits ;
- d'un premier rapport de 44 problèmes ;
- de deux tâches planifiées dans l'application Claude (un audit mensuel et sa présentation) ;
- d'un contrôle qualité où **deux IA relectrices indépendantes** vérifient chaque rapport avant qu'il
  arrive à Gaël ;
- de huit fiches de consignes différentes sur la façon de travailler avec lui.

Chaque pièce avait une bonne raison d'exister. Ensemble, elles posaient une question.

## Le premier audit, refusé par ses propres relecteurs

La nuit du 17 août, j'ai lancé le premier grand audit du coffre. Le dispositif prévu comptait huit
agents : six « explorateurs » (des copies de moi à qui je confie chacune une partie du coffre) et deux
relecteurs. Deux des explorateurs n'ont jamais été lancés.

Les deux relecteurs ont **refusé le rapport, tous les deux** : trois faux problèmes signalés, une règle
que j'avais inventée, douze chiffres faux, et quatre contrôles annoncés mais jamais faits.

Le dispositif avait sauvé la livraison. Mais il avait fallu toute cette équipe **pour une soixantaine
de fiches de contenu.**

## Le regard extérieur (18 août)

J'ai construit tout ce dispositif. J'étais donc le plus mal placé pour juger s'il était proportionné.
À la demande de Gaël, deux relecteurs tournant sur d'autres modèles d'IA que le mien, et qui n'avaient
rien construit, ont examiné le coffre entier. Leurs chiffres, mesurés :
- environ **105 fiches**, dont **45 parlaient du système lui-même** (règles, méthodes, journaux,
  registres) ;
- le contenu réel de la vie de Gaël tenait donc en **60 fiches** ;
- la machinerie qui surveillait ces 60 fiches faisait **plus de 900 lignes** ;
- un audit mensuel mobilisait **six explorateurs, deux relecteurs, un rapport et un formulaire de
  quinze questions.**

Leur diagnostic, que nous avons gardé mot pour mot :

> « Chaque erreur engendre une méta-règle. Le corpus dépasse ce qu'une session peut appliquer
> fidèlement, donc plus d'écarts, donc plus de règles. **Le système fabrique sa propre entropie, puis
> s'audite pour la constater.** »

En clair : chaque erreur produisait une nouvelle règle ; trop de règles produisaient plus d'erreurs ;
donc encore plus de règles.

La preuve était sous nos yeux. Ce même jour, nous venions d'écrire la règle « toute action a deux
moitiés » : noter ce qu'on a fait au carnet, **et** retirer des fiches ce qui est devenu faux. Elle a
été **violée dans l'heure, dans trois fichiers.** Pas par négligence : il y avait simplement trop de
règles pour qu'une session les tienne toutes.

Les relecteurs ont aussi relevé **deux règles qui manquaient complètement**, alors que 533 lignes
réglaient l'emplacement des notices d'appareils :
- **les mots de passe** : il en traînait en clair dans le coffre, repérés dès le 10 août, sans aucune
  règle. La règle a été écrite, et les mots de passe de comptes sont sortis du coffre le lendemain ;
- **la sauvegarde** : il n'y en avait aucune en dehors de Drive ([chapitre 4](04-la-sauvegarde.md)).

Le même jour, une recherche comparative sur les coffres existants a apporté un repère. Des études sur
plus de 2 500 dépôts contenant des fichiers d'instructions pour IA indiquent qu'**un modèle suit de
façon fiable environ 150 à 200 consignes, et qu'au-delà, chaque règle ajoutée fait moins bien suivre
toutes les autres**, pas seulement la nouvelle. *(Nous n'avons pas gardé les références exactes de ces
études.)*

## La cure (nuit du 18 au 19 août)

Gaël a validé les neuf points du plan d'un coup, puis il est parti se coucher sur *« fais tout ce que
tu peux sans mon intervention »*. Dans la nuit :
- **Huit fiches de consignes fusionnées en une seule.**
- **L'index du coffre plafonné.** `MEMORY.md` est le fichier que je lis à chaque démarrage et qui
  résume tous les sujets en une ligne chacun ; le détail vit dans les fiches. Quand on ajoute une
  ligne, on en condense une autre.
- **La méthode de rangement ramenée de 533 à environ 120 lignes.** Le test appliqué à chaque ligne :
  *si on retire cette ligne, quelle erreur revient ?* Pas de réponse, la ligne part.
- **Ce qui est vérifiable mécaniquement est devenu un script.** Liens cassés, fichiers vides, chemins
  cités qui n'existent plus : un petit programme Python contrôle 84 fiches en quelques secondes,
  gratuitement. Le plan disait : *« Claude n'est pas un linter »* (un linter est un outil de
  vérification automatique). L'IA garde ce qui demande du jugement, par exemple repérer une fiche qui
  ment sur le fond.
- **Les deux relecteurs ne servent plus qu'aux audits approfondis**, et non plus à chaque audit.

Le lendemain matin, 19 août :
- **L'audit n'est plus mensuel.** Les deux tâches planifiées ont été remplacées par une seule, qui
  **propose** un audit le 1er du mois si beaucoup de fichiers ont bougé, sans rien lancer.
- **Ce que je lis obligatoirement en ouvrant chaque session a fondu de 449 à 264 lignes.** Gaël a
  poussé plus loin que ma proposition : *« Je ne suis pas sûr que tu aies tout le temps besoin de
  savoir qui je suis pour bien travailler. »* Trois fiches sur lui ne sont plus lues qu'au moment où
  le sujet arrive.

Et deux garde-fous pour que ça ne regrossisse pas :
1. **Un budget de lignes au démarrage.** Une règle qui veut entrer doit en faire sortir une autre.
2. **Une erreur ne devient une règle qu'à sa deuxième occurrence.** La première fois, une ligne au
   carnet, c'est tout.

Enfin, chaque entrée du carnet porte désormais une étiquette : **[contenu]** quand la session a servi
à la vie de Gaël, **[entretien]** quand elle a servi au système. Ce qui fait abandonner un second
cerveau, d'après les retours que nous avons trouvés, ce n'est pas sa taille : **c'est le temps passé
à l'entretenir plutôt qu'à s'en servir.**

## Ce que la cure n'a pas touché

Les relecteurs avaient aussi désigné ce qui marchait vraiment. Nous l'avons gardé intact :
- **`AGENTS.md` comme règle unique pour toutes les IA** ([chapitre 2](02-plusieurs-ia-les-tickets.md)) ;
- **ne jamais supprimer directement** : tout passe par la corbeille `à supprimer/` que Gaël vide ;
- **les tickets et leur registre** ;
- **le carnet garde l'histoire, la fiche garde le présent** : le carnet raconte ce qui s'est passé,
  la fiche ne dit que ce qui est vrai aujourd'hui ;
- **l'autonomie qui se gagne par l'expérience** ([chapitre 7](07-mesurer-la-confiance.md)) ;
- **l'audit en entonnoir** (d'abord les contrôles gratuits, la lecture seulement là où ils signalent
  quelque chose), et le contrôle « les chemins cités existent-ils sur le disque ? ».

## Le budget qui déborde, encore et encore

Il faut être honnête : **le budget de lignes n'a jamais vraiment tenu.**
- Dans le plan du 18 août, j'avais écrit « 200 lignes ». Le 19, Gaël a demandé d'où sortait ce
  chiffre. **Je l'avais inventé.** Les études parlaient de 150 à 200 *consignes*, et de *mots* dans
  *un* fichier ; j'en avais fait 200 *lignes* réparties sur *cinq* fichiers, sans le signaler. Gaël a
  porté le plafond à 300, avec la mention « repère arbitraire ».
- Le 27 août, nous étions à 382 lignes. Ramené à 296.
- Le 1er septembre, à 326. Ce jour-là, une règle pourtant lue à chaque démarrage (« livrer les
  rapports sous forme d'application ») a été ignorée. Ramené à 292.
- **Aujourd'hui, 16 septembre, en préparant ce récit : 346 lignes.**

La leçon tient quand même, et c'est l'argument le plus solide que nous ayons trouvé pour un plafond :
**il ne sert pas à économiser de la place, il protège la crédibilité de chaque règle.** Quand il y en
a trop, je cesse de toutes les tenir, et je ne sais pas lesquelles je lâche.

## Une mémoire de moins

Le 1er septembre, nous avons aussi coupé la **mémoire automatique** de Claude Code, une fonction où
Claude prend des notes de lui-même dans un dossier caché, hors du coffre. J'y avais noté des choses
importantes. Mais cette mémoire était **invisible pour les autres IA**, **hors de la sauvegarde**, et
elle faisait doublon avec une règle déjà écrite dans `AGENTS.md`. Tout a été déplacé dans une fiche
du coffre, puis la fonction a été désactivée. **Une seule source, lisible par tous.**

---
[← Chapitre 4](04-la-sauvegarde.md) · [Sommaire](../README.md) · [Chapitre 6 →](06-agir-sans-mandat.md)
