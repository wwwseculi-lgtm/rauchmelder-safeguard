#!/usr/bin/env python3
"""
SEO-Seiten Generator für Berliner Bezirke und Ortsteile
"""

import os

# Alle 12 Berliner Bezirke mit Ortsteilen
BERLIN_BEZIRKE = {
    "mitte": {
        "name": "Berlin-Mitte",
        "kurz": "Mitte",
        "ortsteile": ["Wedding", "Gesundbrunnen", "Moabit", "Hansaviertel", "Tiergarten", "Mitte"],
        "beschreibung": "Das Herz der Hauptstadt mit Regierungsviertel, Brandenburger Tor und historischer Altstadt.",
        "einwohner": "385.000"
    },
    "friedrichshain-kreuzberg": {
        "name": "Friedrichshain-Kreuzberg",
        "kurz": "Friedrichshain-Kreuzberg",
        "ortsteile": ["Friedrichshain", "Kreuzberg"],
        "beschreibung": "Der junge, multikulturelle Bezirk mit vielen Altbauwohnungen und lebendiger Kultur.",
        "einwohner": "290.000"
    },
    "pankow": {
        "name": "Berlin-Pankow",
        "kurz": "Pankow",
        "ortsteile": ["Prenzlauer Berg", "Weißensee", "Pankow", "Heinersdorf", "Blankenburg", "Karow", "Buch", "Französisch Buchholz", "Rosenthal", "Wilhelmsruh", "Niederschönhausen", "Blankenfelde"],
        "beschreibung": "Der bevölkerungsreichste Bezirk mit dem beliebten Prenzlauer Berg und ruhigen Wohngebieten.",
        "einwohner": "410.000"
    },
    "charlottenburg-wilmersdorf": {
        "name": "Charlottenburg-Wilmersdorf",
        "kurz": "Charlottenburg-Wilmersdorf",
        "ortsteile": ["Charlottenburg", "Wilmersdorf", "Schmargendorf", "Grunewald", "Westend", "Halensee", "Charlottenburg-Nord"],
        "beschreibung": "Der elegante Westberliner Bezirk mit Kurfürstendamm, Schloss Charlottenburg und Villenviertel.",
        "einwohner": "340.000"
    },
    "spandau": {
        "name": "Berlin-Spandau",
        "kurz": "Spandau",
        "ortsteile": ["Spandau", "Haselhorst", "Siemensstadt", "Staaken", "Gatow", "Kladow", "Hakenfelde", "Falkenhagener Feld", "Wilhelmstadt"],
        "beschreibung": "Der westlichste Bezirk mit der historischen Zitadelle und viel Grün.",
        "einwohner": "245.000"
    },
    "steglitz-zehlendorf": {
        "name": "Steglitz-Zehlendorf",
        "kurz": "Steglitz-Zehlendorf",
        "ortsteile": ["Steglitz", "Zehlendorf", "Dahlem", "Lichterfelde", "Lankwitz", "Nikolassee", "Wannsee", "Schlachtensee"],
        "beschreibung": "Der grüne Villenbezirk im Südwesten mit der Freien Universität und Wannsee.",
        "einwohner": "310.000"
    },
    "tempelhof-schoeneberg": {
        "name": "Tempelhof-Schöneberg",
        "kurz": "Tempelhof-Schöneberg",
        "ortsteile": ["Schöneberg", "Tempelhof", "Friedenau", "Mariendorf", "Marienfelde", "Lichtenrade"],
        "beschreibung": "Zentral gelegener Bezirk mit dem legendären Tempelhofer Feld und urbanem Schöneberg.",
        "einwohner": "350.000"
    },
    "neukoelln": {
        "name": "Berlin-Neukölln",
        "kurz": "Neukölln",
        "ortsteile": ["Neukölln", "Britz", "Buckow", "Rudow", "Gropiusstadt"],
        "beschreibung": "Multikultureller Bezirk im Wandel mit lebendiger Gastro-Szene und Altbauvierteln.",
        "einwohner": "330.000"
    },
    "treptow-koepenick": {
        "name": "Treptow-Köpenick",
        "kurz": "Treptow-Köpenick",
        "ortsteile": ["Treptow", "Köpenick", "Adlershof", "Johannisthal", "Bohnsdorf", "Grünau", "Schmöckwitz", "Friedrichshagen", "Rahnsdorf", "Müggelheim", "Altglienicke"],
        "beschreibung": "Der flächenmäßig größte Bezirk mit viel Wasser, Wald und dem Wissenschaftsstandort Adlershof.",
        "einwohner": "275.000"
    },
    "marzahn-hellersdorf": {
        "name": "Marzahn-Hellersdorf",
        "kurz": "Marzahn-Hellersdorf",
        "ortsteile": ["Marzahn", "Hellersdorf", "Biesdorf", "Kaulsdorf", "Mahlsdorf"],
        "beschreibung": "Östlicher Bezirk mit Plattenbauten, Einfamilienhäusern und den Gärten der Welt.",
        "einwohner": "270.000"
    },
    "lichtenberg": {
        "name": "Berlin-Lichtenberg",
        "kurz": "Lichtenberg",
        "ortsteile": ["Lichtenberg", "Hohenschönhausen", "Friedrichsfelde", "Karlshorst", "Rummelsburg", "Fennpfuhl", "Falkenberg", "Wartenberg", "Malchow"],
        "beschreibung": "Aufstrebender Bezirk im Osten mit dem Tierpark Berlin und wachsender Beliebtheit.",
        "einwohner": "295.000"
    },
    "reinickendorf": {
        "name": "Berlin-Reinickendorf",
        "kurz": "Reinickendorf",
        "ortsteile": ["Reinickendorf", "Tegel", "Wittenau", "Märkisches Viertel", "Hermsdorf", "Frohnau", "Waidmannslust", "Lübars", "Heiligensee", "Borsigwalde"],
        "beschreibung": "Nördlicher Bezirk mit dem Tegeler See, viel Grün und guter Anbindung.",
        "einwohner": "265.000"
    },
}

