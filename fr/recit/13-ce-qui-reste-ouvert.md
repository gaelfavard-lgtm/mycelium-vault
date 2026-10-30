# 13. Ce qui reste ouvert

Un récit qui ne parle que de problèmes résolus donne une fausse image. Voici ce qui ne marche pas, ou
pas encore, **au 3 octobre 2026**. Plusieurs de ces points ont été découverts en préparant ce récit,
puis en le relisant trois semaines plus tard.

## Ce qui s'est réglé depuis le 16 septembre

Pour être juste, commençons par là :
- **Les extraits de session fonctionnent de nouveau** — mais personne ne les a réparés
  ([chapitre 12](12-ce-qui-a-casse.md)).
- **Les quatre hooks tournent tous.** Au 16 septembre, l'un était en panne ; ce n'est plus le cas.
- **La question de la sauvegarde du second ordinateur est tranchée**, et la réponse est non : aucun
  des 136 passages enregistrés n'en vient.
- **Les données de test ne sont plus indistinguables du réel** : une convention de nommage
  (« à supprimer ») et un registre tenu à jour disent ce qui est fictif et comment le purger. Ce
  n'est pas un mécanisme, c'est une discipline écrite — mais le trou n'est plus nu.
- **Le garde-fou qui lit des mots et non des intentions** a reçu un remède, écrit et testé. Il a été
  **refusé** pour son coût, et la friction s'est dissoute parce que Gaël a changé sa façon de parler.

## Des mécanismes qui reposent sur la seule discipline

- **Le compteur d'autonomie ne tourne que dans les audits.** Arrêté du 13 septembre au 3 octobre, il
  s'est rempli d'un coup quand un audit a soumis 32 propositions. C'est le pivot du
  [chapitre 7](07-mesurer-la-confiance.md), et il ne mesure rien du travail ordinaire.
- **L'instantané avant écriture de masse** tient à la main, sans aucun script pour l'exiger.
- **Les consignes écrites avant la règle de signature ne sont pas signées** : personne ne sait
  lesquelles viennent de Gaël et lesquelles d'une IA.

## Des filets incomplets

- **Un seul ordinateur sauvegarde le coffre**, et c'est le portable.
- **Les fichiers lourds** (photos, PDF, plans) **n'ont aucune copie hors de Drive** : la sauvegarde
  couvre 513 fichiers texte, le coffre pèse plusieurs gigaoctets.
- **Les sessions faites ailleurs** (téléphone, Cowork, claude.ai) **ne laissent aucune trace sur le
  PC** ([chapitre 2](02-plusieurs-ia-les-tickets.md)).
- **Ce récit lui-même n'est dans aucune sauvegarde** : le dossier qui le contient est hors du coffre
  et n'est pas encore un dépôt git. Dix-sept jours que c'est signalé.
- **Un mot de passe d'étiquette d'appareil est encore en clair dans le carnet**, signalé le
  16 septembre, toujours là.

## Des problèmes sans mécanisme

- **Rien ne signale qu'une fiche ne dit plus la vérité.** Le script d'audit trouve les liens cassés,
  pas une fiche qui ment sur le fond. La fiche du garde-fou refusé a annoncé pendant dix-sept jours
  une installation qui n'arriverait jamais.
- **Un plafond qui compte les lignes ne limite plus rien** quand les lignes s'allongent : 363 lignes
  au démarrage pour un plafond de 300, et un index de 61 lignes qui pèse 14 Ko. Les **cartes de
  projet** ([chapitre 11](11-les-regles-qui-sont-nees.md)) sont la réponse à ce problème : un plafond
  par projet, réglable, au lieu d'un budget global. Deux cartes sur une vingtaine de projets — c'est
  trop tôt pour dire si la mesure tient.
- **Rien ne lit les boîtes d'entrée quand aucune session ne tourne.**
- **Plusieurs sessions écrivent dans le même fichier sans aucun verrou** — le carnet en porte la
  trace, avec ses deux ordres chronologiques.
- **Un garde-fou éprouvé une fois n'est pas éprouvé** : celui qui protège des exécutions simultanées
  a tenu deux fois, puis cédé.
- **Une panne qui s'arrête sans explication** ne dit pas si le filet est réparé ou en sursis.

## Des tensions que nous ne savons pas trancher

- **Les mécanismes.** Les autres coffres nous ont appris que moins de mécanismes, c'est moins de
  pannes. Nous en avons cinq, plus quatre disciplines humaines, et ce sont les disciplines qui
  lâchent. Le dernier né — le refus de rendre la main sans avoir consigné — est précisément une
  discipline convertie en code : nous verrons s'il tient, et ce qu'il coûte quand il se trompe.
- **Les règles.** Chaque incident donne envie d'écrire une règle. Chaque règle ajoutée fait moins
  bien suivre les autres. Le budget déborde quand même.
- **L'autonomie.** Quatre catégories sont ouvertes, et Gaël arbitre tout le reste. C'est voulu. Mais
  le compteur qui devait en ouvrir d'autres ne tourne plus.

## La question de la durée

Ce coffre a **huit semaines.** En cherchant des retours d'expérience, nous n'avons trouvé presque
aucun récit d'usage prolongé de ce genre de système. Le témoignage le plus détaillé
([sur DEV.to](https://dev.to/huy_tieu/i-finally-built-a-second-brain-that-i-actually-use-6th-attempt-4075))
décrivait un sixième système, après plusieurs abandons, qui tenait depuis trois mois ; trois semaines
plus tard, son auteur l'avait entièrement réorganisé.

Nous ne savons pas si Mycélium tiendra. Une mémoire holistique n'a aucune valeur propre : elle ne
vaut que tant qu'elle est tenue, et le jour où plus personne n'écrit dedans, c'est un dossier de
fichiers périmés. **Le seul indicateur que nous suivons** est l'étiquette [contenu] ou [entretien] de
chaque entrée du carnet ([chapitre 5](05-la-cure.md)). Si les [entretien] finissent par dominer, le
coffre sera devenu ce qu'il devait éviter.

Ce chapitre sera complété. Les chapitres [11](11-les-regles-qui-sont-nees.md) et [12](12-ce-qui-a-casse.md) sont nés comme ça.

---
[← Chapitre 12](12-ce-qui-a-casse.md) · [Sommaire](../README.md) · [Les leçons →](../lecons.md)
