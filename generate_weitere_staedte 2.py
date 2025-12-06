#!/usr/bin/env python3
"""
Erweiterte Städte Generator - Kleinere Städte in Deutschland
"""

import os

# Weitere wichtige Städte
WEITERE_STAEDTE = {
    # Bayern
    "passau": {"name": "Passau", "land": "Bayern", "bezirke": ["Altstadt", "Innstadt", "Grubweg", "Haidenhof"]},
    "landshut": {"name": "Landshut", "land": "Bayern", "bezirke": ["Altstadt", "Frauenberg", "Nikola", "West"]},
    "rosenheim": {"name": "Rosenheim", "land": "Bayern", "bezirke": ["Innenstadt", "Aising", "Pang", "Westerndorf"]},
    "fuerth": {"name": "Fürth", "land": "Bayern", "bezirke": ["Innenstadt", "Südstadt", "Nordstadt", "Hardhöhe"]},
    "bamberg": {"name": "Bamberg", "land": "Bayern", "bezirke": ["Inselstadt", "Bergstadt", "Gärtnerstadt", "Wunderburg"]},
    "bayreuth": {"name": "Bayreuth", "land": "Bayern", "bezirke": ["Innenstadt", "St. Georgen", "Hammerstatt", "Altstadt"]},
    
    # Baden-Württemberg  
    "tuebingen": {"name": "Tübingen", "land": "Baden-Württemberg", "bezirke": ["Altstadt", "Südstadt", "Weststadt", "Waldhäuser-Ost"]},
    "konstanz": {"name": "Konstanz", "land": "Baden-Württemberg", "bezirke": ["Altstadt", "Paradies", "Petershausen", "Allmannsdorf"]},
    "offenburg": {"name": "Offenburg", "land": "Baden-Württemberg", "bezirke": ["Innenstadt", "Nordwest", "Südost", "Griesheim"]},
    "friedrichshafen": {"name": "Friedrichshafen", "land": "Baden-Württemberg", "bezirke": ["Stadtmitte", "Jettenhausen", "Fischbach", "Ailingen"]},
    "sindelfingen": {"name": "Sindelfingen", "land": "Baden-Württemberg", "bezirke": ["Mitte", "Maichingen", "Darmsheim", "Sommerhofen"]},
    "ludwigsburg": {"name": "Ludwigsburg", "land": "Baden-Württemberg", "bezirke": ["Mitte", "West", "Ost", "Eglosheim"]},
    "esslingen": {"name": "Esslingen am Neckar", "land": "Baden-Württemberg", "bezirke": ["Innenstadt", "Mettingen", "Oberesslingen", "Zell"]},
    "goeppingen": {"name": "Göppingen", "land": "Baden-Württemberg", "bezirke": ["Innenstadt", "Faurndau", "Jebenhausen", "Holzheim"]},
    
    # Niedersachsen
    "celle": {"name": "Celle", "land": "Niedersachsen", "bezirke": ["Altstadt", "Neustadt", "Blumlage", "Vorwerk"]},
    "lueneburg": {"name": "Lüneburg", "land": "Niedersachsen", "bezirke": ["Altstadt", "Rotes Feld", "Kaltenmoor", "Ochtmissen"]},
    "delmenhorst": {"name": "Delmenhorst", "land": "Niedersachsen", "bezirke": ["Mitte", "Düsternort", "Deichhorst", "Adelheide"]},
    "wilhelmshaven": {"name": "Wilhelmshaven", "land": "Niedersachsen", "bezirke": ["Mitte", "Voslapp", "Fedderwardergroden", "Heppens"]},
    "emden": {"name": "Emden", "land": "Niedersachsen", "bezirke": ["Innenstadt", "Borssum", "Constantia", "Port Arthur"]},
    
    # Hessen
    "hanau": {"name": "Hanau", "land": "Hessen", "bezirke": ["Innenstadt", "Steinheim", "Großauheim", "Wolfgang"]},
    "giessen": {"name": "Gießen", "land": "Hessen", "bezirke": ["Innenstadt", "Wieseck", "Kleinlinden", "Allendorf"]},
    "marburg": {"name": "Marburg", "land": "Hessen", "bezirke": ["Altstadt", "Südviertel", "Wehrda", "Cappel"]},
    "fulda": {"name": "Fulda", "land": "Hessen", "bezirke": ["Innenstadt", "Galerie", "Aschenberg", "Horas"]},
    "ruesselsheim": {"name": "Rüsselsheim", "land": "Hessen", "bezirke": ["Innenstadt", "Haßloch", "Königstädten", "Bauschheim"]},
    "bad-homburg": {"name": "Bad Homburg", "land": "Hessen", "bezirke": ["Innenstadt", "Gonzenheim", "Kirdorf", "Dornholzhausen"]},
    
    # Nordrhein-Westfalen
    "recklinghausen": {"name": "Recklinghausen", "land": "NRW", "bezirke": ["Stadtmitte", "Süd", "Ost", "Hochlarmark"]},
    "guetersloh": {"name": "Gütersloh", "land": "NRW", "bezirke": ["Mitte", "Nord", "Isselhorst", "Spexard"]},
    "minden": {"name": "Minden", "land": "NRW", "bezirke": ["Innenstadt", "Dankersen", "Hahlen", "Todtenhausen"]},
    "marl": {"name": "Marl", "land": "NRW", "bezirke": ["Mitte", "Alt-Marl", "Hüls", "Sinsen-Lenkerbeck"]},
    "luedinghausen": {"name": "Dülmen", "land": "NRW", "bezirke": ["Innenstadt", "Buldern", "Hiddingsel", "Rorup"]},
    "viersen": {"name": "Viersen", "land": "NRW", "bezirke": ["Viersen", "Dülken", "Süchteln", "Boisheim"]},
    "kerpen": {"name": "Kerpen", "land": "NRW", "bezirke": ["Kerpen", "Horrem", "Sindorf", "Blatzheim"]},
    "troisdorf": {"name": "Troisdorf", "land": "NRW", "bezirke": ["Mitte", "Sieglar", "Oberlar", "Friedrich-Wilhelms-Hütte"]},
    "euskirchen": {"name": "Euskirchen", "land": "NRW", "bezirke": ["Innenstadt", "Kuchenheim", "Flamersheim", "Stotzheim"]},
    "dorsten": {"name": "Dorsten", "land": "NRW", "bezirke": ["Altstadt", "Holsterhausen", "Hervest", "Wulfen"]},
    "luedenscheid": {"name": "Lüdenscheid", "land": "NRW", "bezirke": ["Mitte", "Buckesfeld", "Wehberg", "Brügge"]},
    "iserlohn": {"name": "Iserlohn", "land": "NRW", "bezirke": ["Innenstadt", "Letmathe", "Sümmern", "Hennen"]},
    "witten": {"name": "Witten", "land": "NRW", "bezirke": ["Mitte", "Annen", "Herbede", "Heven"]},
    "velbert": {"name": "Velbert", "land": "NRW", "bezirke": ["Mitte", "Langenberg", "Neviges", "Birth"]},
    "castrop-rauxel": {"name": "Castrop-Rauxel", "land": "NRW", "bezirke": ["Ickern", "Habinghorst", "Bladenhorst", "Schwerin"]},
    "arnsberg": {"name": "Arnsberg", "land": "NRW", "bezirke": ["Arnsberg", "Neheim", "Hüsten", "Oeventrop"]},
    
    # Sachsen
    "zwickau": {"name": "Zwickau", "land": "Sachsen", "bezirke": ["Mitte", "Schedewitz", "Marienthal", "Nordvorstadt"]},
    "plauen": {"name": "Plauen", "land": "Sachsen", "bezirke": ["Innenstadt", "Haselbrunn", "Preißelpöhl", "Chrieschwitz"]},
    "goerlitz": {"name": "Görlitz", "land": "Sachsen", "bezirke": ["Altstadt", "Südstadt", "Königshufen", "Rauschwalde"]},
    "bautzen": {"name": "Bautzen", "land": "Sachsen", "bezirke": ["Altstadt", "Gesundbrunnen", "Westvorstadt", "Seidau"]},
    "pirna": {"name": "Pirna", "land": "Sachsen", "bezirke": ["Altstadt", "Copitz", "Sonnenstein", "Rottwerndorf"]},
    
    # Rheinland-Pfalz
    "kaiserslautern": {"name": "Kaiserslautern", "land": "Rheinland-Pfalz", "bezirke": ["Innenstadt", "Einsiedlerhof", "Erzhütten", "Siegelbach"]},
    "worms": {"name": "Worms", "land": "Rheinland-Pfalz", "bezirke": ["Innenstadt", "Herrnsheim", "Hochheim", "Horchheim"]},
    "neuwied": {"name": "Neuwied", "land": "Rheinland-Pfalz", "bezirke": ["Innenstadt", "Engers", "Oberbieber", "Niederbieber"]},
    "speyer": {"name": "Speyer", "land": "Rheinland-Pfalz", "bezirke": ["Altstadt", "Nord", "Süd", "West"]},
    "bad-kreuznach": {"name": "Bad Kreuznach", "land": "Rheinland-Pfalz", "bezirke": ["Innenstadt", "Bad Münster", "Planig", "Winzenheim"]},
    
    # Brandenburg
    "frankfurt-oder": {"name": "Frankfurt (Oder)", "land": "Brandenburg", "bezirke": ["Zentrum", "Neuberesinchen", "Hansaviertel", "Altberesinchen"]},
    "oranienburg": {"name": "Oranienburg", "land": "Brandenburg", "bezirke": ["Innenstadt", "Lehnitz", "Sachsenhausen", "Friedrichsthal"]},
    "falkensee": {"name": "Falkensee", "land": "Brandenburg", "bezirke": ["Falkensee", "Finkenkrug", "Falkenhain", "Waldheim"]},
    "bernau": {"name": "Bernau bei Berlin", "land": "Brandenburg", "bezirke": ["Innenstadt", "Friedenstal", "Süd", "Schönow"]},
    "eberswalde": {"name": "Eberswalde", "land": "Brandenburg", "bezirke": ["Stadtmitte", "Westend", "Ostende", "Finow"]},
    
    # Schleswig-Holstein
    "flensburg": {"name": "Flensburg", "land": "Schleswig-Holstein", "bezirke": ["Altstadt", "Jürgensby", "Westliche Höhe", "Nordstadt"]},
    "neumuenster": {"name": "Neumünster", "land": "Schleswig-Holstein", "bezirke": ["Innenstadt", "Gadeland", "Tungendorf", "Einfeld"]},
    "norderstedt": {"name": "Norderstedt", "land": "Schleswig-Holstein", "bezirke": ["Mitte", "Harksheide", "Garstedt", "Friedrichsgabe"]},
    "elmshorn": {"name": "Elmshorn", "land": "Schleswig-Holstein", "bezirke": ["Innenstadt", "Kölln-Reisiek", "Vormstegen", "Hainholz"]},
    
    # Thüringen
    "gera": {"name": "Gera", "land": "Thüringen", "bezirke": ["Innenstadt", "Bieblach", "Lusan", "Debschwitz"]},
    "weimar": {"name": "Weimar", "land": "Thüringen", "bezirke": ["Altstadt", "Nord", "West", "Schöndorf"]},
    "gotha": {"name": "Gotha", "land": "Thüringen", "bezirke": ["Innenstadt", "West", "Süd", "Siebleben"]},
    "eisenach": {"name": "Eisenach", "land": "Thüringen", "bezirke": ["Innenstadt", "Nord", "West", "Stregda"]},
    "suhl": {"name": "Suhl", "land": "Thüringen", "bezirke": ["Mitte", "Nord", "Aue", "Lautenberg"]},
    
    # Sachsen-Anhalt
    "dessau": {"name": "Dessau-Roßlau", "land": "Sachsen-Anhalt", "bezirke": ["Innenstadt", "Süd", "Nord", "Roßlau"]},
    "wittenberg": {"name": "Lutherstadt Wittenberg", "land": "Sachsen-Anhalt", "bezirke": ["Altstadt", "West", "Elstervorstadt", "Piesteritz"]},
    "stendal": {"name": "Stendal", "land": "Sachsen-Anhalt", "bezirke": ["Innenstadt", "Stadtsee", "Süd", "Nord"]},
    "wernigerode": {"name": "Wernigerode", "land": "Sachsen-Anhalt", "bezirke": ["Altstadt", "Hasserode", "Silstedt", "Nöschenrode"]},
    
    # Mecklenburg-Vorpommern
    "neubrandenburg": {"name": "Neubrandenburg", "land": "Mecklenburg-Vorpommern", "bezirke": ["Innenstadt", "Datzeberg", "Ihlenfelder Vorstadt", "Katharinenviertel"]},
    "stralsund": {"name": "Stralsund", "land": "Mecklenburg-Vorpommern", "bezirke": ["Altstadt", "Knieper", "Tribseer Vorstadt", "Grünhufe"]},
    "greifswald": {"name": "Greifswald", "land": "Mecklenburg-Vorpommern", "bezirke": ["Innenstadt", "Schönwalde", "Eldena", "Wieck"]},
    "wismar": {"name": "Wismar", "land": "Mecklenburg-Vorpommern", "bezirke": ["Altstadt", "Wendorf", "Friedenshof", "Dargetzow"]},
    "guestrow": {"name": "Güstrow", "land": "Mecklenburg-Vorpommern", "bezirke": ["Altstadt", "Südstadt", "Dettmannsdorf", "Glasewitz"]},
}

