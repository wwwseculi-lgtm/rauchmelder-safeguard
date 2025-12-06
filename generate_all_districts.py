#!/usr/bin/env python3
"""
SEO-Seiten Generator für Stadtteile aller deutschen Großstädte
"""

import os

# Alle Städte mit Stadtteilen
STAEDTE_MIT_STADTTEILEN = {
    "muenchen": {
        "name": "München",
        "land": "Bayern",
        "einwohner": "1.500.000",
        "stadtteile": {
            "schwabing": {"name": "Schwabing", "beschreibung": "Beliebtes Szeneviertel mit Englischem Garten"},
            "bogenhausen": {"name": "Bogenhausen", "beschreibung": "Gehobenes Wohnviertel im Osten"},
            "sendling": {"name": "Sendling", "beschreibung": "Traditionelles Arbeiterviertel im Süden"},
            "pasing": {"name": "Pasing", "beschreibung": "Eigenständiger Stadtteil im Westen"},
            "haidhausen": {"name": "Haidhausen", "beschreibung": "Französisches Viertel mit Altbaucharme"},
            "maxvorstadt": {"name": "Maxvorstadt", "beschreibung": "Universitätsviertel mit Museen"},
            "neuhausen": {"name": "Neuhausen", "beschreibung": "Familienfreundlich nahe Nymphenburg"},
            "giesing": {"name": "Giesing", "beschreibung": "Aufstrebendes Viertel im Süden"},
            "trudering": {"name": "Trudering", "beschreibung": "Ruhiges Wohngebiet im Osten"},
            "laim": {"name": "Laim", "beschreibung": "Zentral gelegen, gute Anbindung"},
            "moosach": {"name": "Moosach", "beschreibung": "Grüner Stadtteil im Nordwesten"},
            "milbertshofen": {"name": "Milbertshofen", "beschreibung": "Wohngebiet nahe BMW"},
        }
    },
    "hamburg": {
        "name": "Hamburg",
        "land": "Hamburg",
        "einwohner": "1.900.000",
        "stadtteile": {
            "altona": {"name": "Altona", "beschreibung": "Trendiger Stadtteil an der Elbe"},
            "eimsbuettel": {"name": "Eimsbüttel", "beschreibung": "Beliebtes Wohnviertel mit Altbauten"},
            "wandsbek": {"name": "Wandsbek", "beschreibung": "Großer Bezirk im Osten"},
            "bergedorf": {"name": "Bergedorf", "beschreibung": "Eigenständiger Charakter im Südosten"},
            "harburg": {"name": "Harburg", "beschreibung": "Südlich der Elbe mit Hafen"},
            "blankenese": {"name": "Blankenese", "beschreibung": "Villenviertel an der Elbe"},
            "winterhude": {"name": "Winterhude", "beschreibung": "Grün und urban am Stadtpark"},
            "barmbek": {"name": "Barmbek", "beschreibung": "Lebendiges Viertel im Norden"},
            "st-pauli": {"name": "St. Pauli", "beschreibung": "Berühmtes Vergnügungsviertel"},
            "ottensen": {"name": "Ottensen", "beschreibung": "Kreatives Viertel in Altona"},
            "st-georg": {"name": "St. Georg", "beschreibung": "Bunt und zentral am Hauptbahnhof"},
            "bahrenfeld": {"name": "Bahrenfeld", "beschreibung": "Aufstrebend mit Wissenschaft"},
        }
    },
    "koeln": {
        "name": "Köln",
        "land": "Nordrhein-Westfalen",
        "einwohner": "1.080.000",
        "stadtteile": {
            "innenstadt": {"name": "Innenstadt", "beschreibung": "Rund um den Dom und Altstadt"},
            "ehrenfeld": {"name": "Ehrenfeld", "beschreibung": "Kreatives Szeneviertel"},
            "nippes": {"name": "Nippes", "beschreibung": "Beliebtes Wohnviertel mit Flair"},
            "lindenthal": {"name": "Lindenthal", "beschreibung": "Grünes Universitätsviertel"},
            "rodenkirchen": {"name": "Rodenkirchen", "beschreibung": "Gehobenes Wohnen am Rhein"},
            "chorweiler": {"name": "Chorweiler", "beschreibung": "Großsiedlung im Norden"},
            "porz": {"name": "Porz", "beschreibung": "Rechtsrheinisch nahe Flughafen"},
            "kalk": {"name": "Kalk", "beschreibung": "Aufstrebendes Viertel im Osten"},
            "deutz": {"name": "Deutz", "beschreibung": "Messestandort am Rhein"},
            "muelheim": {"name": "Mülheim", "beschreibung": "Multikulturell rechtsrheinisch"},
            "suedstadt": {"name": "Südstadt", "beschreibung": "Beliebtes Altbauviertel"},
            "belgisches-viertel": {"name": "Belgisches Viertel", "beschreibung": "Trendviertel mit Cafés"},
        }
    },
    "frankfurt": {
        "name": "Frankfurt am Main",
        "land": "Hessen",
        "einwohner": "750.000",
        "stadtteile": {
            "sachsenhausen": {"name": "Sachsenhausen", "beschreibung": "Apfelweinviertel südlich des Mains"},
            "bornheim": {"name": "Bornheim", "beschreibung": "Beliebtes Ausgehviertel"},
            "bockenheim": {"name": "Bockenheim", "beschreibung": "Studentenviertel mit Charme"},
            "nordend": {"name": "Nordend", "beschreibung": "Gehobenes Altbauviertel"},
            "westend": {"name": "Westend", "beschreibung": "Bankenviertel und Villen"},
            "hoechst": {"name": "Höchst", "beschreibung": "Eigenständig im Westen"},
            "niederrad": {"name": "Niederrad", "beschreibung": "Nahe Flughafen und Stadion"},
            "ostend": {"name": "Ostend", "beschreibung": "Aufstrebend mit EZB"},
            "gallus": {"name": "Gallus", "beschreibung": "Im Wandel nahe Hauptbahnhof"},
            "fechenheim": {"name": "Fechenheim", "beschreibung": "Industriecharakter im Osten"},
        }
    },
    "stuttgart": {
        "name": "Stuttgart",
        "land": "Baden-Württemberg",
        "einwohner": "635.000",
        "stadtteile": {
            "mitte": {"name": "Stuttgart-Mitte", "beschreibung": "Innenstadt und Einkaufszentrum"},
            "bad-cannstatt": {"name": "Bad Cannstatt", "beschreibung": "Größter Stadtbezirk mit Volksfest"},
            "vaihingen": {"name": "Vaihingen", "beschreibung": "Universität und Industrie"},
            "feuerbach": {"name": "Feuerbach", "beschreibung": "Industriegeschichte im Norden"},
            "degerloch": {"name": "Degerloch", "beschreibung": "Gehobenes Wohnen auf der Höhe"},
            "moehringen": {"name": "Möhringen", "beschreibung": "Ruhig im Süden"},
            "zuffenhausen": {"name": "Zuffenhausen", "beschreibung": "Porsche-Standort im Norden"},
            "sillenbuch": {"name": "Sillenbuch", "beschreibung": "Familienfreundlich im Osten"},
        }
    },
    "duesseldorf": {
        "name": "Düsseldorf",
        "land": "Nordrhein-Westfalen",
        "einwohner": "620.000",
        "stadtteile": {
            "altstadt": {"name": "Altstadt", "beschreibung": "Längste Theke der Welt"},
            "bilk": {"name": "Bilk", "beschreibung": "Universitätsnähe, beliebt"},
            "flingern": {"name": "Flingern", "beschreibung": "Kreatives Szeneviertel"},
            "oberkassel": {"name": "Oberkassel", "beschreibung": "Gehobenes linksrheinisch"},
            "pempelfort": {"name": "Pempelfort", "beschreibung": "Zentral mit Altbauten"},
            "unterbilk": {"name": "Unterbilk", "beschreibung": "Medienhafen-Nähe"},
            "gerresheim": {"name": "Gerresheim", "beschreibung": "Eigenständig im Osten"},
            "benrath": {"name": "Benrath", "beschreibung": "Schloss und Rhein im Süden"},
        }
    },
}

