#!/usr/bin/env python3
"""
Script zum Aktualisieren des Footers auf allen Hauptseiten.
Ersetzt den einfachen Footer mit dem professionellen 3-Spalten-Footer.
"""

import os
import re

# Professioneller Footer HTML
PROFESSIONAL_FOOTER = '''    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-brand">
                    <a href="index.html" class="logo" style="color: var(--white); margin-bottom: 1rem;">
                        <span>Secu.li</span>
                    </a>
                    <p>Ihr europäischer Partner für Brandschutz und Sicherheit. Qualität und Zuverlässigkeit seit über 15 Jahren.</p>
                </div>
                <div>
                    <h4>Service</h4>
                    <ul class="footer-links">
                        <li><a href="installation.html">Installation</a></li>
                        <li><a href="wartung.html">Wartung</a></li>
                        <li><a href="b2b.html">B2B-Lösungen</a></li>
                        <li><a href="support.html">Support</a></li>
                    </ul>
                </div>
                <div>
                    <h4>Kontakt</h4>
                    <ul class="footer-links">
                        <li>📞 +49 157 78631120</li>
                        <li>✉️ info@secu.li</li>
                        <li><a href="https://wa.me/4915778631120">💬 WhatsApp</a></li>
                        <li><a href="kontakt.html">Kontaktformular</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>© 2024 Secu.li. Alle Rechte vorbehalten.</p>
                <div class="footer-bottom-links">
                    <a href="impressum.html">Impressum</a>
                    <a href="datenschutz.html">Datenschutz</a>
                </div>
            </div>
        </div>
    </footer>'''

# Pattern für den einfachen Footer
SIMPLE_FOOTER_PATTERN = re.compile(
    r'<footer class="footer">\s*<div class="container">\s*<div class="footer-simple"[^>]*>.*?</div>\s*</div>\s*</footer>',
    re.DOTALL
)

# Hauptseiten die aktualisiert werden sollen (außer index.html)
MAIN_PAGES = [
    'service.html',
    'kontakt.html',
    'support.html',
    'wartung.html',
    'installation.html',
    'produkte.html',
    'faq.html',
    'ratgeber.html',
    'hausverwaltung.html',
    'wohnbaugesellschaft.html',
    'gewerbeimmobilien.html',
    'facility-management.html',
    'hotel-gastgewerbe.html',
    'funkrauchmelder.html',
    'optische-rauchmelder.html',
    'ionisationsmelder.html',
    'thermomelder.html',
    'privat-anfrage.html',
    'gewerbe-anfrage.html',
    'vermieter.html',
]

def update_footer(filepath):
    """Aktualisiere den Footer in einer HTML-Datei."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Prüfe ob einfacher Footer vorhanden
        if SIMPLE_FOOTER_PATTERN.search(content):
            new_content = SIMPLE_FOOTER_PATTERN.sub(PROFESSIONAL_FOOTER, content)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✅ {os.path.basename(filepath)}: Footer aktualisiert")
            return True
        else:
            print(f"⏭️  {os.path.basename(filepath)}: Kein einfacher Footer gefunden")
            return False
    except Exception as e:
        print(f"❌ {os.path.basename(filepath)}: Fehler - {e}")
        return False

def main():
    updated = 0
    skipped = 0
    
    for page in MAIN_PAGES:
        if os.path.exists(page):
            if update_footer(page):
                updated += 1
            else:
                skipped += 1
        else:
            print(f"⚠️  {page}: Datei nicht gefunden")
    
    print(f"\n📊 Ergebnis: {updated} aktualisiert, {skipped} übersprungen")

if __name__ == "__main__":
    main()
