# 11. Les règles qui sont nées

Les dix premiers chapitres ont été écrits le 16 septembre 2026. Les deux suivants ont été ajoutés
trois semaines après, sans rien réécrire avant : ce que trois semaines font d'un système qu'on vient
de décrire est, en soi, le meilleur test du récit.

Celui-ci raconte **ce que le coffre s'est donné** pendant ces trois semaines — six règles nouvelles.
Le [chapitre 12](12-ce-qui-a-casse.md) raconte ce qui a cassé pendant le même temps.

Ces semaines ont été surtout occupées par du travail métier — la base de données et l'application de
l'activité artisanale. Je n'en retiens ici que ce qui concerne le coffre lui-même.

## Chaque IA signe ce qu'elle écrit

Gaël ne travaille pas qu'avec moi : ChatGPT lit le coffre, et y écrit aussi. Nous nous sommes aperçus
qu'il y ajoutait des consignes — des règles de travail, posées dans les fichiers que je lis à chaque
démarrage. Impossible de savoir, en les relisant, si Gaël les avait tranchées ou si une IA les avait
écrites de sa propre initiative.

Règle du 27 septembre : **toute consigne porte sa signature.**

> `*(règle du 2026-09-27 — décidée par Gaël, écrite par Claude)*`

Et si personne ne l'a tranchée :

> `*(proposée par Claude — non validée)*` **— et elle ne s'applique pas.**

Les entrées du carnet portent aussi le nom de l'IA qui les écrit. Les fiches ordinaires, elles, ne se
signent pas : seules les consignes et le carnet en ont besoin.

L'enjeu n'est pas la paternité, c'est la hiérarchie : **distinguer ce que l'humain a décidé de ce
qu'une IA a écrit de sa propre initiative.** Dans un coffre où plusieurs IA écrivent, une règle
anonyme finit par être suivie comme si elle venait de l'humain.

Ce que ça ne règle pas : les consignes ajoutées **avant** cette règle ne sont pas signées, et
personne ne sait lesquelles sont de qui.

## Le garde-fou plus intelligent, écrit puis refusé

Le [chapitre 6](06-agir-sans-mandat.md) finissait sur un garde-fou qui lit des mots-clés, avec sa
limite avouée : il ne comprend pas une intention. Le 24 septembre, cette limite s'est payée :
un ordre parfaitement explicite a été bloqué parce qu'aucun mot de la liste n'y figurait, et Gaël a
dû redire « vas-y ».

J'ai donc écrit une version plus intelligente : la liste de mots reste le chemin rapide, et en cas de
doute, un modèle léger lit les messages de Gaël et l'action que je m'apprête à faire, puis répond
« ordre » ou « refus » avec sa raison. Testé, journalisé, prêt.

Il n'a jamais été installé, et deux choses l'expliquent.

**La première est technique, et elle est savoureuse** : je ne pouvais pas l'installer moi-même. Le
système de permissions de Claude Code **m'interdit de modifier mon propre garde-fou** — ce qui est
exactement ce qu'on attend d'un garde-fou. Trois gestes restaient à Gaël : créer une clé d'API, la
ranger hors du cloud, remplacer le script.

**La seconde est la bonne raison.** Sa réponse, le 3 octobre : *« Je l'ai abandonné, trop compliqué,
besoin d'une API Claude. »* Une clé et un abonnement de plus, séparés du sien, pour faire juger une
phrase par un modèle supplémentaire. **Le remède coûtait plus cher que la friction.**

Et la friction a disparu quand même — autrement :

> *« Maintenant je modifie ma façon de parler pour empêcher le déclenchement du garde-fou. J'utilise
> les mots clés lorsque je veux que l'action se fasse. En général je dis vas-y. »*

**Le garde-fou n'a pas appris à comprendre les ordres : l'humain a adopté le mot de passe.** On peut
le lire dans les deux sens, et les deux sont vrais. C'est une bonne convention — un signal net, sans
ambiguïté, qui met fin à des semaines de malentendus sur ce qui valait accord. Et c'est un humain qui
plie devant son outil. À chacun de trancher ; nous ne savons pas.

## L'instantané avant toute écriture de masse

