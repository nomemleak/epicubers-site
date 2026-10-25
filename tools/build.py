#!/usr/bin/env python3
"""Génère les pages HTML du site EpiCubers à la racine du dépôt"""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

DISCORD = "https://discord.gg/vQwt4qZUBm"
DISCORD_FR = "https://discord.gg/MZ75mtHdGZ"
ATOUT_GUHONG = "https://www.atoutcubes.com/fr/meilleur-cube-3x3/67698-dayan-guhong-pro-m-3x3-54-55-56mm-4000000001294.html"

NAV = [
    ("index.html", "Accueil"),
    ("speedcubing.html", "Le speedcubing"),
    ("methodes.html", "Méthodes"),
    ("notation.html", "Notation"),
    ("cubes.html", "Cubes"),
    ("communaute.html", "Communauté"),
    ("liens.html", "Liens"),
    ("glossaire.html", "Glossaire"),
]

LOGO = """<svg viewBox="0 0 30 30" aria-hidden="true"><g>
<rect x="2" y="2" width="8" height="8" rx="1.5" fill="#1a87db"/><rect x="11" y="2" width="8" height="8" rx="1.5" fill="#f4f4f4"/><rect x="20" y="2" width="8" height="8" rx="1.5" fill="#d91c1c"/>
<rect x="2" y="11" width="8" height="8" rx="1.5" fill="#d8cb1a"/><rect x="11" y="11" width="8" height="8" rx="1.5" fill="#4b4a96"/><rect x="20" y="11" width="8" height="8" rx="1.5" fill="#18c52b"/>
<rect x="2" y="20" width="8" height="8" rx="1.5" fill="#dc7f1a"/><rect x="11" y="20" width="8" height="8" rx="1.5" fill="#d91c1c"/><rect x="20" y="20" width="8" height="8" rx="1.5" fill="#1a87db"/></g></svg>"""

TWISTY = '<script type="module" src="https://cdn.cubing.net/v0/js/cubing/twisty"></script>'


def page(fname, title, desc, body, head_extra="", active=None):
    active = active or fname
    nav = "".join(
        '<a href="%s"%s>%s</a>' % (f, ' aria-current="page"' if f == active else "", label)
        for f, label in NAV
    )
    html = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#15132a">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,500;12..96,700;12..96,800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
{head_extra}
</head>
<body>
<a class="skip" href="#contenu">Aller au contenu</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html">{LOGO}<span>EpiCubers</span></a>
    <button class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button>
    <nav class="nav" id="nav" aria-label="Navigation principale">{nav}</nav>
  </div>
  <div class="stripe"></div>
</header>
<main id="contenu">
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <div>
      <p><strong>EpiCubers</strong>, le serveur Discord des speedcubeurs de l’école.</p>
      <p>Site fait par la communauté. Pas affilié à la World Cube Association. « Rubik’s » est une marque déposée.</p>
    </div>
    <ul>
      <li><a href="{DISCORD}">Discord</a></li>
      <li><a href="https://www.worldcubeassociation.org/">WCA</a></li>
      <li><a href="https://speedcubedb.com/">SpeedCubeDB</a></li>
      <li><a href="https://cstimer.net/">csTimer</a></li>
    </ul>
  </div>
</footer>
<script src="js/main.js"></script>
</body>
</html>
"""
    with open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
        f.write(html)


def head(title, sub):
    return f'<div class="page-head"><div class="wrap"><h1>{title}</h1><p>{sub}</p></div></div>\n'


def algo(name, moves, player=True, note=""):
    p = ""
    if player:
        p = (
            f'<div class="player-box"><twisty-player alg="{moves}" experimental-setup-anchor="end" '
            'visualization="3D" background="none" control-panel="bottom-row" hint-facelets="none">'
            '</twisty-player></div>'
        )
    n = f'<p class="muted" style="margin:6px 0 0">{note}</p>' if note else ""
    return f"""<div class="algo">
  <div class="algo-top"><span class="algo-name">{name}</span><button class="copy" type="button">Copier</button></div>
  <code>{moves}</code>{n}{p}
</div>"""


# ---------------------------------------------------------------- ACCUEIL
body = f"""
<section class="hero">
  <div class="wrap">
    <div class="hero-text">
      <h1>Epi<span>Cubers</span></h1>
      <p class="lead">Le serveur des speedcubeurs de l’école : débutants, habitués, curieux. On résout des Rubik’s cubes le plus vite possible, et on s’entraîne ensemble.</p>
      <div class="btns">
        <a class="btn primary" href="{DISCORD}">Rejoindre le Discord</a>
        <a class="btn" href="methode-debutant.html">Apprendre à résoudre le cube</a>
      </div>
    </div>
    <div class="hero-art"><img src="assets/mascotte.jpg" alt="La mascotte d’EpiCubers : un Rubik’s cube à casquette violette, lunettes noires et baskets roses" width="629" height="900"></div>
  </div>
</section>
<div class="stripe"></div>

<section>
  <div class="wrap">
    <h2>Par où commencer ?</h2>
    <div class="grid c3">
      <a class="card" href="methode-debutant.html">
        <h3><span class="dot" style="background:var(--green)"></span>Une première résolution</h3>
        <p>Une méthode avec très peu d’algorithmes à retenir. Compter entre 40 secondes et une minute une fois qu’elle est acquise.</p>
        <span class="go">Voir la méthode</span>
      </a>
      <a class="card" href="cubes.html">
        <h3><span class="dot" style="background:var(--blue)"></span>Un premier cube</h3>
        <p>Un seul modèle conseillé, où le commander, et pourquoi certaines boutiques sont à éviter.</p>
        <span class="go">Lire le guide d’achat</span>
      </a>
      <a class="card" href="communaute.html">
        <h3><span class="dot" style="background:var(--orange)"></span>Rejoindre la communauté</h3>
        <p>Les salons du serveur, les rôles par niveau et les compétitions officielles à suivre.</p>
        <span class="go">Découvrir la communauté</span>
      </a>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>Projets à venir</h2>
    <p>Pour l’instant, EpiCubers est un serveur Discord et rien de plus. Voici ce qui pourrait se faire par la suite, selon l’envie des membres.</p>
    <div class="grid c2">
      <div class="card">
        <h3>Sessions cubing</h3>
        <p>Se retrouver pour s’entraîner à plusieurs, échanger des astuces et essayer des cubes différents. Des speedcubes pourraient être mis à disposition pendant ces rencontres.</p>
      </div>
      <div class="card">
        <h3>Tournois et compétitions</h3>
        <p>Des tournois ouverts à tous, éventuellement avec des lots à gagner.</p>
      </div>
      <div class="card">
        <h3>Cubes à prix avantageux</h3>
        <p>Une sélection de speedcubes revendus à prix réduit, pour rendre la discipline accessible et peu coûteuse.</p>
      </div>
      <div class="card">
        <h3>Toute autre idée</h3>
        <p>Les idées de projets sont les bienvenues sur le Discord.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>De « sup-1 » à « sub-9 »</h2>
    <p>Sur le serveur, le rôle dépend de la moyenne. Chacun commence quelque part.</p>
    <ul class="ladder" aria-label="Niveaux">
      <li style="--c:var(--white)">sup-1</li>
      <li style="--c:var(--blue)">sub-1</li>
      <li style="--c:var(--blue)">sub-50</li>
      <li style="--c:var(--blue)">sub-40</li>
      <li style="--c:var(--green)">sub-30</li>
      <li style="--c:var(--green)">sub-25</li>
      <li style="--c:var(--yellow)">sub-20</li>
      <li style="--c:var(--yellow)">sub-15</li>
      <li style="--c:var(--orange)">sub-12</li>
      <li style="--c:var(--orange)">sub-10</li>
      <li style="--c:var(--red)">sub-9</li>
    </ul>
    <p><a href="communaute.html#roles">Comment obtenir un rôle</a></p>
  </div>
