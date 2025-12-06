#!/usr/bin/env python3
"""
Generator für lokale SEO-Seiten mit einzigartigem Content und Kontaktformular
Jede Seite hat unterschiedliche Texte um Duplicate Content zu vermeiden
"""

import os
import random
import hashlib
from pathlib import Path

# Landkreise und kleine Städte nach Bundesland (gleiche Liste wie vorher)
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

# Verschiedene Text-Varianten für einzigartigen Content
INTRO_VARIANTEN = [
    "Sie suchen einen zuverlässigen Rauchmelder-Service in {ort}? Dann sind Sie bei Secu.li genau richtig! Wir bieten professionelle Installation, regelmäßige Wartung und schnellen Austausch von Rauchwarnmeldern für Privathaushalte und Gewerbeobjekte.",
    "In {ort} und Umgebung sind wir Ihr kompetenter Partner für alle Fragen rund um Rauchmelder. Ob Neuinstallation, jährliche Prüfung oder Modernisierung - unser erfahrenes Team steht Ihnen zur Verfügung.",
    "Sicherheit beginnt mit funktionierenden Rauchmeldern. Als Ihr lokaler Dienstleister in {ort} sorgen wir dafür, dass Ihre Rauchwarnmelder zuverlässig arbeiten und alle gesetzlichen Anforderungen erfüllen.",
    "Rauchmelder können Leben retten - aber nur wenn sie richtig installiert und regelmäßig gewartet werden. Unser Service in {ort} garantiert höchste Qualität bei Installation und Wartung.",
    "Ihr Rauchmelder-Spezialist für {ort}: Wir installieren, prüfen und warten Rauchwarnmelder in Wohnungen, Mehrfamilienhäusern und Gewerbeimmobilien. Normgerecht nach DIN 14676.",
    "Von der Erstberatung bis zur regelmäßigen Wartung - in {ort} bieten wir den kompletten Rauchmelder-Service aus einer Hand. Vertrauen Sie auf unsere Erfahrung und Expertise."
]

SERVICE_VARIANTEN = [
    "Unsere geschulten Techniker installieren Rauchmelder fachgerecht an den optimalen Positionen in Ihrem Objekt in {ort}. Wir berücksichtigen dabei die baulichen Gegebenheiten und sorgen für maximalen Schutz.",
    "Die Installation von Rauchmeldern in {ort} übernehmen wir schnell und professionell. Unsere Experten wissen genau, wo die Melder platziert werden müssen, um im Ernstfall rechtzeitig zu warnen.",
    "Professionelle Rauchmelder-Montage in {ort}: Wir installieren Ihre Geräte normgerecht und dokumentieren jeden Schritt. So sind Sie auf der sicheren Seite - auch gegenüber Versicherungen.",
    "Bei der Installation in {ort} setzen wir auf hochwertige Rauchmelder führender Hersteller. Die Montage erfolgt sauber, schnell und ohne Beschädigung Ihrer Decken."
]

WARTUNG_VARIANTEN = [
    "Die jährliche Wartung Ihrer Rauchmelder in {ort} ist gesetzlich vorgeschrieben. Wir übernehmen die Prüfung, dokumentieren die Ergebnisse und erinnern Sie rechtzeitig an den nächsten Termin.",
    "Regelmäßige Funktionsprüfungen sichern die Zuverlässigkeit Ihrer Rauchmelder. Unser Wartungsservice in {ort} umfasst Sichtprüfung, Funktionstest und bei Bedarf Batteriewechsel.",
    "Als Vermieter in {ort} sind Sie für die Wartung der Rauchmelder verantwortlich. Wir nehmen Ihnen diese Pflicht ab und sorgen für lückenlose Dokumentation.",
    "Mit unserem Wartungsvertrag in {ort} haben Sie keine Sorgen mehr: Wir kommen regelmäßig, prüfen alle Geräte und tauschen defekte Melder sofort aus."
]

VORTEILE_VARIANTEN = [
    "Warum Kunden in {ort} uns vertrauen: Schnelle Terminvergabe, faire Preise, kompetente Beratung und zuverlässige Ausführung. Wir sind Ihr Partner für Brandschutz.",
    "Unsere Stärken in {ort}: Langjährige Erfahrung, geschultes Fachpersonal, hochwertige Produkte und erstklassiger Kundenservice. Überzeugen Sie sich selbst!",
    "Von der ersten Beratung bis zur Wartung - in {ort} bieten wir Ihnen Komplettservice mit höchsten Qualitätsstandards. Ihre Sicherheit ist unser Anliegen.",
    "Was uns in {ort} auszeichnet: Wir arbeiten pünktlich, sauber und zuverlässig. Alle unsere Techniker sind zertifiziert und regelmäßig geschult."
]

