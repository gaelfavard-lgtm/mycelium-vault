# Annexe : pièges des outils

Ce que nous avons appris sur les outils autour du coffre, souvent en cassant quelque chose. Une grande
partie vient de la gestion d'une petite activité artisanale : une base **Airtable** (une base de
données en ligne qui ressemble à un tableur) pour le suivi des articles et des commandes, et une
application **Softr** (des pages web construites sur Airtable, sans code) pour l'équipe.

## Airtable

**Les automatisations**
- **Supprimer un champ éteint les automatisations qui le surveillent.** Le restaurer ne les rallume pas.
- **Annuler une suppression (Ctrl+Z) rend au champ son identifiant d'origine** ; le recréer lui en donne
  un nouveau, et les scripts qui utilisaient l'ancien cassent.
- **Tester une automatisation depuis l'éditeur ne l'allume pas.** Nous avons eu une automatisation
  « testée OK en live » qui n'avait jamais été activée.
- **L'API sait créer une automatisation à script, mais pas en modifier une existante** : une fois le
  script collé, déclencheur, nom et suppression se règlent dans l'interface.
- **Quarante lignes créées d'un coup lancent quarante exécutions simultanées** de la même
  automatisation, qui se marchent dessus. Il faut une garde (« ne travailler que si je suis la
  dernière »), des suppressions tolérantes, un dédoublonnage final — **et relire après chaque
  génération**, parce que la garde peut céder.
- **Une automatisation de nommage ne surveille pas forcément le champ qu'on vient de changer** : pour
  la relancer, vider puis reposer un champ qu'elle surveille vraiment.
- **Le nom d'un article peut être calculé, pas écrit** : l'écrire à la main donne l'illusion d'avoir
  réussi, jusqu'au prochain recalcul.
- **Plafond de 50 automatisations par base.** Nous avons dû regrouper plusieurs scripts en un seul. La
  vérification après regroupement a trouvé huit points à corriger.
- **Sous forte charge, un déclencheur peut manquer des enregistrements.** Vérifier en cherchant ce qui
  aurait dû changer.
- **Désigner tables, champs et options par leur identifiant dans les scripts**, avec le nom lisible en
  commentaire. Un script qui cherche un champ par son nom casse **sans rien dire** le jour où quelqu'un
  le renomme.
- **Pas de valeur de repli silencieuse dans un script.** Un nom faux mais bien formé passait inaperçu.
  Désormais, la valeur par défaut s'applique **et** le journal le dit.
- **Un commentaire dans un script ne fait pas le réglage qu'il décrit.** Une heure perdue sur un
  commentaire qui décrivait un réglage à faire ailleurs. Écrire plutôt « À RÉGLER DANS… ».

**La structure**
- **Une table vide ne montre pas ses champs cassés** : aucune cellule pour afficher l'erreur.
- **L'API ne supprime aucun champ**, et ne crée pas de page de formulaire.
- **Supprimer une table transforme les liens vers elle en texte figé.**
- **Un regroupement des lignes (« grouper par ») posé par l'API dans une page d'interface ne se retire
  plus dans l'éditeur**, et le menu « Grouper » d'une page publiée ne propose que les champs affichés.
- **Une condition dont la valeur dynamique est vide est ignorée** : un champ vide ne filtre pas sur
  « rien », il laisse tout passer.
- **Fusionner deux enregistrements** se fait par les liens, qui sont symétriques : on ajoute les
  enfants sur la ligne à garder, puis on supprime l'autre. Une écriture, aucun enfant touché.
- **Renommer vers un nom qui existe déjà, c'est fusionner sans le dire** : vérifier d'abord que le nom
  cible est libre.
- **Les URL de pièces jointes sont signées et expirent** : un export de la veille ne télécharge plus
  rien. En contrepartie, on copie une pièce jointe d'un enregistrement à l'autre en réécrivant le
  champ avec l'URL signée.
- **Entrer un modèle dans une commande le verrouille** : ses variantes ne sont plus renommées
  automatiquement, et une correction sur un composant ne se propage plus — il faut la refaire sur les
  lignes.
- **Pour auditer sans pagination** : l'analyse d'une table groupée par champ donne les doublons de nom
  en un appel, les filtres « vide » / « parmi » remplacent les parcours page par page, et un champ de
  synthèse temporaire répond en quelques dizaines de lectures au lieu de centaines.

**Les interfaces**
- **Publier une interface publie tous les brouillons en attente**, y compris ceux d'autres sessions.
- **« Auto » sur la taille d'un élément ne veut pas dire « s'adapte au contenu »** : c'est une hauteur
  courte et fixe. On agrandit par les réglages d'apparence, pas en tirant une poignée.
