#!/usr/bin/env python3
"""
Europäische Länder und Städte SEO-Seiten Generator
Erstellt Seiten für alle europäischen Länder mit deren Städten
"""

import os
from pathlib import Path

OUTPUT_DIR = Path("/Users/neslihanakdeniz/Desktop/Rauchmelder/standorte")

# Europäische Länder mit Städten
EUROPEAN_COUNTRIES = {
    "oesterreich": {
        "name": "Österreich",
        "name_en": "Austria",
        "phone_code": "+43",
        "cities": [
            "Wien", "Graz", "Linz", "Salzburg", "Innsbruck", "Klagenfurt", 
            "Villach", "Wels", "St. Pölten", "Dornbirn", "Wiener Neustadt",
            "Steyr", "Feldkirch", "Bregenz", "Leonding", "Klosterneuburg",
            "Baden bei Wien", "Leoben", "Krems an der Donau", "Traun",
            "Amstetten", "Lustenau", "Kapfenberg", "Mödling", "Hallein",
            "Kufstein", "Traiskirchen", "Schwechat", "Braunau am Inn", "Stockerau"
        ]
    },
    "schweiz": {
        "name": "Schweiz",
        "name_en": "Switzerland",
        "phone_code": "+41",
        "cities": [
            "Zürich", "Genf", "Basel", "Lausanne", "Bern", "Winterthur",
            "Luzern", "St. Gallen", "Lugano", "Biel", "Thun", "Köniz",
            "La Chaux-de-Fonds", "Schaffhausen", "Freiburg", "Chur", "Vernier",
            "Neuchâtel", "Uster", "Sion", "Lancy", "Emmen", "Yverdon-les-Bains",
            "Zug", "Kriens", "Rapperswil-Jona", "Dübendorf", "Montreux", "Frauenfeld"
        ]
    },
    "niederlande": {
        "name": "Niederlande",
        "name_en": "Netherlands",
        "phone_code": "+31",
        "cities": [
            "Amsterdam", "Rotterdam", "Den Haag", "Utrecht", "Eindhoven",
            "Tilburg", "Groningen", "Almere", "Breda", "Nijmegen", "Enschede",
            "Haarlem", "Arnhem", "Amersfoort", "Zaanstad", "Haarlemmermeer",
            "s-Hertogenbosch", "Apeldoorn", "Hoofddorp", "Maastricht", "Leiden",
            "Dordrecht", "Zoetermeer", "Zwolle", "Deventer", "Delft", "Alkmaar"
        ]
    },
    "belgien": {
        "name": "Belgien",
        "name_en": "Belgium",
        "phone_code": "+32",
        "cities": [
            "Brüssel", "Antwerpen", "Gent", "Charleroi", "Lüttich", "Brügge",
            "Namur", "Löwen", "Mons", "Mechelen", "Aalst", "La Louvière",
            "Kortrijk", "Hasselt", "Ostende", "Sint-Niklaas", "Tournai", "Genk",
            "Seraing", "Roeselare", "Verviers", "Mouscron", "Dendermonde"
        ]
    },
    "luxemburg": {
        "name": "Luxemburg",
        "name_en": "Luxembourg",
        "phone_code": "+352",
        "cities": [
            "Luxemburg Stadt", "Esch-sur-Alzette", "Differdingen", "Düdelingen",
            "Petingen", "Ettelbrück", "Diekirch", "Strassen", "Bertrange",
            "Beles", "Mamer", "Hesperingen", "Käerjeng", "Rumelange"
        ]
    },
    "frankreich": {
        "name": "Frankreich",
        "name_en": "France",
        "phone_code": "+33",
        "cities": [
            "Paris", "Marseille", "Lyon", "Toulouse", "Nizza", "Nantes",
            "Straßburg", "Montpellier", "Bordeaux", "Lille", "Rennes", "Reims",
            "Le Havre", "Saint-Étienne", "Toulon", "Grenoble", "Dijon", "Angers",
            "Nîmes", "Villeurbanne", "Le Mans", "Aix-en-Provence", "Clermont-Ferrand",
            "Brest", "Tours", "Limoges", "Amiens", "Perpignan", "Metz", "Besançon"
        ]
    },
    "italien": {
        "name": "Italien",
        "name_en": "Italy",
        "phone_code": "+39",
        "cities": [
            "Rom", "Mailand", "Neapel", "Turin", "Palermo", "Genua", "Bologna",
            "Florenz", "Bari", "Catania", "Venedig", "Verona", "Messina", "Padua",
            "Triest", "Brescia", "Parma", "Tarent", "Prato", "Modena", "Reggio Calabria",
            "Reggio Emilia", "Perugia", "Livorno", "Ravenna", "Cagliari", "Foggia",
            "Rimini", "Ferrara", "Salerno", "Sassari", "Syrakus", "Pescara", "Monza"
        ]
    },
    "spanien": {
        "name": "Spanien",
        "name_en": "Spain",
        "phone_code": "+34",
        "cities": [
            "Madrid", "Barcelona", "Valencia", "Sevilla", "Saragossa", "Málaga",
            "Murcia", "Palma", "Las Palmas", "Bilbao", "Alicante", "Córdoba",
            "Valladolid", "Vigo", "Gijón", "Granada", "A Coruña", "Vitoria-Gasteiz",
            "Elche", "Oviedo", "Santa Cruz de Tenerife", "Pamplona", "Santander",
            "Almería", "San Sebastián", "Burgos", "Salamanca", "Albacete"
        ]
    },
    "polen": {
        "name": "Polen",
        "name_en": "Poland",
        "phone_code": "+48",
        "cities": [
            "Warschau", "Krakau", "Łódź", "Breslau", "Posen", "Danzig", "Stettin",
            "Bydgoszcz", "Lublin", "Białystok", "Kattowitz", "Gdingen", "Tschenstochau",
            "Radom", "Sosnowiec", "Toruń", "Kielce", "Rzeszów", "Gleiwitz", "Zabrze",
            "Olsztyn", "Bielitz-Biala", "Bromberg", "Rzeszow", "Ruda Śląska"
        ]
    },
    "tschechien": {
        "name": "Tschechien",
        "name_en": "Czech Republic",
        "phone_code": "+420",
        "cities": [
            "Prag", "Brünn", "Ostrau", "Pilsen", "Reichenberg", "Olmütz",
            "Budweis", "Hradec Králové", "Ústí nad Labem", "Pardubice",
            "Zlín", "Havířov", "Kladno", "Most", "Opava", "Frýdek-Místek",
            "Karlsbad", "Jihlava", "Teplitz", "Děčín", "Chomutov"
        ]
    },
    "ungarn": {
        "name": "Ungarn",
        "name_en": "Hungary",
        "phone_code": "+36",
        "cities": [
            "Budapest", "Debrecen", "Szeged", "Miskolc", "Pécs", "Győr",
            "Nyíregyháza", "Kecskemét", "Székesfehérvár", "Szombathely",
            "Szolnok", "Tatabánya", "Kaposvár", "Érd", "Veszprém", "Békéscsaba",
            "Zalaegerszeg", "Sopron", "Eger", "Nagykanizsa", "Dunaújváros"
        ]
    },
    "slowakei": {
        "name": "Slowakei",
        "name_en": "Slovakia",
        "phone_code": "+421",
        "cities": [
            "Bratislava", "Košice", "Prešov", "Žilina", "Banská Bystrica",
            "Nitra", "Trnava", "Trenčín", "Martin", "Poprad", "Prievidza",
            "Zvolen", "Považská Bystrica", "Michalovce", "Nové Zámky"
        ]
    },
    "slowenien": {
        "name": "Slowenien",
        "name_en": "Slovenia",
        "phone_code": "+386",
        "cities": [
            "Ljubljana", "Maribor", "Celje", "Kranj", "Velenje", "Koper",
            "Novo Mesto", "Ptuj", "Trbovlje", "Kamnik", "Jesenice", "Nova Gorica"
        ]
    },
    "kroatien": {
        "name": "Kroatien",
        "name_en": "Croatia",
        "phone_code": "+385",
        "cities": [
            "Zagreb", "Split", "Rijeka", "Osijek", "Zadar", "Pula", "Slavonski Brod",
            "Karlovac", "Varaždin", "Šibenik", "Sisak", "Vinkovci", "Dubrovnik"
        ]
    },
    "daenemark": {
        "name": "Dänemark",
        "name_en": "Denmark",
        "phone_code": "+45",
        "cities": [
            "Kopenhagen", "Aarhus", "Odense", "Aalborg", "Esbjerg", "Randers",
            "Kolding", "Horsens", "Vejle", "Roskilde", "Herning", "Hørsholm",
            "Silkeborg", "Næstved", "Frederiksberg", "Viborg", "Køge", "Holstebro"
        ]
    },
    "schweden": {
        "name": "Schweden",
        "name_en": "Sweden",
        "phone_code": "+46",
        "cities": [
            "Stockholm", "Göteborg", "Malmö", "Uppsala", "Västerås", "Örebro",
            "Linköping", "Helsingborg", "Jönköping", "Norrköping", "Lund", "Umeå",
            "Gävle", "Borås", "Södertälje", "Eskilstuna", "Halmstad", "Växjö"
        ]
    },
    "norwegen": {
        "name": "Norwegen",
        "name_en": "Norway",
        "phone_code": "+47",
        "cities": [
            "Oslo", "Bergen", "Trondheim", "Stavanger", "Drammen", "Fredrikstad",
            "Kristiansand", "Sandnes", "Tromsø", "Sarpsborg", "Skien", "Ålesund",
            "Sandefjord", "Haugesund", "Tønsberg", "Moss", "Porsgrunn", "Bodø"
        ]
    },
    "finnland": {
        "name": "Finnland",
        "name_en": "Finland",
        "phone_code": "+358",
        "cities": [
            "Helsinki", "Espoo", "Tampere", "Vantaa", "Oulu", "Turku", "Jyväskylä",
            "Lahti", "Kuopio", "Pori", "Kouvola", "Joensuu", "Lappeenranta",
            "Hämeenlinna", "Vaasa", "Rovaniemi", "Seinäjoki", "Mikkeli"
        ]
    },
    "portugal": {
        "name": "Portugal",
        "name_en": "Portugal",
        "phone_code": "+351",
        "cities": [
            "Lissabon", "Porto", "Vila Nova de Gaia", "Amadora", "Braga", "Funchal",
            "Coimbra", "Setúbal", "Almada", "Agualva-Cacém", "Queluz", "Aveiro",
            "Évora", "Faro", "Guimarães", "Viseu", "Leiria", "Portimão"
        ]
    },
    "griechenland": {
        "name": "Griechenland",
        "name_en": "Greece",
        "phone_code": "+30",
        "cities": [
            "Athen", "Thessaloniki", "Patras", "Piräus", "Heraklion", "Larisa",
            "Volos", "Rhodos", "Ioannina", "Chania", "Chalcis", "Agrinio",
            "Katerini", "Kavala", "Serres", "Alexandroupoli", "Komotini"
        ]
    }
}