</section>
"""
page("index.html", "EpiCubers — le serveur des speedcubeurs de l’école",
     "Communauté de speedcubing : méthode débutant, guide d’achat de cubes, rôles par niveau et compétitions à suivre.",
     body)

# ---------------------------------------------------------------- SPEEDCUBING
body = head("Le speedcubing", "Résoudre un Rubik’s cube, le plus vite possible.") + """
<section>
  <div class="wrap">
    <h2>C’est quoi, exactement ?</h2>
    <p class="lead">Le speedcubing consiste à résoudre des speedcubes (des Rubik’s cubes conçus pour tourner vite) en un minimum de temps. Pour y arriver, il existe de nombreuses méthodes de résolution, de difficultés très différentes.</p>
    <p>Le cube a été inventé en 1974 par Ernő Rubik. Le premier championnat du monde a eu lieu à Budapest en 1982, et la World Cube Association (WCA), qui organise aujourd’hui les compétitions officielles, existe depuis 2004.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>Trois méthodes, trois niveaux</h2>
    <p>Plus on veut aller vite, plus il y a d’algorithmes à apprendre.</p>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Niveau</th><th>Méthode</th><th>Algorithmes</th><th>Temps typique</th></tr></thead>
        <tbody>
          <tr><td>Facile</td><td><a href="methode-debutant.html">Méthode débutant</a></td><td>3 algorithmes simples</td><td>40 s à plus d’une minute</td></tr>
          <tr><td>Intermédiaire</td><td><a href="cfop-simplifiee.html">CFOP simplifiée</a></td><td>14 algorithmes</td><td>15 à 25 s</td></tr>
          <tr><td>Difficile</td><td><a href="cfop.html">CFOP complète</a></td><td>78 à 160 algorithmes</td><td>5 à 15 s</td></tr>
        </tbody>
      </table>
    </div>
    <p><a href="methodes.html">Voir les trois méthodes en détail</a></p>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>Les épreuves officielles</h2>
    <p>Le 3x3 est l’épreuve reine, mais la WCA reconnaît bien d’autres épreuves :</p>
    <ul class="clean">
      <li>les cubes de 2x2 à 7x7 ;</li>
      <li>le 3x3 à une main (OH) ;</li>
      <li>le 3x3 à l’aveugle (BLD), le 4x4 et le 5x5 à l’aveugle, et le multi-blind ;</li>
      <li>le Fewest Moves (FMC), où l’on cherche la solution la plus courte, sur papier ;</li>
      <li>les puzzles non cubiques : Pyraminx, Skewb, Megaminx, Square-1, Clock.</li>
    </ul>
    <div class="note">
      <p>En compétition, l’inspection dure 15 secondes avant le lancement du chrono. Un 3x3 se juge sur 5 résolutions : on retire la meilleure et la pire, et la moyenne des trois autres donne le résultat (l’« ao5 »). Une pénalité de +2 secondes ou un DNF peut s’ajouter.</p>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>S’entraîner</h2>
    <p>Quelques habitudes qui font vraiment progresser :</p>
    <ul class="clean">
      <li>se chronométrer avec des mélanges officiels, par exemple sur <a href="https://cstimer.net/">csTimer</a>, la référence, ou sur <a href="https://cubedesk.io/">CubeDesk</a>, qui propose en plus des duels et un entraîneur d’algorithmes ;</li>
      <li>regarder ses résolutions, pas seulement son temps : à quel endroit s’arrête-t-on ?</li>
      <li>apprendre un algorithme à la fois et le répéter jusqu’à ce qu’il passe tout seul ;</li>
      <li>échanger avec d’autres cubeurs : voir quelqu’un d’autre tourner apprend plus que dix vidéos.</li>
    </ul>
    <p>Pour les compétitions officielles, les prochaines dates sont sur le <a href="https://www.worldcubeassociation.org/competitions">site de la WCA</a>. Sur le serveur, le salon <strong>wca-comps</strong> sert à les repérer et à s’organiser.</p>
    <div class="btns"><a class="btn primary" href="methode-debutant.html">Apprendre la méthode débutant</a><a class="btn" href="glossaire.html">Un mot inconnu ? Le glossaire</a></div>
  </div>
</section>
"""
page("speedcubing.html", "Le speedcubing, c’est quoi ? — EpiCubers",
     "Présentation du speedcubing : les méthodes, les épreuves WCA et comment s’entraîner.", body)

# ---------------------------------------------------------------- COMMUNAUTE
body = head("La communauté", "Un serveur Discord pour les passionnés, les adeptes et les débutants.") + f"""
<section>
  <div class="wrap">
    <h2>Pourquoi ce serveur</h2>
    <p class="lead">Réunir des passionnés, des adeptes et même des débutants en speedcubing, dans la même école.</p>
    <p>On y partage ses temps, on pose ses questions, on suit les compétitions officielles. Pour l’instant, c’est un serveur Discord, et les projets à venir dépendent de l’envie des membres.</p>
    <div class="btns"><a class="btn primary" href="{DISCORD}">Rejoindre EpiCubers</a></div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>Les salons</h2>
    <div class="grid c3">
      <div class="card"><h3>Pour s’y retrouver</h3><p><strong>#rôles</strong> pour prendre son niveau.<br><strong>#à-propos</strong> et <strong>#utile</strong> pour les infos et les liens importants.</p></div>
      <div class="card"><h3>Général</h3><p><strong>#bienvenue</strong> pour se présenter.<br><strong>#annonces</strong> pour ne rien rater.<br><strong>#discussion</strong> pour parler de tout et de rien.</p></div>
      <div class="card"><h3>Cubing</h3><p><strong>#temps-et-pbs</strong> pour partager ses temps et ses records.<br><strong>#aide</strong> pour poser ses questions.<br><strong>#compétitions</strong> et <strong>#wca-comps</strong> pour les compétitions du serveur et les compétitions officielles.<br><strong>#bots-poubelle</strong> pour tester les bots.</p></div>
    </div>
    <p style="margin-top:20px">Il y a aussi un salon vocal <strong>Général</strong>.</p>
  </div>
