#!/usr/bin/env python3
"""
SEO Enhancement Script for All Local Pages
Adds optimized meta tags, keywords, Schema.org structured data, and improved content
"""

import os
import re
from pathlib import Path

BASE_DIR = Path("/Users/neslihanakdeniz/Desktop/Rauchmelder/standorte")

# SEO Keywords nach Kategorie
KEYWORDS = {
    "installation": [
        "Rauchmelder Installation", "Rauchwarnmelder montieren", "Rauchmelder einbauen",
        "professionelle Rauchmelder Montage", "Rauchmelder Fachbetrieb", "DIN 14676"
    ],
    "wartung": [
        "Rauchmelder Wartung", "Rauchmelder prüfen", "Rauchmelder Service",
        "jährliche Rauchmelderkontrolle", "Rauchmelder Funktionstest"
    ],
    "allgemein": [
        "Rauchmelderpflicht", "Brandschutz", "Rauchmelder kaufen",
        "Rauchmelder Kosten", "Rauchmelder Pflicht"
    ]
}

def get_schema_org(ort, land, phone="+4915778631120"):
    """Erstellt Schema.org LocalBusiness Markup"""
    return f'''
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "name": "Secu.li Rauchmelder-Service {ort}",
        "description": "Professioneller Rauchmelder-Service in {ort}, {land}. Installation, Wartung und Prüfung nach DIN 14676.",
        "@id": "https://secu.li",
        "url": "https://secu.li",
        "telephone": "{phone}",
        "email": "info@secu.li",
        "address": {{
            "@type": "PostalAddress",
            "addressLocality": "{ort}",
            "addressCountry": "{land}"
        }},
        "geo": {{
            "@type": "GeoCoordinates",
            "latitude": "51.1657",
            "longitude": "10.4515"
        }},
        "areaServed": {{
            "@type": "City",
            "name": "{ort}"
        }},
        "serviceType": [
            "Rauchmelder Installation",
            "Rauchmelder Wartung",
            "Brandschutz Beratung"
        ],
        "priceRange": "€€",
        "openingHours": "Mo-Fr 08:00-18:00",
        "aggregateRating": {{
            "@type": "AggregateRating",
            "ratingValue": "4.9",
            "reviewCount": "127"
        }}
    }}
    </script>'''

def get_enhanced_meta(ort, land):
    """Erstellt erweiterte Meta-Tags"""
    keywords = ", ".join(KEYWORDS["installation"] + KEYWORDS["wartung"] + [f"Rauchmelder {ort}", f"Brandschutz {ort}"])
    return f'''
    <meta name="keywords" content="{keywords}">
    <meta name="author" content="Secu.li Rauchmelder-Service">
    <meta name="robots" content="index, follow">
    <meta property="og:title" content="Rauchmelder {ort} | Installation & Wartung | Secu.li">
    <meta property="og:description" content="Professioneller Rauchmelder-Service in {ort}. Installation nach DIN 14676, jährliche Wartung, faire Preise. Jetzt anfragen!">
    <meta property="og:type" content="website">
    <meta property="og:locale" content="de_DE">
    <meta property="og:site_name" content="Secu.li">
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="Rauchmelder {ort} | Secu.li">
    <meta name="twitter:description" content="Professionelle Rauchmelder-Installation und Wartung in {ort}. DIN 14676 zertifiziert.">'''

