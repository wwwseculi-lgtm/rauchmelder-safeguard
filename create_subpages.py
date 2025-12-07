#!/usr/bin/env python3
"""
Erstellt Unterseiten für alle anklickbaren Elemente (Räume, Zertifikate, etc.)
"""

from pathlib import Path

BASE_DIR = Path("/Users/neslihanakdeniz/Desktop/Rauchmelder")

def get_subpage(title, desc, h1, badge, content):
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
            padding: 160px 20px 80px;
            text-align: center;
            position: relative;
            z-index: 1;
        }}
        .page-hero h1 {{ font-size: 2.5rem; margin-bottom: 15px; color: white; }}
        .page-hero .subtitle {{ font-size: 1.2rem; opacity: 0.9; max-width: 600px; margin: 0 auto 30px; }}
        .hero-badge {{ display: inline-block; background: var(--primary); color: white; padding: 8px 20px; border-radius: 30px; font-size: 0.9rem; font-weight: 600; margin-bottom: 20px; }}
        .content-section {{ padding: 60px 20px; max-width: 900px; margin: 0 auto; }}
        .content-section h2 {{ color: #1a1a1a; margin-top: 40px; margin-bottom: 20px; padding-bottom: 10px; border-bottom: 2px solid #E5E7EB; }}
        .content-section h2:first-child {{ margin-top: 0; }}
        .info-box {{ background: linear-gradient(135deg, #F0FDF4, #ECFDF5); padding: 25px 30px; border-radius: 15px; margin: 30px 0; border-left: 4px solid #10B981; }}
        .info-box h3 {{ margin-top: 0; color: #047857; }}
        .warning-box {{ background: linear-gradient(135deg, #FFFBEB, #FEF3C7); padding: 25px 30px; border-radius: 15px; margin: 30px 0; border-left: 4px solid #F59E0B; }}
        .cta-box {{ background: linear-gradient(135deg, #C41E3A, #991B1B); color: white; padding: 40px; border-radius: 20px; margin: 50px 0; text-align: center; }}
        .cta-box h3 {{ color: white; margin-top: 0; }}
        .check-list {{ list-style: none; padding: 0; }}
        .check-list li {{ padding: 12px 0; padding-left: 30px; position: relative; border-bottom: 1px solid #E5E7EB; }}
        .check-list li:before {{ content: "✓"; position: absolute; left: 0; color: #10B981; font-weight: bold; }}
        .breadcrumb {{ display: flex; gap: 8px; font-size: 0.9rem; color: rgba(255,255,255,0.7); justify-content: center; margin-bottom: 20px; flex-wrap: wrap; }}
        .breadcrumb a {{ color: rgba(255,255,255,0.7); text-decoration: none; }}
        .related-links {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin: 30px 0; }}
        .related-link {{ display: block; padding: 20px; background: #F9FAFB; border-radius: 10px; text-decoration: none; color: #1a1a1a; font-weight: 500; transition: all 0.3s; }}
        .related-link:hover {{ background: var(--primary); color: white; }}
        @media (max-width: 768px) {{ .page-hero h1 {{ font-size: 1.8rem; }} .page-hero {{ padding: 140px 20px 60px; }} }}
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

pages = {
    # RÄUME
    "rauchmelder-schlafzimmer.html": {
        "title": "Rauchmelder im Schlafzimmer | Pflicht & Tipps | Secu.li",
        "desc": "Rauchmelder im Schlafzimmer sind Pflicht. Alles zur richtigen Platzierung und Installation.",
        "h1": "Rauchmelder im Schlafzimmer",
        "badge": "🛏️ Pflicht",
        "content": '''
        <h2>Warum sind Rauchmelder im Schlafzimmer Pflicht?</h2>
        <p>Im Schlaf ist der Geruchssinn ausgeschaltet. Ohne Rauchmelder besteht die Gefahr, einen Brand zu verschlafen - mit tödlichen Folgen durch Rauchvergiftung.</p>
        
        <div class="info-box">
            <h3>📊 Statistik</h3>
            <p>95% aller Brandtoten sterben an Rauchvergiftung, nicht durch Feuer. Die meisten Brandopfer werden nachts im Schlaf überrascht.</p>
        </div>
        
        <h2>Gesetzliche Grundlage</h2>
        <p>In allen 16 Bundesländern ist mindestens ein Rauchmelder im Schlafzimmer <strong>gesetzlich vorgeschrieben</strong>. Die Verantwortung liegt beim Eigentümer.</p>
        
        <h2>Richtige Platzierung</h2>
        <ul class="check-list">
            <li>Mittig an der Decke montieren</li>
            <li>Mindestens 50cm Abstand zu Wänden</li>
            <li>Nicht über dem Bett direkt</li>
            <li>Nicht in der Nähe von Lüftungen</li>
        </ul>
        
        <h2>Empfohlene Rauchmelder</h2>
        <p>Für Schlafzimmer empfehlen wir besonders leise Modelle mit:</p>
        <ul class="check-list">
            <li>Stummschaltfunktion für Fehlalarme</li>
            <li>Keine blinkende LED (stört den Schlaf nicht)</li>
            <li>Q-Label für 10 Jahre Ruhe</li>
        </ul>
        
        <h2>Weitere Räume</h2>
        <div class="related-links">
            <a href="rauchmelder-kinderzimmer.html" class="related-link">👶 Kinderzimmer →</a>
            <a href="rauchmelder-flur.html" class="related-link">🚪 Flure →</a>
            <a href="rauchmelder-wohnzimmer.html" class="related-link">🛋️ Wohnzimmer →</a>
        </div>
        
        <div class="cta-box">
            <h3>Professionelle Installation</h3>
            <p>Wir installieren Rauchmelder fachgerecht in Ihrem Schlafzimmer.</p>
            <a href="kontakt.html" class="btn" style="background: white; color: var(--primary);">Jetzt anfragen</a>
        </div>
'''
    },
    
    "rauchmelder-kinderzimmer.html": {
        "title": "Rauchmelder im Kinderzimmer | Schutz für die Kleinsten | Secu.li",
        "desc": "Rauchmelder im Kinderzimmer sind Pflicht. So schützen Sie Ihre Kinder optimal.",
        "h1": "Rauchmelder im Kinderzimmer",
        "badge": "👶 Pflicht",
        "content": '''
        <h2>Warum Rauchmelder im Kinderzimmer?</h2>
        <p>Kinder schlafen besonders tief und können den Geruch von Rauch nicht wahrnehmen. Ein Rauchmelder kann lebensrettend sein.</p>
        
        <div class="warning-box">
            <strong>⚠️ Wichtig:</strong> Kinder unter 6 Jahren wachen oft nicht von Rauchmelderalarm auf. Bei kleinen Kindern sollten Eltern zusätzlich durch vernetzte Melder im eigenen Schlafzimmer gewarnt werden.
        </div>
        
        <h2>Gesetzliche Pflicht</h2>
        <p>In <strong>allen Bundesländern</strong> sind Rauchmelder in Kinderzimmern gesetzlich vorgeschrieben.</p>
        
        <h2>Tipps für Kinderzimmer</h2>
        <ul class="check-list">
            <li>Rauchmelder außer Reichweite von Kindern montieren</li>
            <li>Modelle ohne blinkende LED wählen</li>
            <li>Bei Kleinkindern: Funkvernetzte Melder zum Elternschlafzimmer</li>
            <li>Regelmäßig Probealarm durchführen (Kinder gewöhnen)</li>
        </ul>
        
        <h2>Weitere Räume</h2>
        <div class="related-links">
            <a href="rauchmelder-schlafzimmer.html" class="related-link">🛏️ Schlafzimmer →</a>
            <a href="rauchmelder-flur.html" class="related-link">🚪 Flure →</a>
            <a href="rauchmelder-wohnzimmer.html" class="related-link">🛋️ Wohnzimmer →</a>
        </div>
        
        <div class="cta-box">
            <h3>Kindersichere Installation</h3>
            <p>Wir installieren Rauchmelder kindersicher und beraten zu Vernetzung.</p>
            <a href="kontakt.html" class="btn" style="background: white; color: var(--primary);">Beratung anfragen</a>
        </div>
'''
    },
    
    "rauchmelder-flur.html": {
        "title": "Rauchmelder im Flur | Rettungswege sichern | Secu.li",
        "desc": "Rauchmelder im Flur sind Pflicht. So sichern Sie Ihre Flucht- und Rettungswege.",
        "h1": "Rauchmelder im Flur",
        "badge": "🚪 Pflicht",
        "content": '''
        <h2>Warum Rauchmelder im Flur?</h2>
        <p>Flure sind <strong>Flucht- und Rettungswege</strong>. Hier muss ein Brand frühzeitig erkannt werden, damit Sie sicher nach draußen gelangen können.</p>
        
        <h2>Gesetzliche Regelung</h2>
        <p>In allen Bundesländern sind Rauchmelder in Fluren vorgeschrieben, die als Rettungsweg dienen.</p>
        
        <h2>Besonderheiten bei Fluren</h2>
        <ul class="check-list">
            <li>Bei langen Fluren: mehrere Melder (max. 7,5m Abstand)</li>
            <li>Treppenhaus: Melder auf jeder Etage</li>
            <li>Verzweigungen: Jeder Flurbereich braucht einen Melder</li>
            <li>Dachschrägen: Spezialmontage beachten</li>
        </ul>
        
        <div class="info-box">
            <h3>💡 Tipp für Treppenhäuser</h3>
            <p>In offenen Treppenhäusern steigt Rauch schnell auf. Montieren Sie Rauchmelder auf der obersten Ebene und auf jeder Zwischenetage.</p>
        </div>
        
        <h2>Weitere Räume</h2>
        <div class="related-links">
            <a href="rauchmelder-schlafzimmer.html" class="related-link">🛏️ Schlafzimmer →</a>
            <a href="rauchmelder-kinderzimmer.html" class="related-link">👶 Kinderzimmer →</a>
            <a href="rauchmelder-wohnzimmer.html" class="related-link">🛋️ Wohnzimmer →</a>
        </div>
        
        <div class="cta-box">
            <h3>Flur-Konzept erstellen</h3>
            <p>Wir analysieren Ihren Fluchtweg und planen die optimale Melder-Platzierung.</p>
            <a href="kontakt.html" class="btn" style="background: white; color: var(--primary);">Kostenlose Beratung</a>
        </div>
'''
    },
    
    "rauchmelder-wohnzimmer.html": {
        "title": "Rauchmelder im Wohnzimmer | Empfohlen für mehr Sicherheit | Secu.li",
        "desc": "Rauchmelder im Wohnzimmer - empfohlen für zusätzliche Sicherheit bei Kerzen, TV, Elektronik.",
        "h1": "Rauchmelder im Wohnzimmer",
        "badge": "🛋️ Empfohlen",
        "content": '''
        <h2>Ist ein Rauchmelder im Wohnzimmer Pflicht?</h2>
        <p>Nein, in den meisten Bundesländern <strong>nicht gesetzlich vorgeschrieben</strong>. Aber <strong>dringend empfohlen</strong> für zusätzliche Sicherheit.</p>
        
        <h2>Warum trotzdem sinnvoll?</h2>
        <ul class="check-list">
            <li>Viele Elektrogeräte (TV, Lampen, Ladegeräte)</li>
            <li>Kerzen und offene Flammen</li>
            <li>Kamine und Öfen</li>
            <li>Weihnachtsbeleuchtung</li>
            <li>Zigarettenreste (falls Raucher)</li>
        </ul>
        
        <div class="info-box">
            <h3>📊 Wussten Sie?</h3>
            <p>Die häufigsten Brandursachen in Wohnhäusern sind defekte Elektrogeräte und unbeaufsichtigte Kerzen - beides typisch für Wohnzimmer.</p>
        </div>
        
        <h2>Tipps für Wohnzimmer</h2>
        <ul class="check-list">
            <li>Modelle mit Stummschaltung wählen (für Kaminabende)</li>
            <li>Bei offenem Kamin: Wärmemelder als Ergänzung</li>
            <li>Vernetzung mit Schlafzimmer-Melder</li>
        </ul>
        
        <h2>Weitere Räume</h2>
        <div class="related-links">
            <a href="rauchmelder-schlafzimmer.html" class="related-link">🛏️ Schlafzimmer →</a>
            <a href="rauchmelder-kinderzimmer.html" class="related-link">👶 Kinderzimmer →</a>
            <a href="rauchmelder-flur.html" class="related-link">🚪 Flure →</a>
        </div>
        
        <div class="cta-box">
            <h3>Komplettausstattung</h3>
            <p>Wir beraten Sie zur optimalen Rauchmelder-Ausstattung für Ihr Zuhause.</p>
            <a href="kontakt.html" class="btn" style="background: white; color: var(--primary);">Jetzt anfragen</a>
        </div>
'''
    },
    
    # ZERTIFIKATE
    "q-label.html": {
        "title": "Q-Label bei Rauchmeldern | Das Qualitätszeichen | Secu.li",
        "desc": "Das Q-Label ist das wichtigste Qualitätszeichen für Rauchmelder. Was es bedeutet und warum es wichtig ist.",
        "h1": "Q-Label",
        "badge": "🏆 Qualität",
        "content": '''
        <h2>Was ist das Q-Label?</h2>
        <p>Das Q-Label ist ein <strong>unabhängiges Qualitätszeichen</strong> für hochwertige Rauchmelder. Es wird vom Forum Brandrauchprävention in Deutschland vergeben.</p>
        
        <div style="text-align: center; margin: 40px 0;">
            <div style="display: inline-block; background: #C41E3A; color: white; padding: 30px 50px; border-radius: 15px; font-size: 3rem; font-weight: bold;">Q</div>
        </div>
        
        <h2>Anforderungen für das Q-Label</h2>
        <ul class="check-list">
            <li><strong>Fest eingebaute 10-Jahres-Batterie</strong> - kein Batteriewechsel nötig</li>
            <li><strong>Erhöhte Stabilität</strong> gegen Umwelteinflüsse und Alterung</li>
            <li><strong>Reduzierte Fehlalarmrate</strong> durch bessere Sensoren</li>
            <li><strong>Langlebige Komponenten</strong> - Qualität über 10 Jahre garantiert</li>
        </ul>
        
        <h2>Vorteile des Q-Labels</h2>
        <div class="info-box">
            <h3>💡 Warum Q-Label wählen?</h3>
            <ul>
                <li>Keine nervigen Batteriewarnungen nachts</li>
                <li>Weniger Fehlalarme beim Kochen</li>
                <li>10 Jahre Ruhe - danach Austausch</li>
                <li>Höhere Versicherungsakzeptanz</li>
            </ul>
        </div>
        
        <h2>Weitere Zertifikate</h2>
        <div class="related-links">
            <a href="ce-kennzeichnung.html" class="related-link">CE-Kennzeichnung →</a>
            <a href="en-14604.html" class="related-link">EN 14604 →</a>
            <a href="tuev-pruefung.html" class="related-link">TÜV-Prüfung →</a>
        </div>
        
        <div class="cta-box">
            <h3>Q-Label Rauchmelder kaufen</h3>
            <p>Wir installieren ausschließlich Q-Label zertifizierte Rauchmelder.</p>
            <a href="kontakt.html" class="btn" style="background: white; color: var(--primary);">Anfragen</a>
        </div>
'''
    },
    
    "ce-kennzeichnung.html": {
        "title": "CE-Kennzeichnung bei Rauchmeldern | Pflicht in der EU | Secu.li",
        "desc": "Die CE-Kennzeichnung ist Pflicht für alle Rauchmelder in der EU. Was sie bedeutet.",
        "h1": "CE-Kennzeichnung",
        "badge": "🇪🇺 EU-Pflicht",
        "content": '''
        <h2>Was bedeutet CE?</h2>
        <p><strong>C</strong>onformité <strong>E</strong>uropéenne - das Zeichen bestätigt, dass ein Produkt den grundlegenden europäischen Sicherheitsanforderungen entspricht.</p>
        
        <div style="text-align: center; margin: 40px 0;">
            <div style="display: inline-block; background: #1a1a1a; color: white; padding: 25px 35px; border-radius: 10px; font-size: 2.5rem; font-weight: bold;">CE</div>
        </div>
        
        <h2>Ist CE ein Qualitätszeichen?</h2>
        <div class="warning-box">
            <strong>⚠️ Wichtig zu wissen:</strong>
            <p>CE ist <strong>kein Qualitätszeichen</strong>, sondern nur die Bestätigung, dass grundlegende Sicherheitsanforderungen erfüllt sind. Für Qualität achten Sie zusätzlich auf das <a href="q-label.html">Q-Label</a>.</p>
        </div>
        
        <h2>Was prüft CE bei Rauchmeldern?</h2>
        <ul class="check-list">
            <li>Grundlegende Sicherheit des Geräts</li>
            <li>Einhaltung von EU-Richtlinien</li>
            <li>Elektromagnetische Verträglichkeit</li>
        </ul>
        
        <h2>Weitere Zertifikate</h2>
        <div class="related-links">
            <a href="q-label.html" class="related-link">Q-Label →</a>
            <a href="en-14604.html" class="related-link">EN 14604 →</a>
            <a href="tuev-pruefung.html" class="related-link">TÜV-Prüfung →</a>
        </div>
'''
    },
    
    "en-14604.html": {
        "title": "EN 14604 | Europäische Norm für Rauchmelder | Secu.li",
        "desc": "EN 14604 ist die europäische Produktnorm für Rauchmelder. Mindestanforderungen erklärt.",
        "h1": "EN 14604",
        "badge": "📋 EU-Norm",
        "content": '''
        <h2>Was ist EN 14604?</h2>
        <p>EN 14604 ist die <strong>europäische Produktnorm für Rauchmelder</strong>. Sie definiert die Mindestanforderungen an Qualität und Funktion.</p>
        
        <div style="text-align: center; margin: 40px 0;">
            <div style="display: inline-block; background: #10B981; color: white; padding: 20px 30px; border-radius: 10px; font-size: 1.5rem; font-weight: bold;">EN 14604</div>
        </div>
        
        <h2>Anforderungen der EN 14604</h2>
        <ul class="check-list">
            <li><strong>Lautstärke mindestens 85 dB</strong> in 3m Entfernung</li>
            <li><strong>Batterie-Warnsignal</strong> mindestens 30 Tage vor leer</li>
            <li><strong>Testtaste</strong> zur Funktionsprüfung</li>
            <li><strong>Kennzeichnung</strong> mit Herstellerdaten</li>
            <li><strong>Rauch-Empfindlichkeit</strong> in definierten Grenzen</li>
        </ul>
        
        <div class="info-box">
            <h3>💡 Wichtig</h3>
            <p>Jeder in Deutschland verkaufte Rauchmelder muss EN 14604 erfüllen. Es ist das Minimum - für mehr Qualität wählen Sie zusätzlich <a href="q-label.html">Q-Label</a>.</p>
        </div>
        
        <h2>Weitere Zertifikate</h2>
        <div class="related-links">
            <a href="q-label.html" class="related-link">Q-Label →</a>
            <a href="ce-kennzeichnung.html" class="related-link">CE-Kennzeichnung →</a>
            <a href="tuev-pruefung.html" class="related-link">TÜV-Prüfung →</a>
        </div>
'''
    },
    
    "tuev-pruefung.html": {
        "title": "TÜV-Prüfung bei Rauchmeldern | Unabhängige Sicherheit | Secu.li",
        "desc": "TÜV-geprüfte Rauchmelder bieten unabhängig bestätigte Sicherheit. Was die Prüfung bedeutet.",
        "h1": "TÜV-Prüfung",
        "badge": "🔍 Geprüft",
        "content": '''
        <h2>Was bedeutet TÜV-geprüft?</h2>
        <p>Der TÜV (Technischer Überwachungsverein) ist eine <strong>unabhängige Prüforganisation</strong> in Deutschland. TÜV-geprüfte Rauchmelder wurden von Experten auf Sicherheit und Qualität getestet.</p>
        
        <div style="text-align: center; margin: 40px 0;">
            <div style="display: inline-block; background: #3B82F6; color: white; padding: 25px 35px; border-radius: 10px; font-size: 2rem; font-weight: bold;">TÜV</div>
        </div>
        
        <h2>Was prüft der TÜV?</h2>
        <ul class="check-list">
            <li>Einhaltung der EN 14604 Norm</li>
            <li>Elektrische Sicherheit</li>
            <li>Mechanische Stabilität</li>
            <li>Rauch-Erkennungsleistung</li>
            <li>Alarmton-Lautstärke</li>
        </ul>
        
        <div class="info-box">
            <h3>💡 Vertrauenswürdig</h3>
            <p>TÜV-Prüfzeichen genießen in Deutschland hohes Vertrauen. Viele Versicherungen und Vermieter bevorzugen TÜV-geprüfte Melder.</p>
        </div>
        
        <h2>Weitere Zertifikate</h2>
        <div class="related-links">
            <a href="q-label.html" class="related-link">Q-Label →</a>
            <a href="ce-kennzeichnung.html" class="related-link">CE-Kennzeichnung →</a>
            <a href="en-14604.html" class="related-link">EN 14604 →</a>
        </div>
'''
    }
}

def main():
    print("Erstelle Unterseiten...")
    for filename, data in pages.items():
        filepath = BASE_DIR / filename
        html = get_subpage(data['title'], data['desc'], data['h1'], data['badge'], data['content'])
        filepath.write_text(html, encoding='utf-8')
        print(f"✓ {filename}")
    print(f"\n✅ {len(pages)} Unterseiten erstellt!")

if __name__ == "__main__":
    main()