</section>

<section id="roles">
  <div class="wrap">
    <h2>Les rôles par niveau</h2>
    <p>Le rôle dépend de la moyenne (« ao »). Il se prend dans le salon <strong>#rôles</strong>.</p>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Rôle</th><th>Ce qu’il faut montrer</th></tr></thead>
        <tbody>
          <tr><td><kbd>sup-1</kbd></td><td>Rien, c’est le point de départ</td></tr>
          <tr><td><kbd>sub-1</kbd> <kbd>sub-50</kbd> <kbd>sub-40</kbd></td><td>Un ao50</td></tr>
          <tr><td><kbd>sub-30</kbd> <kbd>sub-25</kbd> <kbd>sub-20</kbd> <kbd>sub-15</kbd> <kbd>sub-12</kbd> <kbd>sub-10</kbd></td><td>Un ao100</td></tr>
          <tr><td><kbd>sub-9</kbd></td><td>Un ao500</td></tr>
        </tbody>
      </table>
    </div>
    <div class="note">
      <p><strong>Un AoX, c’est quoi ?</strong> La moyenne élaguée sur X temps (Average of X) : 5 % des meilleurs et 5 % des pires temps sont retirés pour que le résultat soit plus représentatif. Exemples : ao5 (meilleur et pire temps retirés), ao12, ao25, ao50, etc.</p>
    </div>
    <p class="muted">« sub-X » veut dire « sous X secondes » : un sub-30 fait moins de 30 secondes de moyenne. Le « sub-1 » est sous la minute.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>Projets à venir et autres serveurs</h2>
    <div class="grid c2">
      <div class="card"><h3>Sessions, tournois, cubes</h3><p>Des rencontres, des tournois et une sélection de cubes à prix réduit sont envisagés, sans rien de fixé. <a href="index.html">Voir les projets à venir</a>.</p></div>
      <div class="card"><h3>Acheter un cube</h3><p>Le <a href="cubes.html">guide d’achat</a> explique quel cube choisir et où le commander.</p></div>
      <div class="card"><h3>Un autre serveur à connaître</h3><p><a href="{DISCORD_FR}">Cubeurs Francophones</a> réunit toute la communauté francophone du speedcubing : plus de 1 000 membres, ouvert depuis juin 2017.</p></div>
    </div>
  </div>
</section>
"""
page("communaute.html", "La communauté EpiCubers — salons, rôles, projets",
     "Présentation du serveur Discord EpiCubers : salons, rôles par niveau et projets à venir.", body)

# ---------------------------------------------------------------- CUBES
body = head("Quel cube acheter ?", "Un seul modèle conseillé, et comment éviter de payer la marge d’une boutique.") + f"""
<section>
  <div class="wrap">
    <h2>Les meilleurs cubes sont fabriqués en Chine</h2>
    <p class="lead">Les meilleures marques de speedcubes (MoYu, GAN, Dayan, QiYi…) fabriquent leurs cubes en Chine. La meilleure chose à faire est donc de les commander directement là-bas, sur AliExpress par exemple.</p>
    <p>Les boutiques françaises et américaines, elles, achètent ces cubes pour les revendre avec leur marge, et affichent parfois le double du prix d’origine. Pour un cube qui coûte quelques euros à produire, la différence se voit vite.</p>
    <div class="note">
      <p><strong>À savoir avant de commander hors de l’Union européenne.</strong> La livraison est plus longue. S’y ajoutent la TVA et, depuis le 1er juillet 2026, un droit de douane forfaitaire de 3 € par produit pour les colis de moins de 150 € (<a href="https://www.quechoisir.org/actualite-shein-temu-aliexpress-les-petits-colis-bientot-taxes-en-europe-n173386/">source : Que Choisir</a>). Mieux vaut aussi commander dans la boutique officielle de la marque, pour éviter les contrefaçons.</p>
    </div>
    <div class="note">
      <p><strong>L’exception : Atoutcubes.</strong> Cette boutique française (basée à Bayonne, stock en France) vend le Dayan Guhong à un prix correct, 15,90 € au 25 octobre 2026, avec une livraison en 1 à 3 jours ouvrés. Dans ce cas, passer par elle vaut quand même le coup. Les prix peuvent changer : <a href="{ATOUT_GUHONG}">voir la fiche sur Atoutcubes</a>.</p>
    </div>
    <div class="note">
      <p><strong>Pour tous les autres cubes :</strong> toujours comparer le prix en boutique avec celui d’AliExpress, pour voir si on ne se fait pas arnaquer. Si l’écart est important, mieux vaut le prendre sur AliExpress.</p>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>Le cube conseillé : Dayan Guhong M, en MagLev</h2>
    <p>Un seul cube est conseillé, volontairement : son rapport qualité-prix est dingue, et choisir entre dix modèles ne sert à rien quand l’un d’eux fait déjà tout bien. La version à prendre est la <strong>MagLev</strong>.</p>
    <div class="pick">
      <figure>
        <img src="assets/guhong-pro-m.jpg" onerror="this.onerror=null;this.src='assets/cube.svg'" alt="Le Dayan Guhong M 3x3, face blanche, faces verte et rouge" width="800" height="800">
      </figure>
      <div>
        <p class="price">Environ 16 €</p>
        <ul class="clean">
          <li><strong>MagLev</strong> : 94 aimants et aucun ressort.</li>
          <li>Tension réglable.</li>
          <li>Stickerless, finition brillante.</li>
          <li>Trois tailles : 54, 55 ou 56 mm.</li>
        </ul>
        <p class="muted">Selon les boutiques, il s’appelle « Guhong Pro M » ou « Guhong Pro+ M » : tant que c’est un Guhong M, c’est le bon. Prix relevé chez Atoutcubes le 25 octobre 2026 (la fiche n’indique pas de prix distinct pour le MagLev). Les caractéristiques viennent de sa fiche.</p>
        <div class="btns"><a class="btn primary" href="{ATOUT_GUHONG}">Voir sur Atoutcubes</a></div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>Magnétique, MagLev… de quoi parle-t-on ?</h2>
    <p>Quelques mots reviennent dans toutes les fiches de cubes. Les voici en clair.</p>
    <dl class="brands">
      <dt>Cube magnétique</dt>
      <dd>Des aimants sont placés dans les pièces. Ils aident chaque face à se caler exactement après un quart de tour, ce qui rend les rotations plus précises.</dd>
      <dt>Aimants de noyau (core magnets)</dt>
      <dd>Des aimants situés dans le noyau, au centre du cube, qui retiennent les pièces. Selon les modèles, leur force est réglable : plus elle est élevée, plus le cube « s’accroche » à chaque position.</dd>
      <dt>Ressorts et compression</dt>
      <dd>Sur un cube classique, des ressorts maintiennent les pièces ensemble. Les vis règlent la compression : plus elle est forte, plus le cube est serré.</dd>
      <dt>Tension</dt>
      <dd>La façon dont les pièces sont tenues entre elles : un cube tendu est plus contrôlable, un cube lâche tourne plus librement mais risque de « popper ». Sur le Guhong, elle se règle avec une molette.</dd>
      <dt>MagLev (lévitation magnétique)</dt>
      <dd>Une technologie qui remplace les ressorts par des aimants, qui assurent la compression à leur place. Il y a moins de frottements, donc un cube plus libre et plus rapide. C’est ce qui rend la version MagLev du Guhong si intéressante pour son prix.</dd>
    </dl>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>Quelle taille choisir ?</h2>
    <p>La taille ne change pas la qualité du cube, seulement le confort. Le plus simple est de partir de la taille d’un cube qu’on a déjà et qui convient.</p>
    <div class="grid c3">
      <div class="card size"><h3>54 mm</h3><p>Le plus compact. Il convient aux petites mains et à la résolution à une main (OH).</p></div>
      <div class="card size"><h3>55 mm</h3><p>Le plus polyvalent. En cas de doute, c’est le choix le plus sûr.</p></div>
      <div class="card size"><h3>56 mm</h3><p>La taille standard des speedcubes, plus stable dans de grandes mains.</p></div>
    </div>
    <p style="margin-top:20px">Pour comparer, rien ne vaut de tenir un cube d’un autre membre. Et en cas d’hésitation, la question peut se poser dans <strong>#aide</strong>.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>Les marques en deux mots</h2>
    <dl class="brands">
      <dt>Rubik’s</dt>
      <dd>La marque que tout le monde connaît, et la pire pour la rapidité : ses cubes sont pensés pour le jeu, pas pour aller vite.</dd>
      <dt>MoYu</dt>
      <dd>Le Samsung des Rubik’s cubes : une marque très répandue, avec un modèle pour tous les budgets.</dd>
      <dt>GAN</dt>
      <dd>Le Apple des Rubik’s cubes : des cubes très aboutis, mais souvent plus chers.</dd>
    </dl>
    <p style="margin-top:20px">Aucune autre marque n’est conseillée ici : pour débuter comme pour progresser, le Guhong M en MagLev suffit. Pour tout autre cube, comparer toujours avec le prix d’AliExpress.</p>
  </div>