Une API ne connaît pas l'annulation. Quand je modifie trois cents lignes d'une base de données d'un
seul coup et que le script est faux, rien ne revient en arrière.

Depuis fin septembre, une règle s'applique donc : **avant toute écriture de masse, un instantané** —
un fichier dans le coffre qui contient l'état d'avant et le chemin de retour. Treize instantanés ont
été écrits entre le 27 septembre et le 3 octobre.

C'est la bonne habitude, et c'est aussi le défaut que ce récit dénonce depuis le début : **aucun
mécanisme ne l'impose.** C'est une discipline, tenue à la main, qui ne survivra que tant que
quelqu'un y pense.

## Chaque projet a sa carte

Voici le mécanisme le plus intéressant de cette période, et il répond directement au problème du
plafond qui ne plafonne plus.

Jusqu'au 3 octobre, la lecture de démarrage était gouvernée par **un seul budget global** : trois
cents lignes pour tout le coffre. Un projet qui se complique faisait donc grossir ce que je lis avant
le premier mot utile — ou alors son détail restait invisible.

Depuis, chaque projet porte **une carte**, en tête de sa fiche, et la lecture se fait en **trois
étages** :

| Étage | Ce qu'il contient | Quand on l'ouvre |
|---|---|---|
| La ligne d'index | 300 caractères au plus, qui renvoient à la carte | À chaque démarrage |
| **La carte** | À quoi sert le projet · les garde-fous · où on en est · où trouver quoi | Quand on travaille sur ce projet |
| Le détail | Journal, historique, ressources | Seulement par l'index de la carte |

La carte fait **40 lignes de base, et jusqu'à 100 pour un projet compliqué**. Le plafond retenu
s'écrit dans son titre, et — règle posée par Gaël le 5 octobre — **il est évolutif** : on le relève
quand le projet se complique, on le baisse quand il se calme. Le chiffre du titre n'est que le
réglage du moment. Avec une condition, pour que ça ne devienne pas une échappatoire : **une carte
pleine se trie d'abord, on ne relève le plafond qu'ensuite.**

Quatre règles de tenue l'accompagnent, et chacune corrige une erreur que ce récit raconte :
- **Une règle n'est écrite qu'à un seul endroit : la carte.** Ailleurs, un renvoi, jamais une copie —
  parce que deux copies divergent le jour où l'une est corrigée.
- **Chaque garde-fou porte sa date**, et s'il dépend d'un outil extérieur, la date où il a été
  vérifié. Une certification sans date vieillit sans le dire
  ([chapitre 8](08-ouvrir-avant-d-affirmer.md)).
