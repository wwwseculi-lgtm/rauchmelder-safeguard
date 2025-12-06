#!/usr/bin/env python3
"""
SEO-Seiten Generator für deutsche Bundesländer
"""

import os

BUNDESLAENDER = {
    "bayern": {
        "name": "Bayern",
        "hauptstadt": "München",
        "einwohner": "13,2 Millionen",
        "staedte": ["München", "Nürnberg", "Augsburg", "Regensburg", "Ingolstadt", "Würzburg", "Erlangen", "Fürth", "Passau", "Landshut", "Rosenheim", "Freising"],
        "beschreibung": "Bayern ist mit rund 13,2 Millionen Einwohnern das bevölkerungsreichste Bundesland nach Nordrhein-Westfalen. Von der Hauptstadt München bis zu den ländlichen Regionen – überall gilt die Rauchmelderpflicht."
    },
    "nordrhein-westfalen": {
        "name": "Nordrhein-Westfalen",
        "hauptstadt": "Düsseldorf",
        "einwohner": "18 Millionen",
        "staedte": ["Köln", "Düsseldorf", "Dortmund", "Essen", "Duisburg", "Bochum", "Wuppertal", "Bielefeld", "Bonn", "Münster", "Gelsenkirchen", "Mönchengladbach", "Aachen", "Krefeld", "Oberhausen", "Hagen"],
        "beschreibung": "Nordrhein-Westfalen ist mit 18 Millionen Einwohnern das bevölkerungsreichste Bundesland Deutschlands. In NRW gilt seit 2017 die Rauchmelderpflicht für alle Wohnungen."
    },
    "baden-wuerttemberg": {
        "name": "Baden-Württemberg",
        "hauptstadt": "Stuttgart",
        "einwohner": "11,1 Millionen",
        "staedte": ["Stuttgart", "Karlsruhe", "Mannheim", "Freiburg", "Heidelberg", "Ulm", "Heilbronn", "Pforzheim", "Reutlingen", "Tübingen", "Konstanz", "Offenburg"],
        "beschreibung": "Baden-Württemberg mit seiner Hauptstadt Stuttgart ist ein wirtschaftsstarkes Bundesland im Südwesten. Hier gilt die Rauchmelderpflicht seit 2015."
    },
    "niedersachsen": {
        "name": "Niedersachsen",
        "hauptstadt": "Hannover",
        "einwohner": "8 Millionen",
        "staedte": ["Hannover", "Braunschweig", "Oldenburg", "Osnabrück", "Wolfsburg", "Göttingen", "Salzgitter", "Hildesheim", "Wilhelmshaven", "Celle", "Lüneburg"],
        "beschreibung": "Niedersachsen ist flächenmäßig das zweitgrößte Bundesland. Von der Nordseeküste bis zum Harz – überall ist Rauchmelder-Service verfügbar."
    },
    "hessen": {
        "name": "Hessen",
        "hauptstadt": "Wiesbaden",
        "einwohner": "6,3 Millionen",
        "staedte": ["Frankfurt am Main", "Wiesbaden", "Kassel", "Darmstadt", "Offenbach", "Hanau", "Gießen", "Marburg", "Fulda", "Rüsselsheim"],
        "beschreibung": "Hessen mit dem Finanzstandort Frankfurt ist ein wirtschaftliches Zentrum Deutschlands. Die Rauchmelderpflicht gilt seit 2005 für Neubauten, seit 2015 für alle Wohnungen."
    },
    "sachsen": {
        "name": "Sachsen",
        "hauptstadt": "Dresden",
        "einwohner": "4,1 Millionen",
        "staedte": ["Leipzig", "Dresden", "Chemnitz", "Zwickau", "Plauen", "Görlitz", "Freiberg", "Bautzen", "Pirna", "Meißen"],
        "beschreibung": "Sachsen mit seinen Kulturstädten Dresden und Leipzig ist ein wichtiger Standort im Osten Deutschlands. Die Rauchmelderpflicht gilt seit 2016."
    },
    "berlin": {
        "name": "Berlin",
        "hauptstadt": "Berlin",
        "einwohner": "3,7 Millionen",
        "staedte": ["Berlin-Mitte", "Charlottenburg", "Kreuzberg", "Prenzlauer Berg", "Neukölln", "Spandau", "Steglitz", "Pankow", "Lichtenberg", "Reinickendorf"],
        "beschreibung": "Berlin ist Hauptstadt und größte Stadt Deutschlands. Seit 2017 gilt in Berlin die vollständige Rauchmelderpflicht für alle Wohnungen."
    },
    "rheinland-pfalz": {
        "name": "Rheinland-Pfalz",
        "hauptstadt": "Mainz",
        "einwohner": "4,1 Millionen",
        "staedte": ["Mainz", "Ludwigshafen", "Koblenz", "Trier", "Kaiserslautern", "Worms", "Neuwied", "Speyer", "Bad Kreuznach"],
        "beschreibung": "Rheinland-Pfalz mit der Landeshauptstadt Mainz liegt im Westen Deutschlands. Die Rauchmelderpflicht gilt seit 2012."
    },
    "schleswig-holstein": {
        "name": "Schleswig-Holstein",
        "hauptstadt": "Kiel",
        "einwohner": "2,9 Millionen",
        "staedte": ["Kiel", "Lübeck", "Flensburg", "Neumünster", "Norderstedt", "Elmshorn", "Pinneberg", "Itzehoe"],
        "beschreibung": "Schleswig-Holstein ist das nördlichste Bundesland zwischen Nord- und Ostsee. Die Rauchmelderpflicht gilt seit 2011."
    },
    "brandenburg": {
        "name": "Brandenburg",
        "hauptstadt": "Potsdam",
        "einwohner": "2,5 Millionen",
        "staedte": ["Potsdam", "Cottbus", "Brandenburg an der Havel", "Frankfurt (Oder)", "Oranienburg", "Falkensee", "Bernau", "Eberswalde"],
        "beschreibung": "Brandenburg umgibt die Hauptstadt Berlin und bietet eine Mischung aus Stadt und Land. Die Rauchmelderpflicht gilt seit 2016."
    },
    "thueringen": {
        "name": "Thüringen",
        "hauptstadt": "Erfurt",
        "einwohner": "2,1 Millionen",
        "staedte": ["Erfurt", "Jena", "Gera", "Weimar", "Gotha", "Eisenach", "Suhl", "Nordhausen"],
        "beschreibung": "Thüringen im Herzen Deutschlands ist bekannt für seine Geschichte und Kultur. Die Rauchmelderpflicht gilt seit 2008."
    },
    "sachsen-anhalt": {
        "name": "Sachsen-Anhalt",
        "hauptstadt": "Magdeburg",
        "einwohner": "2,2 Millionen",
        "staedte": ["Magdeburg", "Halle (Saale)", "Dessau-Roßlau", "Lutherstadt Wittenberg", "Stendal", "Wernigerode"],
        "beschreibung": "Sachsen-Anhalt mit Magdeburg und Halle ist ein wichtiger Standort im Osten. Die Rauchmelderpflicht gilt seit 2009."
    },
    "mecklenburg-vorpommern": {
        "name": "Mecklenburg-Vorpommern",
        "hauptstadt": "Schwerin",
        "einwohner": "1,6 Millionen",
        "staedte": ["Rostock", "Schwerin", "Neubrandenburg", "Stralsund", "Greifswald", "Wismar", "Güstrow"],
        "beschreibung": "Mecklenburg-Vorpommern an der Ostseeküste ist bekannt für Tourismus und Natur. Die Rauchmelderpflicht gilt seit 2006."
    },
    "saarland": {
        "name": "Saarland",
        "hauptstadt": "Saarbrücken",
        "einwohner": "990.000",
        "staedte": ["Saarbrücken", "Neunkirchen", "Homburg", "Völklingen", "St. Ingbert", "Saarlouis"],
        "beschreibung": "Das Saarland ist das kleinste Flächenland Deutschlands. Die Rauchmelderpflicht gilt seit 2004 – als eines der ersten Bundesländer."
    },
    "hamburg": {
        "name": "Hamburg",
        "hauptstadt": "Hamburg",
        "einwohner": "1,9 Millionen",
        "staedte": ["Altona", "Eimsbüttel", "Wandsbek", "Harburg", "Bergedorf", "Hamburg-Nord", "Hamburg-Mitte"],
        "beschreibung": "Hamburg ist die zweitgrößte Stadt Deutschlands und ein wichtiger Hafenstandort. Die Rauchmelderpflicht gilt seit 2006."
    },
    "bremen": {
        "name": "Bremen",
        "hauptstadt": "Bremen",
        "einwohner": "680.000",
        "staedte": ["Bremen", "Bremerhaven"],
        "beschreibung": "Bremen ist das kleinste Bundesland, bestehend aus den Städten Bremen und Bremerhaven. Die Rauchmelderpflicht gilt seit 2010."
    },
}

