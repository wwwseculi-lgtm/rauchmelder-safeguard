#!/usr/bin/env python3
"""
Verbessert ALLE Content-Seiten mit professionellem Design
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
        .content-section.wide {{
            max-width: 1100px;
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
        .danger-box {{
            background: linear-gradient(135deg, #FEF2F2, #FEE2E2);
            padding: 25px 30px;
            border-radius: 15px;
            margin: 30px 0;
            border-left: 4px solid #DC2626;
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
            flex-wrap: wrap;
        }}
        .breadcrumb a {{
            color: rgba(255,255,255,0.7);
            text-decoration: none;
        }}
        .breadcrumb a:hover {{
            color: white;
        }}
        .pricing-cards {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 25px;
            margin: 40px 0;
        }}
        .pricing-card {{
            background: white;
            border: 2px solid #E5E7EB;
            border-radius: 20px;
            padding: 35px;
            text-align: center;
            position: relative;
        }}
        .pricing-card.featured {{
            border-color: var(--primary);
            transform: scale(1.02);
        }}
        .pricing-card .badge {{
            position: absolute;
            top: -12px;
            left: 50%;
            transform: translateX(-50%);
            background: #F59E0B;
            color: #111;
            padding: 5px 20px;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 600;
        }}
        .pricing-card h3 {{
            margin-top: 10px;
        }}
        .pricing-card .price {{
            font-size: 2.5rem;
            font-weight: 700;
            color: var(--primary);
            margin: 15px 0;
        }}
        .pricing-card ul {{
            list-style: none;
            padding: 0;
            text-align: left;
        }}
        .pricing-card li {{
            padding: 10px 0;
            border-bottom: 1px solid #E5E7EB;
        }}
        .review-card {{
            background: white;
            border: 1px solid #E5E7EB;
            padding: 25px;
            border-radius: 15px;
            margin-bottom: 20px;
        }}
        .review-header {{
            display: flex;
            justify-content: space-between;
            margin-bottom: 15px;
        }}
        .review-stars {{
            color: #F59E0B;
        }}
        .blog-card {{
            background: white;
            border: 1px solid #E5E7EB;
            border-radius: 15px;
            overflow: hidden;
            margin-bottom: 25px;
            transition: all 0.3s;
        }}
        .blog-card:hover {{
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }}
        .blog-card-content {{
            padding: 25px;
        }}
        .blog-tag {{
            display: inline-block;
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 600;
            margin-bottom: 10px;
        }}
        .blog-tag.tip {{ background: #10B981; color: white; }}
        .blog-tag.news {{ background: #3B82F6; color: white; }}
        .blog-tag.info {{ background: #F59E0B; color: #111; }}
        .blog-tag.important {{ background: #DC2626; color: white; }}
        .download-item {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px;
            background: #F9FAFB;
            border-radius: 10px;
            margin-bottom: 15px;
        }}
        .download-item:hover {{
            background: #F3F4F6;
        }}
        .table-container {{
            overflow-x: auto;
            margin: 30px 0;
        }}
        .pro-table {{
            width: 100%;
            border-collapse: collapse;
            min-width: 600px;
        }}
        .pro-table th, .pro-table td {{
            padding: 15px;
            text-align: left;
            border-bottom: 1px solid #E5E7EB;
        }}
        .pro-table th {{
            background: #1a1a1a;
            color: white;
        }}
        .pro-table tr:hover {{
            background: #F9FAFB;
        }}
        @media (max-width: 768px) {{
            .page-hero h1 {{
                font-size: 1.8rem;
            }}
            .page-hero {{
                padding: 120px 20px 60px;
            }}
            .pricing-card.featured {{
                transform: none;
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
            <a href="index.html">Startseite</a> › <span>{h1}</span>
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

pages = {
    "rauchmelderpflicht.html": {
        "title": "Rauchmelderpflicht in Deutschland | Gesetzliche Regelungen | Secu.li",
        "desc": "Alle Infos zur Rauchmelderpflicht: Welche Gesetze gelten? Wer ist verantwortlich?",
        "h1": "Rauchmelderpflicht",
        "badge": "📋 Gesetz",
        "content": '''
        <h2>Wer ist verantwortlich?</h2>
        <div class="feature-cards">
            <div class="feature-card-pro">
                <div class="icon">🏠</div>
                <h4>Eigentümer</h4>
                <p>Installation der Rauchmelder</p>
            </div>
            <div class="feature-card-pro">
                <div class="icon">🔧</div>
                <h4>Mieter/Eigentümer</h4>
                <p>Wartung (je nach Bundesland)</p>
            </div>
        </div>
        
        <h2>Wo müssen Rauchmelder installiert werden?</h2>
        <ul class="check-list">
            <li><strong>Schlafzimmer</strong> - Pflicht</li>
            <li><strong>Kinderzimmer</strong> - Pflicht</li>
            <li><strong>Flure (Rettungswege)</strong> - Pflicht</li>
            <li><strong>Wohnzimmer</strong> - Empfohlen</li>
        </ul>
        
        <h2>Übersicht nach Bundesland</h2>
        <div class="table-container">
            <table class="pro-table">
                <thead><tr><th>Bundesland</th><th>Pflicht seit</th><th>Wartung</th></tr></thead>
                <tbody>
                    <tr><td>Baden-Württemberg</td><td>2015</td><td>Eigentümer/Mieter</td></tr>
                    <tr><td>Bayern</td><td>2018</td><td>Eigentümer</td></tr>
                    <tr><td>Berlin</td><td>2017</td><td>Eigentümer/Mieter</td></tr>
                    <tr><td>Brandenburg</td><td>2020</td><td>Eigentümer</td></tr>
                    <tr><td>Hamburg</td><td>2011</td><td>Eigentümer</td></tr>
                    <tr><td>Nordrhein-Westfalen</td><td>2017</td><td>Eigentümer</td></tr>
                </tbody>
            </table>
        </div>
        
        <h2>Konsequenzen bei Verstoß</h2>
        <div class="danger-box">
            <strong>❌ Risiken bei fehlenden Rauchmeldern:</strong>
            <ul style="margin: 15px 0 0;">
                <li>Bußgelder bis zu 50.000 €</li>
                <li>Versicherungsausfall im Brandfall</li>
                <li>Strafrechtliche Konsequenzen bei Personenschäden</li>
            </ul>
        </div>
        
        <div class="cta-box">
            <h3>Jetzt gesetzeskonform werden</h3>
            <p>Wir installieren und warten Ihre Rauchmelder nach DIN 14676.</p>
            <a href="kontakt.html" class="btn" style="background: white; color: var(--primary);">Kostenlose Beratung</a>
        </div>
'''
    },
    
    "ratgeber.html": {
        "title": "Rauchmelder Ratgeber & Wissen | Secu.li",
        "desc": "Alles was Sie über Rauchmelder wissen müssen: Funktionsweise, Typen, Kauftipps.",
        "h1": "Rauchmelder Ratgeber",
        "badge": "📚 Wissen",
        "content": '''
        <h2>Wie funktioniert ein Rauchmelder?</h2>
        <p>Rauchmelder erkennen Rauchpartikel in der Luft. Die meisten Geräte nutzen das <strong>optische Streulichtverfahren</strong>: Eine LED sendet Licht aus, das bei Rauch auf einen Sensor reflektiert wird.</p>
        
        <h2>Arten von Rauchmeldern</h2>
        <div class="feature-cards">
            <a href="optische-rauchmelder.html" class="feature-card-pro" style="text-decoration: none;">
                <div class="icon">📡</div>
                <h4>Optische Rauchmelder →</h4>
                <p>Am häufigsten, ideal für Wohnräume.</p>
            </a>
            <a href="ionisationsmelder.html" class="feature-card-pro" style="text-decoration: none;">
                <div class="icon">☢️</div>
                <h4>Ionisationsmelder →</h4>
                <p>In Deutschland selten.</p>
            </a>
            <a href="thermomelder.html" class="feature-card-pro" style="text-decoration: none;">
                <div class="icon">🔥</div>
                <h4>Thermomelder →</h4>
                <p>Ideal für Küche und Bad.</p>
            </a>
            <a href="funkrauchmelder.html" class="feature-card-pro" style="text-decoration: none;">
                <div class="icon">📶</div>
                <h4>Funkvernetzte Melder →</h4>
                <p>Alarmieren alle gleichzeitig.</p>
            </a>
        </div>
        
        <h2>Kauftipps</h2>
        <ul class="check-list">
            <li>Achten Sie auf das <strong>Q-Label</strong> für hochwertige Geräte</li>
            <li>Mindestlebensdauer: <strong>10 Jahre</strong></li>
            <li>Prüfzeichen: <strong>CE + EN 14604</strong></li>
            <li>Testtaste und Stummschaltung sollten vorhanden sein</li>
        </ul>
        
        <h2>Richtige Platzierung</h2>
        <div class="feature-cards">
            <div class="feature-card-pro">
                <div class="icon">📍</div>
                <h4>Mittig an die Decke</h4>
            </div>
            <div class="feature-card-pro">
                <div class="icon">📏</div>
                <h4>50cm von Wänden</h4>
            </div>
            <div class="feature-card-pro">
                <div class="icon">📐</div>
                <h4>Max. 60m² pro Melder</h4>
            </div>
        </div>
        
        <div class="cta-box">
            <h3>Professionelle Beratung gewünscht?</h3>
            <p>Wir helfen Ihnen, die richtigen Rauchmelder zu finden.</p>
            <a href="kontakt.html" class="btn" style="background: white; color: var(--primary);">Jetzt anfragen</a>
        </div>
'''
    },
    
    "preise.html": {
        "title": "Preise & Pakete | Rauchmelder Installation | Secu.li",
        "desc": "Transparente Festpreise für Rauchmelder-Installation und Wartung.",
        "h1": "Preise & Pakete",
        "badge": "💰 Transparent",
        "content": '''
        <div class="pricing-cards">
            <div class="pricing-card">
                <h3>Starter</h3>
                <div class="price">ab 99€</div>
                <ul>
                    <li>✓ 3 Rauchmelder</li>
                    <li>✓ Fachgerechte Installation</li>
                    <li>✓ 10 Jahre Garantie</li>
                    <li>✓ Dokumentation</li>
                </ul>
                <a href="kontakt.html" class="btn btn-outline" style="width: 100%;">Anfragen</a>
            </div>
            
            <div class="pricing-card featured">
                <span class="badge">BELIEBT</span>
                <h3>Standard</h3>
                <div class="price">ab 149€</div>
                <ul>
                    <li>✓ 5 Rauchmelder</li>
                    <li>✓ Fachgerechte Installation</li>
                    <li>✓ 10 Jahre Garantie</li>
                    <li>✓ Dokumentation</li>
                    <li>✓ 1x Wartung inklusive</li>
                </ul>
                <a href="kontakt.html" class="btn btn-primary" style="width: 100%;">Anfragen</a>
            </div>
            
            <div class="pricing-card">
                <h3>Premium</h3>
                <div class="price">ab 249€</div>
                <ul>
                    <li>✓ 8 Rauchmelder</li>
                    <li>✓ Fachgerechte Installation</li>
                    <li>✓ 10 Jahre Garantie</li>
                    <li>✓ Dokumentation</li>
                    <li>✓ 3 Jahre Wartung inkl.</li>
                </ul>
                <a href="kontakt.html" class="btn btn-outline" style="width: 100%;">Anfragen</a>
            </div>
        </div>
        
        <h2>Einzelpreise</h2>
        <div class="table-container">
            <table class="pro-table">
                <thead><tr><th>Leistung</th><th>Preis</th></tr></thead>
                <tbody>
                    <tr><td>Installation pro Rauchmelder</td><td>ab 29€</td></tr>
                    <tr><td>Jährliche Wartung pro Melder</td><td>ab 5€</td></tr>
                    <tr><td>Geräteaustausch (nach 10 Jahren)</td><td>ab 25€</td></tr>
                    <tr><td>Anfahrtspauschale</td><td>ab 19€</td></tr>
                </tbody>
            </table>
        </div>
        
        <div class="info-box">
            <h3>💡 Mengenrabatt für Hausverwaltungen</h3>
            <p>Ab 10 Wohneinheiten: 10-20% Rabatt. <a href="vermieter.html">Mehr erfahren →</a></p>
        </div>
'''
    },
    
    "bewertungen.html": {
        "title": "Kundenbewertungen & Referenzen | Secu.li",
        "desc": "Lesen Sie echte Kundenbewertungen und Erfahrungen mit unserem Service.",
        "h1": "Kundenbewertungen",
        "badge": "⭐ 4.9/5 Sterne",
        "content": '''
        <div style="text-align: center; margin-bottom: 40px;">
            <div style="font-size: 3rem;">⭐⭐⭐⭐⭐</div>
            <p><strong>4.9 von 5 Sternen</strong> basierend auf über 500 Bewertungen</p>
        </div>
        
        <div class="review-card">
            <div class="review-header">
                <strong>Thomas M. aus Berlin</strong>
                <span class="review-stars">⭐⭐⭐⭐⭐</span>
            </div>
            <p>"Schneller, professioneller Service. Die Techniker waren pünktlich und haben alles sauber installiert. Die Dokumentation kam direkt per E-Mail. Sehr empfehlenswert!"</p>
        </div>
        
        <div class="review-card">
            <div class="review-header">
                <strong>Hausverwaltung Schmidt GmbH</strong>
                <span class="review-stars">⭐⭐⭐⭐⭐</span>
            </div>
            <p>"Wir lassen seit 3 Jahren alle unsere Objekte von Secu.li betreuen. Die Koordination mit den Mietern funktioniert reibungslos, die Dokumentation ist immer vollständig."</p>
        </div>
        
        <div class="review-card">
            <div class="review-header">
                <strong>Maria K. aus München</strong>
                <span class="review-stars">⭐⭐⭐⭐⭐</span>
            </div>
            <p>"Endlich ein Anbieter, der auch die jährliche Wartung zuverlässig durchführt. Bekomme rechtzeitig eine Erinnerung und kann den Termin online buchen."</p>
        </div>
        
        <div class="cta-box">
            <h3>Werden Sie unser nächster zufriedener Kunde</h3>
            <p>Erleben Sie unseren Service selbst.</p>
            <a href="kontakt.html" class="btn" style="background: white; color: var(--primary);">Jetzt anfragen</a>
        </div>
'''
    },
    
    "blog.html": {
        "title": "Blog & News | Rauchmelder & Brandschutz | Secu.li",
        "desc": "Aktuelle News, Tipps und Wissenswertes rund um Rauchmelder und Brandschutz.",
        "h1": "Blog & News",
        "badge": "📰 Aktuelles",
        "content": '''
        <div class="blog-card">
            <div class="blog-card-content">
                <span class="blog-tag tip">Tipp</span>
                <h2><a href="ratgeber.html" style="color: inherit; text-decoration: none;">5 häufige Fehler bei der Rauchmelder-Installation</a></h2>
                <p style="color: #6B7280;">Vermeiden Sie diese typischen Fehler, die die Funktion Ihres Rauchmelders beeinträchtigen können.</p>
                <a href="ratgeber.html" style="color: var(--primary); font-weight: 600;">Weiterlesen →</a>
            </div>
        </div>
        
        <div class="blog-card">
            <div class="blog-card-content">
                <span class="blog-tag news">News</span>
                <h2><a href="rauchmelderpflicht.html" style="color: inherit; text-decoration: none;">Rauchmelderpflicht: Alle Bundesländer im Überblick</a></h2>
                <p style="color: #6B7280;">Die aktuellen Regelungen für alle 16 Bundesländer auf einen Blick.</p>
                <a href="rauchmelderpflicht.html" style="color: var(--primary); font-weight: 600;">Weiterlesen →</a>
            </div>
        </div>
        
        <div class="blog-card">
            <div class="blog-card-content">
                <span class="blog-tag info">Wissen</span>
                <h2><a href="zertifikate.html" style="color: inherit; text-decoration: none;">Q-Label: Was es bedeutet und warum es wichtig ist</a></h2>
                <p style="color: #6B7280;">Das Q-Label garantiert höchste Qualität bei Rauchmeldern.</p>
                <a href="zertifikate.html" style="color: var(--primary); font-weight: 600;">Weiterlesen →</a>
            </div>
        </div>
        
        <div class="blog-card">
            <div class="blog-card-content">
                <span class="blog-tag important">Wichtig</span>
                <h2><a href="notfall.html" style="color: inherit; text-decoration: none;">Verhalten im Brandfall - Diese Regeln retten Leben</a></h2>
                <p style="color: #6B7280;">Was tun, wenn es brennt? Die wichtigsten Verhaltensregeln.</p>
                <a href="notfall.html" style="color: var(--primary); font-weight: 600;">Weiterlesen →</a>
            </div>
        </div>
'''
    },
    
    "notfall.html": {
        "title": "Notfall & Verhalten im Brandfall | Secu.li",
        "desc": "Was tun wenn der Rauchmelder Alarm gibt? Lebensrettende Verhaltensregeln.",
        "h1": "Verhalten im Brandfall",
        "badge": "🚨 Wichtig",
        "content": '''
        <div class="danger-box" style="text-align: center;">
            <h2 style="color: #DC2626; margin-top: 0;">🚨 Notruf: 112</h2>
            <p style="margin: 0;">Feuerwehr und Rettungsdienst europaweit - kostenlos, 24/7</p>
        </div>
        
        <h2>Wenn der Rauchmelder Alarm gibt</h2>
        <div class="feature-cards">
            <div class="feature-card-pro">
                <div class="icon">😌</div>
                <h4>1. Ruhe bewahren</h4>
                <p>Panik führt zu Fehlern</p>
            </div>
            <div class="feature-card-pro">
                <div class="icon">🚪</div>
                <h4>2. Tür prüfen</h4>
                <p>Ist sie heiß? Nicht öffnen!</p>
            </div>
            <div class="feature-card-pro">
                <div class="icon">🏃</div>
                <h4>3. Gebückt gehen</h4>
                <p>Rauch steigt nach oben</p>
            </div>
            <div class="feature-card-pro">
                <div class="icon">📞</div>
                <h4>4. Notruf wählen</h4>
                <p>112 anrufen</p>
            </div>
        </div>
        
        <h2>Wichtige Verhaltensregeln</h2>
        <ul class="check-list">
            <li><strong>Türen schließen</strong> - halten Feuer und Rauch auf</li>
            <li><strong>Fenster nicht öffnen</strong> - Sauerstoff facht Feuer an</li>
            <li><strong>Kinder zuerst</strong> - helfen Sie zuerst Hilfsbedürftigen</li>
            <li><strong>Nicht zurückgehen</strong> - niemals für Wertsachen</li>
        </ul>
        
        <div class="warning-box">
            <h3>⚠️ Wenn Sie nicht flüchten können</h3>
            <ul>
                <li>Fenster öffnen und um Hilfe rufen</li>
                <li>Tür mit nassen Tüchern abdichten</li>
                <li>Am Boden bleiben (weniger Rauch)</li>
                <li>Auf Rettung warten</li>
            </ul>
        </div>
        
        <div class="info-box">
            <h3>💡 Vorsorge ist besser</h3>
            <p>Funktionierende Rauchmelder geben Ihnen wertvolle Zeit zur Flucht. <a href="wartung.html">Mehr zur Wartung →</a></p>
        </div>
'''
    },
    
    "zertifikate.html": {
        "title": "Rauchmelder Zertifikate erklärt | Q-Label, CE, TÜV | Secu.li",
        "desc": "Was bedeuten Q-Label, EN 14604, CE und TÜV bei Rauchmeldern?",
        "h1": "Zertifikate erklärt",
        "badge": "🏆 Qualität",
        "content": '''
        <div class="feature-cards">
            <div class="feature-card-pro">
                <div class="icon" style="font-size: 1.5rem; background: #1a1a1a; color: white; padding: 10px 20px; border-radius: 10px;">CE</div>
                <h4>CE-Kennzeichnung</h4>
                <p>Pflicht für EU-Markt. Grundlegende Sicherheit.</p>
            </div>
            <div class="feature-card-pro">
                <div class="icon" style="font-size: 1.5rem; background: #10B981; color: white; padding: 10px 15px; border-radius: 10px;">EN 14604</div>
                <h4>EN 14604</h4>
                <p>Europäische Produktnorm. Mindestanforderungen.</p>
            </div>
            <div class="feature-card-pro">
                <div class="icon" style="font-size: 2rem; background: #C41E3A; color: white; padding: 10px 25px; border-radius: 10px;">Q</div>
                <h4>Q-Label</h4>
                <p>Höchste Qualität. 10-Jahre-Batterie.</p>
            </div>
            <div class="feature-card-pro">
                <div class="icon" style="font-size: 1.5rem; background: #3B82F6; color: white; padding: 10px 20px; border-radius: 10px;">TÜV</div>
                <h4>TÜV-Prüfung</h4>
                <p>Unabhängige Sicherheitsprüfung.</p>
            </div>
        </div>
        
        <h2>Q-Label im Detail</h2>
        <div class="info-box">
            <h3>Das wichtigste Qualitätsmerkmal!</h3>
            <ul class="check-list" style="background: transparent; padding: 0;">
                <li>Festeingebaute 10-Jahres-Batterie</li>
                <li>Erhöhte Stabilität gegen äußere Einflüsse</li>
                <li>Reduzierte Fehlalarme</li>
                <li>Erhöhte Langlebigkeit der Komponenten</li>
            </ul>
        </div>
        
        <h2>Unsere Empfehlung</h2>
        <p>Achten Sie beim Kauf auf mindestens:</p>
        <ul class="check-list">
            <li><strong>CE + EN 14604</strong> - gesetzlich vorgeschrieben</li>
            <li><strong>Q-Label</strong> - für beste Qualität</li>
            <li>VdS - empfohlen</li>
        </ul>
        
        <p style="margin-top: 30px;"><strong>Alle unsere Rauchmelder sind CE, EN 14604 und Q-Label zertifiziert.</strong></p>
'''
    },
    
    "downloads.html": {
        "title": "Downloads | PDFs & Datenblätter | Secu.li", 
        "desc": "Datenblätter, Montageanleitungen und Informationsmaterial herunterladen.",
        "h1": "Download-Bereich",
        "badge": "📥 Dokumente",
        "content": '''
        <h2>Produktinformationen</h2>
        <div class="download-item">
            <div>
                <strong>Rauchmelder Ei650 - Datenblatt</strong>
                <p style="margin: 0; color: #6B7280; font-size: 0.9rem;">PDF, 450 KB</p>
            </div>
            <a href="kontakt.html" class="btn btn-outline btn-sm">Anfragen</a>
        </div>
        <div class="download-item">
            <div>
                <strong>Funkrauchmelder - Übersicht</strong>
                <p style="margin: 0; color: #6B7280; font-size: 0.9rem;">PDF, 320 KB</p>
            </div>
            <a href="kontakt.html" class="btn btn-outline btn-sm">Anfragen</a>
        </div>
        
        <h2>Montage & Wartung</h2>
        <div class="download-item">
            <div>
                <strong>Montage-Anleitung nach DIN 14676</strong>
                <p style="margin: 0; color: #6B7280; font-size: 0.9rem;">PDF, 1.2 MB</p>
            </div>
            <a href="kontakt.html" class="btn btn-outline btn-sm">Anfragen</a>
        </div>
        <div class="download-item">
            <div>
                <strong>Wartungsprotokoll - Vorlage</strong>
                <p style="margin: 0; color: #6B7280; font-size: 0.9rem;">PDF, 85 KB</p>
            </div>
            <a href="kontakt.html" class="btn btn-outline btn-sm">Anfragen</a>
        </div>
        
        <div class="cta-box">
            <h3>Benötigen Sie weitere Unterlagen?</h3>
            <p>Kontaktieren Sie uns - wir senden Ihnen gerne weitere Informationen zu.</p>
            <a href="kontakt.html" class="btn" style="background: white; color: var(--primary);">Kontakt aufnehmen</a>
        </div>
'''
    },
    
    "privatkunden.html": {
        "title": "Rauchmelder für Privatkunden | Secu.li",
        "desc": "Rauchmelder-Service für Privatkunden: Beratung, Installation und Wartung.",
        "h1": "Für Privatkunden",
        "badge": "🏠 Privat",
        "content": '''
        <h2>Unser Service für Sie</h2>
        <div class="feature-cards">
            <div class="feature-card-pro">
                <div class="icon">🏡</div>
                <h4>Einfamilienhaus</h4>
                <p>3-10 Melder je nach Größe</p>
            </div>
            <div class="feature-card-pro">
                <div class="icon">🏢</div>
                <h4>Eigentumswohnung</h4>
                <p>Individuelle Lösung</p>
            </div>
            <div class="feature-card-pro">
                <div class="icon">👴</div>
                <h4>Seniorenhaushalte</h4>
                <p>Extra lauter Alarm</p>
            </div>
        </div>
        
        <h2>Warum professionelle Installation?</h2>
        <ul class="check-list">
            <li><strong>Garantiert richtige Platzierung</strong></li>
            <li><strong>Hochwertige, geprüfte Melder</strong></li>
            <li><strong>10 Jahre Garantie</strong></li>
            <li><strong>Dokumentation für Versicherung</strong></li>
            <li><strong>Jährliche Wartungserinnerung</strong></li>
        </ul>
        
        <h2>Unsere Pakete</h2>
        <div class="table-container">
            <table class="pro-table">
                <thead><tr><th>Paket</th><th>Inhalt</th><th>Ideal für</th></tr></thead>
                <tbody>
                    <tr><td>Starter</td><td>3 Rauchmelder</td><td>Kleine Wohnung</td></tr>
                    <tr><td>Standard</td><td>5 Rauchmelder</td><td>3-4 Zimmer</td></tr>
                    <tr><td>Komplett</td><td>8 Rauchmelder</td><td>Einfamilienhaus</td></tr>
                </tbody>
            </table>
        </div>
        
        <div class="cta-box">
            <h3>Kostenloses Angebot</h3>
            <p>Wir beraten Sie unverbindlich.</p>
            <a href="kontakt.html" class="btn" style="background: white; color: var(--primary);">Jetzt anfragen</a>
        </div>
'''
    },
    
    "vermieter.html": {
        "title": "Rauchmelder für Vermieter & Hausverwaltungen | Secu.li",
        "desc": "Professioneller Rauchmelder-Service für Vermieter: Installation, Wartung, Dokumentation.",
        "h1": "Für Vermieter",
        "badge": "🏢 Business",
        "content": '''
        <h2>Ihre Pflichten als Vermieter</h2>
        <ul class="check-list">
            <li><strong>Installation</strong> in Schlaf-, Kinderzimmern und Fluren</li>
            <li><strong>Regelmäßige Wartung</strong> (je nach Bundesland)</li>
            <li><strong>Dokumentation</strong> für Versicherung und Nachweis</li>
        </ul>
        
        <h2>Unser Komplett-Service</h2>
        <div class="feature-cards">
            <div class="feature-card-pro">
                <div class="icon">🏗️</div>
                <h4>Erstinstallation</h4>
                <p>Fachgerechte Montage nach DIN 14676</p>
            </div>
            <div class="feature-card-pro">
                <div class="icon">🔍</div>
                <h4>Jährliche Wartung</h4>
                <p>Funktionsprüfung, Batterietest</p>
            </div>
            <div class="feature-card-pro">
                <div class="icon">📄</div>
                <h4>Dokumentation</h4>
                <p>Rechtssichere Protokolle</p>
            </div>
            <div class="feature-card-pro">
                <div class="icon">🔔</div>
                <h4>Erinnerungsservice</h4>
                <p>Automatische Terminbenachrichtigung</p>
            </div>
        </div>
        
        <h2>Mengenrabatte</h2>
        <div class="table-container">
            <table class="pro-table">
                <thead><tr><th>Anzahl Einheiten</th><th>Rabatt</th></tr></thead>
                <tbody>
                    <tr><td>10-50 Wohnungen</td><td>10%</td></tr>
                    <tr><td>51-100 Wohnungen</td><td>15%</td></tr>
                    <tr><td>100+ Wohnungen</td><td>Individuell</td></tr>
                </tbody>
            </table>
        </div>
        
        <div class="cta-box">
            <h3>Kostenlose Erstberatung für Vermieter</h3>
            <p>Lassen Sie uns über Ihre Anforderungen sprechen.</p>
            <a href="kontakt.html" class="btn" style="background: white; color: var(--primary);">Termin vereinbaren</a>
        </div>
'''
    },
    
    "montage-anleitung.html": {
        "title": "Rauchmelder Montage-Anleitung | Schritt für Schritt | Secu.li",
        "desc": "So montieren Sie Rauchmelder richtig: Anleitung mit Tipps vom Profi.",
        "h1": "Montage-Anleitung",
        "badge": "🔧 DIY",
        "content": '''
        <h2>Was Sie brauchen</h2>
        <div class="feature-cards">
            <div class="feature-card-pro">
                <div class="icon">🔧</div>
                <h4>Bohrmaschine</h4>
                <p>Mit 6mm Bohrer</p>
            </div>
            <div class="feature-card-pro">
                <div class="icon">🔩</div>
                <h4>Dübel & Schrauben</h4>
                <p>Meist im Lieferumfang</p>
            </div>
            <div class="feature-card-pro">
                <div class="icon">✏️</div>
                <h4>Bleistift</h4>
                <p>Zum Anzeichnen</p>
            </div>
            <div class="feature-card-pro">
                <div class="icon">🪜</div>
                <h4>Leiter</h4>
                <p>Oder Tritthocker</p>
            </div>
        </div>
        
        <h2>Schritt-für-Schritt</h2>
        <ul class="check-list">
            <li><strong>Schritt 1:</strong> Position bestimmen (Mitte des Raumes, 50cm von Wänden)</li>
            <li><strong>Schritt 2:</strong> Halterung an die Decke halten, Bohrlöcher anzeichnen</li>
            <li><strong>Schritt 3:</strong> Löcher bohren (6mm), Dübel einsetzen</li>
            <li><strong>Schritt 4:</strong> Halterung festschrauben</li>
            <li><strong>Schritt 5:</strong> Rauchmelder eindrehen bis er einrastet</li>
            <li><strong>Schritt 6:</strong> Testtaste 3-5 Sekunden drücken</li>
        </ul>
        
        <h2>Häufige Fehler</h2>
        <ul class="check-list cross-list">
            <li>Montage in der Nähe von Lüftungsöffnungen</li>
            <li>Montage an Dachschrägen über 45°</li>
            <li>Übermalen des Rauchmelders</li>
            <li>Montage in staubigen Räumen</li>
        </ul>
        
        <div class="cta-box">
            <h3>Keine Lust auf DIY?</h3>
            <p>Wir übernehmen die fachgerechte Montage für Sie.</p>
            <a href="kontakt.html" class="btn" style="background: white; color: var(--primary);">Montage anfragen</a>
        </div>
'''
    },
    
    "rauchmelder-vergleich.html": {
        "title": "Rauchmelder Vergleich | Die besten Modelle | Secu.li",
        "desc": "Die besten Rauchmelder im direkten Vergleich: Ei650, Hekatron, Jung.",
        "h1": "Rauchmelder Vergleich",
        "badge": "🏆 Test",
        "content": '''
        <div class="table-container">
            <table class="pro-table">
                <thead>
                    <tr>
                        <th>Modell</th>
                        <th>Ei650</th>
                        <th>Hekatron Genius</th>
                        <th>Jung Basic</th>
                    </tr>
                </thead>
                <tbody>
                    <tr><td><strong>Preis</strong></td><td>~25€</td><td>~30€</td><td>~20€</td></tr>
                    <tr><td><strong>Q-Label</strong></td><td>✓ Ja</td><td>✓ Ja</td><td>✓ Ja</td></tr>
                    <tr><td><strong>Batterie</strong></td><td>10 Jahre</td><td>10 Jahre</td><td>10 Jahre</td></tr>
                    <tr><td><strong>Vernetzbar</strong></td><td>Optional</td><td>Optional</td><td>Nein</td></tr>
                    <tr><td><strong>Besonderheit</strong></td><td>Testsieger</td><td>Made in Germany</td><td>Preis-Leistung</td></tr>
                    <tr><td><strong>Bewertung</strong></td><td>⭐⭐⭐⭐⭐</td><td>⭐⭐⭐⭐⭐</td><td>⭐⭐⭐⭐</td></tr>
                </tbody>
            </table>
        </div>
        
        <h2>Unsere Empfehlung</h2>
        <div class="info-box">
            <h3>Ei Electronics Ei650</h3>
            <ul class="check-list" style="background: transparent; padding: 0;">
                <li>Mehrfacher Testsieger bei Stiftung Warentest</li>
                <li>10 Jahre Herstellergarantie</li>
                <li>Sehr geringe Fehlalarmrate</li>
                <li>Einfache Montage</li>
            </ul>
        </div>
        
        <div class="cta-box">
            <h3>Lassen Sie sich beraten</h3>
            <p>Wir helfen Ihnen, den richtigen Rauchmelder zu finden.</p>
            <a href="kontakt.html" class="btn" style="background: white; color: var(--primary);">Kostenlose Beratung</a>
        </div>
'''
    }
}

def main():
    print("Aktualisiere alle Content-Seiten mit professionellem Design...")
    for filename, data in pages.items():
        filepath = BASE_DIR / filename
        html = get_pro_page(data['title'], data['desc'], data['h1'], data['badge'], data['content'])
        filepath.write_text(html, encoding='utf-8')
        print(f"✓ {filename}")
    print(f"\n✅ {len(pages)} Seiten mit professionellem Design aktualisiert!")

if __name__ == "__main__":
    main()