- **Un seul document peut être imposé en plus de la carte**, et seulement pour un geste précis
  (« avant d'écrire dans la base, lire ceci ») ; jamais une chaîne de documents qui en appelle une
  autre.
- **L'index de la carte renvoie à des titres de section, jamais à des numéros de ligne** : les
  numéros bougent, et nous nous y sommes déjà fait prendre deux fois.

Deux cartes existent, écrites le 3 octobre, sur une vingtaine de projets. C'est trop neuf pour en
tirer une leçon : nous saurons dans un mois si elles sont tenues ou si elles rejoignent le compteur
d'autonomie.

## L'entretien se fait en silence

Autre règle, et celle-là est de Gaël, mot pour mot :

> *« Je veux absolument que les audits se fassent de manière autonome sans que j'aie besoin de donner
> aucune autorisation ; je veux simplement avoir un compte rendu et un questionnaire à la fin si
> besoin. C'est un entretien du coffre qui doit se faire en silence. »*

Elle est née d'un agacement légitime : pendant un audit du coffre, il avait été interrompu deux fois
par des demandes d'autorisation — dont une de ma part, deux minutes après avoir promis que l'audit ne
le dérangerait pas.

Elle a produit une exception écrite dans la règle de sécurité, qui dit pourtant depuis août que rien
ne se fait sans ordre explicite : **l'audit agit seul quand il est sûr à 80 % ou plus, et en
silence.** Ce qui est en dessous de 80 % ne m'autorise rien : ça devient une liste de propositions,
présentée dans une petite page web où Gaël valide, corrige ou écarte quand il veut.

C'est le premier mécanisme du coffre où **l'humain a choisi de ne plus être consulté**. Et le seuil
retenu, 80 %, est plus bas que ceux du [chapitre 7](07-mesurer-la-confiance.md) — 90 % pour un geste
réversible et visible, 95 % sinon. La différence est assumée : un geste de rangement se voit, se
raconte au carnet, et se défait.

## Le rappel devient un refus

Le [chapitre 9](09-pieges-de-claude-code.md) raconte le hook qui rappelle de tenir le carnet, et sa
correction du 10 septembre, quand on a découvert qu'il parlait dans le vide.

Le 5 octobre, Gaël a voulu savoir pourquoi, puisqu'il me demande de consigner, le script ne le
faisait pas lui-même. La réponse est qu'il **me le demande déjà** — la consigne lui est transmise —
mais qu'il avait été écrit pour ne jamais forcer. La phrase était dans son en-tête : *« ne bloque
jamais : un refus forcerait Claude à continuer, ce n'est pas voulu. »*

Avant de changer quoi que ce soit, nous avons mesuré. Le hook garde un fichier d'état par
conversation ; il y en avait quarante-neuf depuis le 1er septembre. **Dix-neuf conversations avaient
dépassé le seuil de douze échanges, et le rappel ne s'était déclenché que trois fois** — des séances
de 18, 28 et **41 échanges sans une ligne au carnet.**

Ordre de Gaël : activer le refus, **une seule fois par séance**, et pouvoir revenir en arrière sans
moi. Puis, dans la même conversation, deux précisions qui ont changé le mécanisme :
- **le seuil de douze échanges était trop haut** — il laissait passer les séances courtes où l'on
  tranche quelque chose. Le vrai déclencheur est devenu : **un fichier du coffre a été modifié**
  depuis le début de la séance ;
- **et il a gardé un second seuil, à cinq échanges**, « pour consigner la discussion si elle a lieu
  d'être consignée » — y compris donc les conversations où l'on n'écrit aucun fichier.

Trois détails de fabrication valent d'être dits, parce qu'ils viennent tous d'une leçon de ce récit :
- **le droit de refuser est consommé avant d'être exercé** : le drapeau est posé *avant* la réponse,
  si bien qu'une séance ne peut pas tourner en boucle, même si l'écriture échoue ensuite ;
- **une porte de sortie explicite** : je peux répondre « rien à consigner » en une phrase. Sans elle,
  le mécanisme fabriquerait des entrées vides ;
- **un interrupteur d'arrêt**, parce que Gaël a demandé de pouvoir revenir en arrière : un fichier
  vide à créer dans son dossier personnel et le hook redevient un simple rappel. La version d'avant
  est gardée à côté, et retirer trois lignes de réglage coupe tout.

Le scan du coffre, qui cherche s'il y a eu une écriture, coûte **un dixième de seconde** pour deux
mille quatre cents fichiers. Et il a été éprouvé sur dix cas limites — dans un faux coffre, avec un
faux dossier personnel — avant d'être laissé en service, parce qu'**un hook ne se teste pas dans la
séance qui le modifie.**

## Ce que ces six règles ont en commun

Six mécanismes, et une seule question pour les juger : **qui doit y penser ?**

| Règle | Tenue par |
|---|---|
| La signature des IA | une discipline d'écriture |
| L'instantané avant écriture de masse | une discipline, aucun script ne l'impose |
| Les cartes de projet | une discipline, et deux cartes sur une vingtaine de projets |
| L'audit autonome et silencieux | une règle, plus les permissions qui vont avec |
| La garde contre les exécutions simultanées | du code |
| Le refus de rendre la main sans consigner | du code |

**Deux sur six tiennent toutes seules.** Les autres tiennent tant que quelqu'un y pense — et le
[chapitre 12](12-ce-qui-a-casse.md) montre ce que ça donne.

Le mouvement de ces trois semaines va pourtant dans le bon sens : **ce qui était une consigne devient
un mécanisme.** L'accord avant d'agir l'était déjà ; la consignation vient de le devenir. Reste à voir
ce que ça donne quand le mécanisme, lui, se trompe.

---
[← Chapitre 10](10-trois-jours-pour-rien.md) · [Sommaire](../README.md) · [Chapitre 12 →](12-ce-qui-a-casse.md)
