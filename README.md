# EpiCubers

Site de support du serveur Discord EpiCubers, la communauté des speedcubeurs de l'école : présentation du speedcubing, les trois méthodes de résolution, guide d'achat de cube, rôles par niveau, liens et glossaire.

Site statique : aucune dépendance, aucune étape de build pour le publier.

## Voir le site

Ouvrir `index.html` dans un navigateur, ou lancer un petit serveur local :

```bash
python3 -m http.server 8000
```

Puis aller sur http://localhost:8000.

## Publier

Le dépôt peut être servi tel quel par n'importe quel hébergeur statique (GitHub Pages, Netlify, Cloudflare Pages…). Pour GitHub Pages : Settings > Pages > Deploy from a branch > `main` / `/ (root)`.

## Structure

```
index.html, speedcubing.html, communaute.html, cubes.html, liens.html, glossaire.html
methodes.html            comparaison des trois méthodes
methode-debutant.html    méthode débutant (3 algorithmes)
cfop-simplifiee.html     CFOP simplifiée (14 algorithmes, avec vidéos)
cfop.html                CFOP complète (renvoi vers SpeedCubeDB)
css/style.css            feuille de style unique
js/main.js               menu mobile, bouton « copier », recherche du glossaire
assets/                  mascotte, favicon, illustration du cube
tools/build.py           génère les pages HTML (contenu + en-tête/pied de page communs)
```

## Modifier le contenu

Les pages sont générées par `tools/build.py` pour que le menu et le pied de page restent identiques partout. Le texte se modifie dans ce fichier, puis :

```bash
python3 tools/build.py
```

Les fichiers `.html` peuvent aussi être édités directement pour une retouche rapide, mais elle sera écrasée au prochain build.

### Photo du cube conseillé

La page `cubes.html` affiche `assets/guhong-pro-m.jpg` si le fichier existe, et l'illustration `assets/cube.svg` sinon. Pour mettre la vraie photo, il suffit de déposer l'image sous ce nom dans `assets/`.

## À savoir

- Les animations 3D des algorithmes de la page méthode débutant utilisent [cubing.js](https://js.cubing.net/cubing/) chargé depuis un CDN.
- La dernière étape de la méthode débutant est marquée « à confirmer ».
- Les prix du guide d'achat sont indicatifs et datés dans la page.

## Transparence sur l'IA

Ce site a été réalisé avec l'aide d'une IA (Claude, d'Anthropic) pour la structure, le code et une partie de la rédaction. Le fond vient de l'équipe EpiCubers : la présentation de la communauté, les rôles, les méthodes et les liens. C'est l'équipe qui décide de ce qui est publié.

L'IA est utilisée ici comme un outil, pas comme une source d'autorité. Les informations qui bougent ou qui demandent une vérification (prix et modèles de cubes, algorithmes) sont à contrôler avant de s'y fier. En cas d'erreur, ouvrir une issue ou prévenir l'équipe sur le Discord.