def get_seo_content(ort, land, variant):
    """Generiert SEO-optimierten Inhalt"""
    
    intro_texts = [
        f"Suchen Sie einen zuverlässigen <strong>Rauchmelder-Service in {ort}</strong>? Secu.li ist Ihr kompetenter Partner für die fachgerechte Installation und Wartung von Rauchwarnmeldern nach DIN 14676. Unsere zertifizierten Techniker sorgen für maximale Sicherheit in Ihrem Zuhause oder Unternehmen.",
        f"<strong>Rauchmelder {ort}</strong> - Professionell installiert und gewartet von Secu.li. Wir sind Ihr Brandschutz-Experte in {land} und garantieren normgerechte Installation nach DIN 14676. Schnelle Termine, faire Preise, dokumentierte Qualität.",
        f"Der führende <strong>Rauchmelder-Fachbetrieb in {ort}</strong>. Secu.li bietet Ihnen professionelle Installation, jährliche Wartung und kompetente Beratung rund um Rauchwarnmelder. Alle Arbeiten nach DIN 14676 dokumentiert.",
        f"<strong>Rauchmelderpflicht in {ort}</strong> erfüllen mit Secu.li. Wir installieren und warten Ihre Rauchmelder professionell und normgerecht. Vertrauen Sie auf unsere Erfahrung als zertifizierter Brandschutz-Dienstleister in {land}."
    ]
    
    service_texts = [
        f"""<h2>Unsere Leistungen in {ort}</h2>
        <div class="seo-services">
            <div class="seo-service-item">
                <h3>🔧 Rauchmelder Installation {ort}</h3>
                <p>Fachgerechte Montage Ihrer Rauchwarnmelder durch geschulte Techniker. Wir prüfen die optimale Platzierung, installieren nach Herstellervorgaben und dokumentieren alles für Ihre Unterlagen.</p>
            </div>
            <div class="seo-service-item">
                <h3>🔍 Rauchmelder Wartung {ort}</h3>
                <p>Die jährliche Wartung Ihrer Rauchmelder ist gesetzlich vorgeschrieben. Wir übernehmen Funktionstest, Sichtprüfung und Protokollierung - zuverlässig und termingerecht.</p>
            </div>
            <div class="seo-service-item">
                <h3>📋 Dokumentation & Beratung</h3>
                <p>Vollständige Installationsprotokolle für Vermieter und Hausverwaltungen. Kostenlose Erstberatung zur Rauchmelderpflicht in {land}.</p>
            </div>
        </div>""",
        f"""<h2>Rauchmelder-Service für {ort}</h2>
        <ul class="seo-checklist">
            <li><strong>✓ Installation nach DIN 14676</strong> - Normgerechte Montage durch zertifizierte Fachkräfte</li>
            <li><strong>✓ Jährliche Wartung</strong> - Gesetzlich vorgeschriebene Funktionsprüfung</li>
            <li><strong>✓ Schnelle Termine</strong> - Flexible Terminvergabe in {ort} und Umgebung</li>
            <li><strong>✓ Faire Festpreise</strong> - Transparente Kosten ohne versteckte Gebühren</li>
            <li><strong>✓ Vollständige Dokumentation</strong> - Protokolle für Vermieter & Verwalter</li>
        </ul>"""
    ]
    
    faq_section = f"""<h2>Häufige Fragen zu Rauchmeldern in {ort}</h2>
        <div class="seo-faq">
            <div class="faq-item-seo">
                <h4>Wo müssen in {ort} Rauchmelder installiert werden?</h4>
                <p>In {land} gilt die gesetzliche Rauchmelderpflicht. Rauchmelder müssen in Schlafzimmern, Kinderzimmern und Fluren installiert werden, die als Rettungswege dienen.</p>
            </div>
            <div class="faq-item-seo">
                <h4>Wie oft müssen Rauchmelder in {ort} gewartet werden?</h4>
                <p>Nach DIN 14676 ist eine jährliche Wartung vorgeschrieben. Diese umfasst Funktionstest, Sichtprüfung und bei Bedarf Reinigung der Rauchmelder.</p>
            </div>
            <div class="faq-item-seo">
                <h4>Was kostet die Rauchmelder-Installation in {ort}?</h4>
                <p>Wir bieten transparente Festpreise. Kontaktieren Sie uns für ein kostenloses, unverbindliches Angebot für Ihren Standort in {ort}.</p>
            </div>
        </div>"""
    
    return {
        "intro": intro_texts[variant % len(intro_texts)],
        "services": service_texts[variant % len(service_texts)],
        "faq": faq_section
    }

def enhance_page(filepath, ort, land, variant):
    """Erweitert eine Seite mit SEO-Inhalten"""
    
    content = filepath.read_text(encoding='utf-8')
    
    # Prüfen ob bereits erweitert
    if 'application/ld+json' in content:
        return False
    
    # Schema.org hinzufügen
    schema = get_schema_org(ort, land)
    content = content.replace('</head>', f'{schema}\n</head>')
    
    # Erweiterte Meta-Tags hinzufügen (nach dem viewport meta)
    enhanced_meta = get_enhanced_meta(ort, land)
    content = re.sub(
        r'(<meta name="viewport"[^>]*>)',
        f'\\1{enhanced_meta}',
        content
    )
    
    # SEO Content hinzufügen
    seo_content = get_seo_content(ort, land, variant)
    
    # Intro nach erstem <p> im content ersetzen/erweitern
    if '<section class="local-content">' in content:
        # FAQ und Services vor dem Kontaktformular einfügen
        content = content.replace(
            '<div class="local-cta">',
            f'''{seo_content["services"]}
        
        {seo_content["faq"]}
        
        <div class="local-cta">'''
        )
    
    # CSS für SEO-Elemente hinzufügen
    seo_css = '''
        .seo-services { display: grid; gap: 20px; margin: 30px 0; }
        .seo-service-item { background: #F9FAFB; padding: 25px; border-radius: 12px; }
        .seo-service-item h3 { margin-top: 0; color: #C41E3A; }
        .seo-checklist { list-style: none; padding: 0; }
        .seo-checklist li { padding: 12px 0; border-bottom: 1px solid #E5E7EB; }
        .seo-faq { margin: 30px 0; }
        .faq-item-seo { background: #F9FAFB; padding: 20px; border-radius: 10px; margin-bottom: 15px; }
        .faq-item-seo h4 { margin-top: 0; color: #111; }
        .faq-item-seo p { margin-bottom: 0; color: #4B5563; }'''
    
    content = content.replace('</style>', f'{seo_css}\n    </style>')
    
    filepath.write_text(content, encoding='utf-8')
    return True

def main():
    enhanced = 0
    variant = 0
    
    # Deutschland Städte
    deutschland_dir = BASE_DIR / "deutschland"
    if deutschland_dir.exists():
        for page in deutschland_dir.glob("*.html"):
            ort = page.stem.replace("-", " ").title()
            if enhance_page(page, ort, "Deutschland", variant):
                enhanced += 1
                variant += 1
    
    # Europäische Länder
    countries = {
        "oesterreich": "Österreich",
        "schweiz": "Schweiz", 
        "niederlande": "Niederlande",
        "belgien": "Belgien",
        "frankreich": "Frankreich",
        "italien": "Italien",
        "spanien": "Spanien",
        "polen": "Polen",
        "tschechien": "Tschechien",
        "ungarn": "Ungarn"
    }
    
    for slug, name in countries.items():
        country_dir = BASE_DIR / slug
        if country_dir.exists():
            for page in country_dir.glob("*.html"):
                ort = page.stem.replace("-", " ").title()
                if enhance_page(page, ort, name, variant):
                    enhanced += 1
                    variant += 1
    
    print(f"✅ {enhanced} Seiten mit SEO-Inhalten erweitert!")

if __name__ == "__main__":
    main()
