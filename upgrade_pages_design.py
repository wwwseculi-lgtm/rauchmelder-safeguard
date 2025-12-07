#!/usr/bin/env python3
"""
Verbessert alle Content-Seiten mit professionellem Design
"""

from pathlib import Path

BASE_DIR = Path("/Users/neslihanakdeniz/Desktop/Rauchmelder")

def get_pro_page(title, desc, h1, badge, content):
    return f'''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{desc}">
    <title>{title}</title>
    <link rel="stylesheet" href="styles.css">
    <meta name="theme-color" content="#C41E3A">
    <style>
        .page-hero {{
            background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
            color: white;
            padding: 140px 20px 80px;
            text-align: center;
        }}
        .page-hero h1 {{
            font-size: 2.5rem;
            margin-bottom: 15px;
            color: white;
        }}
        .page-hero .subtitle {{
            font-size: 1.2rem;
            opacity: 0.9;
            max-width: 600px;
            margin: 0 auto 30px;
        }}
        .hero-badge {{
            display: inline-block;
            background: var(--primary);
            color: white;
            padding: 8px 20px;
            border-radius: 30px;
            font-size: 0.9rem;
            font-weight: 600;
            margin-bottom: 20px;
        }}
        .content-section {{
            padding: 60px 20px;
            max-width: 900px;
            margin: 0 auto;
        }}
        .content-section h2 {{
            color: #1a1a1a;
            margin-top: 40px;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid #E5E7EB;
        }}
        .content-section h2:first-child {{
            margin-top: 0;
        }}
        .info-box {{
            background: linear-gradient(135deg, #F0FDF4, #ECFDF5);
            padding: 25px 30px;
            border-radius: 15px;
            margin: 30px 0;
            border-left: 4px solid #10B981;
        }}
        .info-box h3 {{
            margin-top: 0;
            color: #047857;
        }}
        .warning-box {{
            background: linear-gradient(135deg, #FFFBEB, #FEF3C7);
            padding: 25px 30px;
            border-radius: 15px;
            margin: 30px 0;
            border-left: 4px solid #F59E0B;
        }}
        .cta-box {{
            background: linear-gradient(135deg, #C41E3A, #991B1B);
            color: white;
            padding: 40px;
            border-radius: 20px;
            margin: 50px 0;
            text-align: center;
        }}
        .cta-box h3 {{
            color: white;
            margin-top: 0;
        }}
        .cta-box p {{
            opacity: 0.95;
        }}
        .feature-cards {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 20px;
            margin: 30px 0;
        }}
        .feature-card-pro {{
            background: white;
            border: 1px solid #E5E7EB;
            border-radius: 15px;
            padding: 25px;
            text-align: center;
            transition: all 0.3s;
        }}
        .feature-card-pro:hover {{
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }}
        .feature-card-pro .icon {{
            font-size: 2.5rem;
            margin-bottom: 15px;
        }}
        .feature-card-pro h4 {{
            margin: 0 0 10px;
            color: #1a1a1a;
        }}
        .feature-card-pro p {{
            margin: 0;
            color: #6B7280;
            font-size: 0.95rem;
        }}
        .check-list {{
            list-style: none;
            padding: 0;
        }}
        .check-list li {{
            padding: 12px 0;
            padding-left: 30px;
            position: relative;
            border-bottom: 1px solid #E5E7EB;
        }}
        .check-list li:before {{
            content: "✓";
            position: absolute;
            left: 0;
            color: #10B981;
            font-weight: bold;
        }}
        .cross-list li:before {{
            content: "✗";
            color: #DC2626;
        }}
        .breadcrumb {{
            display: flex;
            gap: 8px;
            font-size: 0.9rem;
            color: rgba(255,255,255,0.7);
            justify-content: center;
            margin-bottom: 20px;
        }}
        .breadcrumb a {{
            color: rgba(255,255,255,0.7);
            text-decoration: none;
        }}
        .breadcrumb a:hover {{
            color: white;
        }}
        .related-links {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin: 30px 0;
        }}
        .related-link {{
            display: block;
            padding: 20px;
            background: #F9FAFB;
            border-radius: 10px;
            text-decoration: none;
            color: #1a1a1a;
            font-weight: 500;
            transition: all 0.3s;
        }}
        .related-link:hover {{
            background: var(--primary);
            color: white;
        }}
        @media (max-width: 768px) {{
            .page-hero h1 {{
                font-size: 1.8rem;
            }}
            .page-hero {{
                padding: 120px 20px 60px;
            }}
        }}
    </style>
</head>
<body>
    <header class="header">
        <div class="container">
            <a href="index.html" class="logo">Secu.li</a>
            <nav class="nav">
                <ul class="nav-links">
                    <li><a href="index.html">Startseite</a></li>
                    <li><a href="produkte.html">Produkte</a></li>
                    <li><a href="service.html">Service</a></li>
                    <li><a href="kontakt.html">Kontakt</a></li>
                </ul>
                <a href="kontakt.html" class="btn btn-primary btn-sm">Anfrage</a>
            </nav>
        </div>
    </header>
    
    <section class="page-hero">
        <nav class="breadcrumb">
            <a href="index.html">Startseite</a> › <a href="ratgeber.html">Ratgeber</a> › <span>{h1}</span>
        </nav>
        <span class="hero-badge">{badge}</span>
        <h1>{h1}</h1>
        <p class="subtitle">{desc}</p>
    </section>
    
    <div class="content-section">
        {content}
    </div>
    
    <footer class="footer">
        <div class="container" style="text-align: center; padding: 30px;">
            <p>&copy; 2024 Secu.li - {h1}</p>
            <a href="impressum.html">Impressum</a> | <a href="datenschutz.html">Datenschutz</a>
        </div>
    </footer>
    <script src="script.js"></script>
</body>
</html>'''

