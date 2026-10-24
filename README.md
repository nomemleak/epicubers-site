# EpiCubers

Site de support du serveur Discord EpiCubers, la communauté des speedcubeurs de l'école : présentation du speedcubing, guide d'achat de cubes, méthode débutant, passage à la CFOP, rôles par niveau, liens et glossaire.

Site statique : pas de dépendance, pas d'étape de build pour le publier.

## Voir le site

Ouvre `index.html` dans un navigateur, ou lance un petit serveur local :

```bash
python3 -m http.server 8000
```

Puis va sur http://localhost:8000.

## Publier

Le dépôt peut être servi tel quel par n'importe quel hébergeur statique (GitHub Pages, Netlify, Cloudflare Pages…). Pour GitHub Pages : Settings > Pages > Deploy from a branch > `main` / `/ (root)`.

## Structure

```
index.html, speedcubing.html, communaute.html, cubes.html,
methode-debutant.html, cfop.html, liens.html, glossaire.html
css/style.css     feuille de style unique
js/main.js        menu mobile, bouton « copier », recherche du glossaire
assets/           mascotte et favicon
tools/build.py    génère les pages HTML (contenu + en-tête/pied de page communs)
```

## Modifier le contenu

Les pages sont générées par `tools/build.py` pour que le menu et le pied de page restent identiques partout. Modifie le texte dans ce fichier, puis :

```bash
python3 tools/build.py
```

Tu peux aussi éditer les fichiers `.html` directement pour une retouche rapide, mais elle sera écrasée au prochain build.

## À savoir

- Les animations 3D des algorithmes de la page méthode débutant utilisent [cubing.js](https://js.cubing.net/cubing/) chargé depuis un CDN.
- La page méthode débutant est une version provisoire, à relire.
- Les prix du guide d'achat sont indicatifs et à vérifier.

## Transparence sur l'IA

Ce site a été réalisé avec l'aide d'une IA (Claude, d'Anthropic) pour la structure, le code et une partie de la rédaction. Le fond vient de l'équipe EpiCubers : la présentation de la communauté, les rôles, les méthodes et les liens. C'est l'équipe qui décide de ce qui est publié.

L'IA est utilisée ici comme un outil, pas comme une source d'autorité. Les informations qui bougent ou qui demandent une vérification (prix et modèles de cubes, algorithmes) sont à contrôler avant de s'y fier. Si tu repères une erreur, ouvre une issue ou préviens-nous sur le Discord.