</section>
"""
page("cubes.html", "Quel speedcube acheter ? — EpiCubers",
     "Le cube conseillé (Dayan Guhong M en MagLev), comment choisir la taille, où le commander et pourquoi éviter les marges des boutiques.", body)

# ---------------------------------------------------------------- METHODES (page de comparaison)
body = head("Les méthodes", "Trois niveaux, du premier cube résolu aux temps de compétition.") + """
<section>
  <div class="wrap">
    <p class="lead">Chaque méthode a son nombre d’algorithmes et son temps typique. On peut rester sur la première aussi longtemps qu’on veut : le passage à la suivante se fait quand la précédente est devenue automatique.</p>

    <div class="method" style="--c:var(--green)">
      <h2>1. Méthode débutant</h2>
      <p class="level">Facile</p>
      <ul class="stats"><li>3<small>algorithmes simples</small></li><li>40 s à plus d’1 min<small>temps typique</small></li></ul>
      <p>Pour résoudre le cube la première fois, sans surcharger la mémoire. La version du serveur n’utilise que trois algorithmes, dont un très court : le sexy move.</p>
      <div class="btns"><a class="btn primary" href="methode-debutant.html">Voir la méthode débutant</a></div>
    </div>

    <div class="method" style="--c:var(--yellow)">
      <h2>2. CFOP simplifiée</h2>
      <p class="level">Intermédiaire · aussi appelée Fridrich simplifiée</p>
      <ul class="stats"><li>14<small>algorithmes</small></li><li>15 à 25 s<small>temps typique</small></li></ul>
      <p>La CFOP (Cross, F2L, OLL, PLL) avec seulement les algorithmes essentiels. Trois vidéos guident chaque étape.</p>
      <div class="btns"><a class="btn primary" href="cfop-simplifiee.html">Voir la CFOP simplifiée</a></div>
    </div>

    <div class="method" style="--c:var(--red)">
      <h2>3. CFOP complète</h2>
      <p class="level">Difficile · aussi appelée méthode Fridrich</p>
      <ul class="stats"><li>78 à 160<small>algorithmes</small></li><li>5 à 15 s<small>temps typique</small></li></ul>
      <p>La méthode des cubeurs rapides. Tous les algorithmes sont recensés sur SpeedCubeDB.</p>
      <div class="btns"><a class="btn primary" href="cfop.html">Voir la CFOP complète</a></div>
    </div>
  </div>
</section>
"""
page("methodes.html", "Les trois méthodes de résolution — EpiCubers",
     "Méthode débutant, CFOP simplifiée et CFOP complète : nombre d’algorithmes, temps typique et ressources pour chaque niveau.", body)

# ---------------------------------------------------------------- METHODE DEBUTANT
M_SEXY = "R U R' U'"
steps = []


def step(n, color, title, inner):
    steps.append(f"""<section><div class="wrap"><div class="step"><div class="step-num" style="--c:var(--{color})">{n}</div><div>
<h2>{title}</h2>
{inner}
</div></div></div></section>""")


step(1, "white", "La croix blanche",
     """<p>Pas d’algorithme ici : tout se fait en regardant le cube. Placer les quatre arêtes blanches autour du centre blanc, puis tourner chacune pour que sa deuxième couleur soit alignée avec le centre de sa face. Cela donne une croix blanche dont chaque arête correspond au centre voisin.</p>