TEMPLATE = '''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Rauchmelder Installation & Wartung in {name} ✓ Alle Ortsteile ✓ TÜV-geprüft ✓ 10 Jahre Garantie ✓ Schnelle Termine. Jetzt kostenlos anfragen!">
    <meta name="keywords" content="Rauchmelder {kurz}, Rauchmelder Installation {kurz}, Rauchmelder Wartung {kurz}, Brandschutz {kurz}, Rauchwarnmelder Berlin {kurz}">
    <title>Rauchmelder Service {name} | Installation & Wartung | Secu.li</title>
    <link rel="canonical" href="https://secu.li/standorte/deutschland/berlin/{slug}.html">
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
                    <span class="hero-badge-top">📍 {name}</span>
                    <h1>Rauchmelder Service in {kurz}</h1>
                    <p class="subtitle">Professionelle Rauchmelder-Installation und Wartung in {kurz} und allen Ortsteilen. TÜV-geprüft, faire Preise, schnelle Termine.</p>
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
                <h2>Rauchmelder in {kurz} – Ihr lokaler Partner</h2>
            </div>
            <div style="max-width: 800px; margin: 0 auto; line-height: 1.8;">
                <p><strong>{name}</strong> ist ein beliebter Berliner Bezirk mit rund <strong>{einwohner} Einwohnern</strong>. {beschreibung}</p>
                
                <p>In Berlin gilt seit 2017 die <strong>gesetzliche Rauchmelderpflicht</strong>. Als Eigentümer oder Vermieter in {kurz} sind Sie verpflichtet, in allen Schlafräumen, Kinderzimmern und Fluren Rauchmelder zu installieren und jährlich zu warten.</p>
                
                <h3 style="margin-top: 2rem;">Unser Service in {kurz}</h3>
                <ul style="margin: 1rem 0;">
                    <li>✓ <strong>Schnelle Termine</strong> – meist innerhalb von 3-5 Werktagen</li>
                    <li>✓ <strong>Alle Ortsteile</strong> von {kurz} werden bedient</li>
                    <li>✓ <strong>Festpreise</strong> ohne versteckte Kosten</li>
                    <li>✓ <strong>Rechtssichere Dokumentation</strong> für Vermieter</li>
                    <li>✓ <strong>Jährliche Wartung</strong> mit automatischer Terminerinnerung</li>
                </ul>
                
                <p>Ob Altbau in {ortsteile_text} – wir installieren und warten Ihre Rauchmelder fachgerecht und zuverlässig.</p>
            </div>
        </div>
    </section>

    <section class="section bg-gray">
        <div class="container">
            <div class="section-header">
                <span class="section-badge">Ortsteile</span>
                <h2>Rauchmelder-Service in allen Ortsteilen von {kurz}</h2>
            </div>
            <div class="countries-grid">
                {ortsteile_html}
            </div>
        </div>
    </section>

    <section class="section">
        <div class="container">
            <div class="section-header">
                <span class="section-badge">Leistungen</span>
                <h2>Was wir in {kurz} anbieten</h2>
            </div>
            <div class="features-grid">
                <div class="feature-card">
                    <div class="feature-icon">🔧</div>
                    <h4>Neuinstallation</h4>
                    <p>Fachgerechte Montage nach DIN 14676 in Wohnungen und Häusern in {kurz}.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">🔍</div>
                    <h4>Jährliche Wartung</h4>
                    <p>Funktionsprüfung aller Rauchmelder mit rechtssicherer Dokumentation.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">🔄</div>
                    <h4>Austausch</h4>
                    <p>Nach 10 Jahren müssen Rauchmelder ersetzt werden. Wir übernehmen das.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">🏢</div>
                    <h4>Hausverwaltungen</h4>
                    <p>Spezielle Konditionen für Hausverwaltungen und WEGs in {kurz}.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="section bg-gray">
        <div class="container">
            <div class="section-header">
                <span class="section-badge">Häufige Fragen</span>
                <h2>FAQ – Rauchmelder in {kurz}</h2>
            </div>
            <div style="max-width: 800px; margin: 0 auto;">
                <div style="margin-bottom: 1.5rem; padding: 1.5rem; background: var(--white); border-radius: var(--radius-lg);">
                    <h4 style="margin-bottom: 0.5rem;">Gilt die Rauchmelderpflicht auch in {kurz}?</h4>
                    <p style="color: var(--gray-600); margin: 0;">Ja, in ganz Berlin gilt seit 2017 die Rauchmelderpflicht. Eigentümer müssen installieren, die Wartung kann auf Mieter übertragen werden.</p>
                </div>
                <div style="margin-bottom: 1.5rem; padding: 1.5rem; background: var(--white); border-radius: var(--radius-lg);">
                    <h4 style="margin-bottom: 0.5rem;">Wie schnell können Sie in {kurz} einen Termin anbieten?</h4>
                    <p style="color: var(--gray-600); margin: 0;">In der Regel können wir Termine in {kurz} innerhalb von 3-5 Werktagen anbieten.</p>
                </div>
                <div style="margin-bottom: 1.5rem; padding: 1.5rem; background: var(--white); border-radius: var(--radius-lg);">
                    <h4 style="margin-bottom: 0.5rem;">Was kostet die Rauchmelder-Installation in {kurz}?</h4>
                    <p style="color: var(--gray-600); margin: 0;">Wir arbeiten mit transparenten Festpreisen. Fordern Sie jetzt Ihr kostenloses Angebot an.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="contact-form-section" id="kontaktformular">
        <div class="container">
            <div class="contact-header-centered">
                <span class="section-badge">Jetzt anfragen</span>
                <h2>Kostenloses Angebot für {kurz}</h2>
                <p>Antwort innerhalb von 24 Stunden – unverbindlich und kostenlos.</p>
                <div class="contact-benefits-row">
                    <div class="benefit-item"><span class="benefit-icon">✓</span><span>Kostenlos</span></div>
                    <div class="benefit-item"><span class="benefit-icon">✓</span><span>Unverbindlich</span></div>
                    <div class="benefit-item"><span class="benefit-icon">✓</span><span>24h Antwort</span></div>
                </div>
            </div>
            <div class="contact-form-card contact-form-large">
                <form class="contact-form" id="localContactForm">
                    <input type="hidden" name="city" value="{name}">
                    <div class="form-grid-3">
                        <div class="form-group"><label for="name">Name *</label><input type="text" id="name" name="name" placeholder="Ihr Name" required></div>
                        <div class="form-group"><label for="email">E-Mail *</label><input type="email" id="email" name="email" placeholder="ihre@email.de" required></div>
                        <div class="form-group"><label for="phone">Telefon</label><input type="tel" id="phone" name="phone" placeholder="+49 30 123456"></div>
                    </div>
                    <div class="form-grid-2">
                        <div class="form-group"><label for="ortsteil">Ortsteil in {kurz}</label>
                            <select id="ortsteil" name="ortsteil">
                                <option value="">Bitte auswählen...</option>
                                {ortsteile_options}
                            </select>
                        </div>
                        <div class="form-group"><label for="units">Anzahl Wohneinheiten</label>
                            <select id="units" name="units">
                                <option value="">Bitte auswählen...</option>
                                <option value="1">1 Wohnung</option>
                                <option value="2-5">2-5 Wohnungen</option>
                                <option value="6-20">6-20 Wohnungen</option>
                                <option value="20+">Mehr als 20</option>
                            </select>
                        </div>
                    </div>
                    <div class="form-group"><label for="message">Ihre Nachricht</label><textarea id="message" name="message" placeholder="z.B. Anzahl Räume, Altbau/Neubau, gewünschter Termin..." rows="4"></textarea></div>
                    <div class="form-submit-row">
                        <button type="submit" class="btn btn-primary btn-xl">Kostenloses Angebot für {kurz} →</button>
                        <p class="form-privacy">🔒 Ihre Daten sind sicher.</p>
                    </div>
                </form>
            </div>
        </div>
    </section>

    <footer class="footer">
        <div class="container">
            <div class="footer-bottom">
                <p>© 2024 Secu.li – Rauchmelder Service in {name} | <a href="../berlin.html" style="color: var(--gray-400);">Zurück zu Berlin</a> | <a href="../../../kontakt.html" style="color: var(--gray-400);">Kontakt</a></p>
            </div>
        </div>
    </footer>
    <script src="../../../script.js"></script>
</body>
</html>'''