- **Une grille n'a pas d'édition champ par champ** : pour saisir en place, il faut une page de fiche
  détail. L'API lit ce réglage sans pouvoir l'écrire — pratique pour vérifier une page.
- **Il n'y a pas d'historique des versions des interfaces.** Une page disparue se reconstruit à la main.
- **Une page jamais publiée se supprime sans aucun retour possible.** Ne jamais la supprimer sans
  demander si quelqu'un l'a retouchée à la main.

**Les suppressions faites par l'humain**
- Nous avons demandé à Gaël de supprimer un champ en donnant son nom. Deux champs avaient des noms
  proches : **il a supprimé le mauvais.** Première parade : donner l'identifiant du champ. La parade
  retenue ensuite vient de Gaël : *« Renomme-la "à supprimer" dessus, je ne pourrai pas me tromper. »*
  On renomme d'abord le champ **« À SUPPRIMER — raison »**, avec l'explication dans sa description, puis
  on demande la suppression. *Un nom qu'on lit à l'écran vaut mieux qu'un identifiant qu'on doit
  comparer.*

**Travailler à deux**
- **L'humain modifie la base pendant que l'IA travaille.** Les compteurs bougent pendant la séance. Ne
  jamais reprendre un comptage relevé plus tôt dans la même session.

## Softr

- **Softr relie les champs par leur nom.** Renommer un champ dans Airtable casse le bloc correspondant,
  sans message.
- **Après une publication, le cache retarde l'affichage.** Attendre avant de chercher une panne.
- **Des enregistrements supprimés dans Airtable restent affichés.** Softr se synchronise par
  « webhooks » (des adresses qui reçoivent les changements), limités à deux par base. Nous avons trouvé
  un webhook oublié par un ancien scénario Make, qui pouvait occuper une place ; il a été supprimé. Le
  problème n'est pas réglé : mail envoyé au support.