# Define enhanced pages
pages = {
    "optische-rauchmelder.html": {
        "title": "Optische Rauchmelder | Funktionsweise & Vorteile | Secu.li",
        "desc": "Die häufigste und zuverlässigste Art von Rauchmeldern für den Wohnbereich.",
        "h1": "Optische Rauchmelder",
        "badge": "📡 Meistverwendet",
        "content": '''
        <h2>Wie funktioniert ein optischer Rauchmelder?</h2>
        <p>Optische Rauchmelder nutzen das <strong>Streulichtprinzip</strong> zur Raucherkennung:</p>
        
        <div class="feature-cards">
            <div class="feature-card-pro">
                <div class="icon">💡</div>
                <h4>1. LED sendet Licht</h4>
                <p>Eine LED sendet kontinuierlich einen Lichtstrahl in die Rauchkammer.</p>
            </div>
            <div class="feature-card-pro">
                <div class="icon">🌫️</div>
                <h4>2. Rauch streut Licht</h4>
                <p>Bei Rauch werden die Lichtpartikel in alle Richtungen gestreut.</p>
            </div>
            <div class="feature-card-pro">
                <div class="icon">📸</div>
                <h4>3. Sensor erkennt</h4>
                <p>Das gestreute Licht trifft auf den Fotosensor.</p>
            </div>
            <div class="feature-card-pro">
                <div class="icon">🔔</div>
                <h4>4. Alarm!</h4>
                <p>Der Rauchmelder löst einen lauten Alarm aus.</p>
            </div>
        </div>
        
        <h2>Vorteile optischer Rauchmelder</h2>
        <ul class="check-list">
            <li><strong>Keine radioaktiven Stoffe</strong> - umweltfreundlich und sicher</li>
            <li><strong>Reagieren früh</strong> auf sichtbaren Rauch (Schwelbrände)</li>
            <li><strong>Wenige Fehlalarme</strong> bei korrekter Installation</li>
            <li><strong>Wartungsarm</strong> - lange Lebensdauer</li>
            <li><strong>Günstig</strong> - erschwinglicher Preis ab 20€</li>
        </ul>
        
        <h2>Ideale Einsatzorte</h2>
        <div class="feature-cards">
            <div class="feature-card-pro">
                <div class="icon">🛏️</div>
                <h4>Schlafzimmer</h4>
            </div>
            <div class="feature-card-pro">
                <div class="icon">👶</div>
                <h4>Kinderzimmer</h4>
            </div>
            <div class="feature-card-pro">
                <div class="icon">🚪</div>
                <h4>Flure</h4>
            </div>
            <div class="feature-card-pro">
                <div class="icon">🛋️</div>
                <h4>Wohnzimmer</h4>
            </div>
        </div>
        
        <h2>Nicht geeignet für</h2>
        <ul class="check-list cross-list">
            <li>Küchen (wegen Kochdämpfen)</li>
            <li>Badezimmer (wegen Wasserdampf)</li>
            <li>Garagen (wegen Abgasen)</li>
            <li>Staubige Werkstätten</li>
        </ul>
        
        <div class="info-box">
            <h3>💡 Unsere Empfehlung</h3>
            <p>Für die meisten Wohnräume ist der optische Rauchmelder die beste Wahl. Wir empfehlen Modelle mit dem <a href="zertifikate.html">Q-Label</a> für höchste Qualität.</p>
        </div>
        
        <h2>Weitere Rauchmelder-Arten</h2>
        <div class="related-links">
            <a href="ionisationsmelder.html" class="related-link">Ionisationsmelder →</a>
            <a href="thermomelder.html" class="related-link">Thermomelder →</a>
            <a href="funkrauchmelder.html" class="related-link">Funkvernetzte Melder →</a>
        </div>
        
        <div class="cta-box">
            <h3>Professionelle Installation gewünscht?</h3>
            <p>Wir installieren und warten Ihre optischen Rauchmelder nach DIN 14676.</p>
            <a href="kontakt.html" class="btn" style="background: white; color: var(--primary);">Kostenlose Beratung</a>
        </div>
'''
    },
    
    "ionisationsmelder.html": {
        "title": "Ionisationsmelder | Funktionsweise & Info | Secu.li",
        "desc": "Reagieren auf unsichtbare Rauchpartikel - in Deutschland jedoch selten im Einsatz.",
        "h1": "Ionisationsmelder",
        "badge": "⚠️ In DE selten",
        "content": '''
        <div class="warning-box">
            <strong>⚠️ Wichtiger Hinweis</strong>
            <p style="margin: 10px 0 0;">Ionisationsmelder sind in Deutschland aufgrund ihrer radioaktiven Komponenten kaum erhältlich und erfordern eine spezielle Entsorgung.</p>
        </div>
        
        <h2>Funktionsweise</h2>
        <p>Ionisationsmelder nutzen eine kleine Menge radioaktives Material (Americium-241):</p>
        
        <div class="feature-cards">
            <div class="feature-card-pro">
                <div class="icon">☢️</div>
                <h4>1. Ionisation</h4>
                <p>Radioaktives Element ionisiert die Luft in der Messkammer.</p>
            </div>
            <div class="feature-card-pro">
                <div class="icon">⚡</div>
                <h4>2. Stromfluss</h4>
                <p>Zwischen Elektroden fließt ein konstanter Strom.</p>
            </div>
            <div class="feature-card-pro">
                <div class="icon">🌫️</div>
                <h4>3. Unterbrechung</h4>
                <p>Rauchpartikel absorbieren Ionen, Strom sinkt.</p>
            </div>
            <div class="feature-card-pro">
                <div class="icon">🔔</div>
                <h4>4. Alarm</h4>
                <p>Stromabfall löst Alarm aus.</p>
            </div>
        </div>
        
        <h2>Vorteile</h2>
        <ul class="check-list">
            <li>Reagieren sehr schnell auf offene Flammen</li>
            <li>Erkennen auch unsichtbare Rauchpartikel</li>
            <li>Sehr empfindlich</li>
        </ul>
        
        <h2>Nachteile</h2>
        <ul class="check-list cross-list">
            <li>Enthalten radioaktives Material</li>
            <li>Spezielle Entsorgung erforderlich</li>
            <li>In Deutschland kaum erhältlich</li>
            <li>Häufige Fehlalarme bei Kochdämpfen</li>
            <li>Weniger wirksam bei Schwelbränden</li>
        </ul>
        
        <h2>Rechtliche Situation in Deutschland</h2>
        <p>Ionisationsmelder unterliegen der <strong>Strahlenschutzverordnung</strong>. Sie dürfen nur von zugelassenen Stellen verkauft und entsorgt werden.</p>
        
        <div class="info-box">
            <h3>💡 Unsere Empfehlung</h3>
            <p>Für den Hausgebrauch empfehlen wir <a href="optische-rauchmelder.html">optische Rauchmelder</a>. Sie bieten vergleichbare Sicherheit ohne die Nachteile radioaktiver Komponenten.</p>
        </div>
        
        <h2>Weitere Rauchmelder-Arten</h2>
        <div class="related-links">
            <a href="optische-rauchmelder.html" class="related-link">Optische Rauchmelder →</a>
            <a href="thermomelder.html" class="related-link">Thermomelder →</a>
            <a href="funkrauchmelder.html" class="related-link">Funkvernetzte Melder →</a>
        </div>
        
        <div class="cta-box">
            <h3>Beratung zu Rauchmelder-Alternativen?</h3>
            <p>Wir helfen Ihnen, den richtigen Rauchmelder für Ihre Bedürfnisse zu finden.</p>
            <a href="kontakt.html" class="btn" style="background: white; color: var(--primary);">Jetzt beraten lassen</a>
        </div>
'''
    },
    
    "thermomelder.html": {
        "title": "Thermomelder / Wärmemelder | Für Küche & Bad | Secu.li",
        "desc": "Die ideale Lösung für Küche, Bad und andere Räume mit Dampf oder Staub.",
        "h1": "Thermomelder",
        "badge": "🔥 Für Küche & Bad",
        "content": '''
        <h2>Funktionsweise</h2>
        <p>Thermomelder reagieren auf <strong>Temperaturveränderungen</strong> statt auf Rauch:</p>
        
        <div class="feature-cards">
            <div class="feature-card-pro">
                <div class="icon">🌡️</div>
                <h4>Festtemperaturmelder</h4>
                <p>Lösen bei 57°C oder 68°C aus.</p>
            </div>
            <div class="feature-card-pro">
                <div class="icon">📈</div>
                <h4>Differenzialmelder</h4>
                <p>Reagieren auf schnelle Temperaturanstiege.</p>
            </div>
            <div class="feature-card-pro">
                <div class="icon">🔄</div>
                <h4>Kombimelder</h4>
                <p>Vereinen beide Funktionen.</p>
            </div>
        </div>
        
        <h2>Vorteile</h2>
        <ul class="check-list">
            <li><strong>Keine Fehlalarme</strong> durch Dampf oder Staub</li>
            <li><strong>Ideal für Küche</strong> - reagiert nicht auf Kochdämpfe</li>
            <li><strong>Badezimmer-geeignet</strong> - kein Alarm bei heißer Dusche</li>
            <li><strong>Wartungsarm</strong> - lange Lebensdauer</li>
            <li><strong>Zuverlässig</strong> bei offenen Flammen</li>
        </ul>
        
        <h2>Ideale Einsatzorte</h2>
        <div class="feature-cards">
            <div class="feature-card-pro">
                <div class="icon">🍳</div>
                <h4>Küchen</h4>
            </div>
            <div class="feature-card-pro">
                <div class="icon">🚿</div>
                <h4>Badezimmer</h4>
            </div>
            <div class="feature-card-pro">
                <div class="icon">🔧</div>
                <h4>Werkstätten</h4>
            </div>
            <div class="feature-card-pro">
                <div class="icon">🚗</div>
                <h4>Garagen</h4>
            </div>
        </div>
        
        <div class="warning-box">
            <strong>⚠️ Keine Schlafzimmer!</strong>
            <p style="margin: 10px 0 0;">Thermomelder erfüllen NICHT die gesetzliche Rauchmelderpflicht für Schlaf- und Kinderzimmer. Dort sind <a href="optische-rauchmelder.html">optische Rauchmelder</a> vorgeschrieben.</p>
        </div>
        
        <h2>Weitere Rauchmelder-Arten</h2>
        <div class="related-links">
            <a href="optische-rauchmelder.html" class="related-link">Optische Rauchmelder →</a>
            <a href="ionisationsmelder.html" class="related-link">Ionisationsmelder →</a>
            <a href="funkrauchmelder.html" class="related-link">Funkvernetzte Melder →</a>
        </div>
        
        <div class="cta-box">
            <h3>Thermomelder für Ihre Küche?</h3>
            <p>Wir beraten Sie zur optimalen Kombination aus Rauch- und Wärmemeldern.</p>
            <a href="kontakt.html" class="btn" style="background: white; color: var(--primary);">Beratung anfragen</a>
        </div>
'''
    },
    
    "funkrauchmelder.html": {
        "title": "Funkvernetzte Rauchmelder | Vernetzung für mehr Sicherheit | Secu.li",
        "desc": "Wenn einer Alarm schlägt, alarmieren alle - maximale Sicherheit für Ihr Zuhause.",
        "h1": "Funkvernetzte Rauchmelder",
        "badge": "📶 Vernetzt",
        "content": '''
        <h2>Das Prinzip der Vernetzung</h2>
        <p>Funkvernetzte Rauchmelder kommunizieren drahtlos. <strong>Löst ein Melder aus, alarmieren alle anderen gleichzeitig.</strong></p>
        
        <div class="info-box">
            <h3>🔊 Beispiel</h3>
            <p>Ein Brand entsteht im Keller. Der Kellermelder löst aus. Gleichzeitig alarmieren alle Melder im Haus - auch im 2. Stock wo Sie schlafen.</p>
        </div>
        
        <h2>Vorteile</h2>
        <ul class="check-list">
            <li><strong>Hören den Alarm überall</strong> - auch weit entfernt vom Brandherd</li>
            <li><strong>Mehr Zeit zur Flucht</strong> - schnellere Warnung</li>
            <li><strong>Ideal für mehrstöckige Häuser</strong></li>
            <li><strong>Keine Kabel</strong> - einfache Installation</li>
            <li><strong>Erweiterbar</strong> - beliebig viele Melder vernetzbar</li>
        </ul>
        
        <h2>Wann sind Funkrauchmelder sinnvoll?</h2>
        <div class="feature-cards">
            <div class="feature-card-pro">
                <div class="icon">🏠</div>
                <h4>Mehrstöckige Häuser</h4>
            </div>
            <div class="feature-card-pro">
                <div class="icon">📏</div>
                <h4>Große Wohnungen</h4>
                <p>Über 100m²</p>
            </div>
            <div class="feature-card-pro">
                <div class="icon">👴</div>
                <h4>Senioren</h4>
                <p>Hörgeschädigte</p>
            </div>
            <div class="feature-card-pro">
                <div class="icon">👶</div>
                <h4>Familien</h4>
                <p>Mit Kindern</p>
            </div>
        </div>
        
        <h2>Reichweite & Kosten</h2>
        <p>Reichweite: <strong>50-100m</strong> im Freien, 30-40m in Gebäuden.</p>
        <table class="service-table" style="margin-top: 20px;">
            <thead><tr><th>Typ</th><th>Preis</th></tr></thead>
            <tbody>
                <tr><td>Einzelmelder ohne Funk</td><td>ab 20€</td></tr>
                <tr><td>Funkrauchmelder</td><td>ab 40€</td></tr>
                <tr><td>Funk-Set (5 Melder)</td><td>ab 180€</td></tr>
            </tbody>
        </table>
        
        <h2>Weitere Rauchmelder-Arten</h2>
        <div class="related-links">
            <a href="optische-rauchmelder.html" class="related-link">Optische Rauchmelder →</a>
            <a href="ionisationsmelder.html" class="related-link">Ionisationsmelder →</a>
            <a href="thermomelder.html" class="related-link">Thermomelder →</a>
        </div>
        
        <div class="cta-box">
            <h3>Vernetztes System für Ihr Zuhause?</h3>
            <p>Wir planen und installieren Ihr vernetztes Rauchmelder-System.</p>
            <a href="kontakt.html" class="btn" style="background: white; color: var(--primary);">Jetzt anfragen</a>
        </div>
'''
    }
}

def main():
    print("Aktualisiere Seiten mit professionellem Design...")
    for filename, data in pages.items():
        filepath = BASE_DIR / filename
        html = get_pro_page(data['title'], data['desc'], data['h1'], data['badge'], data['content'])
        filepath.write_text(html, encoding='utf-8')
        print(f"✓ {filename}")
    print(f"\n✅ {len(pages)} Seiten mit professionellem Design aktualisiert!")

if __name__ == "__main__":
    main()
