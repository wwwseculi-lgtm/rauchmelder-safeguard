#!/usr/bin/env python3
"""
Generator für lokale SEO-Seiten für kleinere Orte in Deutschland
Erstellt Seiten für Landkreise, Kleinstädte und Dörfer
"""

import os
from pathlib import Path

# Landkreise und kleine Städte nach Bundesland
ORTE_NACH_BUNDESLAND = {
    "Baden-Württemberg": [
        "Aalen", "Albstadt", "Backnang", "Baden-Baden", "Balingen", "Biberach", "Böblingen",
        "Bruchsal", "Buchen", "Calw", "Crailsheim", "Donaueschingen", "Ehingen", "Ellwangen",
        "Emmendingen", "Ettlingen", "Filderstadt", "Freudenstadt", "Gaggenau", "Geislingen",
        "Heidenheim", "Herrenberg", "Horb", "Kehl", "Kirchheim", "Kornwestheim", "Künzelsau",
        "Lahr", "Leonberg", "Lörrach", "Mosbach", "Mühlacker", "Nagold", "Neckarsulm",
        "Nürtingen", "Oberkirch", "Öhringen", "Ostfildern", "Radolfzell", "Rastatt",
        "Ravensburg", "Rheinfelden", "Rottenburg", "Rottweil", "Schorndorf", "Schwäbisch Gmünd",
        "Schwäbisch Hall", "Singen", "Stockach", "Tuttlingen", "Vaihingen", "Villingen-Schwenningen",
        "Waiblingen", "Waldshut-Tiengen", "Wangen", "Weinheim", "Wendlingen", "Wertheim"
    ],
    "Bayern": [
        "Altötting", "Amberg", "Ansbach", "Aschaffenburg", "Bad Kissingen", "Bad Reichenhall",
        "Bad Tölz", "Bad Windsheim", "Berchtesgaden", "Burglengenfeld", "Coburg", "Dachau",
        "Deggendorf", "Dillingen", "Dingolfing", "Donauwörth", "Ebersberg", "Eichstätt",
        "Erding", "Forchheim", "Freising", "Friedberg", "Fürstenfeldbruck", "Garmisch-Partenkirchen",
        "Germering", "Grafenau", "Günzburg", "Haßfurt", "Herzogenaurach", "Hof", "Kaufbeuren",
        "Kelheim", "Kempten", "Kitzingen", "Kronach", "Kulmbach", "Lauf", "Lichtenfels",
        "Lindau", "Marktoberdorf", "Memmingen", "Miesbach", "Miltenberg", "Moosburg",
        "Neuburg", "Neumarkt", "Neustadt", "Nördlingen", "Oberasbach", "Pegnitz", "Pfaffenhofen",
        "Regen", "Roth", "Schwabach", "Schweinfurt", "Schwandorf", "Sonthofen", "Starnberg",
        "Straubing", "Sulzbach-Rosenberg", "Traunstein", "Weiden", "Weißenburg", "Zirndorf"
    ],
    "Brandenburg": [
        "Bad Belzig", "Bad Freienwalde", "Beeskow", "Brandenburg", "Eisenhüttenstadt", "Elsterwerda",
        "Finow", "Forst", "Fürstenwalde", "Guben", "Hennigsdorf", "Herzberg", "Hohen Neuendorf",
        "Jüterbog", "Königs Wusterhausen", "Kyritz", "Lauchhammer", "Lübben", "Lübbenau",
        "Luckenwalde", "Nauen", "Neuruppin", "Perleberg", "Prenzlau", "Pritzwalk", "Rathenow",
        "Schönefeld", "Schwedt", "Senftenberg", "Spremberg", "Strausberg", "Teltow",
        "Templin", "Velten", "Werder", "Wittstock", "Zehdenick", "Zossen"
    ],
    "Hessen": [
        "Alsfeld", "Bad Hersfeld", "Bad Nauheim", "Bad Schwalbach", "Bad Soden", "Bad Vilbel",
        "Baunatal", "Bensheim", "Biedenkopf", "Büdingen", "Dillenburg", "Dreieich", "Eltville",
        "Erbach", "Eschwege", "Friedberg", "Fritzlar", "Gelnhausen", "Griesheim", "Groß-Gerau",
        "Hattersheim", "Herborn", "Hofheim", "Homberg", "Hünfeld", "Idstein", "Karben",
        "Kelkheim", "Kirchhain", "Korbach", "Lampertheim", "Langen", "Limburg", "Melsungen",
        "Michelstadt", "Mörfelden-Walldorf", "Mühlheim", "Nidda", "Nidderau", "Ober-Ramstadt",
        "Oberursel", "Pfungstadt", "Raunheim", "Reinheim", "Riedstadt", "Rodgau", "Rödermark",
        "Rüsselsheim", "Schlüchtern", "Seligenstadt", "Stadtallendorf", "Taunusstein",
        "Viernheim", "Wächtersbach", "Wetzlar", "Witzenhausen"
    ],
    "Mecklenburg-Vorpommern": [
        "Anklam", "Bad Doberan", "Barth", "Bergen", "Boizenburg", "Demmin", "Gadebusch",
        "Grevesmühlen", "Grimmen", "Hagenow", "Ludwigslust", "Malchin", "Neustrelitz",
        "Parchim", "Pasewalk", "Ribnitz-Damgarten", "Röbel", "Sassnitz", "Stavenhagen",
        "Teterow", "Torgelow", "Ueckermünde", "Waren", "Wolgast"
    ],
    "Niedersachsen": [
        "Achim", "Alfeld", "Bad Bentheim", "Bad Essen", "Bad Gandersheim", "Bad Harzburg",
        "Bad Iburg", "Bad Münder", "Bad Nenndorf", "Bad Pyrmont", "Bad Salzdetfurth",
        "Barsinghausen", "Bramsche", "Buchholz", "Bückeburg", "Burgdorf", "Buxtehude",
        "Clausthal-Zellerfeld", "Cloppenburg", "Cuxhaven", "Damme", "Diepholz", "Duderstadt",
        "Einbeck", "Friesoythe", "Garbsen", "Georgsmarienhütte", "Gifhorn", "Goslar", "Hameln",
        "Hann. Münden", "Helmstedt", "Herzberg", "Holzminden", "Jever", "Leer", "Lingen",
        "Lohne", "Melle", "Meppen", "Neustadt", "Nienburg", "Nordenham", "Nordhorn",
        "Northeim", "Osterholz-Scharmbeck", "Osterode", "Papenburg", "Peine", "Quakenbrück",
        "Rinteln", "Sarstedt", "Schneverdingen", "Seesen", "Sehnde", "Soltau", "Springe",
        "Stade", "Stadthagen", "Sulingen", "Syke", "Uelzen", "Uslar", "Vechta", "Verden",
        "Walsrode", "Wennigsen", "Westerstede", "Winsen", "Wittmund", "Wunstorf"
    ],
    "Nordrhein-Westfalen": [
        "Ahlen", "Alsdorf", "Altena", "Attendorn", "Bad Berleburg", "Bad Driburg", "Bad Laasphe",
        "Bad Lippspringe", "Bad Oeynhausen", "Bad Salzuflen", "Beckum", "Bedburg", "Bergheim",
        "Bergneustadt", "Borgholzhausen", "Borken", "Brilon", "Brühl", "Bünde", "Burscheid",
        "Coesfeld", "Datteln", "Dinslaken", "Dülmen", "Emmerich", "Ennepetal", "Erftstadt",
        "Erkrath", "Erwitte", "Espelkamp", "Frechen", "Geilenkirchen", "Gescher", "Geseke",
        "Gevelsberg", "Gladbeck", "Goch", "Greven", "Gronau", "Gummersbach", "Gütersloh",
        "Haltern", "Halver", "Hamminkeln", "Hattingen", "Heinsberg", "Hemer", "Hennef",
        "Herdecke", "Herford", "Herten", "Herzogenrath", "Hilden", "Höxter", "Hückelhoven",
        "Hürth", "Ibbenbüren", "Jülich", "Kaarst", "Kamen", "Kamp-Lintfort", "Kempen",
        "Kleve", "Königswinter", "Langenfeld", "Lemgo", "Lennestadt", "Leopoldshoehe",
        "Lippstadt", "Lohmar", "Löhne", "Lübbecke", "Lüdenscheid", "Lünen", "Mechernich",
        "Meckenheim", "Meerbusch", "Meinerzhagen", "Menden", "Meschede", "Mettmann", "Monheim",
        "Much", "Netphen", "Nettetal", "Neukirchen-Vluyn", "Niederkassel", "Ochtrup", "Oer-Erkenschwick",
        "Oerlinghausen", "Olpe", "Overath", "Petershagen", "Plettenberg", "Porta Westfalica",
        "Pulheim", "Radevormwald", "Ratingen", "Rheda-Wiedenbrück", "Rheinbach", "Rheinberg",
        "Rheine", "Rietberg", "Rödinghausen", "Rösrath", "Salzkotten", "Schmallenberg", "Schwelm",
        "Schwerte", "Selm", "Siegburg", "Soest", "Sprockhövel", "Steinfurt", "Stolberg",
        "Straelen", "Sundern", "Swisttal", "Tönisvorst", "Übach-Palenberg", "Versmold",
        "Voerde", "Vreden", "Waltrop", "Warburg", "Warendorf", "Warstein", "Werl", "Wermelskirchen",
        "Wesseling", "Wetter", "Wiehl", "Willich", "Wilnsdorf", "Winterberg", "Wipperfürth", "Xanten"
    ],
    "Rheinland-Pfalz": [
        "Alzey", "Andernach", "Bad Dürkheim", "Bad Ems", "Bad Neuenahr-Ahrweiler", "Bendorf",
        "Betzdorf", "Bingen", "Bitburg", "Boppard", "Cochem", "Daun", "Diez", "Frankenthal",
        "Germersheim", "Grünstadt", "Haßloch", "Herxheim", "Idar-Oberstein", "Ingelheim",
        "Kirn", "Konz", "Kusel", "Lahnstein", "Landau", "Mayen", "Montabaur", "Morbach",
        "Neustadt", "Neuwied", "Pirmasens", "Prüm", "Remagen", "Schifferstadt", "Sinzig",
        "Wittlich", "Worms", "Zweibrücken"
    ],
    "Saarland": [
        "Blieskastel", "Dillingen", "Friedrichsthal", "Heusweiler", "Homburg", "Kirkel",
        "Lebach", "Losheim", "Marpingen", "Merzig", "Neunkirchen", "Ottweiler", "Püttlingen",
        "Quierschied", "Rehlingen-Siersburg", "Saarlouis", "Sankt Ingbert", "Sankt Wendel",
        "Schmelz", "Sulzbach", "Völklingen", "Wadern"
    ],
    "Sachsen": [
        "Annaberg-Buchholz", "Aue", "Borna", "Brand-Erbisdorf", "Burgstädt", "Coswig", "Crimmitschau",
        "Delitzsch", "Dippoldiswalde", "Döbeln", "Eilenburg", "Falkenstein", "Flöha", "Frankenberg",
        "Freital", "Glauchau", "Grimma", "Großenhain", "Hainichen", "Heidenau", "Hohenstein-Ernstthal",
        "Kamenz", "Limbach-Oberfrohna", "Löbau", "Marienberg", "Markkleeberg", "Meißen", "Mittweida",
        "Mülsen", "Niesky", "Oelsnitz", "Oschatz", "Pirna", "Radeberg", "Radebeul", "Reichenbach",
        "Riesa", "Rochlitz", "Schneeberg", "Schwarzenberg", "Stollberg", "Torgau", "Weißwasser",
        "Werdau", "Wurzen", "Zittau"
    ],
    "Sachsen-Anhalt": [
        "Aschersleben", "Ballenstedt", "Bernburg", "Bitterfeld-Wolfen", "Blankenburg",
        "Burg", "Calbe", "Eisleben", "Gardelegen", "Genthin", "Gommern", "Halberstadt",
        "Harzgerode", "Hettstedt", "Köthen", "Merseburg", "Naumburg", "Oschersleben",
        "Osterburg", "Quedlinburg", "Sangerhausen", "Schönebeck", "Staßfurt", "Thale",
        "Weißenfels", "Wittenberg", "Wolmirstedt", "Zeitz", "Zerbst"
    ],
    "Schleswig-Holstein": [
        "Ahrensburg", "Bad Bramstedt", "Bad Oldesloe", "Bad Segeberg", "Bargteheide", "Brunsbüttel",
        "Büdelsdorf", "Eckernförde", "Eutin", "Geesthacht", "Glückstadt", "Halstenbek",
        "Heide", "Henstedt-Ulzburg", "Husum", "Itzehoe", "Kaltenkirchen", "Lauenburg",
        "Mölln", "Norderstedt", "Pinneberg", "Plön", "Quickborn", "Ratzeburg", "Reinbek",
        "Rendsburg", "Schleswig", "Schenefeld", "Schwarzenbek", "Tornesch", "Uetersen",
        "Wedel"
    ],
    "Thüringen": [
        "Altenburg", "Apolda", "Arnstadt", "Bad Frankenhausen", "Bad Langensalza", "Bad Salzungen",
        "Eisenberg", "Gera", "Gotha", "Greiz", "Heiligenstadt", "Hildburghausen", "Ilmenau",
        "Leinefelde-Worbis", "Meiningen", "Mühlhausen", "Nordhausen", "Pößneck", "Rudolstadt",
        "Saalfeld", "Schmalkalden", "Schmölln", "Sömmerda", "Sondershausen", "Sonneberg",
        "Bad Liebenstein", "Waltershausen", "Zeulenroda-Triebes"
    ]
}

