#!/usr/bin/env python3
"""
SEO-Seiten Generator für polnische und bulgarische Städte
"""

import os

# Polnische Städte
POLEN_STAEDTE = {
    "warschau": {"name": "Warschau", "local": "Warszawa", "bezirke": ["Śródmieście", "Mokotów", "Praga", "Wola", "Ursynów", "Bielany", "Bemowo", "Targówek"]},
    "krakau": {"name": "Krakau", "local": "Kraków", "bezirke": ["Stare Miasto", "Kazimierz", "Podgórze", "Nowa Huta", "Krowodrza", "Bronowice"]},
    "breslau": {"name": "Breslau", "local": "Wrocław", "bezirke": ["Stare Miasto", "Śródmieście", "Krzyki", "Fabryczna", "Psie Pole"]},
    "posen": {"name": "Posen", "local": "Poznań", "bezirke": ["Stare Miasto", "Grunwald", "Jeżyce", "Nowe Miasto", "Wilda"]},
    "danzig": {"name": "Danzig", "local": "Gdańsk", "bezirke": ["Śródmieście", "Wrzeszcz", "Oliwa", "Przymorze", "Zaspa"]},
    "lodz": {"name": "Łódź", "local": "Łódź", "bezirke": ["Śródmieście", "Bałuty", "Górna", "Polesie", "Widzew"]},
    "stettin": {"name": "Stettin", "local": "Szczecin", "bezirke": ["Śródmieście", "Niebuszewo", "Pogodno", "Dąbie", "Prawobrzeże"]},
    "lublin": {"name": "Lublin", "local": "Lublin", "bezirke": ["Stare Miasto", "Śródmieście", "Czuby", "Kalinowszczyzna"]},
    "kattowitz": {"name": "Kattowitz", "local": "Katowice", "bezirke": ["Śródmieście", "Ligota", "Brynów", "Załęże", "Szopienice"]},
    "bialystok": {"name": "Białystok", "local": "Białystok", "bezirke": ["Centrum", "Antoniuk", "Bojary", "Piasta"]},
    "bromberg": {"name": "Bromberg", "local": "Bydgoszcz", "bezirke": ["Śródmieście", "Fordon", "Bartodzieje", "Błonie"]},
    "thorn": {"name": "Thorn", "local": "Toruń", "bezirke": ["Stare Miasto", "Bydgoskie", "Chełmińskie", "Rubinkowo"]},
}

# Bulgarische Städte
BULGARIEN_STAEDTE = {
    "sofia": {"name": "Sofia", "local": "София", "bezirke": ["Zentrum", "Lozenets", "Mladost", "Oborishte", "Vitosha", "Krasno selo"]},
    "plovdiv": {"name": "Plovdiv", "local": "Пловдив", "bezirke": ["Zentrum", "Trakiya", "Karshiyaka", "Maritza"]},
    "varna": {"name": "Varna", "local": "Варна", "bezirke": ["Zentrum", "Primorski", "Mladost", "Vladislavovo"]},
    "burgas": {"name": "Burgas", "local": "Бургас", "bezirke": ["Zentrum", "Meden Rudnik", "Slaveykov", "Lazur"]},
    "ruse": {"name": "Ruse", "local": "Русе", "bezirke": ["Zentrum", "Zdravets", "Druzhba", "Charodeyka"]},
    "stara-sagora": {"name": "Stara Sagora", "local": "Стара Загора", "bezirke": ["Zentrum", "ATC", "Industrialen"]},
    "pleven": {"name": "Pleven", "local": "Плевен", "bezirke": ["Zentrum", "Storgozia", "Druzhba"]},
    "dobrich": {"name": "Dobrich", "local": "Добрич", "bezirke": ["Zentrum", "Druzhba", "Balchik"]},
    "sliven": {"name": "Sliven", "local": "Сливен", "bezirke": ["Zentrum", "Dabrovo", "Klutsohor"]},
    "shumen": {"name": "Schumen", "local": "Шумен", "bezirke": ["Zentrum", "Makedonia", "Divdyadovo"]},
}