# Textvariationen
def get_country_intro(country_name, variant):
    texts = [
        f"Professioneller Rauchmelder-Service in {country_name}. Installation, Wartung und Beratung durch zertifizierte Experten. Jetzt anfragen!",
        f"Rauchmelder für {country_name}: Fachgerechte Installation nach europäischen Normen. Ihr Partner für Brandschutz in ganz {country_name}.",
        f"Brandschutz-Service in {country_name}. Unsere Techniker installieren und warten Ihre Rauchmelder professionell und zuverlässig.",
        f"Ihr Rauchmelder-Experte in {country_name}. Von der Beratung bis zur Installation - alles aus einer Hand. Europaweit tätig."
    ]
    return texts[variant % len(texts)]

def get_city_intro(city, country, variant):
    texts = [
        f"Rauchmelder-Service in {city}, {country}. Professionelle Installation und Wartung durch zertifizierte Fachkräfte. Jetzt unverbindlich anfragen!",
        f"Suchen Sie Rauchmelder-Experten in {city}? Wir bieten Installation, Wartung und Beratung in {country}. TÜV-geprüft und normgerecht.",
        f"Brandschutz für {city}: Fachgerechte Rauchmelder-Montage und jährliche Wartung. Ihr Partner für Sicherheit in {country}.",
        f"Professionelle Rauchmelder in {city}. Schnelle Terminvergabe, faire Preise, vollständige Dokumentation. Europaweit aktiv."
    ]
    return texts[variant % len(texts)]