CTA_VARIANTEN = [
    "Fordern Sie jetzt Ihr kostenloses Angebot für {ort} an - wir melden uns innerhalb von 24 Stunden bei Ihnen!",
    "Kontaktieren Sie uns noch heute für eine unverbindliche Beratung zu Ihrem Objekt in {ort}.",
    "Sichern Sie sich jetzt Ihren Termin in {ort} - kostenlose Erstberatung inklusive!",
    "Jetzt Anfrage senden und professionellen Rauchmelder-Service in {ort} genießen.",
    "Haben Sie Fragen zu Rauchmeldern in {ort}? Unser Team berät Sie gerne - kostenlos und unverbindlich!"
]

GESETZ_VARIANTEN = [
    "In {bundesland} gilt die Rauchmelderpflicht für alle Wohnungen. In Schlafzimmern, Kinderzimmern und Fluren, die als Rettungswege dienen, müssen Rauchmelder installiert sein.",
    "Die Landesbauordnung {bundesland} schreibt Rauchmelder in Wohnräumen vor. Als Eigentümer sind Sie für die Installation verantwortlich - wir helfen Ihnen dabei.",
    "Seit der Einführung der Rauchmelderpflicht in {bundesland} sind funktionsfähige Rauchmelder in jeder Wohnung Pflicht. Wir sorgen in {ort} für die korrekte Umsetzung.",
    "Die gesetzlichen Anforderungen an Rauchmelder in {bundesland} sind klar geregelt. Mit unserem Service in {ort} erfüllen Sie alle Vorgaben problemlos."
]

def get_deterministic_choice(choices, seed_string):
    """Wählt deterministisch basierend auf einem Seed-String"""
    hash_val = int(hashlib.md5(seed_string.encode()).hexdigest(), 16)
    return choices[hash_val % len(choices)]

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

TEMPLATE = '''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Rauchmelder Service in {ort} - Professionelle Installation, Wartung und Prüfung von Rauchwarnmeldern nach DIN 14676. ☎ Jetzt kostenlos anfragen!">
    <meta name="keywords" content="Rauchmelder {ort}, Rauchmelder Installation {ort}, Rauchmelder Wartung {ort}, Brandschutz {ort}, Rauchwarnmelder {ort}, Rauchmelder Pflicht {bundesland}">
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
                <a href="#kontakt" class="btn btn-primary btn-sm">Anfrage</a>
            </nav>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="hero-simple" style="padding-top: 140px; padding-bottom: 60px;">
        <div class="container">
            <div class="hero-centered">
                <span class="hero-badge-top">📍 {ort}, {bundesland}</span>
                <h1>Rauchmelder Service in {ort}</h1>
                <p class="subtitle">{intro_text}</p>
                <div class="hero-buttons">
                    <a href="#kontakt" class="btn btn-primary btn-lg">Kostenlos anfragen</a>
                    <a href="tel:+498001234567" class="btn btn-secondary btn-lg">📞 Anrufen</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Intro Text Section -->
    <section class="section">
        <div class="container">
            <div class="content-text" style="max-width: 800px; margin: 0 auto;">
                <h2>Ihr Rauchmelder-Experte in {ort}</h2>
                <p>{service_text}</p>
                <p>{wartung_text}</p>
            </div>
        </div>
    </section>

    <!-- Services Section -->
    <section class="section bg-gray">
        <div class="container">
            <div class="section-header">
                <h2>Unsere Leistungen in {ort}</h2>
                <p>Komplettservice für private und gewerbliche Kunden</p>
            </div>
            <div class="features-grid">
                <div class="feature-card">
                    <div class="feature-icon">🔧</div>
                    <h4>Installation</h4>
                    <p>Fachgerechte Montage von Rauchmeldern in Wohnungen, Häusern und Gewerbeimmobilien in {ort}. DIN 14676 konform.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">🔍</div>
                    <h4>Wartung & Prüfung</h4>
                    <p>Jährliche Funktionsprüfung mit vollständiger Dokumentation für Vermieter und Eigentümer in {ort}.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">🔄</div>
                    <h4>Austausch</h4>
                    <p>Ersatz veralteter oder defekter Rauchmelder. Inklusive fachgerechter Entsorgung der Altgeräte.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">📋</div>
                    <h4>Beratung</h4>
                    <p>Individuelle Beratung zu Rauchmeldertypen, Positionierung und gesetzlichen Anforderungen in {bundesland}.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Gesetzliche Anforderungen -->
    <section class="section">
        <div class="container">
            <div class="content-text" style="max-width: 800px; margin: 0 auto;">
                <h2>Rauchmelderpflicht in {bundesland}</h2>
                <p>{gesetz_text}</p>
                <p>{vorteile_text}</p>
            </div>
        </div>
    </section>

    <!-- Contact Form Section -->
    <section class="section bg-gray" id="kontakt">
        <div class="container">
            <div class="section-header">
                <h2>Jetzt Angebot für {ort} anfordern</h2>
                <p>{cta_text}</p>
            </div>
            <div class="contact-form-wrapper" style="max-width: 600px; margin: 0 auto;">
                <form class="contact-form" id="localContactForm" action="https://formspree.io/f/xrbnlwal" method="POST">
                    <input type="hidden" name="_subject" value="Anfrage aus {ort} - secu.li">
                    <input type="hidden" name="standort" value="{ort}, {bundesland}">
                    <div class="form-group">
                        <label for="name">Name *</label>
                        <input type="text" id="name" name="name" placeholder="Ihr vollständiger Name" required>
                    </div>
                    <div class="form-row" style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
                        <div class="form-group">
                            <label for="email">E-Mail *</label>
                            <input type="email" id="email" name="email" placeholder="ihre@email.de" required>
                        </div>
                        <div class="form-group">
                            <label for="phone">Telefon</label>
                            <input type="tel" id="phone" name="phone" placeholder="+49 123 456789">
                        </div>
                    </div>
                    <div class="form-group">
                        <label for="service">Was benötigen Sie?</label>
                        <select id="service" name="service">
                            <option value="">Bitte auswählen...</option>
                            <option value="installation">Rauchmelder Installation</option>
                            <option value="wartung">Wartung & Prüfung</option>
                            <option value="austausch">Austausch alter Rauchmelder</option>
                            <option value="beratung">Kostenlose Beratung</option>
                            <option value="gewerbe">Gewerbliche Anfrage</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="units">Anzahl Wohneinheiten / Räume</label>
                        <select id="units" name="units">
                            <option value="">Bitte auswählen...</option>
                            <option value="1-5">1-5 Räume</option>
                            <option value="6-20">6-20 Räume</option>
                            <option value="21-50">21-50 Räume</option>
                            <option value="50+">Mehr als 50 Räume</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="message">Ihre Nachricht</label>
                        <textarea id="message" name="message" rows="4" placeholder="Beschreiben Sie kurz Ihr Anliegen..."></textarea>
                    </div>
                    <button type="submit" class="btn btn-primary btn-lg" style="width: 100%;">Kostenlose Anfrage senden</button>
                    <p style="font-size: 0.875rem; color: #6B7280; margin-top: 1rem; text-align: center;">
                        🔒 Ihre Daten werden vertraulich behandelt. Antwort innerhalb von 24 Stunden.
                    </p>
                </form>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-simple">
                <p>&copy; 2024 Secu.li - Rauchmelder Service {ort}, {bundesland}</p>
                <div class="footer-links">
                    <a href="../../impressum.html">Impressum</a>
                    <a href="../../datenschutz.html">Datenschutz</a>
                </div>
            </div>
        </div>
    </footer>

    <script src="../../script.js"></script>
    <script>
        // Local form AJAX handling
        document.getElementById('localContactForm')?.addEventListener('submit', async function(e) {{
            e.preventDefault();
            const btn = this.querySelector('button[type="submit"]');
            const originalText = btn.textContent;
            btn.textContent = 'Wird gesendet...';
            btn.disabled = true;
            
            try {{
                const response = await fetch(this.action, {{
                    method: 'POST',
                    body: new FormData(this),
                    headers: {{ 'Accept': 'application/json' }}
                }});
                if (response.ok) {{
                    window.location.href = '../../danke.html';
                }} else {{
                    throw new Error('Fehler');
                }}
            }} catch (error) {{
                btn.textContent = '❌ Fehler - erneut versuchen';
                btn.disabled = false;
                setTimeout(() => {{ btn.textContent = originalText; }}, 3000);
            }}
        }});
    </script>
</body>
</html>'''

