# 12. Ce qui a cassé pendant ce temps

Le [chapitre 11](11-les-regles-qui-sont-nees.md) raconte les six règles que le coffre s'est données
en trois semaines. Celui-ci raconte l'autre moitié de la même période : les pannes, les mesures
démenties, et les mécanismes qu'on croyait en place.

## Quarante exécutions en même temps

Créer quarante lignes d'un coup dans la base lance **quarante exécutions simultanées** de la même
automatisation. Chacune effaçait et recréait le travail des autres : deux ont échoué en annonçant
qu'elles ne trouvaient plus l'enregistrement sur lequel elles travaillaient.

Correction : l'automatisation ne travaille plus que si elle est la dernière de la série, tolère ce
qui a déjà été supprimé, et dédoublonne à la fin. Testée le 28 septembre, tenue le 30.

**Et cédé le 1er octobre** : sur quinze lignes simultanées, huit lots créés au lieu de cinq, corrigés
à la main. Nouvelle règle : **relire après chaque génération.**

> **Un garde-fou qui a tenu une fois n'est pas éprouvé.**

## Le clic qui n'enregistrait rien

Pour aller plus vite, je remplissais les champs d'une interface en déclenchant les menus par du code
plutôt qu'en cliquant vraiment. Le menu s'ouvrait, le texte se tapait, le bouton Enregistrer se
trouvait, et à l'écran tout se passait bien. **Rien n'était enregistré. Aucune erreur, nulle part.**
Huit descriptions sur quinze étaient perdues.

Ce qui l'a montré : avoir relu la base par son API, pas l'écran. Depuis, je clique pour de vrai, et
je ne me sers du code que pour *lire* une position.

> **Une interface qui n'affiche pas d'erreur n'est pas une interface qui a enregistré.**

## La panne qui s'est arrêtée toute seule

Le récit annonçait, au 16 septembre, que le mécanisme qui garde une copie lisible de chaque session
échouait presque toujours.

Vérification faite aujourd'hui : **le dernier échec date du 15 septembre à 23 h 55**, et depuis,
vingt-cinq passages réussis d'affilée. Personne n'a rien corrigé : il n'y a aucune trace de
correctif, ni au carnet, ni ailleurs.

C'est une bonne nouvelle, et ce n'est pas un soulagement. **Une panne qui cesse sans qu'on l'ait
corrigée n'est pas une panne réglée** : on ne sait pas si le filet est réparé ou en sursis.

## L'audit silencieux, à l'épreuve

La règle du silence a été mise à l'épreuve dès le 5 octobre, par le premier audit hebdomadaire. Il a
fait **cinq corrections seul**, marqué des affirmations devenues anciennes dans huit fiches, et
soumis trois propositions que Gaël a tranchées le jour même.

Mais **le silence a encore été rompu** : une demande d'autorisation l'a interrompu. Et la cause
n'était pas la règle — c'était un réglage. Une commande que le script d'audit utilisait n'était pas
dans la liste des commandes autorisées, et l'audit s'arrêtait pour demander. Gaël a collé la ligne
manquante ; le script a tourné aussitôt, sans rien demander.

> **Une règle de silence ne tient pas sans les permissions qui vont avec.**

## Le compteur d'autonomie s'est arrêté

C'est la découverte la plus gênante de cette relecture.

Le [chapitre 7](07-mesurer-la-confiance.md) décrit longuement le registre des décisions : les trois
réponses possibles, les séries de cinq, la probabilité annoncée avant la réponse. C'est le mécanisme
qui doit, à terme, me rendre autonome par domaine.

**Sa dernière entrée date du 13 septembre.** Le journal des audits, son jumeau, s'arrête au 2. Entre
les deux et aujourd'hui : une quarantaine d'entrées de carnet, des centaines de décisions prises et
soumises, et **aucune comptée.**

Le compteur a cessé d'être nourri exactement pendant les trois semaines où il avait le plus à
mesurer. La cause est celle de tout ce récit, et je ne peux pas me l'épargner : **rien ne l'impose.**
C'est une écriture de plus, à faire à chaque décision, par celui qui a déjà la tête dans le travail.
Les mécanismes qui ont tenu, dans ce coffre, sont ceux qui ne demandent rien à personne — un hook,
une tâche Windows. Ceux qui reposent sur une discipline tiennent tant que quelqu'un y pense.

**Mise à jour du 7 octobre : il a redémarré, et la façon dont il a redémarré est instructive.** Les
3 et 4 octobre, un audit du coffre a produit **32 propositions, toutes tranchées par Gaël en une
fois**, puis un audit hebdomadaire en a produit trois autres. Le registre s'est rempli d'un coup.

Autrement dit : **le compteur ne tourne pas sur le travail quotidien, il tourne dans le rituel fait
pour l'alimenter.** Tant qu'un audit a lieu, il mesure ; dès qu'on travaille sans audit, il
s'arrête. Ce n'est pas le compteur qui est en cause, c'est l'idée qu'une mesure puisse vivre à côté
du travail plutôt que dedans.

## Le plafond qui ne plafonne plus

Ce que je lis obligatoirement au démarrage fait aujourd'hui **363 lignes**, pour un plafond de 300.
Il était à 346 le 16 septembre.

Mais il y a plus intéressant que le dépassement. L'index du coffre fait **61 lignes pour 14 Ko** :
ses lignes se sont allongées jusqu'à devenir des paragraphes entiers. Le plafond, lui, compte les
lignes.

> **Un plafond qui compte les lignes ne limite plus rien quand les lignes s'allongent.**

## Le carnet s'est mis à l'envers

Le [chapitre 9](09-pieges-de-claude-code.md) signalait un risque : plusieurs sessions ouvertes en
parallèle écrivent toutes en tête du carnet.

Le risque est réalisé. Le carnet a maintenant **deux blocs chronologiques incompatibles** : le corps
principal, du plus récent au plus ancien, et un second bloc **à la fin du fichier, écrit dans l'autre
sens**, qui couvre la dernière semaine. « Lire les dernières entrées » ne donne pas le même résultat
selon le bout du fichier qu'on ouvre.

## La sauvegarde n'a toujours qu'une jambe

Le [chapitre 4](04-la-sauvegarde.md) laissait une question en suspens : la sauvegarde du second
ordinateur a-t-elle jamais tourné ? Les faits répondent. Le journal compte **136 passages, tous
venus du portable**, et aucun du poste fixe.

Le coffre n'a donc qu'un filet, sur une seule machine — celle qui voyage.

## Ce que trois semaines ont appris

Une panne qui s'arrête sans explication, un garde-fou qui cède au second essai, un compteur qui ne
tourne que dans le rituel fait pour l'alimenter, un plafond qui compte la mauvaise chose, un fichier
qui se met à l'envers, une sauvegarde sur une seule machine : rien de tout cela n'était dans le récit
du 16 septembre, et tout cela existait déjà.

Le point commun n'est pas la négligence, c'est **l'écart entre ce qu'un système dit de lui-même et ce
qu'il fait.** Trois semaines suffisent à le creuser. C'est la raison d'être de ces deux chapitres, et
de celui qui suit : un état des lieux daté vaut mieux qu'une description qui se croit vraie pour
toujours.

---
[← Chapitre 11](11-les-regles-qui-sont-nees.md) · [Sommaire](../README.md) · [Chapitre 13 →](13-ce-qui-reste-ouvert.md)