<p>Ensuite, <strong>retourner le cube</strong> : la croix blanche passe en bas et y reste pour la suite.</p>""")

step(2, "blue", "Les coins blancs",
     """<p>Chercher un coin blanc dans la couche du haut. Tourner la face du haut (U) pour l’amener juste au-dessus de sa place, c’est-à-dire entre les deux centres qui correspondent à ses deux autres couleurs. Tourner ensuite tout le cube pour que cette place soit en bas à droite, face à soi, puis répéter le sexy move jusqu’à ce que le blanc soit en bas.</p>"""
     + algo("Le sexy move", M_SEXY, note="À répéter 1 à 5 fois jusqu’à ce que le coin soit en place. C’est l’algorithme le plus utilisé de la méthode.")
     + """<p>Faire de même pour les quatre coins. La première couche (le blanc) est terminée.</p>""")

step(3, "green", "La deuxième couronne",
     """<p>La face jaune est en haut. Chercher dans la couche du haut une arête sans jaune. Tourner U pour que sa couleur de face s’aligne avec le centre de la face de devant, puis regarder si l’arête doit aller à droite ou à gauche.</p>"""
     + algo("Arête vers la droite", "U R U' R' U' F' U F")
     + algo("Arête vers la gauche", "U' L' U L U F U' F'")
     + """<p>Faire de même pour les quatre arêtes. Si une arête est déjà dans la deuxième couronne mais mal placée, utiliser l’algorithme avec n’importe quelle arête du haut pour la faire sortir, puis recommencer.</p>""")

step(4, "yellow", "La croix jaune",
     """<p>Regarder la face jaune : on voit un point, un « L », une barre ou déjà une croix. Tourner le cube pour mettre le « L » en haut à gauche, ou la barre à l’horizontale, puis faire l’algorithme. Recommencer jusqu’à obtenir une croix.</p>"""
     + algo("La croix jaune", "F R U R' U' F'", note="C’est le sexy move entouré de F et F'. Depuis un point, l’enchaîner deux ou trois fois : point, puis L, puis barre, puis croix.")
     )

step(5, "orange", "Les arêtes jaunes",
     """<p>Tourner la face du haut jusqu’à ce que le plus d’arêtes possible correspondent à la couleur de leur centre. Si deux arêtes voisines sont bonnes, les placer à l’arrière et à droite, puis faire l’algorithme. Si deux arêtes opposées sont bonnes, faire l’algorithme une fois depuis n’importe quel côté, puis reprendre depuis le cas précédent. Répéter jusqu’à ce que les quatre arêtes soient alignées.</p>"""
     + algo("Aligner les arêtes", "R U R' U R U2 R' U"))

step(6, "red", "Les coins jaunes",
     """<p><strong>Retourner le cube</strong> : la face jaune passe en bas. Placer les coins jaunes un par un : tourner D pour amener le coin au-dessus de son emplacement, puis répéter le sexy move jusqu’à ce que le coin soit en place. Les couches du haut se mélangent en route, c’est normal.</p>"""
     + algo("Le sexy move, encore", M_SEXY, player=False)
     + """<h3>Le cas particulier</h3>