def slugify(text):
    replacements = {
        'ä': 'ae', 'ö': 'oe', 'ü': 'ue', 'ß': 'ss', 'é': 'e', 'è': 'e',
        'ê': 'e', 'à': 'a', 'á': 'a', 'â': 'a', 'ô': 'o', 'ó': 'o',
        'ł': 'l', 'ń': 'n', 'ś': 's', 'ź': 'z', 'ż': 'z', 'ć': 'c',
        'ø': 'oe', 'å': 'aa', 'æ': 'ae', 'í': 'i', 'ú': 'u', 'ý': 'y',
        'ñ': 'n', 'č': 'c', 'ř': 'r', 'š': 's', 'ž': 'z', 'ď': 'd',
        'ť': 't', 'ň': 'n', 'ě': 'e', 'ů': 'u', 'ő': 'oe', 'ű': 'ue',
        ' ': '-', '/': '-', '.': '', '(': '', ')': '', "'": '', '-': '-'
    }
    slug = text.lower()
    for old, new in replacements.items():
        slug = slug.replace(old, new)
    return slug

def create_country_page(country_slug, country_data, variant):
    country_name = country_data["name"]
    cities = country_data["cities"]
    intro = get_country_intro(country_name, variant)
    
    city_links = "\n".join([
        f'                    <li><a href="{country_slug}/{slugify(city)}.html">{city}</a></li>'
        for city in cities
    ])
    
    return f'''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{intro[:155]}">
    <title>Rauchmelder {country_name} | Installation & Service | Secu.li</title>
    <link rel="canonical" href="https://secu.li/standorte/{country_slug}.html">
    <link rel="stylesheet" href="../styles.css">
    <meta name="theme-color" content="#C41E3A">
    <style>
        .country-hero {{ padding: 100px 20px 40px; background: linear-gradient(135deg, #EEF2FF, #FFF); text-align: center; }}
        .country-hero h1 {{ font-size: 2rem; margin-bottom: 15px; }}
        .country-content {{ padding: 40px 20px; max-width: 1000px; margin: 0 auto; }}
        .city-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 15px; margin-top: 30px; }}
        .city-grid li {{ list-style: none; }}
        .city-grid a {{ display: block; padding: 15px; background: #F9FAFB; border-radius: 8px; text-decoration: none; color: #111; transition: all 0.3s; }}
        .city-grid a:hover {{ background: #C41E3A; color: white; }}
        @media (min-width: 768px) {{ .country-hero h1 {{ font-size: 2.5rem; }} }}
    </style>
</head>
<body>
    <header class="header">
        <div class="container">
            <a href="../index.html" class="logo">Secu.li</a>
            <nav class="nav">
                <ul class="nav-links">
                    <li><a href="../index.html">Startseite</a></li>
                    <li><a href="../kontakt.html">Kontakt</a></li>
                </ul>
                <a href="../kontakt.html" class="btn btn-primary btn-sm">Anfrage</a>
            </nav>
        </div>
    </header>

    <section class="country-hero">
        <div class="container">
            <span class="hero-badge-top">🇪🇺 Europaweiter Service</span>
            <h1>Rauchmelder-Service in {country_name}</h1>
            <p>{intro}</p>
            <div style="margin-top: 20px;">
                <a href="../kontakt.html" class="btn btn-primary">Jetzt anfragen</a>
                <a href="tel:+4915778631120" class="btn btn-outline">📞 Anrufen</a>
            </div>
        </div>
    </section>

    <section class="country-content">
        <h2>Unsere Städte in {country_name}</h2>
        <p>Wir bieten unseren Rauchmelder-Service in folgenden Städten in {country_name} an:</p>
        
        <ul class="city-grid">
{city_links}
        </ul>

        <div style="background: #F9FAFB; padding: 30px; border-radius: 15px; margin-top: 40px; text-align: center;">
            <h3>Ihre Stadt nicht dabei?</h3>
            <p>Kontaktieren Sie uns - wir sind in ganz {country_name} für Sie da!</p>
            <a href="../kontakt.html" class="btn btn-primary">Anfrage senden</a>
        </div>
    </section>

    <footer class="footer">
        <div class="container" style="text-align: center; padding: 30px;">
            <p>&copy; 2024 Secu.li - Rauchmelder {country_name}</p>
            <a href="../impressum.html">Impressum</a> | <a href="../datenschutz.html">Datenschutz</a>
        </div>
    </footer>
</body>
</html>'''