TEMPLATE_PL = '''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Rauchmelder Installation & Wartung in {name} ({local}), Polen ✓ Professionell ✓ Zertifiziert ✓ Schnelle Termine.">
    <meta name="keywords" content="Rauchmelder {name}, Czujnik dymu {local}, Rauchmelder Polen, Brandschutz {name}">
    <title>Rauchmelder Service {name} (Polen) | Secu.li</title>
    <link rel="canonical" href="https://secu.li/standorte/polen/{slug}.html">
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
                    <span class="hero-badge-top">🇵🇱 {name} ({local})</span>
                    <h1>Rauchmelder Service in {name}</h1>
                    <p class="subtitle">Profesjonalna instalacja i konserwacja czujników dymu w {local}. Professionelle Installation und Wartung von Rauchmeldern in {name}, Polen.</p>
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
                <div class="trust-badge-item"><div class="badge-icon">EU</div><span>EU-Normen</span></div>
                <div class="trust-badge-item"><div class="badge-icon">VdS</div><span>VdS anerkannt</span></div>
                <div class="trust-badge-item"><div class="badge-icon">10J</div><span>10 Jahre Garantie</span></div>
            </div>
        </div>
    </section>

    <section class="section">
        <div class="container">
            <div class="section-header">
                <h2>Rauchmelder in {name}, Polen</h2>
            </div>
            <div style="max-width: 800px; margin: 0 auto; line-height: 1.8;">
                <p><strong>{name}</strong> ({local}) ist eine wichtige Stadt in Polen. Wir bieten professionellen Rauchmelder-Service mit deutschem Qualitätsstandard.</p>
                
                <h3 style="margin-top: 2rem;">Unsere Leistungen in {name}</h3>
                <ul style="margin: 1rem 0;">
                    <li>✓ <strong>Installation</strong> nach EU-Normen</li>
                    <li>✓ <strong>Wartung</strong> und Funktionsprüfung</li>
                    <li>✓ <strong>Austausch</strong> alter Geräte</li>
                    <li>✓ <strong>Deutschsprachiger Service</strong></li>
                </ul>
            </div>
        </div>
    </section>

    <section class="section bg-gray">
        <div class="container">
            <div class="section-header">
                <span class="section-badge">Stadtteile</span>
                <h2>Service in {name}</h2>
            </div>
            <div class="countries-grid">
                {bezirke_html}
            </div>
        </div>
    </section>

    <section class="contact-form-section" id="kontaktformular">
        <div class="container">
            <div class="contact-header-centered">
                <span class="section-badge">Jetzt anfragen</span>
                <h2>Angebot für {name}</h2>
            </div>
            <div class="contact-form-card contact-form-large">
                <form class="contact-form" id="localContactForm">
                    <input type="hidden" name="city" value="{name}">
                    <input type="hidden" name="country" value="Polen">
                    <div class="form-grid-3">
                        <div class="form-group"><label for="name">Name / Imię *</label><input type="text" id="name" name="name" required></div>
                        <div class="form-group"><label for="email">E-Mail *</label><input type="email" id="email" name="email" required></div>
                        <div class="form-group"><label for="phone">Telefon</label><input type="tel" id="phone" name="phone"></div>
                    </div>
                    <div class="form-group"><label for="message">Nachricht / Wiadomość</label><textarea id="message" name="message" rows="4"></textarea></div>
                    <div class="form-submit-row">
                        <button type="submit" class="btn btn-primary btn-xl">Angebot anfordern →</button>
                    </div>
                </form>
            </div>
        </div>
    </section>

    <footer class="footer">
        <div class="container">
            <div class="footer-bottom">
                <p>© 2024 Secu.li – Rauchmelder {name}, Polen | <a href="../../impressum.html" style="color: var(--gray-400);">Impressum</a></p>
            </div>
        </div>
    </footer>
    <script src="../../script.js"></script>
</body>
</html>'''