TEMPLATE = '''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Rauchmelder Installation & Wartung in {stadtteil_name}, {stadt} ✓ Professionell ✓ TÜV-geprüft ✓ 10 Jahre Garantie. Jetzt anfragen!">
    <meta name="keywords" content="Rauchmelder {stadtteil_name}, Rauchmelder {stadt} {stadtteil_name}, Rauchmelder Installation {stadtteil_name}, Brandschutz {stadtteil_name}">
    <title>Rauchmelder Service {stadtteil_name} ({stadt}) | Secu.li</title>
    <link rel="canonical" href="https://secu.li/standorte/deutschland/{stadt_slug}/{stadtteil_slug}.html">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../../../styles.css">
</head>
<body>
    <header class="header" id="header">
        <div class="container">
            <a href="../../../index.html" class="logo"><span>Secu.li</span></a>
            <nav class="nav">
                <ul class="nav-links">
                    <li><a href="../../../index.html">Startseite</a></li>
                    <li><a href="../../../produkte.html">Produkte</a></li>
                    <li><a href="../../../service.html">Montage & Service</a></li>
                    <li><a href="../../../ueber-uns.html">Über uns</a></li>
                    <li><a href="../../../kontakt.html">Kontakt</a></li>
                </ul>
                <a href="../../../kontakt.html" class="btn btn-primary">Jetzt anfragen</a>
            </nav>
        </div>
    </header>

    <section class="hero hero-simple">
        <div class="container">
            <div class="hero-content hero-centered">
                <div class="hero-text">
                    <span class="hero-badge-top">📍 {stadtteil_name}, {stadt}</span>
                    <h1>Rauchmelder Service in {stadtteil_name}</h1>
                    <p class="subtitle">{beschreibung}. Professionelle Rauchmelder-Installation und Wartung mit 10 Jahren Garantie.</p>
                    <div class="hero-buttons">
                        <a href="#kontaktformular" class="btn btn-primary btn-lg">Kostenloses Angebot</a>
                        <a href="tel:+498001234567" class="btn btn-outline btn-lg">📞 Anrufen</a>
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

    <section class="section">
        <div class="container">
            <div class="section-header">
                <h2>Rauchmelder-Service in {stadtteil_name}</h2>
            </div>
            <div style="max-width: 800px; margin: 0 auto; line-height: 1.8;">
                <p><strong>{stadtteil_name}</strong> ist ein beliebter Stadtteil von {stadt}. {beschreibung}. In {land} gilt die gesetzliche <strong>Rauchmelderpflicht</strong> – wir helfen Ihnen bei Installation und Wartung.</p>
                
                <h3 style="margin-top: 2rem;">Unsere Leistungen in {stadtteil_name}</h3>
                <ul style="margin: 1rem 0;">
                    <li>✓ <strong>Neuinstallation</strong> von Rauchmeldern nach DIN 14676</li>
                    <li>✓ <strong>Jährliche Wartung</strong> mit Funktionsprüfung</li>
                    <li>✓ <strong>Austausch</strong> alter Geräte (nach 10 Jahren Pflicht)</li>
                    <li>✓ <strong>Dokumentation</strong> für Vermieter und Versicherungen</li>
                    <li>✓ <strong>Schnelle Termine</strong> in {stadtteil_name}</li>
                </ul>
                
                <p>Fordern Sie jetzt Ihr <strong>kostenloses Angebot</strong> für {stadtteil_name} an!</p>
            </div>
        </div>
    </section>

    <section class="section bg-gray">
        <div class="container">
            <div class="section-header">
                <span class="section-badge">Leistungen</span>
                <h2>Was wir bieten</h2>
            </div>
            <div class="features-grid">
                <div class="feature-card"><div class="feature-icon">🔧</div><h4>Installation</h4><p>Fachgerechte Montage in {stadtteil_name}.</p></div>
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
                <h2>Angebot für {stadtteil_name}</h2>
                <p>Kostenlos und unverbindlich – Antwort in 24 Stunden.</p>
            </div>
            <div class="contact-form-card contact-form-large">
                <form class="contact-form" id="localContactForm">
                    <input type="hidden" name="city" value="{stadt}">
                    <input type="hidden" name="district" value="{stadtteil_name}">
                    <div class="form-grid-3">
                        <div class="form-group"><label for="name">Name *</label><input type="text" id="name" name="name" required></div>
                        <div class="form-group"><label for="email">E-Mail *</label><input type="email" id="email" name="email" required></div>
                        <div class="form-group"><label for="phone">Telefon</label><input type="tel" id="phone" name="phone"></div>
                    </div>
                    <div class="form-group"><label for="message">Ihre Nachricht</label><textarea id="message" name="message" rows="4"></textarea></div>
                    <div class="form-submit-row">
                        <button type="submit" class="btn btn-primary btn-xl">Angebot für {stadtteil_name} anfordern →</button>
                    </div>
                </form>
            </div>
        </div>
    </section>

    <footer class="footer">
        <div class="container">
            <div class="footer-bottom">
                <p>© 2024 Secu.li – Rauchmelder in {stadtteil_name}, {stadt} | <a href="../{stadt_slug}.html" style="color: var(--gray-400);">Zurück zu {stadt}</a></p>
            </div>
        </div>
    </footer>
    <script src="../../../script.js"></script>
</body>
</html>'''

def generate_all_districts():
    total = 0
    
    for stadt_slug, stadt_data in STAEDTE_MIT_STADTTEILEN.items():
        stadt = stadt_data["name"]
        land = stadt_data["land"]
        
        # Ordner erstellen
        output_dir = f"standorte/deutschland/{stadt_slug}"
        os.makedirs(output_dir, exist_ok=True)
        
        print(f"\n📍 {stadt}:")
        
        for stadtteil_slug, stadtteil_data in stadt_data["stadtteile"].items():
            stadtteil_name = stadtteil_data["name"]
            beschreibung = stadtteil_data["beschreibung"]
            
            content = TEMPLATE.format(
                stadt=stadt,
                stadt_slug=stadt_slug,
                land=land,
                stadtteil_name=stadtteil_name,
                stadtteil_slug=stadtteil_slug,
                beschreibung=beschreibung
            )
            
            filepath = os.path.join(output_dir, f"{stadtteil_slug}.html")
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            
            print(f"   ✅ {stadtteil_name}")
            total += 1
    
    print(f"\n🎉 {total} Stadtteilseiten erstellt!")

if __name__ == "__main__":
    generate_all_districts()
