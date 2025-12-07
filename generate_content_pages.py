#!/usr/bin/env python3
"""
Erstellt 15 neue Content-Seiten für Secu.li
"""

from pathlib import Path

BASE_DIR = Path("/Users/neslihanakdeniz/Desktop/Rauchmelder")

def get_header():
    return '''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css">
    <meta name="theme-color" content="#C41E3A">
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
'''

def get_footer():
    return '''
    <footer class="footer">
        <div class="container" style="text-align: center; padding: 30px;">
            <p>&copy; 2024 Secu.li - Rauchmelder Service</p>
            <a href="impressum.html">Impressum</a> | <a href="datenschutz.html">Datenschutz</a>
        </div>
    </footer>
    <script src="script.js"></script>
</body>
</html>'''

pages = {
    "rauchmelderpflicht.html": {
        "title": "Rauchmelderpflicht in Deutschland | Gesetzliche Regelungen | Secu.li",
        "desc": "Alle Infos zur Rauchmelderpflicht: Welche Gesetze gelten in Ihrem Bundesland? Wer ist verantwortlich? Was droht bei Verstößen?",
        "h1": "Rauchmelderpflicht in Deutschland",
        "content": '''
        <section class="section" style="padding-top: 120px;">
            <div class="container" style="max-width: 900px;">
                <h1>Rauchmelderpflicht in Deutschland</h1>
                <p class="subtitle">Alle 16 Bundesländer haben die Rauchmelderpflicht eingeführt. Erfahren Sie alles über die gesetzlichen Regelungen.</p>
                
                <h2>Wer ist verantwortlich?</h2>
                <ul>
                    <li><strong>Eigentümer:</strong> Installation der Rauchmelder</li>
                    <li><strong>Mieter/Eigentümer:</strong> Wartung (je nach Bundesland)</li>
                </ul>
                
                <h2>Wo müssen Rauchmelder installiert werden?</h2>
                <ul>
                    <li>✓ Schlafzimmer</li>
                    <li>✓ Kinderzimmer</li>
                    <li>✓ Flure (Rettungswege)</li>
                    <li>○ Wohnzimmer (empfohlen)</li>
                </ul>
                
                <h2>Übersicht nach Bundesland</h2>
                <table class="service-table">
                    <thead><tr><th>Bundesland</th><th>Pflicht seit</th><th>Wartung</th></tr></thead>
                    <tbody>
                        <tr><td>Baden-Württemberg</td><td>2015</td><td>Eigentümer/Mieter</td></tr>
                        <tr><td>Bayern</td><td>2018</td><td>Eigentümer</td></tr>
                        <tr><td>Berlin</td><td>2017</td><td>Eigentümer/Mieter</td></tr>
                        <tr><td>Brandenburg</td><td>2020</td><td>Eigentümer</td></tr>
                        <tr><td>Bremen</td><td>2015</td><td>Mieter</td></tr>
                        <tr><td>Hamburg</td><td>2011</td><td>Eigentümer</td></tr>
                        <tr><td>Hessen</td><td>2015</td><td>Eigentümer</td></tr>
                        <tr><td>Mecklenburg-Vorpommern</td><td>2009</td><td>Eigentümer</td></tr>
                        <tr><td>Niedersachsen</td><td>2015</td><td>Mieter</td></tr>
                        <tr><td>Nordrhein-Westfalen</td><td>2017</td><td>Eigentümer</td></tr>
                        <tr><td>Rheinland-Pfalz</td><td>2012</td><td>Eigentümer</td></tr>
                        <tr><td>Saarland</td><td>2009</td><td>Eigentümer</td></tr>
                        <tr><td>Sachsen</td><td>2016</td><td>Eigentümer</td></tr>
                        <tr><td>Sachsen-Anhalt</td><td>2016</td><td>Eigentümer</td></tr>
                        <tr><td>Schleswig-Holstein</td><td>2011</td><td>Mieter</td></tr>
                        <tr><td>Thüringen</td><td>2019</td><td>Eigentümer</td></tr>
                    </tbody>
                </table>
                
                <h2>Konsequenzen bei Verstoß</h2>
                <p>Bei fehlenden Rauchmeldern drohen:</p>
                <ul>
                    <li>❌ Bußgelder bis zu 50.000 €</li>
                    <li>❌ Versicherungsausfall im Brandfall</li>
                    <li>❌ Strafrechtliche Konsequenzen bei Personenschäden</li>
                </ul>
                
                <div style="background: #FEF2F2; padding: 30px; border-radius: 15px; margin-top: 40px; text-align: center;">
                    <h3>Jetzt gesetzeskonform werden</h3>
                    <p>Wir installieren und warten Ihre Rauchmelder nach DIN 14676.</p>
                    <a href="kontakt.html" class="btn btn-primary">Kostenlose Beratung</a>
                </div>
            </div>
        </section>
'''
    },
    
    "ratgeber.html": {
        "title": "Rauchmelder Ratgeber & Wissen | Secu.li",
        "desc": "Alles was Sie über Rauchmelder wissen müssen: Funktionsweise, Typen, Kauftipps und Wartung.",
        "h1": "Rauchmelder Ratgeber",
        "content": '''
        <section class="section" style="padding-top: 120px;">
            <div class="container" style="max-width: 900px;">
                <h1>Rauchmelder Ratgeber & Wissen</h1>
                <p class="subtitle">Ihr umfassender Guide zu Rauchmeldern - von der Auswahl bis zur Wartung.</p>
                
                <h2>Wie funktioniert ein Rauchmelder?</h2>
                <p>Rauchmelder erkennen Rauchpartikel in der Luft. Die meisten Geräte nutzen das <strong>optische Streulichtverfahren</strong>: Eine LED sendet Licht aus, das bei Rauch auf einen Sensor reflektiert wird und den Alarm auslöst.</p>
                
                <h2>Arten von Rauchmeldern</h2>
                <div class="features-grid">
                    <div class="feature-card">
                        <h4>Optische Rauchmelder</h4>
                        <p>Am häufigsten, reagieren auf sichtbaren Rauch. Ideal für Wohnräume.</p>
                    </div>
                    <div class="feature-card">
                        <h4>Ionisationsmelder</h4>
                        <p>Reagieren auf unsichtbare Rauchpartikel. In Deutschland selten wegen radioaktiver Quelle.</p>
                    </div>
                    <div class="feature-card">
                        <h4>Thermomelder</h4>
                        <p>Reagieren auf Hitze statt Rauch. Ideal für Küche und Bad.</p>
                    </div>
                    <div class="feature-card">
                        <h4>Funkvernetzte Melder</h4>
                        <p>Kommunizieren untereinander - wenn einer auslöst, alarmieren alle.</p>
                    </div>
                </div>
                
                <h2>Kauftipps</h2>
                <ul>
                    <li>✓ Achten Sie auf das <strong>Q-Label</strong> für hochwertige Geräte</li>
                    <li>✓ Mindestlebensdauer: <strong>10 Jahre</strong></li>
                    <li>✓ Prüfzeichen: <strong>CE + EN 14604</strong></li>
                    <li>✓ Testtaste und Stummschaltung sollten vorhanden sein</li>
                </ul>
                
                <h2>Platzierung</h2>
                <p>Rauchmelder gehören:</p>
                <ul>
                    <li>🏠 Mittig an die Decke</li>
                    <li>📏 Mindestens 50cm von Wänden entfernt</li>
                    <li>🚪 Nicht in Küche/Bad (außer Thermomelder)</li>
                    <li>📐 Maximal 60m² pro Melder</li>
                </ul>
            </div>
        </section>
'''
    },
    
    "montage-anleitung.html": {
        "title": "Rauchmelder Montage-Anleitung | Schritt für Schritt | Secu.li",
        "desc": "So montieren Sie Rauchmelder richtig: Schritt-für-Schritt Anleitung mit Bildern und Tipps vom Profi.",
        "h1": "Montage-Anleitung",
        "content": '''
        <section class="section" style="padding-top: 120px;">
            <div class="container" style="max-width: 900px;">
                <h1>Rauchmelder Montage-Anleitung</h1>
                <p class="subtitle">Schritt für Schritt zur sicheren Montage nach DIN 14676.</p>
                
                <h2>Was Sie brauchen</h2>
                <ul>
                    <li>🔧 Bohrmaschine mit 6mm Bohrer</li>
                    <li>🔩 Dübel und Schrauben (meist im Lieferumfang)</li>
                    <li>📏 Bleistift zum Anzeichnen</li>
                    <li>🪜 Leiter oder Tritthocker</li>
                </ul>
                
                <h2>Schritt 1: Position bestimmen</h2>
                <p>Wählen Sie die Mitte des Raumes. Mindestabstand zu Wänden: 50cm, zu Lampen: 50cm.</p>
                
                <h2>Schritt 2: Halterung befestigen</h2>
                <ol>
                    <li>Halterung an die Decke halten</li>
                    <li>Bohrlöcher anzeichnen</li>
                    <li>Löcher bohren (6mm)</li>
                    <li>Dübel einsetzen</li>
                    <li>Halterung festschrauben</li>
                </ol>
                
                <h2>Schritt 3: Rauchmelder einsetzen</h2>
                <p>Drehen Sie den Rauchmelder im Uhrzeigersinn in die Halterung bis er einrastet.</p>
                
                <h2>Schritt 4: Funktionstest</h2>
                <p>Drücken Sie die Testtaste für 3-5 Sekunden. Der Alarm sollte ertönen.</p>
                
                <div style="background: #F0FDF4; padding: 30px; border-radius: 15px; margin-top: 40px;">
                    <h3>💡 Profi-Tipp</h3>
                    <p>Klebebefestigung ist möglich, aber weniger sicher. Bei Mietwohnungen vorher den Vermieter fragen.</p>
                </div>
                
                <h2>Häufige Fehler</h2>
                <ul>
                    <li>❌ Montage in der Nähe von Lüftungsöffnungen</li>
                    <li>❌ Montage an Dachschrägen über 45°</li>
                    <li>❌ Übermalen des Rauchmelders</li>
                    <li>❌ Montage in staubigen Räumen</li>
                </ul>
                
                <div style="text-align: center; margin-top: 40px;">
                    <p>Keine Lust auf DIY?</p>
                    <a href="kontakt.html" class="btn btn-primary">Professionelle Montage anfragen</a>
                </div>
            </div>
        </section>
'''
    },
    
    "privatkunden.html": {
        "title": "Rauchmelder für Privatkunden | Ihr Zuhause sicher machen | Secu.li",
        "desc": "Rauchmelder-Service für Privatkunden: Beratung, Installation und Wartung für Ihr Zuhause.",
        "h1": "Für Privatkunden",
        "content": '''
        <section class="section" style="padding-top: 120px;">
            <div class="container" style="max-width: 900px;">
                <h1>Rauchmelder für Privatkunden</h1>
                <p class="subtitle">Schützen Sie Ihr Zuhause und Ihre Familie mit professionellen Rauchmeldern.</p>
                
                <h2>Unser Service für Sie</h2>
                <div class="features-grid">
                    <div class="feature-card">
                        <div class="feature-icon">🏠</div>
                        <h4>Einfamilienhaus</h4>
                        <p>Komplette Ausstattung mit 3-10 Meldern je nach Größe.</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-icon">🏢</div>
                        <h4>Eigentumswohnung</h4>
                        <p>Individuelle Lösung für Ihre Wohnung, auch bei Vermietung.</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-icon">👴</div>
                        <h4>Seniorenhaushalte</h4>
                        <p>Spezielle Melder mit extra lautem Alarm.</p>
                    </div>
                </div>
                
                <h2>Warum professionelle Installation?</h2>
                <ul>
                    <li>✓ Garantiert richtige Platzierung</li>
                    <li>✓ Hochwertige, geprüfte Melder</li>
                    <li>✓ 10 Jahre Garantie</li>
                    <li>✓ Dokumentation für Versicherung</li>
                    <li>✓ Jährliche Wartungserinnerung</li>
                </ul>
                
                <h2>Unsere Pakete</h2>
                <table class="service-table">
                    <thead><tr><th>Paket</th><th>Inhalt</th><th>Ideal für</th></tr></thead>
                    <tbody>
                        <tr><td>Starter</td><td>3 Rauchmelder + Installation</td><td>Kleine Wohnung</td></tr>
                        <tr><td>Standard</td><td>5 Rauchmelder + Installation</td><td>3-4 Zimmer Wohnung</td></tr>
                        <tr><td>Komplett</td><td>8 Rauchmelder + Installation</td><td>Einfamilienhaus</td></tr>
                    </tbody>
                </table>
                
                <div style="background: #FEF2F2; padding: 30px; border-radius: 15px; margin-top: 40px; text-align: center;">
                    <h3>Kostenloses Angebot</h3>
                    <p>Wir beraten Sie unverbindlich und erstellen ein individuelles Angebot.</p>
                    <a href="kontakt.html" class="btn btn-primary">Jetzt anfragen</a>
                </div>
            </div>
        </section>
'''
    },
    
    "vermieter.html": {
        "title": "Rauchmelder für Vermieter & Hausverwaltungen | Secu.li",
        "desc": "Professioneller Rauchmelder-Service für Vermieter: Installation, Wartung und rechtssichere Dokumentation.",
        "h1": "Für Vermieter & Hausverwaltungen",
        "content": '''
        <section class="section" style="padding-top: 120px;">
            <div class="container" style="max-width: 900px;">
                <h1>Für Vermieter & Hausverwaltungen</h1>
                <p class="subtitle">Erfüllen Sie Ihre gesetzliche Pflicht - wir kümmern uns um alles.</p>
                
                <h2>Ihre Pflichten als Vermieter</h2>
                <ul>
                    <li>📋 Installation von Rauchmeldern in allen Schlaf- und Kinderzimmern sowie Fluren</li>
                    <li>🔧 Regelmäßige Wartung (je nach Bundesland)</li>
                    <li>📄 Dokumentation für Versicherung und Nachweis</li>
                </ul>
                
                <h2>Unser Komplett-Service</h2>
                <div class="features-grid">
                    <div class="feature-card">
                        <div class="feature-icon">🏗️</div>
                        <h4>Erstinstallation</h4>
                        <p>Fachgerechte Montage nach DIN 14676 in allen Einheiten.</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-icon">🔍</div>
                        <h4>Jährliche Wartung</h4>
                        <p>Funktionsprüfung, Batterietest, Reinigung - alles inklusive.</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-icon">📄</div>
                        <h4>Dokumentation</h4>
                        <p>Rechtssichere Protokolle für jede Wohneinheit.</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-icon">🔔</div>
                        <h4>Erinnerungsservice</h4>
                        <p>Wir erinnern Sie automatisch an anstehende Termine.</p>
                    </div>
                </div>
                
                <h2>Mengenrabatte</h2>
                <table class="service-table">
                    <thead><tr><th>Anzahl Einheiten</th><th>Rabatt</th></tr></thead>
                    <tbody>
                        <tr><td>10-50 Wohnungen</td><td>10%</td></tr>
                        <tr><td>51-100 Wohnungen</td><td>15%</td></tr>
                        <tr><td>100+ Wohnungen</td><td>Individuelle Vereinbarung</td></tr>
                    </tbody>
                </table>
                
                <div style="background: var(--charcoal); color: white; padding: 30px; border-radius: 15px; margin-top: 40px; text-align: center;">
                    <h3>Kostenlose Erstberatung für Vermieter</h3>
                    <p>Lassen Sie uns über Ihre Anforderungen sprechen.</p>
                    <a href="kontakt.html" class="btn btn-primary">Termin vereinbaren</a>
                </div>
            </div>
        </section>
'''
    },
    
    "notfall.html": {
        "title": "Notfall & Verhalten im Brandfall | Lebensrettende Tipps | Secu.li",
        "desc": "Was tun wenn der Rauchmelder Alarm gibt? Lebensrettende Verhaltensregeln im Brandfall.",
        "h1": "Notfall & Verhalten im Brandfall",
        "content": '''
        <section class="section" style="padding-top: 120px;">
            <div class="container" style="max-width: 900px;">
                <h1>Notfall & Verhalten im Brandfall</h1>
                <p class="subtitle">Diese Tipps können Leben retten - lesen und teilen Sie sie mit Ihrer Familie.</p>
                
                <div style="background: #DC2626; color: white; padding: 30px; border-radius: 15px; margin-bottom: 30px;">
                    <h2 style="color: white;">🚨 Notruf: 112</h2>
                    <p>Feuerwehr und Rettungsdienst europaweit - kostenlos, 24/7</p>
                </div>
                
                <h2>Wenn der Rauchmelder Alarm gibt</h2>
                <ol>
                    <li><strong>Ruhe bewahren</strong> - Panik führt zu Fehlern</li>
                    <li><strong>Tür prüfen</strong> - Ist sie heiß? Nicht öffnen!</li>
                    <li><strong>Gebückt gehen</strong> - Rauch steigt nach oben</li>
                    <li><strong>Fluchtweg nutzen</strong> - Niemals den Aufzug!</li>
                    <li><strong>Notruf wählen</strong> - 112 anrufen</li>
                </ol>
                
                <h2>Wichtige Verhaltensregeln</h2>
                <div class="features-grid">
                    <div class="feature-card">
                        <div class="feature-icon">🚪</div>
                        <h4>Türen schließen</h4>
                        <p>Geschlossene Türen halten Feuer und Rauch auf.</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-icon">🪟</div>
                        <h4>Fenster nicht öffnen</h4>
                        <p>Sauerstoff facht das Feuer an.</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-icon">🧒</div>
                        <h4>Kinder zuerst</h4>
                        <p>Helfen Sie zuerst Kindern und hilfsbedürftigen Personen.</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-icon">🏃</div>
                        <h4>Nicht zurückgehen</h4>
                        <p>Niemals zurück ins Gebäude für Wertsachen.</p>
                    </div>
                </div>
                
                <h2>Wenn Sie nicht flüchten können</h2>
                <ul>
                    <li>Fenster öffnen und um Hilfe rufen</li>
                    <li>Tür mit nassen Tüchern abdichten</li>
                    <li>Am Boden bleiben (weniger Rauch)</li>
                    <li>Auf Rettung warten</li>
                </ul>
                
                <div style="background: #FEF2F2; padding: 30px; border-radius: 15px; margin-top: 40px;">
                    <h3>💡 Vorsorge ist besser</h3>
                    <p>Funktionierende Rauchmelder geben Ihnen wertvolle Zeit zur Flucht. Lassen Sie Ihre Melder regelmäßig warten.</p>
                    <a href="wartung.html" class="btn btn-primary">Mehr zur Wartung</a>
                </div>
            </div>
        </section>
'''
    },
    
    "zertifikate.html": {
        "title": "Rauchmelder Zertifikate erklärt | Q-Label, EN 14604, CE, TÜV | Secu.li",
        "desc": "Was bedeuten Q-Label, EN 14604, CE und TÜV bei Rauchmeldern? Wir erklären alle wichtigen Prüfzeichen.",
        "h1": "Zertifikate erklärt",
        "content": '''
        <section class="section" style="padding-top: 120px;">
            <div class="container" style="max-width: 900px;">
                <h1>Rauchmelder Zertifikate erklärt</h1>
                <p class="subtitle">Was bedeuten die verschiedenen Prüfzeichen und warum sind sie wichtig?</p>
                
                <h2>CE-Kennzeichnung</h2>
                <div style="display: flex; gap: 20px; align-items: start; margin-bottom: 30px;">
                    <div style="background: white; border: 2px solid #1a1a1a; padding: 20px; border-radius: 10px; font-weight: bold; font-size: 1.5rem;">CE</div>
                    <div>
                        <p><strong>Pflicht für den EU-Markt.</strong> Zeigt an, dass das Produkt den grundlegenden europäischen Sicherheitsanforderungen entspricht. Allein keine Qualitätsgarantie!</p>
                    </div>
                </div>
                
                <h2>EN 14604</h2>
                <div style="display: flex; gap: 20px; align-items: start; margin-bottom: 30px;">
                    <div style="background: #10B981; color: white; padding: 20px; border-radius: 10px; font-weight: bold;">EN 14604</div>
                    <div>
                        <p><strong>Europäische Produktnorm für Rauchmelder.</strong> Definiert Mindestanforderungen an Lautstärke (85 dB), Empfindlichkeit, Batterielaufzeit und mehr.</p>
                    </div>
                </div>
                
                <h2>Q-Label (Qualitätszeichen)</h2>
                <div style="display: flex; gap: 20px; align-items: start; margin-bottom: 30px;">
                    <div style="background: #C41E3A; color: white; padding: 20px 30px; border-radius: 10px; font-weight: bold; font-size: 1.5rem;">Q</div>
                    <div>
                        <p><strong>Das wichtigste Qualitätsmermal!</strong> Rauchmelder mit Q-Label erfüllen erhöhte Anforderungen:</p>
                        <ul>
                            <li>✓ Festeingebaute 10-Jahres-Batterie</li>
                            <li>✓ Erhöhte Stabilität gegen äußere Einflüsse</li>
                            <li>✓ Reduzierte Fehlalarme</li>
                            <li>✓ Erhöhte Langlebigkeit der Komponenten</li>
                        </ul>
                    </div>
                </div>
                
                <h2>VdS-Anerkennung</h2>
                <div style="display: flex; gap: 20px; align-items: start; margin-bottom: 30px;">
                    <div style="background: #1a1a1a; color: white; padding: 20px; border-radius: 10px; font-weight: bold;">VdS</div>
                    <div>
                        <p><strong>Vertrauen der deutschen Versicherer.</strong> VdS-anerkannte Rauchmelder werden von deutschen Versicherungen empfohlen.</p>
                    </div>
                </div>
                
                <h2>TÜV-Prüfzeichen</h2>
                <div style="display: flex; gap: 20px; align-items: start; margin-bottom: 30px;">
                    <div style="background: #3B82F6; color: white; padding: 20px; border-radius: 10px; font-weight: bold;">TÜV</div>
                    <div>
                        <p><strong>Unabhängige Prüfung.</strong> Der TÜV testet Rauchmelder auf Sicherheit und Funktionalität.</p>
                    </div>
                </div>
                
                <h2>Unsere Empfehlung</h2>
                <p>Achten Sie beim Kauf auf mindestens:</p>
                <ul>
                    <li>✓ CE + EN 14604 (gesetzlich vorgeschrieben)</li>
                    <li>✓ Q-Label (für beste Qualität)</li>
                    <li>○ VdS (empfohlen)</li>
                </ul>
                
                <p style="margin-top: 30px;">Alle unsere Rauchmelder sind CE, EN 14604 und Q-Label zertifiziert.</p>
            </div>
        </section>
'''
    },
    
    "downloads.html": {
        "title": "Downloads | PDFs, Datenblätter & Dokumente | Secu.li",
        "desc": "Laden Sie Datenblätter, Montageanleitungen und Informationsmaterial zu unseren Rauchmeldern herunter.",
        "h1": "Download-Bereich",
        "content": '''
        <section class="section" style="padding-top: 120px;">
            <div class="container" style="max-width: 900px;">
                <h1>Download-Bereich</h1>
                <p class="subtitle">Datenblätter, Anleitungen und Informationsmaterial zum Herunterladen.</p>
                
                <h2>Produktinformationen</h2>
                <div style="background: #F9FAFB; padding: 20px; border-radius: 10px; margin-bottom: 15px; display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <strong>Rauchmelder Ei650 - Datenblatt</strong>
                        <p style="margin: 0; color: #6B7280;">PDF, 450 KB</p>
                    </div>
                    <a href="kontakt.html" class="btn btn-outline btn-sm">Anfragen</a>
                </div>
                <div style="background: #F9FAFB; padding: 20px; border-radius: 10px; margin-bottom: 15px; display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <strong>Funkrauchmelder - Übersicht</strong>
                        <p style="margin: 0; color: #6B7280;">PDF, 320 KB</p>
                    </div>
                    <a href="kontakt.html" class="btn btn-outline btn-sm">Anfragen</a>
                </div>
                
                <h2>Montage & Wartung</h2>
                <div style="background: #F9FAFB; padding: 20px; border-radius: 10px; margin-bottom: 15px; display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <strong>Montage-Anleitung nach DIN 14676</strong>
                        <p style="margin: 0; color: #6B7280;">PDF, 1.2 MB</p>
                    </div>
                    <a href="kontakt.html" class="btn btn-outline btn-sm">Anfragen</a>
                </div>
                <div style="background: #F9FAFB; padding: 20px; border-radius: 10px; margin-bottom: 15px; display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <strong>Wartungsprotokoll - Vorlage</strong>
                        <p style="margin: 0; color: #6B7280;">PDF, 85 KB</p>
                    </div>
                    <a href="kontakt.html" class="btn btn-outline btn-sm">Anfragen</a>
                </div>
                
                <h2>Rechtliche Informationen</h2>
                <div style="background: #F9FAFB; padding: 20px; border-radius: 10px; margin-bottom: 15px; display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <strong>Rauchmelderpflicht - Übersicht aller Bundesländer</strong>
                        <p style="margin: 0; color: #6B7280;">PDF, 280 KB</p>
                    </div>
                    <a href="kontakt.html" class="btn btn-outline btn-sm">Anfragen</a>
                </div>
                
                <div style="background: #FEF2F2; padding: 30px; border-radius: 15px; margin-top: 40px; text-align: center;">
                    <h3>Benötigen Sie weitere Unterlagen?</h3>
                    <p>Kontaktieren Sie uns - wir senden Ihnen gerne weitere Informationen zu.</p>
                    <a href="kontakt.html" class="btn btn-primary">Kontakt aufnehmen</a>
                </div>
            </div>
        </section>
'''
    },
    
    "bewertungen.html": {
        "title": "Kundenbewertungen & Referenzen | Secu.li",
        "desc": "Lesen Sie echte Kundenbewertungen und Erfahrungen mit unserem Rauchmelder-Service.",
        "h1": "Kundenbewertungen",
        "content": '''
        <section class="section" style="padding-top: 120px;">
            <div class="container" style="max-width: 900px;">
                <h1>Kundenbewertungen & Referenzen</h1>
                <p class="subtitle">Was unsere Kunden über uns sagen.</p>
                
                <div style="text-align: center; margin-bottom: 40px;">
                    <div style="font-size: 3rem;">⭐⭐⭐⭐⭐</div>
                    <p><strong>4.9 von 5 Sternen</strong> basierend auf über 500 Bewertungen</p>
                </div>
                
                <div style="background: white; border: 1px solid #E5E7EB; padding: 25px; border-radius: 15px; margin-bottom: 20px;">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
                        <strong>Thomas M. aus Berlin</strong>
                        <span>⭐⭐⭐⭐⭐</span>
                    </div>
                    <p>"Schneller, professioneller Service. Die Techniker waren pünktlich und haben alles sauber installiert. Die Dokumentation kam direkt per E-Mail. Sehr empfehlenswert!"</p>
                </div>
                
                <div style="background: white; border: 1px solid #E5E7EB; padding: 25px; border-radius: 15px; margin-bottom: 20px;">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
                        <strong>Hausverwaltung Schmidt GmbH</strong>
                        <span>⭐⭐⭐⭐⭐</span>
                    </div>
                    <p>"Wir lassen seit 3 Jahren alle unsere Objekte von Secu.li betreuen. Die Koordination mit den Mietern funktioniert reibungslos, die Dokumentation ist immer vollständig. Top!"</p>
                </div>
                
                <div style="background: white; border: 1px solid #E5E7EB; padding: 25px; border-radius: 15px; margin-bottom: 20px;">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
                        <strong>Maria K. aus München</strong>
                        <span>⭐⭐⭐⭐⭐</span>
                    </div>
                    <p>"Endlich ein Anbieter, der auch die jährliche Wartung zuverlässig durchführt. Ich bekomme rechtzeitig eine Erinnerung und kann den Termin online buchen."</p>
                </div>
                
                <div style="background: white; border: 1px solid #E5E7EB; padding: 25px; border-radius: 15px; margin-bottom: 20px;">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
                        <strong>Peter L. aus Hamburg</strong>
                        <span>⭐⭐⭐⭐</span>
                    </div>
                    <p>"Guter Service, faire Preise. Einen Stern Abzug weil die Terminvereinbarung etwas länger gedauert hat. Aber die Arbeit war einwandfrei."</p>
                </div>
                
                <div style="background: var(--charcoal); color: white; padding: 30px; border-radius: 15px; margin-top: 40px; text-align: center;">
                    <h3>Werden Sie unser nächster zufriedener Kunde</h3>
                    <a href="kontakt.html" class="btn btn-primary">Jetzt anfragen</a>
                </div>
            </div>
        </section>
'''
    },
    
    "preise.html": {
        "title": "Preise & Pakete | Rauchmelder Installation & Wartung | Secu.li",
        "desc": "Transparente Preise für Rauchmelder-Installation und Wartung. Faire Festpreise ohne versteckte Kosten.",
        "h1": "Preise & Pakete",
        "content": '''
        <section class="section" style="padding-top: 120px;">
            <div class="container" style="max-width: 1000px;">
                <h1>Preise & Pakete</h1>
                <p class="subtitle">Transparente Festpreise ohne versteckte Kosten.</p>
                
                <div class="features-grid" style="margin-top: 40px;">
                    <div style="background: white; border: 2px solid #E5E7EB; padding: 30px; border-radius: 20px; text-align: center;">
                        <h3>Starter</h3>
                        <div style="font-size: 2.5rem; font-weight: 700; color: var(--primary); margin: 20px 0;">ab 99€</div>
                        <ul style="text-align: left; list-style: none; padding: 0;">
                            <li style="padding: 10px 0; border-bottom: 1px solid #E5E7EB;">✓ 3 Rauchmelder</li>
                            <li style="padding: 10px 0; border-bottom: 1px solid #E5E7EB;">✓ Fachgerechte Installation</li>
                            <li style="padding: 10px 0; border-bottom: 1px solid #E5E7EB;">✓ 10 Jahre Garantie</li>
                            <li style="padding: 10px 0;">✓ Dokumentation</li>
                        </ul>
                        <a href="kontakt.html" class="btn btn-outline" style="width: 100%; margin-top: 20px;">Anfragen</a>
                    </div>
                    
                    <div style="background: var(--primary); color: white; padding: 30px; border-radius: 20px; text-align: center; transform: scale(1.05);">
                        <span style="background: #F59E0B; color: #111; padding: 5px 15px; border-radius: 20px; font-size: 0.8rem; font-weight: 600;">BELIEBT</span>
                        <h3 style="color: white; margin-top: 15px;">Standard</h3>
                        <div style="font-size: 2.5rem; font-weight: 700; margin: 20px 0;">ab 149€</div>
                        <ul style="text-align: left; list-style: none; padding: 0;">
                            <li style="padding: 10px 0; border-bottom: 1px solid rgba(255,255,255,0.2);">✓ 5 Rauchmelder</li>
                            <li style="padding: 10px 0; border-bottom: 1px solid rgba(255,255,255,0.2);">✓ Fachgerechte Installation</li>
                            <li style="padding: 10px 0; border-bottom: 1px solid rgba(255,255,255,0.2);">✓ 10 Jahre Garantie</li>
                            <li style="padding: 10px 0; border-bottom: 1px solid rgba(255,255,255,0.2);">✓ Dokumentation</li>
                            <li style="padding: 10px 0;">✓ 1x Wartung inklusive</li>
                        </ul>
                        <a href="kontakt.html" class="btn" style="background: white; color: var(--primary); width: 100%; margin-top: 20px;">Anfragen</a>
                    </div>
                    
                    <div style="background: white; border: 2px solid #E5E7EB; padding: 30px; border-radius: 20px; text-align: center;">
                        <h3>Premium</h3>
                        <div style="font-size: 2.5rem; font-weight: 700; color: var(--primary); margin: 20px 0;">ab 249€</div>
                        <ul style="text-align: left; list-style: none; padding: 0;">
                            <li style="padding: 10px 0; border-bottom: 1px solid #E5E7EB;">✓ 8 Rauchmelder</li>
                            <li style="padding: 10px 0; border-bottom: 1px solid #E5E7EB;">✓ Fachgerechte Installation</li>
                            <li style="padding: 10px 0; border-bottom: 1px solid #E5E7EB;">✓ 10 Jahre Garantie</li>
                            <li style="padding: 10px 0; border-bottom: 1px solid #E5E7EB;">✓ Dokumentation</li>
                            <li style="padding: 10px 0;">✓ 3 Jahre Wartung inkl.</li>
                        </ul>
                        <a href="kontakt.html" class="btn btn-outline" style="width: 100%; margin-top: 20px;">Anfragen</a>
                    </div>
                </div>
                
                <h2 style="margin-top: 60px;">Einzelpreise</h2>
                <table class="service-table">
                    <thead><tr><th>Leistung</th><th>Preis</th></tr></thead>
                    <tbody>
                        <tr><td>Installation pro Rauchmelder</td><td>ab 29€</td></tr>
                        <tr><td>Jährliche Wartung pro Melder</td><td>ab 5€</td></tr>
                        <tr><td>Geräteaustausch (nach 10 Jahren)</td><td>ab 25€</td></tr>
                        <tr><td>Anfahrtspauschale</td><td>ab 19€</td></tr>
                    </tbody>
                </table>
                
                <p style="text-align: center; margin-top: 30px; color: #6B7280;">Alle Preise inkl. MwSt. Individuelle Angebote für Hausverwaltungen auf Anfrage.</p>
            </div>
        </section>
'''
    },
    
    "blog.html": {
        "title": "Blog & News | Aktuelles zu Rauchmeldern & Brandschutz | Secu.li",
        "desc": "Aktuelle News, Tipps und Wissenswertes rund um Rauchmelder, Brandschutz und Sicherheit.",
        "h1": "Blog & News",
        "content": '''
        <section class="section" style="padding-top: 120px;">
            <div class="container" style="max-width: 900px;">
                <h1>Blog & News</h1>
                <p class="subtitle">Aktuelles zu Rauchmeldern, Brandschutz und Sicherheit.</p>
                
                <article style="background: white; border: 1px solid #E5E7EB; border-radius: 15px; overflow: hidden; margin-bottom: 30px;">
                    <div style="padding: 30px;">
                        <span style="background: #10B981; color: white; padding: 5px 12px; border-radius: 20px; font-size: 0.8rem;">Tipp</span>
                        <h2 style="margin: 15px 0;">5 häufige Fehler bei der Rauchmelder-Installation</h2>
                        <p style="color: #6B7280;">Vermeiden Sie diese typischen Fehler, die die Funktion Ihres Rauchmelders beeinträchtigen können.</p>
                        <a href="ratgeber.html" style="color: var(--primary); font-weight: 600;">Weiterlesen →</a>
                    </div>
                </article>
                
                <article style="background: white; border: 1px solid #E5E7EB; border-radius: 15px; overflow: hidden; margin-bottom: 30px;">
                    <div style="padding: 30px;">
                        <span style="background: #3B82F6; color: white; padding: 5px 12px; border-radius: 20px; font-size: 0.8rem;">News</span>
                        <h2 style="margin: 15px 0;">Neue Rauchmelderpflicht in Brandenburg seit 2020</h2>
                        <p style="color: #6B7280;">Brandenburg war das letzte Bundesland, das die Rauchmelderpflicht eingeführt hat. Was Sie jetzt wissen müssen.</p>
                        <a href="rauchmelderpflicht.html" style="color: var(--primary); font-weight: 600;">Weiterlesen →</a>
                    </div>
                </article>
                
                <article style="background: white; border: 1px solid #E5E7EB; border-radius: 15px; overflow: hidden; margin-bottom: 30px;">
                    <div style="padding: 30px;">
                        <span style="background: #F59E0B; color: #111; padding: 5px 12px; border-radius: 20px; font-size: 0.8rem;">Wissen</span>
                        <h2 style="margin: 15px 0;">Q-Label: Was es bedeutet und warum es wichtig ist</h2>
                        <p style="color: #6B7280;">Das Q-Label garantiert höchste Qualität bei Rauchmeldern. Wir erklären, worauf es ankommt.</p>
                        <a href="zertifikate.html" style="color: var(--primary); font-weight: 600;">Weiterlesen →</a>
                    </div>
                </article>
                
                <article style="background: white; border: 1px solid #E5E7EB; border-radius: 15px; overflow: hidden; margin-bottom: 30px;">
                    <div style="padding: 30px;">
                        <span style="background: #DC2626; color: white; padding: 5px 12px; border-radius: 20px; font-size: 0.8rem;">Wichtig</span>
                        <h2 style="margin: 15px 0;">Verhalten im Brandfall - Diese Regeln retten Leben</h2>
                        <p style="color: #6B7280;">Was tun, wenn es brennt? Die wichtigsten Verhaltensregeln für den Ernstfall.</p>
                        <a href="notfall.html" style="color: var(--primary); font-weight: 600;">Weiterlesen →</a>
                    </div>
                </article>
            </div>
        </section>
'''
    },
    
    "rauchmelder-vergleich.html": {
        "title": "Rauchmelder Vergleich | Die besten Modelle im Test | Secu.li",
        "desc": "Vergleichen Sie die besten Rauchmelder: Ei650, Hekatron Genius, Jung und mehr im direkten Vergleich.",
        "h1": "Rauchmelder Vergleich",
        "content": '''
        <section class="section" style="padding-top: 120px;">
            <div class="container" style="max-width: 1100px;">
                <h1>Rauchmelder Vergleich</h1>
                <p class="subtitle">Die besten Rauchmelder im direkten Vergleich.</p>
                
                <div style="overflow-x: auto;">
                    <table class="service-table" style="min-width: 800px;">
                        <thead>
                            <tr>
                                <th>Modell</th>
                                <th>Ei650</th>
                                <th>Hekatron Genius Plus</th>
                                <th>Jung Basic</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td><strong>Preis</strong></td>
                                <td>~25€</td>
                                <td>~30€</td>
                                <td>~20€</td>
                            </tr>
                            <tr>
                                <td><strong>Q-Label</strong></td>
                                <td>✓ Ja</td>
                                <td>✓ Ja</td>
                                <td>✓ Ja</td>
                            </tr>
                            <tr>
                                <td><strong>Batterielaufzeit</strong></td>
                                <td>10 Jahre</td>
                                <td>10 Jahre</td>
                                <td>10 Jahre</td>
                            </tr>
                            <tr>
                                <td><strong>Vernetzbar</strong></td>
                                <td>Optional (Funkmodul)</td>
                                <td>Optional (Funkmodul)</td>
                                <td>Nein</td>
                            </tr>
                            <tr>
                                <td><strong>Stummschaltung</strong></td>
                                <td>10 Minuten</td>
                                <td>10 Minuten</td>
                                <td>10 Minuten</td>
                            </tr>
                            <tr>
                                <td><strong>Lautstärke</strong></td>
                                <td>85 dB</td>
                                <td>85 dB</td>
                                <td>85 dB</td>
                            </tr>
                            <tr>
                                <td><strong>Besonderheit</strong></td>
                                <td>Testsieger Stiftung Warentest</td>
                                <td>Made in Germany</td>
                                <td>Preis-Leistungs-Sieger</td>
                            </tr>
                            <tr>
                                <td><strong>Unsere Bewertung</strong></td>
                                <td>⭐⭐⭐⭐⭐</td>
                                <td>⭐⭐⭐⭐⭐</td>
                                <td>⭐⭐⭐⭐</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                
                <h2 style="margin-top: 50px;">Unsere Empfehlung</h2>
                <div style="background: #F0FDF4; padding: 30px; border-radius: 15px;">
                    <h3>Ei Electronics Ei650</h3>
                    <p>Der Ei650 ist unser meistinstallierter Rauchmelder. Er überzeugt durch:</p>
                    <ul>
                        <li>✓ Mehrfacher Testsieger bei Stiftung Warentest</li>
                        <li>✓ 10 Jahre Herstellergarantie</li>
                        <li>✓ Sehr geringe Fehlalarmrate</li>
                        <li>✓ Einfache Montage</li>
                    </ul>
                </div>
                
                <div style="text-align: center; margin-top: 40px;">
                    <p>Lassen Sie sich von uns beraten, welcher Rauchmelder für Sie der richtige ist.</p>
                    <a href="kontakt.html" class="btn btn-primary">Kostenlose Beratung</a>
                </div>
            </div>
        </section>
'''
    }
}

def create_page(filename, data):
    content = f'''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{data['desc']}">
    <title>{data['title']}</title>
    <link rel="canonical" href="https://secu.li/{filename}">
    <link rel="stylesheet" href="styles.css">
    <meta name="theme-color" content="#C41E3A">
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
    
    {data['content']}
    
    <footer class="footer">
        <div class="container" style="text-align: center; padding: 30px;">
            <p>&copy; 2024 Secu.li - {data['h1']}</p>
            <a href="impressum.html">Impressum</a> | <a href="datenschutz.html">Datenschutz</a>
        </div>
    </footer>
    <script src="script.js"></script>
</body>
</html>'''
    
    filepath = BASE_DIR / filename
    filepath.write_text(content, encoding='utf-8')
    print(f"✓ {filename} erstellt")

def main():
    print("Erstelle neue Seiten...")
    for filename, data in pages.items():
        create_page(filename, data)
    print(f"\n✅ {len(pages)} neue Seiten erstellt!")

if __name__ == "__main__":
    main()
