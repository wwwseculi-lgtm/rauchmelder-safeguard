#!/usr/bin/env python3
"""
Stadtteile/Bezirke Seiten Generator
Erstellt detaillierte Seiten für alle Stadtteile der Großstädte
"""

import os
from pathlib import Path

OUTPUT_DIR = Path("/Users/neslihanakdeniz/Desktop/Rauchmelder/standorte/deutschland")

# Großstädte mit allen Stadtteilen/Bezirken
CITY_DISTRICTS = {
    "berlin": {
        "name": "Berlin",
        "stadtteile": [
            "Mitte", "Prenzlauer Berg", "Pankow", "Weißensee", "Friedrichshain", 
            "Kreuzberg", "Neukölln", "Treptow", "Köpenick", "Lichtenberg",
            "Hohenschönhausen", "Marzahn", "Hellersdorf", "Charlottenburg",
            "Wilmersdorf", "Spandau", "Steglitz", "Zehlendorf", "Tempelhof",
            "Schöneberg", "Reinickendorf", "Wedding", "Moabit", "Tiergarten",
            "Grunewald", "Dahlem", "Wannsee", "Frohnau", "Hermsdorf", "Tegel",
            "Lübars", "Waidmannslust", "Wittenau", "Borsigwalde", "Märkisches Viertel",
            "Rosenthal", "Blankenburg", "Heinersdorf", "Karow", "Buch",
            "Französisch Buchholz", "Niederschönhausen", "Wilhelmsruh", "Schönholz",
            "Blankenfelde", "Malchow", "Wartenberg", "Falkenberg", "Fennpfuhl",
            "Rummelsburg", "Karlshorst", "Friedrichsfelde", "Biesdorf", "Kaulsdorf",
            "Mahlsdorf", "Alt-Hohenschönhausen", "Neu-Hohenschönhausen",
            "Adlershof", "Altglienicke", "Baumschulenweg", "Johannisthal", "Niederschöneweide",
            "Oberschöneweide", "Plänterwald", "Alt-Treptow", "Grünau", "Müggelheim",
            "Rahnsdorf", "Schmöckwitz", "Friedrichshagen", "Britz", "Buckow", "Rudow",
            "Gropiusstadt", "Marienfelde", "Lichtenrade", "Mariendorf", "Lankwitz",
            "Lichterfelde", "Nikolassee", "Schlachtensee", "Schmargendorf", "Westend",
            "Halensee", "Haselhorst", "Siemensstadt", "Staaken", "Gatow", "Kladow",
            "Hakenfelde", "Falkenhagener Feld"
        ]
    },
    "hamburg": {
        "name": "Hamburg",
        "stadtteile": [
            "Altona", "Altona-Altstadt", "Altona-Nord", "Bahrenfeld", "Blankenese",
            "Eimsbüttel", "Eppendorf", "Harvestehude", "Hoheluft-Ost", "Hoheluft-West",
            "Lokstedt", "Niendorf", "Schnelsen", "Stellingen", "Hamburg-Nord",
            "Alsterdorf", "Barmbek-Nord", "Barmbek-Süd", "Dulsberg", "Eppendorf",
            "Fuhlsbüttel", "Groß Borstel", "Hohenfelde", "Langenhorn", "Ohlsdorf",
            "Uhlenhorst", "Winterhude", "Bergedorf", "Allermöhe", "Billwerder",
            "Curslack", "Kirchwerder", "Lohbrügge", "Moorfleet", "Neuallermöhe",
            "Ochsenwerder", "Reitbrook", "Spadenland", "Tatenberg", "Harburg",
            "Cranz", "Eißendorf", "Francop", "Gut Moor", "Hausbruch", "Heimfeld",
            "Langenbek", "Marmstorf", "Neugraben-Fischbek", "Neuland", "Rönneburg",
            "Sinstorf", "Wilstorf", "Wandsbek", "Bergstedt", "Bramfeld", "Duvenstedt",
            "Eilbek", "Farmsen-Berne", "Hummelsbüttel", "Jenfeld", "Lemsahl-Mellingstedt",
            "Marienthal", "Poppenbüttel", "Rahlstedt", "Sasel", "Steilshoop",
            "Tonndorf", "Volksdorf", "Wellingsbüttel", "Wohldorf-Ohlstedt",
            "St. Pauli", "St. Georg", "HafenCity", "Neustadt", "Hammerbrook",
            "Borgfelde", "Hamm", "Horn", "Billstedt", "Rothenburgsort", "Veddel",
            "Wilhelmsburg", "Finkenwerder"
        ]
    },
    "muenchen": {
        "name": "München",
        "stadtteile": [
            "Altstadt-Lehel", "Ludwigsvorstadt-Isarvorstadt", "Maxvorstadt",
            "Schwabing-West", "Au-Haidhausen", "Sendling", "Sendling-Westpark",
            "Schwanthalerhöhe", "Neuhausen-Nymphenburg", "Moosach",
            "Milbertshofen-Am Hart", "Schwabing-Freimann", "Bogenhausen",
            "Berg am Laim", "Trudering-Riem", "Ramersdorf-Perlach",
            "Obergiesing-Fasangarten", "Untergiesing-Harlaching",
            "Thalkirchen-Obersendling-Forstenried-Fürstenried-Solln",
            "Hadern", "Pasing-Obermenzing", "Aubing-Lochhausen-Langwied",
            "Allach-Untermenzing", "Feldmoching-Hasenbergl", "Laim",
            "Giesing", "Haidhausen", "Schwabing", "Maximilianeum",
            "Englischer Garten", "Nymphenburg", "Olympiapark", "Westpark"
        ]
    },
    "koeln": {
        "name": "Köln",
        "stadtteile": [
            "Innenstadt", "Altstadt-Nord", "Altstadt-Süd", "Neustadt-Nord",
            "Neustadt-Süd", "Deutz", "Rodenkirchen", "Bayenthal", "Marienburg",
            "Raderberg", "Raderthal", "Sürth", "Godorf", "Hahnwald", "Immendorf",
            "Meschenich", "Rondorf", "Weiß", "Zollstock", "Lindenthal", "Klettenberg",
            "Müngersdorf", "Braunsfeld", "Junkersdorf", "Lövenich", "Weiden",
            "Widdersdorf", "Ehrenfeld", "Bickendorf", "Bocklemünd-Mengenich",
            "Neuehrenfeld", "Ossendorf", "Vogelsang", "Nippes", "Bilderstöckchen",
            "Longerich", "Mauenheim", "Niehl", "Riehl", "Weidenpesch", "Chorweiler",
            "Blumenberg", "Esch-Auweiler", "Fühlingen", "Heimersdorf", "Lindweiler",
            "Merkenich", "Pesch", "Roggendorf-Thenhoven", "Seeberg-Nord", "Volkhoven-Weiler",
            "Worringen", "Porz", "Eil", "Elsdorf", "Ensen", "Finkenberg", "Gremberghoven",
            "Grengel", "Langel", "Libur", "Lind", "Poll", "Urbach", "Wahn", "Wahnheide",
            "Westhoven", "Zündorf", "Kalk", "Brück", "Höhenberg", "Humboldt-Gremberg",
            "Merheim", "Neubrück", "Ostheim", "Rath-Heumar", "Vingst", "Mülheim",
            "Buchforst", "Buchheim", "Dellbrück", "Dünnwald", "Flittard", "Höhenhaus",
            "Holweide", "Mülheim-Stadt", "Stammheim"
        ]
    },
    "frankfurt": {
        "name": "Frankfurt",
        "stadtteile": [
            "Altstadt", "Innenstadt", "Bahnhofsviertel", "Westend-Süd", "Westend-Nord",
            "Nordend-Ost", "Nordend-West", "Ostend", "Bornheim", "Gutleutviertel",
            "Gallus", "Bockenheim", "Sachsenhausen-Nord", "Sachsenhausen-Süd",
            "Oberrad", "Niederrad", "Schwanheim", "Goldstein", "Griesheim",
            "Nied", "Höchst", "Sindlingen", "Zeilsheim", "Unterliederbach",
            "Sossenheim", "Rödelheim", "Hausen", "Praunheim", "Heddernheim",
            "Niederursel", "Ginnheim", "Dornbusch", "Eschersheim", "Eckenheim",
            "Preungesheim", "Bonames", "Berkersheim", "Riederwald", "Seckbach",
            "Fechenheim", "Enkheim", "Bergen-Enkheim", "Nieder-Erlenbach",
            "Kalbach-Riedberg", "Harheim", "Nieder-Eschbach"
        ]
    },
    "stuttgart": {
        "name": "Stuttgart",
        "stadtteile": [
            "Mitte", "Nord", "Ost", "Süd", "West", "Bad Cannstatt", "Birkach",
            "Botnang", "Degerloch", "Feuerbach", "Hedelfingen", "Möhringen",
            "Mühlhausen", "Münster", "Obertürkheim", "Plieningen", "Sillenbuch",
            "Stammheim", "Untertürkheim", "Vaihingen", "Wangen", "Weilimdorf",
            "Zuffenhausen", "Rohr", "Dürrlewang", "Fasanenhof", "Sonnenberg",
            "Hofen", "Neugereut", "Steinhaldenfeld", "Sommerrain", "Freiberg",
            "Mönchfeld", "Rot", "Zazenhausen", "Giebel", "Hausen", "Bergheim"
        ]
    },
    "duesseldorf": {
        "name": "Düsseldorf",
        "stadtteile": [
            "Altstadt", "Carlstadt", "Stadtmitte", "Pempelfort", "Derendorf",
            "Golzheim", "Flingern-Nord", "Flingern-Süd", "Düsseltal", "Mörsenbroich",
            "Rath", "Unterrath", "Lichtenbroich", "Lohausen", "Stockum", "Oberkassel",
            "Niederkassel", "Heerdt", "Lörick", "Bilk", "Unterbilk", "Friedrichstadt",
            "Hafen", "Hamm", "Flehe", "Volmerswerth", "Oberbilk", "Eller", "Lierenfeld",
            "Vennhausen", "Unterbach", "Gerresheim", "Grafenberg", "Ludenberg",
            "Hubbelrath", "Knittkuhl", "Benrath", "Urdenbach", "Wersten", "Himmelgeist",
            "Holthausen", "Itter", "Reisholz", "Hassels", "Garath", "Hellerhof"
        ]
    }
}