TEMPLATE_BG = '''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Rauchmelder Installation & Wartung in {name} ({local}), Bulgarien ✓ Professionell ✓ Zertifiziert ✓ Schnelle Termine.">
    <meta name="keywords" content="Rauchmelder {name}, Детектор за дим {local}, Rauchmelder Bulgarien, Brandschutz {name}">
    <title>Rauchmelder Service {name} (Bulgarien) | Secu.li</title>
    <link rel="canonical" href="https://secu.li/standorte/bulgarien/{slug}.html">
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
                    <span class="hero-badge-top">🇧🇬 {name} ({local})</span>
                    <h1>Rauchmelder Service in {name}</h1>
                    <p class="subtitle">Професионална инсталация на пожароизвестители в {local}. Professionelle Installation und Wartung von Rauchmeldern in {name}, Bulgarien.</p>
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
                <div class="trust-badge-item"><div class="badge-icon">EU</div><span>EU-Normen</span></div>
                <div class="trust-badge-item"><div class="badge-icon">VdS</div><span>VdS anerkannt</span></div>
                <div class="trust-badge-item"><div class="badge-icon">10J</div><span>10 Jahre Garantie</span></div>
            </div>
        </div>
    </section>

    <section class="section">
        <div class="container">
            <div class="section-header">
                <h2>Rauchmelder in {name}, Bulgarien</h2>
            </div>
            <div style="max-width: 800px; margin: 0 auto; line-height: 1.8;">
                <p><strong>{name}</strong> ({local}) ist eine wichtige Stadt in Bulgarien. Wir bieten professionellen Rauchmelder-Service mit deutschem Qualitätsstandard.</p>
                
                <h3 style="margin-top: 2rem;">Unsere Leistungen in {name}</h3>
                <ul style="margin: 1rem 0;">
                    <li>✓ <strong>Installation</strong> nach EU-Normen</li>
                    <li>✓ <strong>Wartung</strong> und Funktionsprüfung</li>
                    <li>✓ <strong>Austausch</strong> alter Geräte</li>
                    <li>✓ <strong>Deutschsprachiger Service</strong></li>
                </ul>
            </div>
        </div>
    </section>

    <section class="section bg-gray">
        <div class="container">
            <div class="section-header">
                <span class="section-badge">Stadtteile</span>
                <h2>Service in {name}</h2>
            </div>
            <div class="countries-grid">
                {bezirke_html}
            </div>
        </div>
    </section>

    <section class="contact-form-section" id="kontaktformular">
        <div class="container">
            <div class="contact-header-centered">
                <span class="section-badge">Jetzt anfragen</span>
                <h2>Angebot für {name}</h2>
            </div>
            <div class="contact-form-card contact-form-large">
                <form class="contact-form" id="localContactForm">
                    <input type="hidden" name="city" value="{name}">
                    <input type="hidden" name="country" value="Bulgarien">
                    <div class="form-grid-3">
                        <div class="form-group"><label for="name">Name / Име *</label><input type="text" id="name" name="name" required></div>
                        <div class="form-group"><label for="email">E-Mail *</label><input type="email" id="email" name="email" required></div>
                        <div class="form-group"><label for="phone">Telefon</label><input type="tel" id="phone" name="phone"></div>
                    </div>
                    <div class="form-group"><label for="message">Nachricht / Съобщение</label><textarea id="message" name="message" rows="4"></textarea></div>
                    <div class="form-submit-row">
                        <button type="submit" class="btn btn-primary btn-xl">Angebot anfordern →</button>
                    </div>
                </form>
            </div>
        </div>
    </section>

    <footer class="footer">
        <div class="container">
            <div class="footer-bottom">
                <p>© 2024 Secu.li – Rauchmelder {name}, Bulgarien | <a href="../../impressum.html" style="color: var(--gray-400);">Impressum</a></p>
            </div>
        </div>
    </footer>
    <script src="../../script.js"></script>
</body>
</html>'''

def generate_pages():
    # Polen
    os.makedirs("standorte/polen", exist_ok=True)
    print("🇵🇱 Polen:")
    for slug, data in POLEN_STAEDTE.items():
        bezirke_html = ""
        for b in data["bezirke"]:
            bezirke_html += f'<div class="country-card"><h5>{b}</h5><p>Service verfügbar</p></div>\n                '
        
        content = TEMPLATE_PL.format(
            name=data["name"],
            local=data["local"],
            slug=slug,
            bezirke_html=bezirke_html.strip()
        )
        with open(f"standorte/polen/{slug}.html", "w", encoding="utf-8") as f:
            f.write(content)
        print(f"   ✅ {data['name']}")
    
    # Bulgarien
    os.makedirs("standorte/bulgarien", exist_ok=True)
    print("\n🇧🇬 Bulgarien:")
    for slug, data in BULGARIEN_STAEDTE.items():
        bezirke_html = ""
        for b in data["bezirke"]:
            bezirke_html += f'<div class="country-card"><h5>{b}</h5><p>Service verfügbar</p></div>\n                '
        
        content = TEMPLATE_BG.format(
            name=data["name"],
            local=data["local"],
            slug=slug,
            bezirke_html=bezirke_html.strip()
        )
        with open(f"standorte/bulgarien/{slug}.html", "w", encoding="utf-8") as f:
            f.write(content)
        print(f"   ✅ {data['name']}")
    
    print(f"\n🎉 {len(POLEN_STAEDTE)} polnische + {len(BULGARIEN_STAEDTE)} bulgarische Städte erstellt!")

if __name__ == "__main__":
    generate_pages()
