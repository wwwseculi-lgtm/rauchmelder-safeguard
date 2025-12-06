#!/usr/bin/env python3
"""
SEO-Seiten Generator für deutsche Städte - MIT TEXTEN
"""

import os

STAEDTE = {
    "berlin": {"name": "Berlin", "land": "Berlin", "bezirke": ["Mitte", "Kreuzberg", "Prenzlauer Berg", "Charlottenburg", "Neukölln", "Spandau", "Steglitz", "Pankow"]},
    "hamburg": {"name": "Hamburg", "land": "Hamburg", "bezirke": ["Altona", "Eimsbüttel", "Hamburg-Nord", "Wandsbek", "Bergedorf", "Harburg", "Hamburg-Mitte", "Blankenese"]},
    "muenchen": {"name": "München", "land": "Bayern", "bezirke": ["Schwabing", "Bogenhausen", "Sendling", "Pasing", "Trudering", "Neuhausen", "Laim", "Maxvorstadt"]},
    "koeln": {"name": "Köln", "land": "NRW", "bezirke": ["Innenstadt", "Ehrenfeld", "Nippes", "Lindenthal", "Rodenkirchen", "Chorweiler", "Porz", "Kalk"]},
    "frankfurt": {"name": "Frankfurt am Main", "land": "Hessen", "bezirke": ["Innenstadt", "Sachsenhausen", "Bornheim", "Bockenheim", "Nordend", "Westend", "Höchst", "Rödelheim"]},
    "stuttgart": {"name": "Stuttgart", "land": "Baden-Württemberg", "bezirke": ["Mitte", "Nord", "Ost", "Süd", "West", "Bad Cannstatt", "Vaihingen", "Möhringen"]},
    "duesseldorf": {"name": "Düsseldorf", "land": "NRW", "bezirke": ["Altstadt", "Bilk", "Flingern", "Oberkassel", "Pempelfort", "Unterbilk", "Gerresheim", "Benrath"]},
    "dortmund": {"name": "Dortmund", "land": "NRW", "bezirke": ["Mitte", "Hörde", "Hombruch", "Aplerbeck", "Brackel", "Scharnhorst", "Eving", "Mengede"]},
    "essen": {"name": "Essen", "land": "NRW", "bezirke": ["Stadtmitte", "Rüttenscheid", "Steele", "Werden", "Kettwig", "Borbeck", "Altenessen", "Frohnhausen"]},
    "leipzig": {"name": "Leipzig", "land": "Sachsen", "bezirke": ["Mitte", "Südvorstadt", "Connewitz", "Plagwitz", "Lindenau", "Gohlis", "Mockau", "Reudnitz"]},
    "bremen": {"name": "Bremen", "land": "Bremen", "bezirke": ["Mitte", "Neustadt", "Viertel", "Findorff", "Schwachhausen", "Horn-Lehe", "Vegesack", "Blumenthal"]},
    "dresden": {"name": "Dresden", "land": "Sachsen", "bezirke": ["Altstadt", "Neustadt", "Blasewitz", "Striesen", "Löbtau", "Cotta", "Pieschen", "Klotzsche"]},
    "hannover": {"name": "Hannover", "land": "Niedersachsen", "bezirke": ["Mitte", "Südstadt", "List", "Döhren", "Bothfeld", "Vahrenwald", "Linden-Nord", "Ricklingen"]},
    "nuernberg": {"name": "Nürnberg", "land": "Bayern", "bezirke": ["Altstadt", "Gostenhof", "Maxfeld", "Gleißhammer", "Mögeldorf", "Langwasser", "Schweinau", "Eibach"]},
    "duisburg": {"name": "Duisburg", "land": "NRW", "bezirke": ["Mitte", "Hamborn", "Meiderich", "Homberg", "Rheinhausen", "Walsum", "Hochfeld", "Baerl"]},
    "bochum": {"name": "Bochum", "land": "NRW", "bezirke": ["Mitte", "Wattenscheid", "Langendreer", "Weitmar", "Gerthe", "Querenburg", "Dahlhausen", "Linden"]},
    "wuppertal": {"name": "Wuppertal", "land": "NRW", "bezirke": ["Elberfeld", "Barmen", "Vohwinkel", "Cronenberg", "Ronsdorf", "Langerfeld", "Beyenburg", "Oberbarmen"]},
    "bielefeld": {"name": "Bielefeld", "land": "NRW", "bezirke": ["Mitte", "Schildesche", "Gadderbaum", "Brackwede", "Dornberg", "Jöllenbeck", "Heepen", "Stieghorst"]},
    "bonn": {"name": "Bonn", "land": "NRW", "bezirke": ["Zentrum", "Beuel", "Bad Godesberg", "Hardtberg", "Poppelsdorf", "Endenich", "Dottendorf", "Kessenich"]},
    "muenster": {"name": "Münster", "land": "NRW", "bezirke": ["Altstadt", "Aegidii", "Geist", "Hiltrup", "Gievenbeck", "Roxel", "Kinderhaus", "Handorf"]},
    "karlsruhe": {"name": "Karlsruhe", "land": "Baden-Württemberg", "bezirke": ["Innenstadt", "Südstadt", "Weststadt", "Mühlburg", "Durlach", "Knielingen", "Rüppurr", "Oberreut"]},
    "mannheim": {"name": "Mannheim", "land": "Baden-Württemberg", "bezirke": ["Innenstadt", "Neckarstadt", "Lindenhof", "Schwetzingerstadt", "Feudenheim", "Seckenheim", "Käfertal", "Wallstadt"]},
    "augsburg": {"name": "Augsburg", "land": "Bayern", "bezirke": ["Innenstadt", "Lechhausen", "Oberhausen", "Haunstetten", "Göggingen", "Pfersee", "Kriegshaber", "Hochzoll"]},
    "wiesbaden": {"name": "Wiesbaden", "land": "Hessen", "bezirke": ["Mitte", "Biebrich", "Dotzheim", "Schierstein", "Kostheim", "Kastel", "Nordenstadt", "Sonnenberg"]},
    "gelsenkirchen": {"name": "Gelsenkirchen", "land": "NRW", "bezirke": ["Altstadt", "Buer", "Horst", "Schalke", "Bismarck", "Erle", "Resse", "Hassel"]},
    "moenchengladbach": {"name": "Mönchengladbach", "land": "NRW", "bezirke": ["Stadtmitte", "Rheydt", "Odenkirchen", "Giesenkirchen", "Neuwerk", "Wickrath", "Hardt", "Windberg"]},
    "braunschweig": {"name": "Braunschweig", "land": "Niedersachsen", "bezirke": ["Innenstadt", "Weststadt", "Östliches Ringgebiet", "Lehndorf", "Volkmarode", "Stöckheim", "Rüningen", "Querum"]},
    "chemnitz": {"name": "Chemnitz", "land": "Sachsen", "bezirke": ["Zentrum", "Kaßberg", "Schloßchemnitz", "Sonnenberg", "Altendorf", "Kapellenberg", "Lutherviertel", "Bernsdorf"]},
    "kiel": {"name": "Kiel", "land": "Schleswig-Holstein", "bezirke": ["Altstadt", "Gaarden", "Wik", "Düsternbrook", "Hassee", "Mettenhof", "Elmschenhagen", "Holtenau"]},
    "aachen": {"name": "Aachen", "land": "NRW", "bezirke": ["Mitte", "Burtscheid", "Brand", "Eilendorf", "Haaren", "Kornelimünster", "Laurensberg", "Richterich"]},
    "halle": {"name": "Halle (Saale)", "land": "Sachsen-Anhalt", "bezirke": ["Altstadt", "Neustadt", "Giebichenstein", "Kröllwitz", "Trotha", "Heide-Süd", "Silberhöhe", "Südstadt"]},
    "magdeburg": {"name": "Magdeburg", "land": "Sachsen-Anhalt", "bezirke": ["Altstadt", "Stadtfeld", "Buckau", "Sudenburg", "Cracau", "Herrenkrug", "Reform", "Olvenstedt"]},
    "freiburg": {"name": "Freiburg im Breisgau", "land": "Baden-Württemberg", "bezirke": ["Altstadt", "Wiehre", "Herdern", "Stühlinger", "Haslach", "Weingarten", "Littenweiler", "Rieselfeld"]},
    "krefeld": {"name": "Krefeld", "land": "NRW", "bezirke": ["Mitte", "Bockum", "Uerdingen", "Hüls", "Fischeln", "Oppum", "Linn", "Gellep-Stratum"]},
    "luebeck": {"name": "Lübeck", "land": "Schleswig-Holstein", "bezirke": ["Innenstadt", "St. Lorenz", "St. Gertrud", "Moisling", "Buntekuh", "St. Jürgen", "Travemünde", "Kücknitz"]},
    "oberhausen": {"name": "Oberhausen", "land": "NRW", "bezirke": ["Alt-Oberhausen", "Sterkrade", "Osterfeld", "Lirich", "Styrum", "Königshardt", "Alstaden", "Buschhausen"]},
    "erfurt": {"name": "Erfurt", "land": "Thüringen", "bezirke": ["Altstadt", "Löbervorstadt", "Brühlervorstadt", "Andreasvorstadt", "Johannesvorstadt", "Krämpfervorstadt", "Daberstedt", "Melchendorf"]},
    "mainz": {"name": "Mainz", "land": "Rheinland-Pfalz", "bezirke": ["Altstadt", "Neustadt", "Oberstadt", "Hartenberg", "Bretzenheim", "Gonsenheim", "Finthen", "Weisenau"]},
    "rostock": {"name": "Rostock", "land": "Mecklenburg-Vorpommern", "bezirke": ["Stadtmitte", "Kröpeliner-Tor-Vorstadt", "Warnemünde", "Lichtenhagen", "Evershagen", "Lütten Klein", "Toitenwinkel", "Dierkow"]},
    "kassel": {"name": "Kassel", "land": "Hessen", "bezirke": ["Mitte", "Vorderer Westen", "Bad Wilhelmshöhe", "Wehlheiden", "Kirchditmold", "Rothenditmold", "Nord-Holland", "Bettenhausen"]},
    "hagen": {"name": "Hagen", "land": "NRW", "bezirke": ["Mitte", "Hohenlimburg", "Haspe", "Boele", "Eilpe", "Dahl", "Vorhalle", "Wehringhausen"]},
    "hamm": {"name": "Hamm", "land": "NRW", "bezirke": ["Mitte", "Uentrop", "Rhynern", "Pelkum", "Herringen", "Bockum-Hövel", "Heessen", "Mark"]},
    "saarbruecken": {"name": "Saarbrücken", "land": "Saarland", "bezirke": ["Alt-Saarbrücken", "St. Johann", "Malstatt", "Burbach", "Dudweiler", "Scheidt", "Brebach", "Gersweiler"]},
    "muelheim": {"name": "Mülheim an der Ruhr", "land": "NRW", "bezirke": ["Altstadt", "Styrum", "Dümpten", "Heißen", "Speldorf", "Saarn", "Broich", "Mintard"]},
    "potsdam": {"name": "Potsdam", "land": "Brandenburg", "bezirke": ["Innenstadt", "Babelsberg", "Potsdam West", "Bornim", "Bornstedt", "Eiche", "Golm", "Drewitz"]},
    "ludwigshafen": {"name": "Ludwigshafen", "land": "Rheinland-Pfalz", "bezirke": ["Mitte", "Süd", "Nord", "Friesenheim", "Oggersheim", "Gartenstadt", "Mundenheim", "Rheingönheim"]},
    "oldenburg": {"name": "Oldenburg", "land": "Niedersachsen", "bezirke": ["Innenstadt", "Eversten", "Kreyenbrück", "Osternburg", "Nadorst", "Bürgerfelde", "Bloherfelde", "Ofenerdiek"]},
    "leverkusen": {"name": "Leverkusen", "land": "NRW", "bezirke": ["Wiesdorf", "Opladen", "Schlebusch", "Küppersteg", "Steinbüchel", "Rheindorf", "Bürrig", "Quettingen"]},
    "osnabrueck": {"name": "Osnabrück", "land": "Niedersachsen", "bezirke": ["Innenstadt", "Wüste", "Schinkel", "Sonnenhügel", "Dodesheide", "Sutthausen", "Nahne", "Hellern"]},
    "solingen": {"name": "Solingen", "land": "NRW", "bezirke": ["Mitte", "Burg", "Ohligs", "Höhscheid", "Wald", "Gräfrath", "Aufderhöhe", "Merscheid"]},
    "heidelberg": {"name": "Heidelberg", "land": "Baden-Württemberg", "bezirke": ["Altstadt", "Bergheim", "Weststadt", "Neuenheim", "Handschuhsheim", "Rohrbach", "Kirchheim", "Wieblingen"]},
    "herne": {"name": "Herne", "land": "NRW", "bezirke": ["Mitte", "Wanne", "Eickel", "Crange", "Röhlinghausen", "Sodingen", "Horsthausen", "Constantin"]},
    "neuss": {"name": "Neuss", "land": "NRW", "bezirke": ["Innenstadt", "Furth", "Holzheim", "Reuschenberg", "Pomona", "Norf", "Rosellen", "Grimlinghausen"]},
    "darmstadt": {"name": "Darmstadt", "land": "Hessen", "bezirke": ["Mitte", "Bessungen", "Martinsviertel", "Johannesviertel", "Eberstadt", "Arheilgen", "Kranichstein", "Wixhausen"]},
    "paderborn": {"name": "Paderborn", "land": "NRW", "bezirke": ["Kernstadt", "Schloß Neuhaus", "Sennelager", "Elsen", "Wewer", "Marienloh", "Dahl", "Neuenbeken"]},
    "regensburg": {"name": "Regensburg", "land": "Bayern", "bezirke": ["Altstadt", "Stadtamhof", "Steinweg", "Kumpfmühl", "Oberisling", "Burgweinting", "Schwabelweis", "Winzer"]},
    "ingolstadt": {"name": "Ingolstadt", "land": "Bayern", "bezirke": ["Mitte", "Nordost", "Nordwest", "Süd", "Südwest", "Friedrichshofen", "Haunwöhr", "Mailing"]},
    "wuerzburg": {"name": "Würzburg", "land": "Bayern", "bezirke": ["Altstadt", "Sanderau", "Grombühl", "Frauenland", "Zellerau", "Heidingsfeld", "Heuchelhof", "Lengfeld"]},
    "wolfsburg": {"name": "Wolfsburg", "land": "Niedersachsen", "bezirke": ["Stadtmitte", "Nordstadt", "Westhagen", "Detmerode", "Vorsfelde", "Fallersleben", "Heiligendorf", "Sülfeld"]},
    "ulm": {"name": "Ulm", "land": "Baden-Württemberg", "bezirke": ["Mitte", "Weststadt", "Oststadt", "Böfingen", "Söflingen", "Wiblingen", "Einsingen", "Eggingen"]},
    "goettingen": {"name": "Göttingen", "land": "Niedersachsen", "bezirke": ["Innenstadt", "Weende", "Grone", "Geismar", "Nikolausberg", "Herberhausen", "Elliehausen", "Holtensen"]},
    "offenbach": {"name": "Offenbach am Main", "land": "Hessen", "bezirke": ["Stadtmitte", "Mathildenviertel", "Nordend", "Bürgel", "Rumpenheim", "Bieber", "Tempelsee", "Lauterborn"]},
    "pforzheim": {"name": "Pforzheim", "land": "Baden-Württemberg", "bezirke": ["Innenstadt", "Nordstadt", "Oststadt", "Südweststadt", "Brötzingen", "Eutingen", "Huchenfeld", "Dillweißenstein"]},
    "heilbronn": {"name": "Heilbronn", "land": "Baden-Württemberg", "bezirke": ["Innenstadt", "Sontheim", "Neckargartach", "Böckingen", "Frankenbach", "Biberach", "Kirchhausen", "Klingenberg"]},
    "bottrop": {"name": "Bottrop", "land": "NRW", "bezirke": ["Mitte", "Boy", "Welheim", "Batenbrock", "Fuhlenbrock", "Kirchhellen", "Grafenwald", "Feldhausen"]},
    "reutlingen": {"name": "Reutlingen", "land": "Baden-Württemberg", "bezirke": ["Innenstadt", "Ringelbach", "Gönningen", "Betzingen", "Ohmenhausen", "Sickenhausen", "Sondelfingen", "Altenburg"]},
    "koblenz": {"name": "Koblenz", "land": "Rheinland-Pfalz", "bezirke": ["Altstadt", "Südliche Vorstadt", "Ehrenbreitstein", "Karthause", "Güls", "Metternich", "Neuendorf", "Wallersheim"]},
    "remscheid": {"name": "Remscheid", "land": "NRW", "bezirke": ["Mitte", "Lennep", "Lüttringhausen", "Süd", "Hasten", "Bliedinghausen", "Reinshagen", "Vieringhausen"]},
    "bergisch-gladbach": {"name": "Bergisch Gladbach", "land": "NRW", "bezirke": ["Stadtmitte", "Bensberg", "Refrath", "Schildgen", "Hand", "Moitzfeld", "Frankenforst", "Lustheide"]},
    "jena": {"name": "Jena", "land": "Thüringen", "bezirke": ["Zentrum", "Jena-Nord", "Jena-Ost", "Lobeda", "Winzerla", "Göschwitz", "Burgau", "Wenigenjena"]},
    "trier": {"name": "Trier", "land": "Rheinland-Pfalz", "bezirke": ["Mitte", "Süd", "West", "Heiligkreuz", "Olewig", "Tarforst", "Mariahof", "Ehrang"]},
    "erlangen": {"name": "Erlangen", "land": "Bayern", "bezirke": ["Innenstadt", "Röthelheim", "Alterlangen", "Bruck", "Büchenbach", "Eltersdorf", "Frauenaurach", "Kriegenbrunn"]},
    "moers": {"name": "Moers", "land": "NRW", "bezirke": ["Mitte", "Asberg", "Scherpenberg", "Hülsdonk", "Meerbeck", "Repelen", "Schwafheim", "Kapellen"]},
    "siegen": {"name": "Siegen", "land": "NRW", "bezirke": ["Mitte", "Geisweid", "Weidenau", "Eiserfeld", "Kaan-Marienborn", "Niederschelden", "Bürbach", "Kreuztal"]},
    "hildesheim": {"name": "Hildesheim", "land": "Niedersachsen", "bezirke": ["Mitte", "Nordstadt", "Oststadt", "Moritzberg", "Marienburger Höhe", "Itzum", "Ochtersum", "Neuhof"]},
    "salzgitter": {"name": "Salzgitter", "land": "Niedersachsen", "bezirke": ["Lebenstedt", "Bad", "Gebhardshagen", "Thiede", "Fredenberg", "Hallendorf", "Engelnstedt", "Beddingen"]},
    "cottbus": {"name": "Cottbus", "land": "Brandenburg", "bezirke": ["Mitte", "Sandow", "Spremberger Vorstadt", "Sachsendorf", "Ströbitz", "Schmellwitz", "Sielow", "Branitz"]},
    "schwerin": {"name": "Schwerin", "land": "Mecklenburg-Vorpommern", "bezirke": ["Altstadt", "Paulsstadt", "Feldstadt", "Schelfstadt", "Weststadt", "Lankow", "Großer Dreesch", "Mueßer Holz"]},
}