- **Plusieurs fonctions utiles sont payantes**, et on les découvre en route (par exemple, installer
  l'appli sur le téléphone). Contournement : un raccourci sur l'écran d'accueil.
- **Restreindre l'accès aux données dans Airtable protège partout** ; ne le restreindre que dans les
  pages Softr demande l'offre payante.
- **Le thème général ne règle pas le remplissage des boutons** : ça se fait bloc par bloc, et certains
  blocs (la page de connexion, par exemple) n'ont aucun réglage.
- **Le pincement pour zoomer sur Android** était bloqué par une fenêtre modale, pas par la page : en
  pleine page, il fonctionne.
- **L'éditeur se pilote par recherche d'élément, pas aux coordonnées** : elles changent avec le zoom
  de l'onglet.

## Google Drive

- **Le connecteur Drive de Claude ne sait pas distribuer les droits comme on veut** : il ne partage
  jamais en « tout le monde avec le lien ». Et il a affiché « propriétaire seul » sur des dossiers
  réellement partagés. Le journal d'un script qui partage fait foi, pas le connecteur.
- **Un fichier créé par l'API sans dossier parent atterrit à la racine du Drive.** Mieux vaut écrire sur
  le disque et laisser la synchronisation faire.
- **Envoyer un fichier par le connecteur coûte très cher** : le fichier passe encodé en texte, environ
  460 000 tokens pour 1,3 Mo. Copier le fichier dans le dossier Drive local est gratuit.
- **Google Drive sur téléphone n'ouvre pas les fichiers Markdown.**
- **La synchronisation du mode Miroir peut prendre plusieurs minutes de retard.**
- **L'aperçu de Drive pagine et ignore les fonds CSS** : des pastilles de couleur s'affichaient
  blanches. Ce qui doit se voir ne doit pas dépendre d'un fond — nous les avons remplacées par des
  images. Les marges de pagination ne s'enlèvent pas : on compense en agrandissant.
- **Le connecteur Gmail ne rend pas les pièces jointes** : une facture reçue en PDF reste illisible.

## Google Apps Script

- **La page est servie dans un cadre fourni par Google.** Conséquences : pas d'icône d'écran d'accueil,
  pas de plein écran (les balises Apple sont refusées et font planter la page), et pas de simulation de
  gestes tactiles depuis l'ordinateur.
- **`ScriptApp.getService().getUrl()` n'est pas fiable** selon le contexte : l'adresse de l'appli doit
  être écrite en dur.
- **Tous les liens internes doivent porter `target="_top"`**, sinon ils s'ouvrent dans le cadre et sont
  bloqués.
- **`location.reload()` donne une page blanche.** Mettre la page à jour en remplaçant son contenu.
- **Les modèles HTML échappent déjà les variables** : `<?= JSON.stringify(x) ?>` ajoute des guillemets en
  trop. Écrire `<?= x ?>`.
- **Le déploiement peut resservir l'ancienne version.** Vérifier le numéro annoncé dans la fenêtre de
  confirmation.
- **Vérifier quel fichier est ouvert avant de coller le code.**

## Windows

- **Un fichier `.bat` doit avoir des fins de ligne Windows (CRLF).** Sinon Windows mange un caractère par
  ligne, en silence.
- **Pas de pause ni d'attente de saisie dans un script lancé automatiquement** : il attendrait pour
  toujours.
- **Le Planificateur de tâches coupe la commande au premier espace.** Mettre l'exécutable seul dans
  « Programme », et le chemin du script entre guillemets dans « Arguments ».
- **Sur un portable qui se met en veille, une tâche lancée « à l'ouverture de session » puis répétée
  toutes les heures cesse de se répéter**, et rien n'est rattrapé. Mettre plusieurs déclencheurs, et
  cocher « exécuter la tâche dès que possible après un démarrage planifié manqué ».
- **L'écran « Tâches en cours » du Planificateur ne se rafraîchit pas tout seul** : appuyer sur F5. La
  preuve qu'une tâche a tourné est son journal, pas l'affichage.
- **Modifier une tâche planifiée demande les droits administrateur.**
- **La commande `python` peut n'être qu'un raccourci vers le Microsoft Store** ; c'est `py` qui lance
  Python.
- **PowerShell 5.1 lit mal les accents d'un script enregistré sans BOM** (une marque invisible en début
  de fichier qui indique l'encodage) : enregistrer en UTF-8 avec BOM.
- **En PowerShell, `$Out` et `$out` sont la même variable** : les majuscules ne comptent pas. Un script a
  ainsi écrasé l'une de ses propres variables — et la même faute est revenue avec `$V` et `$v`, où une
  boucle interne a écrasé la liste de la boucle externe, pour un résultat faux d'un facteur six.
  **Nommer les collections avec un mot entier.**
- **`perl -i` avec une notation d'échappement large (`\x{...}`) sur un fichier accentué réencode tout le
  fichier** : 2 354 lignes sur 3 773 en double-encodage pour une correction d'une seule ligne. La
  conversion inverse (`iconv -f UTF-8 -t LATIN1`) défait exactement ce dommage. **C'est la sortie de la
  commande elle-même qui a trahi l'erreur** — il faut la lire.
- **Un script qui écrit un alphabet non latin doit être enregistré en UTF-8 avec BOM**, sinon
  PowerShell 5.1 l'abîme.
- **Pour produire un PDF sans rien installer** : le navigateur en mode sans fenêtre
  (`msedge --headless --print-to-pdf`) sur le fichier HTML local.
- **Un script de récupération de pages web a écrasé 252 fichiers de résultats**, parce qu'on avait
  prévu où il lisait mais pas où il écrivait. Écrire les résultats au fil de l'eau, avec reprise.
- **L'« Assistant de stockage » de Windows et OneDrive** transforment les fichiers en fantômes « en ligne
  uniquement ». Épingler les fichiers et couper la purge automatique.
- **Les photos iPhone (HEIC)** se convertissent sans logiciel supplémentaire, avec les composants déjà
  présents dans Windows.

## Claude Code

*Le [chapitre 9](recit/09-pieges-de-claude-code.md) raconte l'essentiel ; voici ce qui s'y est ajouté
depuis.*

- **Le système de permissions interdit à Claude de modifier son propre garde-fou.** C'est le
  comportement attendu, mais il faut le savoir : l'installation d'un garde-fou reste un geste humain.
- **Republier une page web depuis un autre chemin de fichier crée une seconde page** au lieu de mettre
  la première à jour : il faut passer l'adresse de la page existante.
- **Les résultats d'outil ne sont pas toujours écrits sur le disque** : impossible, alors, d'en
  fabriquer un script. Contournement : écrire à la main, par lots à préfixe constant, où une erreur
  saute aux yeux.

## Divers

- **Les photos transmises perdent leurs données de date (EXIF)**, quel que soit le canal. La date ne
  survit que dans le nom du fichier.
- **Une apostrophe droite dans une chaîne JavaScript** a tué une page entière. Utiliser l'apostrophe
  typographique dans les textes.
- **ChatGPT invente des noms plausibles** quand on lui demande d'identifier des objets sur des photos à
  partir d'un catalogue fermé de 28 types : trois noms inventés sur quinze. La liste fermée doit lui être
  imposée, pas proposée.
- **Les sites marchands refusent souvent la lecture automatique.** Code 402 : boutique Shopify suspendue ;
  404 : page supprimée ; 403 : site vivant, mais lecture automatique bloquée.

---
[← Sommaire](README.md)