def slugify(text):
    replacements = {
        'ä': 'ae', 'ö': 'oe', 'ü': 'ue', 'ß': 'ss',
        ' ': '-', '/': '-', '.': '', '(': '', ')': '', '-': '-'
    }
    slug = text.lower()
    for old, new in replacements.items():
        slug = slug.replace(old, new)
    return slug

def get_schema_org(stadtteil, city):
    return f'''
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "name": "Secu.li Rauchmelder-Service {stadtteil}",
        "description": "Professioneller Rauchmelder-Service in {stadtteil}, {city}. Installation und Wartung nach DIN 14676.",
        "url": "https://secu.li",
        "telephone": "+4915778631120",
        "email": "info@secu.li",
        "address": {{
            "@type": "PostalAddress",
            "addressLocality": "{stadtteil}",
            "addressRegion": "{city}",
            "addressCountry": "DE"
        }},
        "areaServed": {{
            "@type": "Place",
            "name": "{stadtteil}, {city}"
        }},
        "serviceType": ["Rauchmelder Installation", "Rauchmelder Wartung"],
        "priceRange": "€€",
        "aggregateRating": {{
            "@type": "AggregateRating",
            "ratingValue": "4.9",
            "reviewCount": "89"
        }}
    }}
    </script>'''

def create_stadtteil_page(stadtteil, city, city_slug, variant):
    stadtteil_slug = slugify(stadtteil)
    schema = get_schema_org(stadtteil, city)
    
    keywords = f"Rauchmelder {stadtteil}, Rauchmelder {city} {stadtteil}, Rauchwarnmelder {stadtteil}, Brandschutz {stadtteil}, Rauchmelder Installation {stadtteil}, DIN 14676 {stadtteil}"
    
    intro_texts = [
        f"Professioneller <strong>Rauchmelder-Service in {stadtteil}</strong>, {city}. Unsere zertifizierten Experten installieren und warten Ihre Rauchmelder nach DIN 14676 - schnell, zuverlässig und zu fairen Preisen.",
        f"<strong>Rauchmelder {stadtteil}</strong> - Ihr lokaler Partner für Brandschutz in {city}. Fachgerechte Installation, jährliche Wartung und kompetente Beratung direkt vor Ort.",
        f"Suchen Sie einen <strong>Rauchmelder-Fachbetrieb in {stadtteil}</strong>? Secu.li bietet professionellen Service für alle Haushalte und Vermieter im Stadtteil {stadtteil}.",
        f"<strong>Rauchmelderpflicht in {stadtteil}</strong> erfüllen mit Secu.li. Wir sind Ihr erfahrener Partner für normgerechte Rauchmelder-Installation in diesem Teil von {city}."
    ]
    
    intro = intro_texts[variant % len(intro_texts)]
    
    return f'''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Rauchmelder {stadtteil} ({city}): Professionelle Installation und Wartung nach DIN 14676. Jetzt kostenlos anfragen! ☎ +49 157 78631120">
    <meta name="keywords" content="{keywords}">
    <meta name="robots" content="index, follow">
    <meta property="og:title" content="Rauchmelder {stadtteil} | {city} | Secu.li">
    <meta property="og:description" content="Professioneller Rauchmelder-Service in {stadtteil}. Installation und Wartung nach DIN 14676. Jetzt anfragen!">
    <meta property="og:type" content="website">
    <meta property="og:locale" content="de_DE">
    <title>Rauchmelder {stadtteil} | {city} | Installation & Wartung | Secu.li</title>
    <link rel="canonical" href="https://secu.li/standorte/deutschland/{city_slug}/{stadtteil_slug}.html">
    <link rel="stylesheet" href="../../../styles.css">
    <meta name="theme-color" content="#C41E3A">
    {schema}
    <style>
        .district-hero {{ padding: 100px 20px 40px; background: linear-gradient(135deg, #FEF2F2, #FFF); text-align: center; }}
        .district-hero h1 {{ font-size: 1.75rem; margin-bottom: 15px; }}
        .district-content {{ padding: 40px 20px; max-width: 800px; margin: 0 auto; }}
        .district-content h2 {{ color: #C41E3A; margin-top: 30px; }}
        .service-grid {{ display: grid; gap: 20px; margin: 30px 0; }}
        .service-card {{ background: #F9FAFB; padding: 25px; border-radius: 12px; }}
        .service-card h3 {{ margin-top: 0; color: #C41E3A; }}
        .benefits-list {{ list-style: none; padding: 0; }}
        .benefits-list li {{ padding: 12px 0; border-bottom: 1px solid #E5E7EB; display: flex; align-items: center; gap: 10px; }}
        .benefits-list li:last-child {{ border-bottom: none; }}
        .faq-section {{ margin: 40px 0; }}
        .faq-item {{ background: #F9FAFB; padding: 20px; border-radius: 10px; margin-bottom: 15px; }}
        .faq-item h4 {{ margin-top: 0; color: #111; }}
        .cta-box {{ background: linear-gradient(135deg, #C41E3A, #E53E3E); color: white; padding: 30px; border-radius: 15px; text-align: center; margin: 30px 0; }}
        .cta-box h3 {{ color: white; margin-top: 0; }}
        .cta-box .btn {{ background: white; color: #C41E3A; }}
        .contact-form {{ background: #F3F4F6; padding: 30px; border-radius: 15px; }}
        .contact-form .form-group {{ margin-bottom: 15px; }}
        .contact-form input, .contact-form select, .contact-form textarea {{ width: 100%; padding: 12px; border: 1px solid #E5E7EB; border-radius: 8px; font-size: 1rem; }}
        @media (min-width: 768px) {{ .district-hero h1 {{ font-size: 2.25rem; }} }}
    </style>
</head>
<body>
    <header class="header">
        <div class="container">
            <a href="../../../index.html" class="logo">Secu.li</a>
            <nav class="nav">
                <ul class="nav-links">
                    <li><a href="../../../index.html">Startseite</a></li>
                    <li><a href="../../deutschland.html">Deutschland</a></li>
                    <li><a href="../{city_slug}.html">{city}</a></li>
                </ul>
                <a href="#kontakt" class="btn btn-primary btn-sm">Anfrage</a>
            </nav>
        </div>
    </header>

    <section class="district-hero">
        <div class="container">
            <span class="hero-badge-top">📍 {city}</span>
            <h1>Rauchmelder-Service in {stadtteil}</h1>
            <p>{intro}</p>
            <div style="margin-top: 20px; display: flex; gap: 10px; justify-content: center; flex-wrap: wrap;">
                <a href="#kontakt" class="btn btn-primary">Jetzt anfragen</a>
                <a href="tel:+4915778631120" class="btn btn-outline">📞 Anrufen</a>
            </div>
        </div>
    </section>

    <section class="district-content">
        <h2>Rauchmelder-Installation in {stadtteil}</h2>
        <p>Unser erfahrenes Team ist regelmäßig in {stadtteil} und Umgebung im Einsatz. Ob Neuinstallation, jährliche Wartung oder Austausch alter Geräte - wir sind Ihr zuverlässiger Partner für alle Rauchmelder-Dienstleistungen in diesem Stadtteil von {city}.</p>

        <div class="service-grid">
            <div class="service-card">
                <h3>🔧 Installation in {stadtteil}</h3>
                <p>Fachgerechte Montage Ihrer Rauchmelder nach DIN 14676. Wir beraten Sie zur optimalen Platzierung und installieren alle Geräte normgerecht mit vollständiger Dokumentation.</p>
            </div>
            <div class="service-card">
                <h3>🔍 Wartung & Prüfung</h3>
                <p>Die jährliche Wartung ist gesetzlich vorgeschrieben. Wir übernehmen Funktionstest, Sichtprüfung und Protokollierung für Ihren Standort in {stadtteil}.</p>
            </div>
            <div class="service-card">
                <h3>📋 Für Vermieter & Hausverwaltungen</h3>
                <p>Vollständige Dokumentation, Wartungsverträge und termingerechte Prüfung aller Wohneinheiten in {stadtteil}.</p>
            </div>
        </div>

        <h2>Ihre Vorteile in {stadtteil}</h2>
        <ul class="benefits-list">
            <li><span style="color: #10B981;">✓</span> <strong>Lokale Präsenz</strong> - Regelmäßig in {stadtteil} im Einsatz</li>
            <li><span style="color: #10B981;">✓</span> <strong>DIN 14676 zertifiziert</strong> - Normgerechte Installation</li>
            <li><span style="color: #10B981;">✓</span> <strong>Schnelle Termine</strong> - Kurzfristige Verfügbarkeit</li>
            <li><span style="color: #10B981;">✓</span> <strong>Faire Preise</strong> - Transparente Festpreise ohne Überraschungen</li>
            <li><span style="color: #10B981;">✓</span> <strong>Komplettservice</strong> - Von Beratung bis Dokumentation</li>
        </ul>

        <div class="faq-section">
            <h2>Häufige Fragen für {stadtteil}</h2>
            
            <div class="faq-item">
                <h4>Welche Rauchmelder sind für {stadtteil} geeignet?</h4>
                <p>Wir empfehlen hochwertige Rauchmelder mit Q-Label und 10-Jahres-Batterie. Diese sind besonders zuverlässig und wartungsarm - ideal für Wohnungen in {stadtteil}.</p>
            </div>
            
            <div class="faq-item">
                <h4>Wie schnell können Sie in {stadtteil} einen Termin machen?</h4>
                <p>Da wir regelmäßig in {city}-{stadtteil} im Einsatz sind, können wir oft innerhalb weniger Tage einen Termin anbieten. Rufen Sie uns an!</p>
            </div>
            
            <div class="faq-item">
                <h4>Was kostet die Installation in {stadtteil}?</h4>
                <p>Unsere Preise sind fair und transparent. Kontaktieren Sie uns für ein kostenloses Angebot für Ihren Standort in {stadtteil}.</p>
            </div>
        </div>

        <div class="cta-box">
            <h3>Kostenlose Beratung für {stadtteil}</h3>
            <p>Rufen Sie uns jetzt an oder nutzen Sie unser Kontaktformular!</p>
            <a href="tel:+4915778631120" class="btn">📞 +49 157 78631120</a>
        </div>

        <div class="contact-form" id="kontakt">
            <h3>Anfrage für {stadtteil}, {city}</h3>
            <form action="https://formspree.io/f/xrbnlwal" method="POST">
                <input type="hidden" name="_subject" value="Anfrage {stadtteil}, {city} - secu.li">
                <input type="hidden" name="standort" value="{stadtteil}, {city}">
                <div class="form-group">
                    <input type="text" name="name" placeholder="Ihr Name" required>
                </div>
                <div class="form-group">
                    <input type="email" name="email" placeholder="E-Mail-Adresse" required>
                </div>
                <div class="form-group">
                    <input type="tel" name="phone" placeholder="Telefonnummer">
                </div>
                <div class="form-group">
                    <select name="service">
                        <option value="">Gewünschter Service</option>
                        <option value="Installation">Neuinstallation</option>
                        <option value="Wartung">Wartung</option>
                        <option value="Austausch">Geräteaustausch</option>
                        <option value="Beratung">Beratung</option>
                    </select>
                </div>
                <div class="form-group">
                    <textarea name="message" rows="3" placeholder="Ihre Nachricht (optional)"></textarea>
                </div>
                <button type="submit" class="btn btn-primary" style="width: 100%;">Anfrage senden</button>
                <p style="font-size: 0.85rem; color: #6B7280; margin-top: 10px; text-align: center;">
                    🔒 Ihre Daten werden vertraulich behandelt
                </p>
            </form>
        </div>

        <p style="margin-top: 30px; text-align: center;">
            <a href="../{city_slug}.html">← Zurück zu {city}</a>
        </p>
    </section>

    <footer class="footer">
        <div class="container" style="text-align: center; padding: 30px;">
            <p>&copy; 2024 Secu.li - Rauchmelder {stadtteil}</p>
            <a href="../../../impressum.html">Impressum</a> | <a href="../../../datenschutz.html">Datenschutz</a>
        </div>
    </footer>
</body>
</html>'''