TEMPLATE = '''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Rauchmelder Installation & Wartung in {stadt} ✓ Professionelle Montage ✓ TÜV-geprüft ✓ 10 Jahre Garantie ✓ Schnelle Termine. Jetzt kostenlos anfragen!">
    <meta name="keywords" content="Rauchmelder {stadt}, Rauchmelder Installation {stadt}, Rauchmelder Wartung {stadt}, Brandschutz {stadt}, Rauchwarnmelder {stadt}, Rauchmelder montieren {stadt}">
    <title>Rauchmelder Service {stadt} | Installation & Wartung | Secu.li</title>
    <link rel="canonical" href="https://secu.li/standorte/deutschland/{slug}.html">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../../styles.css">
</head>
<body>
    <header class="header" id="header">
        <div class="container">
            <a href="../../index.html" class="logo"><span>Secu.li</span></a>
            <nav class="nav">
                <ul class="nav-links">
                    <li><a href="../../index.html">Startseite</a></li>
                    <li><a href="../../produkte.html">Produkte</a></li>
                    <li><a href="../../service.html">Montage & Service</a></li>
                    <li><a href="../../ueber-uns.html">Über uns</a></li>
                    <li><a href="../../kontakt.html">Kontakt</a></li>
                </ul>
                <a href="../../kontakt.html" class="btn btn-primary">Jetzt anfragen</a>
            </nav>
        </div>
    </header>

    <section class="hero hero-simple">
        <div class="container">
            <div class="hero-content hero-centered">
                <div class="hero-text">
                    <span class="hero-badge-top">📍 {stadt}</span>
                    <h1>Rauchmelder Service in {stadt}</h1>
                    <p class="subtitle">Ihr zuverlässiger Partner für Rauchmelder-Installation und Wartung in {stadt}. Schnelle Termine, faire Preise, 10 Jahre Garantie.</p>
                    <div class="hero-buttons">
                        <a href="#kontaktformular" class="btn btn-primary btn-lg">Kostenloses Angebot</a>
                        <a href="tel:+498001234567" class="btn btn-outline btn-lg">📞 Jetzt anrufen</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="trust-badges-section">
        <div class="container">
            <div class="trust-badges-grid">
                <div class="trust-badge-item"><div class="badge-icon">CE</div><span>CE-zertifiziert</span></div>
                <div class="trust-badge-item"><div class="badge-icon">TÜV</div><span>TÜV geprüft</span></div>
                <div class="trust-badge-item"><div class="badge-icon">VdS</div><span>VdS anerkannt</span></div>
                <div class="trust-badge-item"><div class="badge-icon">10J</div><span>10 Jahre Garantie</span></div>
            </div>
        </div>
    </section>

    <!-- SEO Text Section -->
    <section class="section">
        <div class="container">
            <div class="section-header">
                <h2>Rauchmelder in {stadt} – Sicherheit für Ihr Zuhause</h2>
            </div>
            <div style="max-width: 800px; margin: 0 auto; line-height: 1.8;">
                <p>In {stadt} gilt wie in ganz {land} die <strong>gesetzliche Rauchmelderpflicht</strong>. Als Eigentümer oder Vermieter sind Sie verpflichtet, in allen Schlafräumen, Kinderzimmern und Fluren Rauchmelder zu installieren. Wir von Secu.li übernehmen diese Aufgabe professionell und zuverlässig.</p>
                
                <p>Unsere <strong>zertifizierten Techniker in {stadt}</strong> installieren Ihre Rauchmelder fachgerecht nach DIN 14676. Sie erhalten eine rechtssichere Dokumentation für Ihre Unterlagen – ideal für Vermieter und Hausverwaltungen.</p>
                
                <h3 style="margin-top: 2rem;">Warum Secu.li in {stadt}?</h3>
                <ul style="margin: 1rem 0;">
                    <li>✓ <strong>Schnelle Terminvergabe</strong> – oft innerhalb weniger Tage</li>
                    <li>✓ <strong>Festpreise ohne versteckte Kosten</strong></li>
                    <li>✓ <strong>TÜV-geprüfte Rauchmelder</strong> mit 10 Jahren Garantie</li>
                    <li>✓ <strong>Jährliche Wartung</strong> nach gesetzlichen Vorgaben</li>
                    <li>✓ <strong>Dokumentation</strong> für Vermieter und Versicherungen</li>
                </ul>
                
                <p>Ob Sie eine <strong>Neuinstallation</strong>, einen <strong>Austausch alter Geräte</strong> oder die <strong>jährliche Wartung</strong> benötigen – wir sind Ihr Ansprechpartner für Brandschutz in {stadt} und Umgebung.</p>
            </div>
        </div>
    </section>

    <section class="section bg-gray">
        <div class="container">
            <div class="section-header">
                <span class="section-badge">Unsere Leistungen</span>
                <h2>Rauchmelder-Service in {stadt}</h2>
            </div>
            <div class="features-grid">
                <div class="feature-card">
                    <div class="feature-icon">🔧</div>
                    <h4>Installation</h4>
                    <p>Fachgerechte Montage von Rauchmeldern in Wohnungen und Häusern in {stadt}. Inkl. Beratung zur optimalen Platzierung.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">🔍</div>
                    <h4>Wartung & Prüfung</h4>
                    <p>Jährliche Funktionsprüfung und Wartung nach DIN 14676. Rechtssicher dokumentiert für Ihre Unterlagen.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">🔄</div>
                    <h4>Austausch</h4>
                    <p>Nach 10 Jahren müssen Rauchmelder ersetzt werden. Wir kümmern uns um den fachgerechten Austausch.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">🏢</div>
                    <h4>Gewerblich</h4>
                    <p>Spezielle Lösungen für Hausverwaltungen, Hotels und Gewerbeimmobilien in {stadt}.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="section">
        <div class="container">
            <div class="section-header">
                <span class="section-badge">Servicegebiet</span>
                <h2>Rauchmelder-Service in {stadt} und Umgebung</h2>
                <p>Wir sind in allen Stadtteilen für Sie im Einsatz.</p>
            </div>
            <div class="countries-grid">
                {bezirke_html}
            </div>
        </div>
    </section>

    <!-- FAQ Section -->
    <section class="section bg-gray">
        <div class="container">
            <div class="section-header">
                <span class="section-badge">Häufige Fragen</span>
                <h2>FAQ – Rauchmelder in {stadt}</h2>
            </div>
            <div style="max-width: 800px; margin: 0 auto;">
                <div style="margin-bottom: 2rem; padding: 1.5rem; background: var(--white); border-radius: var(--radius-lg);">
                    <h4 style="margin-bottom: 0.5rem;">Wer ist für Rauchmelder in {stadt} verantwortlich?</h4>
                    <p style="color: var(--gray-600); margin: 0;">In {land} ist der Eigentümer für die Installation verantwortlich, die Wartung kann vertraglich auf Mieter übertragen werden.</p>
                </div>
                <div style="margin-bottom: 2rem; padding: 1.5rem; background: var(--white); border-radius: var(--radius-lg);">
                    <h4 style="margin-bottom: 0.5rem;">Was kostet die Rauchmelder-Installation in {stadt}?</h4>
                    <p style="color: var(--gray-600); margin: 0;">Wir bieten transparente Festpreise. Fordern Sie jetzt ein kostenloses Angebot an.</p>
                </div>
                <div style="margin-bottom: 2rem; padding: 1.5rem; background: var(--white); border-radius: var(--radius-lg);">
                    <h4 style="margin-bottom: 0.5rem;">Wie oft müssen Rauchmelder gewartet werden?</h4>
                    <p style="color: var(--gray-600); margin: 0;">Die gesetzliche Wartung muss mindestens einmal jährlich erfolgen. Wir erinnern Sie automatisch.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="contact-form-section" id="kontaktformular">
        <div class="container">
            <div class="contact-header-centered">
                <span class="section-badge">Jetzt anfragen</span>
                <h2>Kostenloses Angebot für {stadt}</h2>
                <p>Erhalten Sie innerhalb von 24 Stunden ein unverbindliches Angebot.</p>
                <div class="contact-benefits-row">
                    <div class="benefit-item"><span class="benefit-icon">✓</span><span>Kostenlos & unverbindlich</span></div>
                    <div class="benefit-item"><span class="benefit-icon">✓</span><span>Antwort in 24h</span></div>
                    <div class="benefit-item"><span class="benefit-icon">✓</span><span>Faire Festpreise</span></div>
                </div>
            </div>
            <div class="contact-form-card contact-form-large">
                <form class="contact-form" id="localContactForm">
                    <input type="hidden" name="city" value="{stadt}">
                    <div class="form-grid-3">
                        <div class="form-group"><label for="name">Name *</label><input type="text" id="name" name="name" placeholder="Ihr Name" required></div>
                        <div class="form-group"><label for="email">E-Mail *</label><input type="email" id="email" name="email" placeholder="ihre@email.de" required></div>
                        <div class="form-group"><label for="phone">Telefon</label><input type="tel" id="phone" name="phone" placeholder="+49 123 456789"></div>
                    </div>
                    <div class="form-grid-2">
                        <div class="form-group"><label for="service">Was benötigen Sie?</label>
                            <select id="service" name="service">
                                <option value="">Bitte auswählen...</option>
                                <option value="installation">Rauchmelder Installation</option>
                                <option value="wartung">Wartung & Prüfung</option>
                                <option value="austausch">Geräte-Austausch</option>
                                <option value="beratung">Kostenlose Beratung</option>
                            </select>
                        </div>
                        <div class="form-group"><label for="units">Anzahl Wohneinheiten</label>
                            <select id="units" name="units">
                                <option value="">Bitte auswählen...</option>
                                <option value="1">1 Wohnung / Haus</option>
                                <option value="2-5">2-5 Wohnungen</option>
                                <option value="6-20">6-20 Wohnungen</option>
                                <option value="21-50">21-50 Wohnungen</option>
                                <option value="50+">Mehr als 50</option>
                            </select>
                        </div>
                    </div>
                    <div class="form-group"><label for="message">Ihre Nachricht</label><textarea id="message" name="message" placeholder="Beschreiben Sie kurz Ihr Anliegen..." rows="4"></textarea></div>
                    <div class="form-submit-row">
                        <button type="submit" class="btn btn-primary btn-xl">Kostenloses Angebot anfordern →</button>
                        <p class="form-privacy">🔒 Ihre Daten sind sicher. Keine Weitergabe an Dritte.</p>
                    </div>
                </form>
            </div>
        </div>
    </section>

    <footer class="footer">
        <div class="container">
            <div class="footer-bottom">
                <p>© 2024 Secu.li – Ihr Partner für Rauchmelder in {stadt} | <a href="../../kontakt.html" style="color: var(--gray-400);">Kontakt</a> | <a href="../../index.html" style="color: var(--gray-400);">Startseite</a></p>
            </div>
        </div>
    </footer>
    <script src="../../script.js"></script>
</body>
</html>'''

def generate_pages():
    output_dir = "standorte/deutschland"
    os.makedirs(output_dir, exist_ok=True)
    
    count = 0
    for slug, data in STAEDTE.items():
        stadt = data["name"]
        land = data["land"]
        bezirke = data.get("bezirke", [])
        
        bezirke_html = ""
        for bezirk in bezirke:
            bezirke_html += f'<div class="country-card"><h5>{bezirk}</h5><p>Rauchmelder Service verfügbar</p></div>\n                '
        
        content = TEMPLATE.format(
            stadt=stadt,
            slug=slug,
            land=land,
            bezirke_html=bezirke_html.strip()
        )
        
        filepath = os.path.join(output_dir, f"{slug}.html")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        
        count += 1
        print(f"✅ {stadt}")
    
    print(f"\n🎉 {count} Seiten mit SEO-Texten erstellt!")

if __name__ == "__main__":
    generate_pages()