def main():
    base_path = Path("/Users/neslihanakdeniz/Desktop/Rauchmelder/standorte/deutschland")
    updated_count = 0
    
    for bundesland, orte in ORTE_NACH_BUNDESLAND.items():
        for ort in orte:
            slug = create_slug(ort)
            filepath = base_path / f"{slug}.html"
            
            # Einzigartige Texte basierend auf Ortsnamen wählen
            seed = f"{ort}-{bundesland}"
            intro_text = get_deterministic_choice(INTRO_VARIANTEN, seed + "intro").format(ort=ort)
            service_text = get_deterministic_choice(SERVICE_VARIANTEN, seed + "service").format(ort=ort)
            wartung_text = get_deterministic_choice(WARTUNG_VARIANTEN, seed + "wartung").format(ort=ort)
            vorteile_text = get_deterministic_choice(VORTEILE_VARIANTEN, seed + "vorteile").format(ort=ort)
            cta_text = get_deterministic_choice(CTA_VARIANTEN, seed + "cta").format(ort=ort)
            gesetz_text = get_deterministic_choice(GESETZ_VARIANTEN, seed + "gesetz").format(ort=ort, bundesland=bundesland)
            
            content = TEMPLATE.format(
                ort=ort,
                bundesland=bundesland,
                slug=slug,
                intro_text=intro_text,
                service_text=service_text,
                wartung_text=wartung_text,
                vorteile_text=vorteile_text,
                cta_text=cta_text,
                gesetz_text=gesetz_text
            )
            
            filepath.write_text(content, encoding='utf-8')
            updated_count += 1
            print(f"✓ Aktualisiert: {slug}.html")
    
    print(f"\n✅ {updated_count} Seiten mit einzigartigem Content und Kontaktformular aktualisiert!")

if __name__ == "__main__":
    main()