def update_city_page(city_slug, city_name, stadtteile):
    """Aktualisiert die Stadt-Hauptseite mit Links zu Stadtteilen"""
    city_page = OUTPUT_DIR / f"{city_slug}.html"
    
    if not city_page.exists():
        return False
    
    content = city_page.read_text(encoding='utf-8')
    
    # Prüfen ob bereits Stadtteile-Links vorhanden
    if 'stadtteil-grid' in content:
        return False
    
    # Stadtteile-Grid erstellen
    stadtteil_links = "\n".join([
        f'                <a href="{city_slug}/{slugify(s)}.html">{s}</a>'
        for s in sorted(stadtteile)
    ])
    
    stadtteile_section = f'''
    <section class="section" style="background: #F9FAFB;">
        <div class="container">
            <h2 style="text-align: center; margin-bottom: 30px;">Stadtteile in {city_name}</h2>
            <p style="text-align: center; margin-bottom: 30px;">Wir sind in allen Stadtteilen von {city_name} für Sie da. Wählen Sie Ihren Stadtteil:</p>
            <div class="stadtteil-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 10px;">
{stadtteil_links}
            </div>
        </div>
    </section>

    <footer'''
    
    # Vor dem Footer einfügen
    content = content.replace('<footer', stadtteile_section)
    
    # CSS für Stadtteil-Links hinzufügen
    css = '''
        .stadtteil-grid a { display: block; padding: 12px 15px; background: white; border-radius: 8px; text-decoration: none; color: #111; transition: all 0.3s; text-align: center; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
        .stadtteil-grid a:hover { background: #C41E3A; color: white; }
    '''
    if '</style>' in content:
        content = content.replace('</style>', f'{css}\n    </style>')
    
    city_page.write_text(content, encoding='utf-8')
    return True

def main():
    pages_created = 0
    variant = 0
    
    for city_slug, data in CITY_DISTRICTS.items():
        city_name = data["name"]
        stadtteile = data["stadtteile"]
        
        # Ordner für Stadt erstellen
        city_dir = OUTPUT_DIR / city_slug
        city_dir.mkdir(parents=True, exist_ok=True)
        
        # Stadtteile-Seiten erstellen
        for stadtteil in stadtteile:
            stadtteil_slug = slugify(stadtteil)
            page_path = city_dir / f"{stadtteil_slug}.html"
            
            if not page_path.exists():
                content = create_stadtteil_page(stadtteil, city_name, city_slug, variant)
                page_path.write_text(content, encoding='utf-8')
                pages_created += 1
                variant += 1
        
        # Stadt-Hauptseite aktualisieren
        update_city_page(city_slug, city_name, stadtteile)
    
    print(f"✅ {pages_created} Stadtteile-Seiten erstellt!")

if __name__ == "__main__":
    main()