# Template für lokale Seiten
TEMPLATE = '''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Rauchmelder Service in {ort} - Professionelle Installation, Wartung und Prüfung von Rauchwarnmeldern nach DIN 14676. ☎ Jetzt kostenlos anfragen!">
    <meta name="keywords" content="Rauchmelder {ort}, Rauchmelder Installation {ort}, Rauchmelder Wartung {ort}, Brandschutz {ort}, Rauchwarnmelder {ort}">
    <title>Rauchmelder Service {ort} | Installation & Wartung | Secu.li</title>
    <link rel="canonical" href="https://secu.li/standorte/deutschland/{slug}.html">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../../styles.css">
    <meta name="theme-color" content="#C41E3A">
</head>
<body>
    <!-- Header -->
    <header class="header">
        <div class="container">
            <a href="../../index.html" class="logo">Secu.li</a>
            <nav class="nav">
                <ul class="nav-links">
                    <li><a href="index.html">Deutschland</a></li>
                    <li><a href="../../kontakt.html">Kontakt</a></li>
                </ul>
                <a href="../../index.html#kontakt" class="btn btn-primary btn-sm">Anfrage</a>
            </nav>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="hero-simple" style="padding-top: 140px; padding-bottom: 80px;">
        <div class="container">
            <div class="hero-centered">
                <span class="hero-badge-top">📍 {ort}, {bundesland}</span>
                <h1>Rauchmelder Service in {ort}</h1>
                <p class="subtitle">Professionelle Installation, Wartung und Prüfung von Rauchwarnmeldern in {ort} und Umgebung. Zertifizierte Fachkräfte. DIN 14676 konform.</p>
                <div class="hero-buttons">
                    <a href="../../index.html#kontakt" class="btn btn-primary btn-lg">Kostenlos anfragen</a>
                    <a href="tel:+498001234567" class="btn btn-secondary btn-lg">📞 Anrufen</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Services Section -->
    <section class="section bg-gray">
        <div class="container">
            <div class="section-header">
                <h2>Unsere Leistungen in {ort}</h2>
                <p>Kompletter Rauchmelder-Service für Privat und Gewerbe in {ort}</p>
            </div>
            <div class="features-grid">
                <div class="feature-card">
                    <div class="feature-icon">🔧</div>
                    <h4>Installation</h4>
                    <p>Fachgerechte Montage von Rauchmeldern in Ihrer Wohnung oder Immobilie in {ort}. Normgerecht nach DIN 14676.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">🔍</div>
                    <h4>Wartung & Prüfung</h4>
                    <p>Regelmäßige Funktionsprüfung und Dokumentation aller Rauchmelder in {ort}. Wir erinnern Sie an fällige Termine.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">🔄</div>
                    <h4>Austausch</h4>
                    <p>Ersatz defekter oder veralteter Rauchmelder in {ort}. Inklusive fachgerechter Entsorgung alter Geräte.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">📋</div>
                    <h4>Dokumentation</h4>
                    <p>Lückenlose Protokollierung für Vermieter und Hausverwaltungen in {ort}. Rechtssichere Nachweise.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Why Choose Us -->
    <section class="section">
        <div class="container">
            <div class="section-header">
                <h2>Warum Secu.li in {ort}?</h2>
            </div>
            <div class="trust-badges">
                <div class="trust-badge">
                    <span class="badge-icon">✓</span>
                    <span>DIN 14676 zertifiziert</span>
                </div>
                <div class="trust-badge">
                    <span class="badge-icon">✓</span>
                    <span>Lokaler Service in {ort}</span>
                </div>
                <div class="trust-badge">
                    <span class="badge-icon">✓</span>
                    <span>Schnelle Terminvergabe</span>
                </div>
                <div class="trust-badge">
                    <span class="badge-icon">✓</span>
                    <span>Faire Preise</span>
                </div>
                <div class="trust-badge">
                    <span class="badge-icon">✓</span>
                    <span>Erfahrene Techniker</span>
                </div>
                <div class="trust-badge">
                    <span class="badge-icon">✓</span>
                    <span>Komplette Dokumentation</span>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA Section -->
    <section class="section bg-primary">
        <div class="container">
            <div class="cta-content" style="text-align: center; color: white;">
                <h2 style="color: white;">Rauchmelder Service in {ort} anfragen</h2>
                <p style="color: rgba(255,255,255,0.9); margin-bottom: 2rem;">Fordern Sie jetzt ein kostenloses Angebot für Ihr Objekt in {ort} an.</p>
                <a href="../../index.html#kontakt" class="btn btn-secondary btn-lg">Jetzt kostenlos anfragen</a>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-simple">
                <p>&copy; 2024 Secu.li - Rauchmelder Service {ort}</p>
                <div class="footer-links">
                    <a href="../../impressum.html">Impressum</a>
                    <a href="../../datenschutz.html">Datenschutz</a>
                </div>
            </div>
        </div>
    </footer>

    <script src="../../script.js"></script>
</body>
</html>'''