TEMPLATE = '''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Rauchmelder Service in {name} - Installation & Wartung in allen Städten. {einwohner} Einwohner, TÜV-geprüft, 10 Jahre Garantie.">
    <meta name="keywords" content="Rauchmelder {name}, Rauchmelderpflicht {name}, Rauchmelder Installation {name}, Brandschutz {name}">
    <title>Rauchmelder Service {name} | Alle Städte | Secu.li</title>
    <link rel="canonical" href="https://secu.li/standorte/deutschland/{slug}.html">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../../styles.css">
    <style>
        .cities-list {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 1rem; margin-top: 2rem; }}
        .city-link {{ display: block; padding: 1rem; background: var(--white); border-radius: var(--radius-lg); border: 1px solid var(--gray-200); text-decoration: none; color: var(--gray-800); transition: all 0.2s; text-align: center; }}
        .city-link:hover {{ border-color: var(--primary); transform: translateY(-2px); }}
    </style>
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
                    <span class="hero-badge-top">🏛️ {name}</span>
                    <h1>Rauchmelder Service in {name}</h1>
                    <p class="subtitle">Professionelle Installation und Wartung in allen Städten von {name}. {einwohner} Einwohner vertrauen auf zertifizierten Brandschutz.</p>
                    <div class="hero-buttons">
                        <a href="#kontaktformular" class="btn btn-primary btn-lg">Kostenloses Angebot</a>
                        <a href="tel:+498001234567" class="btn btn-outline btn-lg">📞 Anrufen</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="section">
        <div class="container">
            <div class="section-header">
                <h2>Rauchmelderpflicht in {name}</h2>
            </div>
            <div style="max-width: 800px; margin: 0 auto; line-height: 1.8;">
                <p>{beschreibung}</p>
                
                <h3 style="margin-top: 2rem;">Unsere Leistungen in {name}</h3>
                <ul style="margin: 1rem 0;">
                    <li>✓ <strong>Neuinstallation</strong> von Rauchmeldern nach DIN 14676</li>
                    <li>✓ <strong>Jährliche Wartung</strong> mit Funktionsprüfung</li>
                    <li>✓ <strong>Austausch</strong> nach Ablauf der 10-Jahres-Frist</li>
                    <li>✓ <strong>Dokumentation</strong> für Vermieter und Hausverwaltungen</li>
                    <li>✓ <strong>Service in allen Städten</strong> von {name}</li>
                </ul>
            </div>
        </div>
    </section>

    <section class="section bg-gray">
        <div class="container">
            <div class="section-header">
                <span class="section-badge">Unsere Standorte</span>
                <h2>Städte in {name}</h2>
                <p>Wir bieten Rauchmelder-Service in allen Städten von {name}.</p>
            </div>
            <div class="cities-list">
                {staedte_html}
            </div>
        </div>
    </section>

    <section class="section">
        <div class="container">
            <div class="section-header">
                <span class="section-badge">Leistungen</span>
                <h2>Was wir in {name} bieten</h2>
            </div>
            <div class="features-grid">
                <div class="feature-card"><div class="feature-icon">🔧</div><h4>Installation</h4><p>Fachgerechte Montage in ganz {name}.</p></div>
                <div class="feature-card"><div class="feature-icon">🔍</div><h4>Wartung</h4><p>Jährliche Prüfung nach Vorschrift.</p></div>
                <div class="feature-card"><div class="feature-icon">🔄</div><h4>Austausch</h4><p>Erneuerung nach 10 Jahren.</p></div>
                <div class="feature-card"><div class="feature-icon">📋</div><h4>Dokumentation</h4><p>Rechtssichere Protokolle.</p></div>
            </div>
        </div>
    </section>

    <section class="contact-form-section" id="kontaktformular">
        <div class="container">
            <div class="contact-header-centered">
                <span class="section-badge">Jetzt anfragen</span>
                <h2>Angebot für {name}</h2>
                <p>Kostenlos und unverbindlich – Antwort in 24 Stunden.</p>
            </div>
            <div class="contact-form-card contact-form-large">
                <form class="contact-form" id="localContactForm">
                    <input type="hidden" name="bundesland" value="{name}">
                    <div class="form-grid-3">
                        <div class="form-group"><label for="name">Name *</label><input type="text" id="name" name="name" required></div>
                        <div class="form-group"><label for="email">E-Mail *</label><input type="email" id="email" name="email" required></div>
                        <div class="form-group"><label for="stadt">Ihre Stadt *</label><input type="text" id="stadt" name="stadt" placeholder="z.B. {hauptstadt}" required></div>
                    </div>
                    <div class="form-group"><label for="message">Ihre Nachricht</label><textarea id="message" name="message" rows="4"></textarea></div>
                    <div class="form-submit-row">
                        <button type="submit" class="btn btn-primary btn-xl">Angebot für {name} anfordern →</button>
                    </div>
                </form>
            </div>
        </div>
    </section>

    <footer class="footer">
        <div class="container">
            <div class="footer-bottom">
                <p>© 2024 Secu.li – Rauchmelder Service {name} | <a href="index.html" style="color: var(--gray-400);">Alle Standorte</a></p>
            </div>
        </div>
    </footer>
    <script src="../../script.js"></script>
</body>
</html>'''

def generate_bundeslaender():
    output_dir = "standorte/bundeslaender"
    os.makedirs(output_dir, exist_ok=True)
    
    count = 0
    for slug, data in BUNDESLAENDER.items():
        name = data["name"]
        hauptstadt = data["hauptstadt"]
        einwohner = data["einwohner"]
        staedte = data["staedte"]
        beschreibung = data["beschreibung"]
        
        # Städte HTML generieren
        staedte_html = ""
        for stadt in staedte:
            staedte_html += f'<a href="#" class="city-link">{stadt}</a>\n                '
        
        content = TEMPLATE.format(
            name=name,
            slug=slug,
            hauptstadt=hauptstadt,
            einwohner=einwohner,
            beschreibung=beschreibung,
            staedte_html=staedte_html.strip()
        )
        
        filepath = os.path.join(output_dir, f"{slug}.html")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        
        count += 1
        print(f"✅ {name}")
    
    print(f"\n🎉 {count} Bundesländer-Seiten erstellt!")

if __name__ == "__main__":
    generate_bundeslaender()