def create_city_page(city, country_name, country_slug, variant):
    intro = get_city_intro(city, country_name, variant)
    city_slug = slugify(city)
    
    return f'''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{intro[:155]}">
    <title>Rauchmelder {city} | Installation & Wartung | Secu.li</title>
    <link rel="canonical" href="https://secu.li/standorte/{country_slug}/{city_slug}.html">
    <link rel="stylesheet" href="../../styles.css">
    <meta name="theme-color" content="#C41E3A">
    <style>
        .local-hero {{ padding: 100px 20px 40px; background: linear-gradient(135deg, #FEF2F2, #FFF); text-align: center; }}
        .local-hero h1 {{ font-size: 1.75rem; margin-bottom: 15px; }}
        .local-content {{ padding: 40px 20px; max-width: 800px; margin: 0 auto; }}
        .local-content h2 {{ color: #C41E3A; margin-top: 30px; }}
        .local-cta {{ background: #F9FAFB; padding: 30px; border-radius: 15px; text-align: center; margin: 30px 0; }}
        .local-form {{ background: #F3F4F6; padding: 30px; border-radius: 15px; margin-top: 30px; }}
        .local-form .form-group {{ margin-bottom: 15px; }}
        .local-form input, .local-form select, .local-form textarea {{ width: 100%; padding: 12px; border: 1px solid #E5E7EB; border-radius: 8px; font-size: 1rem; }}
        @media (min-width: 768px) {{ .local-hero h1 {{ font-size: 2.25rem; }} }}
    </style>
</head>
<body>
    <header class="header">
        <div class="container">
            <a href="../../index.html" class="logo">Secu.li</a>
            <nav class="nav">
                <ul class="nav-links">
                    <li><a href="../../index.html">Startseite</a></li>
                    <li><a href="../../kontakt.html">Kontakt</a></li>
                </ul>
                <a href="#kontakt" class="btn btn-primary btn-sm">Anfrage</a>
            </nav>
        </div>
    </header>

    <section class="local-hero">
        <div class="container">
            <span class="hero-badge-top">📍 {country_name}</span>
            <h1>Rauchmelder-Service in {city}</h1>
            <p>{intro}</p>
            <div style="margin-top: 20px; display: flex; gap: 10px; justify-content: center; flex-wrap: wrap;">
                <a href="#kontakt" class="btn btn-primary">Jetzt anfragen</a>
                <a href="tel:+4915778631120" class="btn btn-outline">📞 Anrufen</a>
            </div>
        </div>
    </section>

    <section class="local-content">
        <h2>Rauchmelder-Installation in {city}</h2>
        <p>Unser professioneller Rauchmelder-Service steht Ihnen in {city} und Umgebung zur Verfügung. Wir bieten fachgerechte Installation, regelmäßige Wartung und kompetente Beratung.</p>
        
        <h2>Warum Secu.li in {city}?</h2>
        <ul>
            <li>✓ Fachgerechte Installation nach europäischen Normen</li>
            <li>✓ Erfahrene, zertifizierte Techniker</li>
            <li>✓ Schnelle Terminvergabe in {city}</li>
            <li>✓ Faire Preise ohne versteckte Kosten</li>
            <li>✓ Vollständige Dokumentation</li>
        </ul>

        <h2>Unser Service für {city}</h2>
        <p>Ob Neuinstallation, jährliche Wartung oder Beratung - wir sind Ihr zuverlässiger Partner für Brandschutz in {city}, {country_name}.</p>

        <div class="local-cta">
            <h3>Kostenlose Beratung für {city}</h3>
            <p>Rufen Sie uns an oder nutzen Sie unser Kontaktformular!</p>
            <a href="tel:+4915778631120" class="btn btn-primary">📞 +49 157 78631120</a>
        </div>

        <div class="local-form" id="kontakt">
            <h3>Anfrage für {city}</h3>
            <form action="https://formspree.io/f/xrbnlwal" method="POST">
                <input type="hidden" name="_subject" value="Anfrage aus {city}, {country_name} - secu.li">
                <input type="hidden" name="standort" value="{city}, {country_name}">
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
                    <textarea name="message" rows="3" placeholder="Ihre Nachricht"></textarea>
                </div>
                <button type="submit" class="btn btn-primary" style="width: 100%;">Anfrage senden</button>
            </form>
        </div>

        <p style="margin-top: 30px; text-align: center;">
            <a href="../{country_slug}.html">← Zurück zu {country_name}</a>
        </p>
    </section>

    <footer class="footer">
        <div class="container" style="text-align: center; padding: 30px;">
            <p>&copy; 2024 Secu.li - Rauchmelder {city}</p>
            <a href="../../impressum.html">Impressum</a> | <a href="../../datenschutz.html">Datenschutz</a>
        </div>
    </footer>
</body>
</html>'''

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    variant = 0
    countries_created = 0
    cities_created = 0
    
    for country_slug, country_data in EUROPEAN_COUNTRIES.items():
        # Länderseite erstellen
        country_dir = OUTPUT_DIR / country_slug
        country_dir.mkdir(parents=True, exist_ok=True)
        
        country_page = OUTPUT_DIR / f"{country_slug}.html"
        if not country_page.exists():
            content = create_country_page(country_slug, country_data, variant)
            country_page.write_text(content, encoding='utf-8')
            countries_created += 1
            variant += 1
        
        # Städteseiten erstellen
        for city in country_data["cities"]:
            city_slug = slugify(city)
            city_page = country_dir / f"{city_slug}.html"
            
            if not city_page.exists():
                content = create_city_page(city, country_data["name"], country_slug, variant)
                city_page.write_text(content, encoding='utf-8')
                cities_created += 1
                variant += 1
    
    print(f"✅ {countries_created} Länderseiten erstellt!")
    print(f"✅ {cities_created} Städteseiten erstellt!")
    print(f"📁 Gespeichert in: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