def generate_pages():
    output_dir = "standorte/deutschland/berlin"
    os.makedirs(output_dir, exist_ok=True)
    
    count = 0
    for slug, data in BERLIN_BEZIRKE.items():
        name = data["name"]
        kurz = data["kurz"]
        ortsteile = data["ortsteile"]
        beschreibung = data["beschreibung"]
        einwohner = data["einwohner"]
        
        # Ortsteile HTML für Grid
        ortsteile_html = ""
        for ortsteil in ortsteile:
            ortsteile_html += f'<div class="country-card"><h5>{ortsteil}</h5><p>Rauchmelder Service</p></div>\n                '
        
        # Ortsteile für Dropdown
        ortsteile_options = ""
        for ortsteil in ortsteile:
            ortsteile_options += f'<option value="{ortsteil}">{ortsteil}</option>\n                                '
        
        # Text für Ortsteile-Aufzählung
        if len(ortsteile) > 2:
            ortsteile_text = ", ".join(ortsteile[:-1]) + " oder " + ortsteile[-1]
        else:
            ortsteile_text = " oder ".join(ortsteile)
        
        content = TEMPLATE.format(
            name=name,
            kurz=kurz,
            slug=slug,
            ortsteile_html=ortsteile_html.strip(),
            ortsteile_options=ortsteile_options.strip(),
            ortsteile_text=ortsteile_text,
            beschreibung=beschreibung,
            einwohner=einwohner
        )
        
        filepath = os.path.join(output_dir, f"{slug}.html")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        
        count += 1
        print(f"✅ {name}")
    
    print(f"\n🎉 {count} Berliner Bezirksseiten erstellt!")

if __name__ == "__main__":
    generate_pages()