def create_slug(name):
    """Erstellt URL-freundlichen Slug aus Ortsnamen"""
    replacements = {
        'ä': 'ae', 'ö': 'oe', 'ü': 'ue', 'ß': 'ss',
        'Ä': 'Ae', 'Ö': 'Oe', 'Ü': 'Ue',
        ' ': '-', '/': '-', '.': ''
    }
    slug = name.lower()
    for old, new in replacements.items():
        slug = slug.replace(old, new)
    return slug

def main():
    base_path = Path("/Users/neslihanakdeniz/Desktop/Rauchmelder/standorte/deutschland")
    created_count = 0
    
    for bundesland, orte in ORTE_NACH_BUNDESLAND.items():
        for ort in orte:
            slug = create_slug(ort)
            filepath = base_path / f"{slug}.html"
            
            # Nur erstellen wenn Datei noch nicht existiert
            if not filepath.exists():
                content = TEMPLATE.format(
                    ort=ort,
                    bundesland=bundesland,
                    slug=slug
                )
                filepath.write_text(content, encoding='utf-8')
                created_count += 1
                print(f"✓ Erstellt: {slug}.html ({ort}, {bundesland})")
    
    print(f"\n✅ {created_count} neue Seiten erstellt!")

if __name__ == "__main__":
    main()