<p>Il peut rester deux coins côte à côte qui ne sont pas résolus. Il suffit de refaire la même chose : les placer en bas, puis répéter le sexy move jusqu’à ce qu’ils soient bien placés.</p>
<p>Un dernier quart de tour de D aligne la couche du bas. Le cube est résolu.</p>""")

notation = """
<section>
  <div class="wrap">
    <h2>La méthode en bref</h2>
    <p>Six étapes, et seulement <strong>trois algorithmes</strong> à retenir :</p>
    <ul class="clean">
      <li>le <strong>sexy move</strong> <kbd>R U R' U'</kbd>, utilisé pour les coins blancs, la croix jaune (entouré de F et F') et les coins jaunes ;</li>
      <li>l’algorithme de la <strong>deuxième couronne</strong>, avec sa version miroir ;</li>
      <li>l’algorithme des <strong>arêtes jaunes</strong>, <kbd>R U R' U R U2 R' U</kbd>.</li>
    </ul>
    <h2 style="margin-top:36px">Lire les algorithmes</h2>
    <p>Les lettres des algorithmes suivent la notation internationale. <a href="notation.html">La page Notation</a> l’explique en détail, avec des animations.</p>
    <p>Chaque lettre est une face du cube, vue de face : <kbd>R</kbd> droite, <kbd>L</kbd> gauche, <kbd>U</kbd> haut, <kbd>D</kbd> bas, <kbd>F</kbd> devant, <kbd>B</kbd> derrière. Une lettre seule, c’est un quart de tour dans le sens des aiguilles d’une montre en regardant cette face. Une apostrophe (<kbd>R'</kbd>) inverse le sens, et un 2 (<kbd>U2</kbd>) fait un demi-tour.</p>
    <p>Chaque algorithme est animé en 3D : un appui sur lecture montre la séquence, et le cube peut être tourné en le faisant glisser.</p>
  </div>
</section>
"""

tutos = """
<section>
  <div class="wrap">
    <h2>Pour aller plus loin en vidéo</h2>
    <p>Ces vidéos montrent la méthode débutant classique. Elle ressemble à celle-ci, sauf pour la fin (placement des coins).</p>
    <div class="grid c2">
      <a class="card" href="https://youtu.be/7Ron6MN45LY"><h3>Méthode débutant, en anglais</h3><p>La version conseillée de préférence.</p><span class="go">Voir sur YouTube</span></a>
      <a class="card" href="https://youtu.be/PLsT1SY1cgg"><h3>Méthode débutant, en français</h3><p>Pour suivre dans sa langue.</p><span class="go">Voir sur YouTube</span></a>
    </div>
    <p style="margin-top:24px">Quand le cube se résout en moins d’une minute et qu’on veut aller plus vite, la suite est la <a href="cfop-simplifiee.html">CFOP simplifiée</a>.</p>
  </div>
</section>
"""
body = head("Méthode débutant", "Résoudre le cube avec très peu d’algorithmes.") + notation + "\n".join(steps) + tutos
page("methode-debutant.html", "Méthode débutant — résoudre le Rubik’s cube — EpiCubers",
     "Une méthode pour résoudre le Rubik’s cube avec trois algorithmes, avec animations 3D de chaque séquence.",
     body, head_extra=TWISTY, active="methodes.html")

# ---------------------------------------------------------------- CFOP SIMPLIFIEE
body = head("CFOP simplifiée", "14 algorithmes, entre 15 et 25 secondes.") + """
<section>
  <div class="wrap">
    <h2>En deux mots</h2>
    <p class="lead">La CFOP (ou méthode Fridrich) se résout en quatre étapes : Cross, F2L, OLL et PLL. La version simplifiée ne retient qu’un petit nombre d’algorithmes par étape, 14 en tout, pour atteindre des temps de 15 à 25 secondes sans avoir à tout apprendre.</p>
    <ul class="stats"><li>14<small>algorithmes</small></li><li>15 à 25 s<small>temps typique</small></li></ul>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>Les vidéos, étape par étape</h2>
    <div class="grid c3">
      <a class="card" href="https://youtu.be/Ar_Zit1VLG0"><h3>F2L</h3><p>Placer les deux premières couronnes.</p><span class="go">Voir la vidéo</span></a>
      <a class="card" href="https://youtu.be/GhmYBgLoQQg"><h3>OLL</h3><p>Orienter la dernière couche.</p><span class="go">Voir la vidéo</span></a>
      <a class="card" href="https://youtu.be/f_Yor-ydZjs"><h3>PLL</h3><p>Permuter la dernière couche.</p><span class="go">Voir la vidéo</span></a>
    </div>
    <p style="margin-top:24px">Un cas qui ne passe pas ? Le salon <strong>#aide</strong> du Discord est là pour ça.</p>
    <div class="btns"><a class="btn" href="methodes.html">Retour aux méthodes</a><a class="btn" href="cfop.html">Voir la CFOP complète</a></div>
  </div>
</section>
"""
page("cfop-simplifiee.html", "CFOP simplifiée : 14 algorithmes — EpiCubers",
     "La CFOP simplifiée en 14 algorithmes, avec les vidéos pour le F2L, l’OLL et le PLL.", body, active="methodes.html")

# ---------------------------------------------------------------- CFOP
body = head("CFOP complète", "La méthode des cubeurs rapides : 78 à 160 algorithmes, 5 à 15 secondes.") + """
<section>
  <div class="wrap">
    <h2>En deux mots</h2>
    <p class="lead">La CFOP (ou méthode Fridrich) se résout en quatre étapes. Elle demande beaucoup plus d’algorithmes que les méthodes précédentes, mais bien moins de mouvements.</p>
    <ul class="stats"><li>78 à 160<small>algorithmes</small></li><li>5 à 15 s<small>temps typique</small></li></ul>
    <div class="grid c2">
      <div class="card"><h3>C comme Cross</h3><p>La croix, faite intuitivement, idéalement en 8 mouvements ou moins.</p></div>
      <div class="card"><h3>F2L</h3><p>Placer ensemble un coin et son arête pour finir les deux premières couronnes. Beaucoup de cas se trouvent à l’intuition.</p></div>
      <div class="card"><h3>OLL</h3><p>Orienter la dernière couche : toute la face jaune de la même couleur.</p></div>
      <div class="card"><h3>PLL</h3><p>Permuter la dernière couche : remettre les pièces jaunes à leur place.</p></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>Tous les algorithmes</h2>
    <p>Les algorithmes de la CFOP sont recensés, classés et animés sur SpeedCubeDB. Ils ne sont pas recopiés ici : mieux vaut les prendre à la source.</p>
    <div class="btns"><a class="btn primary" href="https://speedcubedb.com/">Ouvrir SpeedCubeDB</a></div>
    <p style="margin-top:24px">Avant de se lancer, la <a href="cfop-simplifiee.html">CFOP simplifiée</a> est une bonne étape intermédiaire.</p>
    <div class="btns"><a class="btn" href="methodes.html">Retour aux méthodes</a></div>
  </div>
</section>
"""
page("cfop.html", "CFOP complète : la méthode Fridrich — EpiCubers",
     "La CFOP complète en quatre étapes, avec un renvoi vers SpeedCubeDB pour tous les algorithmes.", body, active="methodes.html")


# ---------------------------------------------------------------- NOTATION
def demo(moves, title, text):
    return f"""<div class="card demo">
  <h3><code class="mv">{title}</code></h3>
  <p>{text}</p>
  <div class="player-box"><twisty-player alg="{moves}" visualization="3D" background="none" control-panel="bottom-row" hint-facelets="none"></twisty-player></div>
</div>"""


NET = """<svg class="net" viewBox="0 0 250 190" role="img" aria-labelledby="net-t net-d">
<title id="net-t">Les six faces du cube à plat</title>
<desc id="net-d">U en haut, puis L, F, R et B en ligne, puis D en bas.</desc>
<g font-family="JetBrains Mono, monospace" font-size="26" font-weight="700" text-anchor="middle" fill="#15132a" stroke="#15132a" stroke-width="3" stroke-linejoin="round">
<rect x="65" y="5" width="55" height="55" rx="6" fill="#f4f4f4"/><text x="92.5" y="43" stroke="none">U</text>
<rect x="5" y="65" width="55" height="55" rx="6" fill="#dc7f1a"/><text x="32.5" y="103" stroke="none">L</text>
<rect x="65" y="65" width="55" height="55" rx="6" fill="#18c52b"/><text x="92.5" y="103" stroke="none">F</text>
<rect x="125" y="65" width="55" height="55" rx="6" fill="#d91c1c"/><text x="152.5" y="103" stroke="none">R</text>
<rect x="185" y="65" width="55" height="55" rx="6" fill="#1a87db"/><text x="212.5" y="103" stroke="none">B</text>
<rect x="65" y="125" width="55" height="55" rx="6" fill="#d8cb1a"/><text x="92.5" y="163" stroke="none">D</text>
</g></svg>"""

body = head("La notation", "Lire un algorithme : les lettres, les apostrophes et les chiffres.") + f"""
<section>
  <div class="wrap">
    <h2>Les six faces</h2>
    <p class="lead">Chaque mouvement est décrit par une lettre : celle de la face qui tourne. C’est la notation internationale, la même partout dans le monde (WCA, SpeedCubeDB, csTimer…).</p>
    <div class="pick">
      <figure style="background:var(--ink-3)">{NET}</figure>
      <div>
        <p>Le cube se tient avec la face <strong>F</strong> (Front) tournée vers soi et la face <strong>U</strong> (Up) sur le dessus. Les autres faces s’en déduisent.</p>
        <div class="table-wrap"><table>
          <thead><tr><th>Lettre</th><th>Anglais</th><th>Face</th></tr></thead>
          <tbody>
            <tr><td><kbd>U</kbd></td><td>Up</td><td>Dessus</td></tr>
            <tr><td><kbd>D</kbd></td><td>Down</td><td>Dessous</td></tr>
            <tr><td><kbd>F</kbd></td><td>Front</td><td>Devant</td></tr>
            <tr><td><kbd>B</kbd></td><td>Back</td><td>Derrière</td></tr>
            <tr><td><kbd>R</kbd></td><td>Right</td><td>Droite</td></tr>
            <tr><td><kbd>L</kbd></td><td>Left</td><td>Gauche</td></tr>
          </tbody>
        </table></div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>Le sens du mouvement</h2>
    <p>Une lettre seule, c’est un <strong>quart de tour dans le sens des aiguilles d’une montre</strong>, en regardant la face concernée de face. C’est le point de vue de cette face qui compte, pas celui de la personne qui tient le cube : pour <kbd>L</kbd> ou <kbd>B</kbd>, le sens a l’air inversé vu de devant.</p>
    <ul class="clean">
      <li>une <strong>apostrophe</strong> (<kbd>R'</kbd>, qui se lit « R prime ») : quart de tour dans l’autre sens ;</li>
      <li>un <strong>2</strong> (<kbd>R2</kbd>) : demi-tour. Le sens n’a pas d’importance, <kbd>R2</kbd> et <kbd>R2'</kbd> sont identiques.</li>
    </ul>
    <p>Le bouton de lecture de chaque animation part d’un cube résolu et montre le mouvement. Le cube se fait tourner en le faisant glisser.</p>
    <div class="grid c3">
      {demo("R", "R", "La face de droite fait un quart de tour horaire : le côté qui fait face monte.")}
      {demo("R'", "R'", "Le même quart de tour, dans l’autre sens : le côté qui fait face descend.")}
      {demo("R2", "R2", "Un demi-tour de la face de droite.")}
      {demo("U", "U", "La face du dessus tourne : le devant part vers la gauche.")}
      {demo("F", "F", "La face de devant tourne dans le sens horaire, comme vue de face.")}
      {demo("L", "L", "La face de gauche, horaire vue depuis la gauche : le côté qui fait face descend.")}
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>Lire un algorithme</h2>
    <p>Un algorithme se lit de gauche à droite, un mouvement après l’autre. Les espaces séparent les mouvements.</p>
    <p>Le sexy move <kbd>R U R' U'</kbd> se lit : <em>R</em>, puis <em>U</em>, puis <em>R'</em>, puis <em>U'</em>.</p>
    <div class="algo">
      <div class="algo-top"><span class="algo-name">Le sexy move</span><button class="copy" type="button">Copier</button></div>
      <code>R U R' U'</code>
      <div class="player-box"><twisty-player alg="R U R' U'" visualization="3D" background="none" control-panel="bottom-row" hint-facelets="none"></twisty-player></div>
    </div>
    <p>Des <strong>parenthèses</strong> regroupent une séquence, et un chiffre derrière indique combien de fois la répéter : <kbd>(R U R' U')3</kbd> veut dire le sexy move trois fois de suite.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>Les autres mouvements</h2>
    <h3>Les mouvements larges</h3>
    <p>Une lettre minuscule (<kbd>r</kbd>) ou suivie d’un <kbd>w</kbd> (<kbd>Rw</kbd>) fait tourner la face <strong>et la couche du milieu</strong> en même temps, dans le même sens que la face. Les deux écritures sont équivalentes, avec l’apostrophe et le 2 qui s’utilisent pareil (<kbd>Rw'</kbd>, <kbd>r2</kbd>).</p>
    <div class="grid c3">
      {demo("Rw", "Rw  ou  r", "Les deux couches de droite tournent ensemble, dans le sens de R.")}
      {demo("Uw", "Uw  ou  u", "Les deux couches du haut tournent ensemble, dans le sens de U.")}
    </div>

    <h3 style="margin-top:36px">Les tranches</h3>
    <p>Trois lettres désignent la couche du milieu, celle qui n’a pas de face à elle :</p>
    <ul class="clean">
      <li><kbd>M</kbd> (Middle) : entre L et R, dans le sens de <kbd>L</kbd> ;</li>
      <li><kbd>E</kbd> (Equator) : entre U et D, dans le sens de <kbd>D</kbd> ;</li>
      <li><kbd>S</kbd> (Standing) : entre F et B, dans le sens de <kbd>F</kbd>.</li>
    </ul>
    <div class="grid c3">
      {demo("M", "M", "La tranche du milieu entre gauche et droite, dans le sens de L.")}
      {demo("E", "E", "La tranche entre le dessus et le dessous, dans le sens de D.")}
      {demo("S", "S", "La tranche entre le devant et le derrière, dans le sens de F.")}
    </div>

    <h3 style="margin-top:36px">Les rotations du cube entier</h3>
    <p>Trois lettres minuscules font tourner <strong>tout le cube</strong>, sans changer sa résolution : <kbd>x</kbd> dans le sens de <kbd>R</kbd>, <kbd>y</kbd> dans le sens de <kbd>U</kbd> et <kbd>z</kbd> dans le sens de <kbd>F</kbd>. L’apostrophe et le 2 s’utilisent pareil (<kbd>x'</kbd>, <kbd>y2</kbd>). Elles servent à changer la face tenue devant ou dessus, par exemple pour retourner le cube avec <kbd>x2</kbd>.</p>
    <div class="grid c3">
      {demo("x", "x", "Tout le cube tourne comme R : la face de devant passe sur le dessus.")}
      {demo("y", "y", "Tout le cube tourne comme U : la face de devant passe à gauche.")}
      {demo("z", "z", "Tout le cube tourne comme F : la face de droite passe sur le dessus.")}
    </div>
    <div class="note"><p>Sur les cubes plus grands (4x4 et plus), un chiffre devant la lettre désigne une couche intérieure, par exemple <kbd>2R</kbd>. Cela ne sert pas sur un 3x3.</p></div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>Pour s’exercer</h2>
    <p>Le site <a href="https://alg.cubing.net/">alg.cubing.net</a> anime n’importe quel algorithme saisi : un bon moyen de vérifier qu’une séquence a été bien lue. Les algorithmes de la <a href="methode-debutant.html">méthode débutant</a> sont tous écrits dans cette notation.</p>
    <div class="btns"><a class="btn primary" href="methode-debutant.html">Voir la méthode débutant</a><a class="btn" href="glossaire.html">Le glossaire</a></div>
  </div>
</section>
"""
page("notation.html", "La notation du Rubik’s cube — EpiCubers",
     "La notation internationale du Rubik’s cube : faces, quarts de tour, apostrophes, mouvements larges, tranches et rotations, avec animations 3D.",
     body, head_extra=TWISTY)

# ---------------------------------------------------------------- LIENS
body = head("Liens utiles", "Les sites que tout cubeur finit par avoir en favori.") + f"""
<section>
  <div class="wrap">
    <div class="grid c2">
      <a class="card" href="https://www.worldcubeassociation.org/"><h3>World Cube Association</h3><p>Le site officiel des compétitions. Les prochaines compétitions dans le monde, l’inscription, les résultats, les classements et le profil de chaque compétiteur.</p><span class="go">worldcubeassociation.org</span></a>
      <a class="card" href="https://cstimer.net/"><h3>csTimer</h3><p>Un chronomètre très complet, avec des mélanges officiels, de nombreuses statistiques et beaucoup d’options.</p><span class="go">cstimer.net</span></a>
      <a class="card" href="https://cubedesk.io/"><h3>CubeDesk</h3><p>Un chronomètre en ligne qui propose en plus des duels 1v1, un entraîneur d’algorithmes, des classements et des mini-jeux. Un compte est nécessaire pour sauvegarder ses résolutions. Pour certains, il a un peu dépassé csTimer, même si csTimer reste la référence.</p><span class="go">cubedesk.io</span></a>
      <a class="card" href="https://speedcubedb.com/"><h3>SpeedCubeDB</h3><p>Une immense base de données : des milliers d’algorithmes, classés par étape et par méthode, pour s’améliorer.</p><span class="go">speedcubedb.com</span></a>
      <a class="card" href="https://www.speedsolving.com/wiki/index.php/Main_Page"><h3>Le wiki de SpeedSolving</h3><p>Le « Wikipédia du speedcubing » : méthodes, tutoriels, histoire, matériel.</p><span class="go">speedsolving.com</span></a>
      <a class="card" href="https://alg.cubing.net/"><h3>alg.cubing.net</h3><p>Pour reconstruire une résolution. Le cube 3D suit les mouvements saisis, ce qui est idéal pour analyser un solve.</p><span class="go">alg.cubing.net</span></a>
      <a class="card" href="{DISCORD_FR}"><h3>Cubeurs Francophones</h3><p>Le serveur Discord de toute la communauté francophone du speedcubing : plus de 1 000 membres depuis juin 2017.</p><span class="go">Rejoindre le serveur</span></a>
    </div>
    <p style="margin-top:28px">Les guides de ce site : <a href="methodes.html">les trois méthodes</a> et <a href="cubes.html">le choix du cube</a>.</p>
  </div>
</section>
"""
page("liens.html", "Liens utiles du speedcubing — EpiCubers",
     "WCA, csTimer, SpeedCubeDB, wiki de SpeedSolving, alg.cubing.net : les sites utiles pour progresser.", body)

# ---------------------------------------------------------------- GLOSSAIRE
G = [
    ("Aimants de noyau (core magnets)", "Des aimants situés dans le noyau du cube, qui retiennent les pièces. Leur force est parfois réglable."),
    ("Algo (algorithme)", "Une séquence de mouvements à connaître par cœur, qui produit un effet précis sur le cube."),
    ("AoX", "Average of X : moyenne élaguée sur X temps, avec les meilleurs et les pires temps retirés. Exemples : ao5, ao12, ao100."),
    ("ao5", "La moyenne officielle d’une compétition sur le 3x3 : on retire le meilleur et le pire de cinq résolutions, et on fait la moyenne des trois autres."),
    ("BLD", "Blindfolded : résoudre le cube les yeux bandés, après l’avoir mémorisé."),
    ("CFOP", "Cross, F2L, OLL, PLL. La méthode la plus utilisée par les cubeurs rapides, aussi appelée méthode Fridrich."),
    ("Corner cutting", "La capacité d’un cube à tourner une face même quand elle n’est pas parfaitement alignée."),
    ("Cross", "La croix : la première étape de la CFOP, avec quatre arêtes d’une même couleur autour du centre."),
    ("DNF", "Did Not Finish : résolution non valide, par exemple quand le cube n’est pas résolu à la fin."),
    ("F2L", "First Two Layers : les deux premières couronnes, résolues en plaçant ensemble un coin et son arête."),
    ("FMC", "Fewest Moves Challenge : trouver la solution la plus courte possible, sans cube, sur papier."),
    ("Inspection", "Les 15 secondes avant le chrono, pendant lesquelles on regarde le cube sans le toucher."),
    ("Lookahead", "Repérer la prochaine pièce à placer pendant qu’on exécute la précédente, pour ne pas s’arrêter."),
    ("Lubrifiant", "Un produit qu’on met à l’intérieur du cube pour le faire tourner plus vite et plus doucement."),
    ("Magnétique", "Un cube équipé d’aimants dans les pièces, qui l’aident à se centrer sur chaque face."),
    ("MagLev", "Une technologie qui remplace les ressorts d’un cube par des aimants, pour réduire les frottements."),
    ("Ressorts", "Sur un cube classique, ils maintiennent les pièces ensemble. Un cube MagLev n’en a pas."),
    ("Tension / compression", "Le serrage des pièces entre elles, réglable avec des vis ou une molette selon le modèle."),
    ("Mélange (scramble)", "La suite de mouvements générée au hasard qu’on applique avant chaque résolution."),
    ("Notation", "Le système de lettres (R, U, F…) qui décrit les mouvements. <a href=\"notation.html\">Voir la page Notation</a>."),
    ("OH", "One-handed : résolution à une main."),
    ("OLL", "Orientation of the Last Layer : mettre toute la dernière face de la même couleur."),
    ("PB (personal best)", "Le meilleur temps personnel, en single ou en moyenne."),
    ("PLL", "Permutation of the Last Layer : remettre les pièces de la dernière couche à leur place."),
    ("Pop", "Quand une pièce du cube sort de son emplacement pendant une résolution. Les cubes réglés trop lâches en font plus."),
    ("Roux, ZZ", "Deux autres méthodes de résolution rapide, qui ne passent pas par la croix de la CFOP."),
    ("Sexy move", "L’algorithme R U R' U', utilisé dans la méthode débutant."),
    ("Single", "Une seule résolution, par opposition à une moyenne."),
    ("Stickerless", "Un cube dont les couleurs sont dans la masse du plastique, sans autocollants."),
    ("Sub-X", "Faire moins de X secondes. Un sub-20 fait en moyenne moins de 20 secondes."),
    ("TPS", "Turns per second : le nombre de mouvements par seconde. Pour un même nombre de mouvements, un TPS plus élevé donne un meilleur temps."),
    ("WCA", "World Cube Association : l’organisme qui gère les compétitions officielles de speedcubing et leurs records."),
    ("+2", "Pénalité de deux secondes quand le cube est résolu mais qu’une face reste décalée d’un quart de tour."),
]
dl = "\n".join(f"<dt>{t}</dt><dd>{d}</dd>" for t, d in G)
body = head("Glossaire", "Les mots du speedcubing, de A à Z.") + f"""
<section>
  <div class="wrap">
    <label for="gloss-search" class="muted">Chercher un mot</label><br>
    <input id="gloss-search" class="search" type="search" placeholder="ex. PLL, sub-20, ao5…" autocomplete="off">
    <dl class="gloss">
{dl}
    </dl>
  </div>
</section>
"""
page("glossaire.html", "Glossaire du speedcubing — EpiCubers",
     "Définition des termes du speedcubing : AoX, F2L, OLL, PLL, TPS, sub-X, WCA et plus.", body)

print("Pages générées.")
