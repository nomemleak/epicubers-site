#!/usr/bin/env python3
"""Génère les pages HTML du site EpiCubers à la racine du dépôt"""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

DISCORD = "https://discord.gg/vQwt4qZUBm"
DISCORD_FR = "https://discord.gg/MZ75mtHdGZ"

NAV = [
    ("index.html", "Accueil"),
    ("speedcubing.html", "Le speedcubing"),
    ("methode-debutant.html", "Méthode débutant"),
    ("cfop.html", "CFOP"),
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


def page(fname, title, desc, body, head_extra="", header_block=""):
    nav = "".join(
        '<a href="%s"%s>%s</a>' % (f, ' aria-current="page"' if f == fname else "", label)
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
{header_block}{body}
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
        <h3><span class="dot" style="background:var(--green)"></span>Je n’ai jamais résolu de cube</h3>
        <p>Une méthode avec très peu d’algorithmes à retenir. Compte entre 40 secondes et une minute une fois qu’elle est acquise.</p>
        <span class="go">Voir la méthode</span>
      </a>
      <a class="card" href="cubes.html">
        <h3><span class="dot" style="background:var(--blue)"></span>Je veux acheter un cube</h3>
        <p>Quels modèles prendre selon le budget, où les commander, et pourquoi éviter les cubes à 3 € sans marque.</p>
        <span class="go">Lire le guide d’achat</span>
      </a>
      <a class="card" href="communaute.html">
        <h3><span class="dot" style="background:var(--orange)"></span>Je veux rejoindre la commu</h3>
        <p>Les salons du serveur, les rôles par niveau, les sessions et les compétitions.</p>
        <span class="go">Découvrir la communauté</span>
      </a>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>Ce qu’on propose</h2>
    <div class="grid c2">
      <div class="card">
        <h3>Sessions cubing</h3>
        <p>Une des meilleures façons de s’améliorer, c’est de pratiquer. On organise des sessions pour échanger et s’entraîner à plusieurs. Des speedcubes sont disponibles sur place, et peuvent être offerts si ton temps de résolution progresse.</p>
      </div>
      <div class="card">
        <h3>Tournois et compétitions</h3>
        <p>Des tournois ouverts à tous, avec des prix à gagner. Ils se préparent et se suivent sur le serveur.</p>
      </div>
      <div class="card">
        <h3>Des cubes à prix réduit</h3>
        <p>Certains speedcubes de notre sélection sont vendus avec des prix avantageux, souvent à la moitié du prix des grands sites. L’idée : rendre la discipline accessible, et financer nos futurs projets.</p>
      </div>
      <div class="card">
        <h3>Une association, peut-être</h3>
        <p>Une association sur le même thème pourrait voir le jour. Si le projet t’intéresse ou que tu veux en faire partie, envoie un message privé sur le Discord.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>De « sup-1 » à « sub-9 »</h2>
    <p>Sur le serveur, ton rôle dépend de ta moyenne. Chacun commence quelque part, et la plupart des membres sont encore en bas de l’échelle.</p>
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
    <p><a href="communaute.html#roles">Comment obtenir ton rôle</a></p>
  </div>
</section>
"""
page("index.html", "EpiCubers — le serveur des speedcubeurs de l’école",
     "Communauté de speedcubing : méthode débutant, guide d’achat de cubes, sessions, compétitions et classement par niveau.",
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
    <h2>Les trois méthodes qu’on conseille</h2>
    <p>Le nombre d’algorithmes à apprendre grimpe vite quand on veut aller plus vite. Voici les trois paliers qu’on utilise sur le serveur.</p>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Niveau</th><th>Méthode</th><th>Algos</th><th>Temps typique</th></tr></thead>
        <tbody>
          <tr><td>Facile</td><td><a href="methode-debutant.html">Méthode débutant</a></td><td>Très peu d’algorithmes, tous courts</td><td>40 s à plus d’une minute</td></tr>
          <tr><td>Intermédiaire</td><td>CFOP simplifiée (Fridrich simplifiée)</td><td>14 algorithmes</td><td>15 à 25 s</td></tr>
          <tr><td>Difficile</td><td><a href="cfop.html">CFOP complète (méthode Fridrich)</a></td><td>78 à 160 algorithmes</td><td>5 à 15 s</td></tr>
        </tbody>
      </table>
    </div>
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
      <p>En compétition, tu as 15 secondes d’inspection avant de lancer le chrono. Un 3x3 se juge sur 5 résolutions : on retire la meilleure et la pire, et la moyenne des trois autres donne ton résultat (l’ « ao5 »). Un +2 ou un DNF peut s’ajouter en cas de pénalité.</p>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>S’entraîner</h2>
    <p>Quelques habitudes qui font vraiment progresser :</p>
    <ul class="clean">
      <li>se chronométrer avec des mélanges officiels, par exemple sur <a href="https://cstimer.net/">csTimer</a> ;</li>
      <li>regarder ses résolutions, pas seulement son temps : où est-ce que tu t’arrêtes ?</li>
      <li>apprendre un algorithme à la fois et le répéter jusqu’à ce qu’il passe tout seul ;</li>
      <li>venir aux sessions du serveur : voir quelqu’un d’autre tourner apprend plus que dix vidéos.</li>
    </ul>
    <p>Un jour, une compétition officielle ? Regarde les prochaines dates sur le <a href="https://www.worldcubeassociation.org/competitions">site de la WCA</a>. Sur le serveur, le salon <strong>wca-comps</strong> sert à les repérer et à s’organiser.</p>
    <div class="btns"><a class="btn primary" href="methode-debutant.html">Apprendre la méthode débutant</a><a class="btn" href="glossaire.html">Un mot t’échappe ? Le glossaire</a></div>
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
    <p>On y partage ses temps, on pose ses questions, on organise des sessions et des compétitions. Une association du même thème pourrait être créée prochainement : si tu veux en faire partie, contacte l’équipe en message privé sur le Discord.</p>
    <div class="btns"><a class="btn primary" href="{DISCORD}">Rejoindre EpiCubers</a></div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>Les salons</h2>
    <div class="grid c3">
      <div class="card"><h3>Pour s’y retrouver</h3><p><strong>#rôles</strong> pour prendre ton niveau.<br><strong>#à-propos</strong> et <strong>#utile</strong> pour les infos et les liens importants.</p></div>
      <div class="card"><h3>Général</h3><p><strong>#bienvenue</strong> pour se présenter.<br><strong>#annonces</strong> pour ne rien rater.<br><strong>#discussion</strong> pour parler de tout et de rien.</p></div>
      <div class="card"><h3>Cubing</h3><p><strong>#temps-et-pbs</strong> pour partager tes temps et tes records.<br><strong>#aide</strong> pour poser tes questions.<br><strong>#compétitions</strong> et <strong>#wca-comps</strong> pour les compétitions du serveur et les compétitions officielles.<br><strong>#bots-poubelle</strong> pour tester les bots.</p></div>
    </div>
    <p style="margin-top:20px">Il y a aussi un salon vocal <strong>Général</strong>, pratique pendant les sessions à distance.</p>
  </div>
</section>

<section id="roles">
  <div class="wrap">
    <h2>Les rôles par niveau</h2>
    <p>Ton rôle dépend de ta moyenne (« ao »). Va dans le salon <strong>#rôles</strong> pour le prendre.</p>
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
      <p><strong>Un AoX, c’est quoi ?</strong> La moyenne élaguée sur X temps (Average of X) : on retire 5 % des meilleurs et 5 % des pires temps pour que le résultat soit plus représentatif. Exemples : ao5 (meilleur et pire temps retirés), ao12, ao25, ao50, etc.</p>
    </div>
    <p class="muted">« sub-X » veut dire « sous X secondes » : un sub-30 fait moins de 30 secondes de moyenne. Le « sub-1 » est sous la minute.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>Sessions, tournois, cubes</h2>
    <div class="grid c2">
      <div class="card"><h3>Sessions cubing</h3><p>S’entraîner à plusieurs, échanger des astuces, essayer des cubes différents. Des speedcubes sont disponibles pendant les événements, et peuvent être offerts si ton temps s’améliore.</p></div>
      <div class="card"><h3>Tournois et compétitions</h3><p>Ouverts à tous, avec des prix à gagner. Les dates sont annoncées dans <strong>#annonces</strong> et <strong>#compétitions</strong>.</p></div>
      <div class="card"><h3>Cubes à prix avantageux</h3><p>Une sélection de speedcubes à prix réduit, parfois la moitié du prix des principaux sites. <a href="cubes.html">Voir le guide d’achat</a>.</p></div>
      <div class="card"><h3>Un autre serveur à connaître</h3><p><a href="{DISCORD_FR}">Cubeurs Francophones</a> réunit toute la communauté francophone du speedcubing : plus de 1 000 membres, ouvert depuis juin 2017.</p></div>
    </div>
  </div>
</section>
"""
page("communaute.html", "La communauté EpiCubers — salons, rôles, sessions",
     "Présentation du serveur Discord EpiCubers : salons, rôles par niveau, sessions cubing et compétitions.", body)

# ---------------------------------------------------------------- CUBES
body = head("Quel cube acheter ?", "Pour débuter, pour progresser, pour viser le haut niveau. Où l’acheter et pourquoi.") + """
<section>
  <div class="wrap">
    <h2>Ce qui compte vraiment</h2>
    <p class="lead">Un speedcube se choisit sur quelques critères, pas sur la marque seule.</p>
    <div class="grid c3">
      <div class="card"><h3>Des aimants</h3><p>Ils stabilisent les faces et évitent les rotations ratées. Même pour un petit budget, prends un cube déjà magnétisé.</p></div>
      <div class="card"><h3>Un cube de marque</h3><p>Les cubes sans nom à quelques euros ont une durée de vie imprévisible : stickers mal collés, tension inégale, vis tordues. Une vingtaine d’euros évite pas mal de déceptions.</p></div>
      <div class="card"><h3>Du lubrifiant</h3><p>Beaucoup de cubes arrivent presque secs. Un petit flacon de lubrifiant change complètement la sensation, surtout sur un modèle à petit prix.</p></div>
    </div>
    <div class="note"><p>Les prix et les modèles bougent vite. Ceux ci-dessous sont des ordres de grandeur relevés en 2026 : vérifie avant d’acheter, et demande sur <strong>#aide</strong> si tu hésites.</p></div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>Notre sélection par budget</h2>
    <div class="grid c3">
      <div class="card">
        <h3><span class="dot" style="background:var(--green)"></span>Premier cube (moins de 10 €)</h3>
        <p><strong>MoYu MeiLong</strong>, <strong>MoYu RS3 M 2020</strong>, <strong>YuXin Little Magic M</strong>, <strong>QiYi MS</strong>.</p>
        <p>Pourquoi : ils sont magnétiques, tournent bien pour leur prix et suffisent pour apprendre et progresser sans se ruiner. Le MeiLong a une bonne réputation de durabilité, et le Little Magic a un toucher plus feutré, moins bruyant.</p>
        <p class="muted">Compte un flacon de lubrifiant en plus.</p>
      </div>
      <div class="card">
        <h3><span class="dot" style="background:var(--yellow)"></span>Pour progresser (15 à 30 €)</h3>
        <p><strong>GAN 356 ME</strong>, <strong>MoYu RS3M V5</strong>, <strong>QiYi M Pro</strong>.</p>
        <p>Pourquoi : meilleure finition, réglages plus fins, coins mieux guidés. À ce prix, un cube commence à se sentir vraiment différent d’un modèle d’entrée de gamme.</p>
      </div>
      <div class="card">
        <h3><span class="dot" style="background:var(--red)"></span>Haut de gamme (30 € et plus)</h3>
        <p><strong>GAN 11 M Pro</strong>, <strong>GAN 12 Maglev</strong> (version UV ou non).</p>
        <p>Pourquoi : ce sont les cubes qu’on voit en compétition. Très réglables, mais ils n’ont d’intérêt que si tu t’entraînes régulièrement et que tu sais ce que tu cherches.</p>
      </div>
    </div>
    <div class="note">
      <p><strong>Une règle simple :</strong> si tu as moins d’un mois de pratique, prends un cube à moins de 10 € et garde le reste de ton budget pour du lubrifiant. Tu sauras ensuite si tu préfères un cube rapide ou contrôlable.</p>
    </div>
    <p><strong>Prix avantageux sur le serveur :</strong> on vend certains cubes de notre sélection bien en dessous des prix des grands sites. Demande sur Discord ce qui est disponible en ce moment.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>Où acheter</h2>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Boutique</th><th>Pays</th><th>Ce qu’on en retient</th></tr></thead>
        <tbody>
          <tr><td><a href="https://www.atoutcubes.com/">Atoutcubes</a></td><td>France (Bayonne)</td><td>Plus de 2 000 références en stock en France, livraison en 1 à 4 jours, retrait en magasin possible, livraison gratuite à partir d’un certain montant.</td></tr>
          <tr><td><a href="https://cuboss.com/">Cuboss</a></td><td>Suède</td><td>Expédie depuis l’Europe, sans frais d’importation. Livraison à 4,99 €, gratuite à partir de 99 €.</td></tr>
          <tr><td><a href="https://speedcubeshop.com/">SpeedCubeShop</a></td><td>États-Unis</td><td>Très grand choix et bons guides d’achat. Hors Europe, prévoir de possibles frais de douane et des délais plus longs.</td></tr>
        </tbody>
      </table>
    </div>
    <p>À éviter : les offres « speed cube » à quelques euros sur les grandes marketplaces, sans marque identifiable. Tu paies peu, mais tu risques d’avoir un cube qui accroche ou qui casse vite.</p>
  </div>
</section>
"""
page("cubes.html", "Quel speedcube acheter ? — EpiCubers",
     "Guide d’achat de speedcubes : quel modèle selon le budget, où commander en France et en Europe, et pourquoi.", body)

# ---------------------------------------------------------------- METHODE DEBUTANT
M_SEXY = "R U R' U'"
steps = []
def step(n, color, title, inner):
    steps.append(f"""<section><div class="wrap"><div class="step"><div class="step-num" style="--c:var(--{color})">{n}</div><div>
<h2>{title}</h2>
{inner}
</div></div></div></section>""")

step(1, "white", "La croix blanche",
     """<p>Pas d’algorithme ici : tu y arrives en regardant le cube. Place les quatre arêtes blanches autour du centre blanc, puis tourne chaque face pour que la deuxième couleur de l’arête soit alignée avec le centre de sa face. Tu obtiens une croix blanche, avec chaque arête qui correspond à la couleur du centre voisin.</p>
<p>Quand c’est fait, <strong>retourne le cube</strong> : la croix blanche est maintenant en bas, et elle y reste pour la suite.</p>""")

step(2, "blue", "Les coins blancs",
     """<p>Cherche un coin blanc dans la couche du haut. Tourne la face du haut (U) pour l’amener juste au-dessus de sa place, c’est-à-dire entre les deux centres qui correspondent à ses deux autres couleurs. Tourne ensuite tout le cube pour que cette place soit en bas à droite, face à toi, puis répète le « sexy move » jusqu’à ce que le blanc soit en bas.</p>"""
     + algo("Le sexy move", M_SEXY, note="Répète-le 1 à 5 fois jusqu’à ce que le coin soit en place. C’est l’algorithme que tu utiliseras le plus.")
     + """<p>Fais-le pour les quatre coins. La première couche (le blanc) est terminée.</p>""")

step(3, "green", "La deuxième couronne",
     """<p>La face jaune est en haut. Cherche dans la couche du haut une arête qui n’a pas de jaune. Tourne U pour que sa couleur du dessus (celle qui est vers toi) s’aligne avec le centre en face, puis regarde si elle doit aller à droite ou à gauche.</p>"""
     + algo("Arête vers la droite", "U R U' R' U' F' U F")
     + algo("Arête vers la gauche", "U' L' U L U F U' F'")
     + """<p>Fais-le pour les quatre arêtes. Si une arête est déjà dans la deuxième couche mais mal placée, utilise l’algorithme avec n’importe quelle arête du haut pour la faire sortir, puis recommence.</p>""")

step(4, "yellow", "La croix jaune",
     """<p>Regarde la face jaune. Tu verras un point, un « L », une barre ou déjà une croix. Tourne le cube pour mettre le « L » en haut à gauche, ou la barre à l’horizontale, puis fais l’algorithme. Recommence jusqu’à avoir une croix.</p>"""
     + algo("La croix jaune", "F R U R' U' F'", note="Depuis un point, tu l’enchaînes deux ou trois fois : point, puis L, puis barre, puis croix."))

step(5, "orange", "Aligner les arêtes jaunes",
     """<p>Tourne la face du haut jusqu’à ce que le plus d’arêtes possible correspondent à la couleur de leur centre. Si deux arêtes voisines sont bonnes, mets-les à l’arrière et à droite, puis fais l’algorithme. Si deux arêtes opposées sont bonnes, fais-le une fois depuis n’importe quel côté, puis reprends depuis le cas précédent.</p>"""
     + algo("Aligner les arêtes", "R U R' U R U2 R' U"))

step(6, "red", "Placer les coins",
     """<p>Regarde les quatre coins jaunes, sans te soucier de leur orientation : un coin est « à sa place » quand ses trois couleurs correspondent aux trois centres autour de lui. Cherche-en un qui est bien placé et tiens-le en haut à droite, face à toi, puis fais l’algorithme. Recommence jusqu’à ce que les quatre coins soient à leur place. Si aucun n’est bien placé, fais l’algorithme une fois depuis n’importe quel côté, puis cherche de nouveau.</p>"""
     + algo("Placer les coins", "U R U' L' U R' U' L", note="Il déplace trois coins en cercle et laisse tout le reste du cube à sa place."))

step(7, "white", "Tourner les coins et finir",
     """<div class="note draft"><p><span class="tag">À relire</span>Cette fin est la variante du serveur : au lieu de retourner le cube pour placer les coins un à un, on les tourne directement avec le sexy move et un quart de tour de la face du bas.</p></div>
<p><strong>Retourne le cube</strong> : la face jaune est maintenant en bas. Regarde le coin en bas à droite, face à toi, et répète le sexy move jusqu’à ce que le jaune soit tourné vers le bas. Les couches du haut ont l’air de se mélanger pendant ce temps, c’est normal : elles se remettent en place quand le coin est terminé.</p>
<p>Ensuite, tourne seulement la face du bas (D) pour amener le coin suivant en bas à droite, sans tourner le cube, et recommence. Après le dernier coin, tourne D pour aligner la couche du bas. Le cube est résolu.</p>"""
     + algo("Le sexy move, encore", M_SEXY, player=False))

notation = """
<section>
  <div class="wrap">
    <h2>Lire les algorithmes</h2>
    <p>Chaque lettre est une face du cube, vue de face : <kbd>R</kbd> droite, <kbd>L</kbd> gauche, <kbd>U</kbd> haut, <kbd>D</kbd> bas, <kbd>F</kbd> devant, <kbd>B</kbd> derrière. Une lettre seule, c’est un quart de tour dans le sens des aiguilles d’une montre en regardant cette face. Une apostrophe (<kbd>R'</kbd>) inverse le sens, et un 2 (<kbd>U2</kbd>) fait un demi-tour.</p>
    <p>Chaque algorithme est animé en 3D : appuie sur lecture pour voir la séquence, et fais glisser le cube pour le tourner.</p>
    <div class="note draft"><p><span class="tag">Version provisoire</span>Cette méthode est en cours de relecture. Les étapes suivent la méthode par couches. La dernière étape est la variante du serveur, qui permet de finir les coins avec un seul algorithme déjà connu : le sexy move.</p></div>
  </div>
</section>
"""

tutos = """
<section>
  <div class="wrap">
    <h2>Pour aller plus loin en vidéo</h2>
    <div class="grid c2">
      <a class="card" href="https://youtu.be/7Ron6MN45LY"><h3>Méthode débutant, en anglais</h3><p>La version qu’on recommande de préférence.</p><span class="go">Voir sur YouTube</span></a>
      <a class="card" href="https://youtu.be/PLsT1SY1cgg"><h3>Méthode débutant, en français</h3><p>Pour suivre dans ta langue.</p><span class="go">Voir sur YouTube</span></a>
    </div>
    <p style="margin-top:24px">Quand tu descends sous la minute et que tu veux aller plus vite, passe à la <a href="cfop.html">méthode CFOP</a>.</p>
  </div>
</section>
"""
body = head("Méthode débutant", "Résoudre le cube avec très peu d’algorithmes.") + notation + "\n".join(steps) + tutos
page("methode-debutant.html", "Méthode débutant — résoudre le Rubik’s cube — EpiCubers",
     "Une méthode pour résoudre le Rubik’s cube avec très peu d’algorithmes, avec animations 3D de chaque séquence.",
     body, head_extra=TWISTY)

# ---------------------------------------------------------------- CFOP
body = head("Passer à la CFOP", "La méthode utilisée par la plupart des speedcubeurs rapides.") + """
<section>
  <div class="wrap">
    <h2>En deux mots</h2>
    <p class="lead">CFOP (ou méthode Fridrich) se résout en quatre étapes, avec plus d’algorithmes à apprendre que la méthode débutant, mais beaucoup moins de mouvements.</p>
    <div class="grid c2">
      <div class="card"><h3>C comme Cross</h3><p>La croix, faite intuitivement, idéalement en 8 mouvements ou moins.</p></div>
      <div class="card"><h3>F2L, les deux premières couronnes</h3><p>On place un coin et son arête ensemble. Il y a 41 cas, la plupart se trouvent à l’intuition.</p></div>
      <div class="card"><h3>OLL, orienter la dernière couche</h3><p>Mettre toute la face jaune de la même couleur. 57 cas en version complète.</p></div>
      <div class="card"><h3>PLL, permuter la dernière couche</h3><p>Remettre les pièces jaunes à leur place. 21 cas.</p></div>
    </div>
    <p style="margin-top:20px">Ça fait environ 120 algorithmes en version complète, c’est pourquoi on conseille de passer d’abord par la version simplifiée (14 algorithmes) avant de tout apprendre.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>La liste complète des algorithmes</h2>
    <p>Les algorithmes de CFOP sont recensés, classés et animés sur SpeedCubeDB. On ne les recopie pas ici : c’est plus fiable de les prendre à la source.</p>
    <div class="btns"><a class="btn primary" href="https://speedcubedb.com/">Ouvrir SpeedCubeDB</a><a class="btn" href="https://www.speedsolving.com/wiki/index.php/Main_Page">Le wiki de SpeedSolving</a></div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>La CFOP simplifiée en vidéo</h2>
    <p>Un bon intermédiaire, avec 14 algorithmes seulement : F2L, puis OLL et PLL en version courte.</p>
    <div class="grid c3">
      <a class="card" href="https://youtu.be/Ar_Zit1VLG0"><h3>F2L</h3><p>Placer les deux premières couronnes.</p><span class="go">Voir la vidéo</span></a>
      <a class="card" href="https://youtu.be/GhmYBgLoQQg"><h3>OLL</h3><p>Orienter la dernière couche.</p><span class="go">Voir la vidéo</span></a>
      <a class="card" href="https://youtu.be/f_Yor-ydZjs"><h3>PLL</h3><p>Permuter la dernière couche.</p><span class="go">Voir la vidéo</span></a>
    </div>
    <p style="margin-top:24px">Besoin d’aide pour un cas qui ne passe pas ? Passe par <strong>#aide</strong> sur le Discord.</p>
  </div>
</section>
"""
page("cfop.html", "CFOP : passer à la méthode Fridrich — EpiCubers",
     "Comprendre la CFOP en quatre étapes, avec les vidéos de la version simplifiée et un renvoi vers SpeedCubeDB.", body)

# ---------------------------------------------------------------- LIENS
body = head("Liens utiles", "Les sites que tout cubeur finit par avoir en favori.") + f"""
<section>
  <div class="wrap">
    <div class="grid c2">
      <a class="card" href="https://www.worldcubeassociation.org/"><h3>World Cube Association</h3><p>Le site officiel des compétitions. Les prochaines compétitions dans le monde, l’inscription, les résultats, les classements et le profil de chaque compétiteur.</p><span class="go">worldcubeassociation.org</span></a>
      <a class="card" href="https://cstimer.net/"><h3>csTimer</h3><p>Un chronomètre très complet, avec des mélanges officiels, de nombreuses statistiques et beaucoup d’options.</p><span class="go">cstimer.net</span></a>
      <a class="card" href="https://speedcubedb.com/"><h3>SpeedCubeDB</h3><p>Une immense base de données : des milliers d’algorithmes, classés par étape et par méthode, pour s’améliorer.</p><span class="go">speedcubedb.com</span></a>
      <a class="card" href="https://www.speedsolving.com/wiki/index.php/Main_Page"><h3>Le wiki de SpeedSolving</h3><p>Le « Wikipédia du speedcubing » : méthodes, tutoriels, histoire, matériel.</p><span class="go">speedsolving.com</span></a>
      <a class="card" href="https://alg.cubing.net/"><h3>alg.cubing.net</h3><p>Pour reconstruire une résolution. Le cube 3D suit les mouvements que tu saisis, ce qui est idéal pour analyser un solve.</p><span class="go">alg.cubing.net</span></a>
      <a class="card" href="{DISCORD_FR}"><h3>Cubeurs Francophones</h3><p>Le serveur Discord de toute la communauté francophone du speedcubing : plus de 1 000 membres depuis juin 2017.</p><span class="go">Rejoindre le serveur</span></a>
    </div>
    <p style="margin-top:28px">Les guides de ce site : <a href="methode-debutant.html">méthode débutant</a>, <a href="cfop.html">CFOP</a>, <a href="cubes.html">choisir son cube</a>.</p>
  </div>
</section>
"""
page("liens.html", "Liens utiles du speedcubing — EpiCubers",
     "WCA, csTimer, SpeedCubeDB, wiki de SpeedSolving, alg.cubing.net : les sites utiles pour progresser.", body)

# ---------------------------------------------------------------- GLOSSAIRE
G = [
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
    ("Mélange (scramble)", "La suite de mouvements générée au hasard qu’on applique avant chaque résolution."),
    ("OH", "One-handed : résolution à une main."),
    ("OLL", "Orientation of the Last Layer : mettre toute la dernière face de la même couleur."),
    ("PB (personal best)", "Ton meilleur temps personnel, en single ou en moyenne."),
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

print("Pages générées :", [f for f, _ in NAV])