TEMPLATE = '''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Rauchmelder Installation & Wartung in {stadt} ✓ TÜV-geprüft ✓ 10 Jahre Garantie ✓ Schnelle Termine. Jetzt kostenlos anfragen!">
    <meta name="keywords" content="Rauchmelder {stadt}, Rauchmelder Installation {stadt}, Rauchmelder Wartung {stadt}, Brandschutz {stadt}">
    <title>Rauchmelder Service {stadt} | Secu.li</title>
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
                    <p class="subtitle">Professionelle Installation und Wartung in {stadt} ({land}). TÜV-geprüft, 10 Jahre Garantie.</p>
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
                <h2>Rauchmelder in {stadt}</h2>
            </div>
            <div style="max-width: 800px; margin: 0 auto; line-height: 1.8;">
                <p>In <strong>{stadt}</strong> ({land}) gilt die gesetzliche <strong>Rauchmelderpflicht</strong>. Wir installieren und warten Ihre Rauchmelder professionell und zuverlässig.</p>
                
                <h3 style="margin-top: 2rem;">Unsere Leistungen in {stadt}</h3>
                <ul style="margin: 1rem 0;">
                    <li>✓ <strong>Installation</strong> nach DIN 14676</li>
                    <li>✓ <strong>Jährliche Wartung</strong> mit Protokoll</li>
                    <li>✓ <strong>Austausch</strong> nach 10 Jahren</li>
                    <li>✓ <strong>Dokumentation</strong> für Vermieter</li>
                </ul>
            </div>
        </div>
    </section>

    <section class="section bg-gray">
        <div class="container">
            <div class="section-header">
                <span class="section-badge">Stadtteile</span>
                <h2>Service in {stadt} und Umgebung</h2>
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
                <h2>Angebot für {stadt}</h2>
            </div>
            <div class="contact-form-card contact-form-large">
                <form class="contact-form" id="localContactForm">
                    <input type="hidden" name="city" value="{stadt}">
                    <div class="form-grid-3">
                        <div class="form-group"><label for="name">Name *</label><input type="text" id="name" name="name" required></div>
                        <div class="form-group"><label for="email">E-Mail *</label><input type="email" id="email" name="email" required></div>
                        <div class="form-group"><label for="phone">Telefon</label><input type="tel" id="phone" name="phone"></div>
                    </div>
                    <div class="form-group"><label for="message">Ihre Nachricht</label><textarea id="message" name="message" rows="4"></textarea></div>
                    <div class="form-submit-row">
                        <button type="submit" class="btn btn-primary btn-xl">Angebot für {stadt} →</button>
                    </div>
                </form>
            </div>
        </div>
    </section>

    <footer class="footer">
        <div class="container">
            <div class="footer-bottom">
                <p>© 2024 Secu.li – Rauchmelder {stadt} | <a href="../../impressum.html" style="color: var(--gray-400);">Impressum</a> | <a href="../../datenschutz.html" style="color: var(--gray-400);">Datenschutz</a></p>
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
    for slug, data in WEITERE_STAEDTE.items():
        stadt = data["name"]
        land = data["land"]
        bezirke = data.get("bezirke", [])
        
        bezirke_html = ""
        for bezirk in bezirke:
            bezirke_html += f'<div class="country-card"><h5>{bezirk}</h5><p>Service verfügbar</p></div>\n                '
        
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
    
    print(f"\n🎉 {count} weitere Städte erstellt!")

if __name__ == "__main__":
    generate_pages()
