#!/usr/bin/env python3
"""
B2B Branchen × Stadt Generator für Secu.li
Erstellt SEO-optimierte Seiten für jede Branche in jeder deutschen Stadt
"""

import os
import re

# =======================
# BRANCHEN-DEFINITIONEN
# =======================
BRANCHEN = {
    # Immobilien & Verwaltung
    "immobilienverwaltung": {
        "name": "Immobilienverwaltungen",
        "icon": "🏢",
        "keywords": ["Immobilienverwaltung Rauchmelder", "Rauchmelder Immobilien", "Brandschutz Immobilienverwaltung"],
        "intro": "Als Immobilienverwaltung tragen Sie die Verantwortung für zahlreiche Objekte und deren Bewohner. Die Rauchmelderpflicht muss eingehalten werden.",
        "vorteile": ["Zentrale Dokumentation aller Objekte", "Automatische Wartungserinnerungen", "Sammelrechnungen für einfache Abwicklung"]
    },
    "hausverwaltung": {
        "name": "Hausverwaltungen", 
        "icon": "🏠",
        "keywords": ["Hausverwaltung Rauchmelder", "Rauchmelder Mietwohnung", "Brandschutz Hausverwaltung"],
        "intro": "Als Hausverwaltung koordinieren Sie die Rauchmelderpflicht für Ihre Wohnungsbestände. Wir übernehmen die komplette Abwicklung.",
        "vorteile": ["Terminkoordination mit Mietern", "Rechtssichere Dokumentation", "Fester Ansprechpartner"]
    },
    "wohnungsunternehmen": {
        "name": "Wohnungsunternehmen",
        "icon": "🏗️", 
        "keywords": ["Wohnungsunternehmen Rauchmelder", "Wohnungswirtschaft Brandschutz", "Rauchmelder Wohnbau"],
        "intro": "Wohnungsunternehmen mit großen Beständen benötigen effiziente Lösungen für die Rauchmelderpflicht.",
        "vorteile": ["Großmengen-Rabatte", "Rahmenverträge", "Digitale Objektverwaltung"]
    },
    "bautraeger": {
        "name": "Bauträger",
        "icon": "🏗️",
        "keywords": ["Bauträger Rauchmelder", "Neubau Rauchmelder", "Erstausstattung Rauchmelder"],
        "intro": "Als Bauträger müssen Sie Neubauten mit Rauchmeldern ausstatten. Wir liefern und installieren termingerecht.",
        "vorteile": ["Koordination mit Bauleitung", "Termingerechte Installation", "Übergabedokumentation"]
    },
    "architekturbuero": {
        "name": "Architekturbüros",
        "icon": "📐",
        "keywords": ["Architekt Rauchmelder", "Brandschutzplanung", "Rauchmelder Planung"],
        "intro": "Bereits in der Planungsphase sollte der Brandschutz berücksichtigt werden. Wir beraten Architekten zur optimalen Platzierung.",
        "vorteile": ["Beratung zur Platzierung", "Planungsunterstützung", "Ausschreibungstexte"]
    },
    "bauunternehmen": {
        "name": "Bauunternehmen",
        "icon": "👷",
        "keywords": ["Bauunternehmen Rauchmelder", "Baustelle Rauchmelder", "Rauchmelder Installation Neubau"],
        "intro": "Bauunternehmen benötigen zuverlässige Partner für die Rauchmelderinstallation im Bauablauf.",
        "vorteile": ["Flexible Terminierung", "Koordination mit Gewerken", "Schnelle Reaktionszeiten"]
    },
    "handwerksbetrieb": {
        "name": "Handwerksbetriebe",
        "icon": "🔧",
        "keywords": ["Handwerker Rauchmelder", "Handwerksbetrieb Brandschutz", "Rauchmelder Werkstatt"],
        "intro": "Handwerksbetriebe mit Werkstätten und Lagerräumen benötigen angepasste Brandschutzlösungen.",
        "vorteile": ["Geeignete Melder für Werkstätten", "Staubresistente Technologie", "Flexible Wartungszeiten"]
    },
    "elektrikerfirma": {
        "name": "Elektrikerfirmen",
        "icon": "⚡",
        "keywords": ["Elektriker Rauchmelder", "Elektrofirma Brandschutz", "Rauchmelder Elektroinstallation"],
        "intro": "Als Elektrofachbetrieb können Sie Ihren Kunden unseren Rauchmelderservice als Zusatzleistung anbieten.",
        "vorteile": ["Partnermodell möglich", "Subunternehmer-Konditionen", "Schulungen verfügbar"]
    },
    "facility-management": {
        "name": "Facility-Management-Firmen",
        "icon": "🔧",
        "keywords": ["Facility Management Rauchmelder", "FM Dienstleister Brandschutz", "Objektbetreuung Rauchmelder"],
        "intro": "Als FM-Dienstleister können Sie den Rauchmelderservice an uns outsourcen oder als Partner anbieten.",
        "vorteile": ["White-Label möglich", "API-Integration", "Digitales Reporting"]
    },
    # Industrie & Gewerbe
    "industriebetrieb": {
        "name": "Industriebetriebe",
        "icon": "🏭",
        "keywords": ["Industrie Rauchmelder", "Industriebetrieb Brandschutz", "Rauchmelder Produktion"],
        "intro": "Industriebetriebe haben besondere Anforderungen an den Brandschutz. Wir bieten passende Lösungen.",
        "vorteile": ["Robuste Industriemelder", "24/7 Service", "Wartung im laufenden Betrieb"]
    },
    "buerogebaeude": {
        "name": "Bürogebäude",
        "icon": "🏢",
        "keywords": ["Bürogebäude Rauchmelder", "Büro Brandschutz", "Rauchmelder Bürohaus"],
        "intro": "Bürogebäude benötigen flächendeckenden Brandschutz für alle Etagen und Bereiche.",
        "vorteile": ["Diskrete Installation", "Wartung außerhalb Bürozeiten", "Zentrale Dokumentation"]
    },
    "lagerhalle": {
        "name": "Lagerhallen",
        "icon": "📦",
        "keywords": ["Lagerhalle Rauchmelder", "Lager Brandschutz", "Rauchmelder Logistik"],
        "intro": "In Lagerhallen sind schnelle Brandentdeckung und große Reichweiten wichtig.",
        "vorteile": ["Hochleistungsmelder", "Große Überwachungsflächen", "Schnelle Reaktionszeiten"]
    },
    "fabrik": {
        "name": "Fabriken",
        "icon": "🏭",
        "keywords": ["Fabrik Rauchmelder", "Fabrikgebäude Brandschutz", "Rauchmelder Fertigung"],
        "intro": "Fabriken benötigen zuverlässigen Brandschutz, der auch unter schwierigen Bedingungen funktioniert.",
        "vorteile": ["Hitzebeständige Melder", "Staubresistent", "Integration möglich"]
    },
    "produktionsstaette": {
        "name": "Produktionsstätten",
        "icon": "⚙️",
        "keywords": ["Produktion Rauchmelder", "Produktionsstätte Brandschutz", "Rauchmelder Fertigung"],
        "intro": "In Produktionsstätten ist der Brandschutz besonders wichtig für Mitarbeiter und Anlagen.",
        "vorteile": ["Anlagenspezifische Lösungen", "Minimale Betriebsunterbrechung", "SLA-Garantie"]
    },
    # Gastgewerbe
    "hotel": {
        "name": "Hotels",
        "icon": "🏨",
        "keywords": ["Hotel Rauchmelder", "Hotelzimmer Brandschutz", "Rauchmelder Beherbergung"],
        "intro": "Hotels unterliegen strengen Brandschutzvorschriften. Wir sorgen für die Einhaltung.",
        "vorteile": ["Diskrete Montage", "Wartung außerhalb Stoßzeiten", "Behördenkonforme Dokumentation"]
    },
    "hostel": {
        "name": "Hostels",
        "icon": "🛏️",
        "keywords": ["Hostel Rauchmelder", "Hostelbetrieb Brandschutz", "Rauchmelder Unterkunft"],
        "intro": "Hostels benötigen zuverlässigen Brandschutz für Mehrbettzimmer und Gemeinschaftsräume.",
        "vorteile": ["Robuste Melder", "Schnelle Wartung", "Günstige Konditionen"]
    },
    "pension": {
        "name": "Pensionen",
        "icon": "🏡",
        "keywords": ["Pension Rauchmelder", "Pensionsbetrieb Brandschutz", "Rauchmelder Gästehaus"],
        "intro": "Auch kleine Beherbergungsbetriebe müssen die Brandschutzvorschriften einhalten.",
        "vorteile": ["Persönliche Betreuung", "Flexible Termine", "Faire Preise"]
    },
    "gastronomie": {
        "name": "Gastronomie",
        "icon": "🍽️",
        "keywords": ["Gastronomie Rauchmelder", "Restaurant Brandschutz", "Rauchmelder Gastro"],
        "intro": "Gastronomiebetriebe haben besondere Anforderungen durch Küchen und öffentlichen Verkehr.",
        "vorteile": ["Küchentaugliche Melder", "Fehlalarm-Prävention", "Schnelle Reaktion"]
    },
    "restaurant": {
        "name": "Restaurants",
        "icon": "🍴",
        "keywords": ["Restaurant Rauchmelder", "Restaurant Brandschutz", "Rauchmelder Gaststätte"],
        "intro": "Restaurants müssen Gäste und Personal vor Brandgefahren schützen.",
        "vorteile": ["Hitzeresistente Melder", "Diskrete Installation", "Wartung in Randzeiten"]
    },
    "imbiss": {
        "name": "Imbisse",
        "icon": "🍔",
        "keywords": ["Imbiss Rauchmelder", "Schnellrestaurant Brandschutz", "Rauchmelder Imbissbude"],
        "intro": "Auch Imbisse und Schnellrestaurants benötigen Brandschutz.",
        "vorteile": ["Kompakte Lösungen", "Schnelle Installation", "Günstige Preise"]
    },
    # Soziale Einrichtungen
    "pflegeheim": {
        "name": "Pflegeheime",
        "icon": "🏥",
        "keywords": ["Pflegeheim Rauchmelder", "Altenheim Brandschutz", "Rauchmelder Seniorenheim"],
        "intro": "Pflegeheime haben besondere Verantwortung für schutzbedürftige Bewohner.",
        "vorteile": ["Vernetzte Melder", "Leise Wartung", "Schulung für Personal"]
    },
    "kindergarten": {
        "name": "Kindergärten",
        "icon": "👶",
        "keywords": ["Kindergarten Rauchmelder", "Kita Brandschutz", "Rauchmelder Kindertagesstätte"],
        "intro": "Der Schutz von Kindern hat höchste Priorität. Wir sorgen für sicheren Brandschutz.",
        "vorteile": ["Kindersichere Montage", "Regelmäßige Prüfung", "Behördenkonforme Doku"]
    },
    "schule": {
        "name": "Schulen",
        "icon": "🏫",
        "keywords": ["Schule Rauchmelder", "Schulgebäude Brandschutz", "Rauchmelder Bildungseinrichtung"],
        "intro": "Schulen müssen umfassenden Brandschutz für Schüler und Personal gewährleisten.",
        "vorteile": ["Großflächenmontage", "Wartung in Ferien", "Vandalismus-resistente Melder"]
    },
    "krankenhaus": {
        "name": "Krankenhäuser",
        "icon": "🏥",
        "keywords": ["Krankenhaus Rauchmelder", "Klinik Brandschutz", "Rauchmelder Gesundheitswesen"],
        "intro": "Krankenhäuser erfordern höchste Brandschutzstandards für Patienten und medizinische Geräte.",
        "vorteile": ["24/7 Service", "Spezialmelder für OP-Bereiche", "Strenge Dokumentation"]
    },
    "notunterkunft": {
        "name": "Notunterkünfte",
        "icon": "🏠",
        "keywords": ["Notunterkunft Rauchmelder", "Flüchtlingsheim Brandschutz", "Rauchmelder Unterkunft"],
        "intro": "Notunterkünfte benötigen schnell installierbaren, zuverlässigen Brandschutz.",
        "vorteile": ["Schnelle Installation", "Robuste Melder", "Flexible Lösungen"]
    },
    # Handel & Dienstleistung  
    "einzelhaendler": {
        "name": "Einzelhändler",
        "icon": "🛍️",
        "keywords": ["Einzelhandel Rauchmelder", "Laden Brandschutz", "Rauchmelder Geschäft"],
        "intro": "Einzelhandelsgeschäfte müssen Kunden, Mitarbeiter und Waren schützen.",
        "vorteile": ["Diskrete Installation", "Wartung außerhalb Öffnungszeiten", "Schneller Service"]
    },
    "supermarkt": {
        "name": "Supermärkte",
        "icon": "🛒",
        "keywords": ["Supermarkt Rauchmelder", "Lebensmittelmarkt Brandschutz", "Rauchmelder Handel"],
        "intro": "Supermärkte mit großen Verkaufsflächen benötigen flächendeckenden Brandschutz.",
        "vorteile": ["Großflächenüberwachung", "Integration mit Haustechnik", "Wartungsverträge"]
    },
    "discounter": {
        "name": "Discounter",
        "icon": "💰",
        "keywords": ["Discounter Rauchmelder", "Discountmarkt Brandschutz", "Rauchmelder Filiale"],
        "intro": "Discounter mit vielen Filialen profitieren von unseren Rahmenverträgen.",
        "vorteile": ["Mengenrabatte", "Einheitliche Standards", "Zentrale Abrechnung"]
    },
    "tankstelle": {
        "name": "Tankstellen",
        "icon": "⛽",
        "keywords": ["Tankstelle Rauchmelder", "Tankstellenshop Brandschutz", "Rauchmelder Tankstellenbetrieb"],
        "intro": "Tankstellen erfordern besondere Brandschutzmaßnahmen wegen brennbarer Stoffe.",
        "vorteile": ["Explosionsgeschützte Melder", "24/7 Erreichbarkeit", "Schnelle Reaktion"]
    },
    "friseursalon": {
        "name": "Friseursalons",
        "icon": "💇",
        "keywords": ["Friseur Rauchmelder", "Friseursalon Brandschutz", "Rauchmelder Kosmetik"],
        "intro": "Auch Friseursalons müssen die Brandschutzanforderungen erfüllen.",
        "vorteile": ["Kompakte Lösungen", "Schnelle Installation", "Faire Preise"]
    },
    "nagelstudio": {
        "name": "Nagelstudios",
        "icon": "💅",
        "keywords": ["Nagelstudio Rauchmelder", "Kosmetikstudio Brandschutz", "Rauchmelder Beautysalon"],
        "intro": "Nagelstudios mit Chemikalien benötigen angepassten Brandschutz.",
        "vorteile": ["Chemikalienresistente Melder", "Individuelle Beratung", "Günstige Konditionen"]
    },
    "fitnessstudio": {
        "name": "Fitnessstudios",
        "icon": "🏋️",
        "keywords": ["Fitnessstudio Rauchmelder", "Sportstudio Brandschutz", "Rauchmelder Fitness"],
        "intro": "Fitnessstudios mit großen Trainingsflächen brauchen umfassenden Brandschutz.",
        "vorteile": ["Feuchtigkeitsresistent", "Große Reichweiten", "Wartung in Randzeiten"]
    },
    "sporthalle": {
        "name": "Sporthallen",
        "icon": "🏀",
        "keywords": ["Sporthalle Rauchmelder", "Turnhalle Brandschutz", "Rauchmelder Sportstätte"],
        "intro": "Sporthallen mit hohen Decken benötigen spezielle Brandschutzlösungen.",
        "vorteile": ["Hochdeckenmelder", "Großflächen-Coverage", "Wartung in Ferien"]
    },
    # Öffentlich & Events
    "verein": {
        "name": "Vereine",
        "icon": "👥",
        "keywords": ["Verein Rauchmelder", "Vereinsheim Brandschutz", "Rauchmelder Clubhaus"],
        "intro": "Vereine mit Vereinsheimen müssen für Brandschutz bei Veranstaltungen sorgen.",
        "vorteile": ["Günstige Konditionen", "Flexible Termine", "Ehrenamts-Rabatte"]
    },
    "gemeinde": {
        "name": "Gemeinden",
        "icon": "🏛️",
        "keywords": ["Gemeinde Rauchmelder", "Kommunaler Brandschutz", "Rauchmelder Gemeindebau"],
        "intro": "Gemeinden müssen öffentliche Gebäude und Einrichtungen brandschützen.",
        "vorteile": ["Rahmenverträge", "Öffentliche Ausschreibung", "Langfristige Partnerschaften"]
    },
    "behoerde": {
        "name": "Behörden",
        "icon": "🏛️",
        "keywords": ["Behörde Rauchmelder", "Amt Brandschutz", "Rauchmelder öffentliche Verwaltung"],
        "intro": "Behörden benötigen zuverlässigen Brandschutz für Mitarbeiter und Besucher.",
        "vorteile": ["Vergaberecht-konforme Angebote", "Dokumentation für Audits", "Langfristige Wartung"]
    },
    "oeffentliche-einrichtung": {
        "name": "Öffentliche Einrichtungen",
        "icon": "🏛️",
        "keywords": ["Öffentliche Einrichtung Rauchmelder", "Öffentlicher Bau Brandschutz", "Rauchmelder Kommune"],
        "intro": "Öffentliche Einrichtungen haben besondere Verantwortung für Besucher.",
        "vorteile": ["Hohe Sicherheitsstandards", "Regelmäßige Prüfungen", "Transparente Preise"]
    },
    "eventlocation": {
        "name": "Eventlocations",
        "icon": "🎉",
        "keywords": ["Eventlocation Rauchmelder", "Veranstaltungshalle Brandschutz", "Rauchmelder Event"],
        "intro": "Eventlocations mit wechselnden Veranstaltungen brauchen flexiblen Brandschutz.",
        "vorteile": ["Schnelle Reaktion bei Events", "Temporäre Lösungen", "Versicherungsnachweis"]
    },
    "messebauer": {
        "name": "Messebauer",
        "icon": "🎪",
        "keywords": ["Messebauer Rauchmelder", "Messestand Brandschutz", "Rauchmelder Messe"],
        "intro": "Messebauer benötigen temporäre Brandschutzlösungen für Messestände.",
        "vorteile": ["Temporäre Installation", "Schneller Auf-/Abbau", "Mobile Lösungen"]
    },
}

# =======================
# STÄDTE-DATEN
# =======================
STAEDTE = {
    "berlin": {"name": "Berlin", "land": "Berlin", "bezirke": ["Mitte", "Kreuzberg", "Prenzlauer Berg", "Charlottenburg", "Neukölln", "Spandau", "Steglitz", "Pankow"]},
    "hamburg": {"name": "Hamburg", "land": "Hamburg", "bezirke": ["Altona", "Eimsbüttel", "Hamburg-Nord", "Wandsbek", "Bergedorf", "Harburg", "Hamburg-Mitte"]},
    "muenchen": {"name": "München", "land": "Bayern", "bezirke": ["Schwabing", "Bogenhausen", "Sendling", "Pasing", "Trudering", "Neuhausen", "Laim", "Maxvorstadt"]},
    "koeln": {"name": "Köln", "land": "NRW", "bezirke": ["Innenstadt", "Ehrenfeld", "Nippes", "Lindenthal", "Rodenkirchen", "Chorweiler", "Porz", "Kalk"]},
    "frankfurt": {"name": "Frankfurt am Main", "land": "Hessen", "bezirke": ["Innenstadt", "Sachsenhausen", "Bornheim", "Bockenheim", "Nordend", "Westend", "Höchst"]},
    "stuttgart": {"name": "Stuttgart", "land": "Baden-Württemberg", "bezirke": ["Mitte", "Nord", "Ost", "Süd", "West", "Bad Cannstatt", "Vaihingen"]},
    "duesseldorf": {"name": "Düsseldorf", "land": "NRW", "bezirke": ["Altstadt", "Bilk", "Flingern", "Oberkassel", "Pempelfort", "Unterbilk", "Gerresheim"]},
    "dortmund": {"name": "Dortmund", "land": "NRW", "bezirke": ["Mitte", "Hörde", "Hombruch", "Aplerbeck", "Brackel", "Scharnhorst", "Eving"]},
    "essen": {"name": "Essen", "land": "NRW", "bezirke": ["Stadtmitte", "Rüttenscheid", "Steele", "Werden", "Kettwig", "Borbeck", "Altenessen"]},
    "leipzig": {"name": "Leipzig", "land": "Sachsen", "bezirke": ["Mitte", "Südvorstadt", "Connewitz", "Plagwitz", "Lindenau", "Gohlis", "Mockau"]},
    "bremen": {"name": "Bremen", "land": "Bremen", "bezirke": ["Mitte", "Neustadt", "Viertel", "Findorff", "Schwachhausen", "Horn-Lehe", "Vegesack"]},
    "dresden": {"name": "Dresden", "land": "Sachsen", "bezirke": ["Altstadt", "Neustadt", "Blasewitz", "Striesen", "Löbtau", "Cotta", "Pieschen"]},
    "hannover": {"name": "Hannover", "land": "Niedersachsen", "bezirke": ["Mitte", "Südstadt", "List", "Döhren", "Bothfeld", "Vahrenwald", "Linden-Nord"]},
    "nuernberg": {"name": "Nürnberg", "land": "Bayern", "bezirke": ["Altstadt", "Gostenhof", "Maxfeld", "Gleißhammer", "Mögeldorf", "Langwasser"]},
    "duisburg": {"name": "Duisburg", "land": "NRW", "bezirke": ["Mitte", "Hamborn", "Meiderich", "Homberg", "Rheinhausen", "Walsum"]},
    "bochum": {"name": "Bochum", "land": "NRW", "bezirke": ["Mitte", "Wattenscheid", "Langendreer", "Weitmar", "Gerthe", "Querenburg"]},
    "wuppertal": {"name": "Wuppertal", "land": "NRW", "bezirke": ["Elberfeld", "Barmen", "Vohwinkel", "Cronenberg", "Ronsdorf", "Langerfeld"]},
    "bielefeld": {"name": "Bielefeld", "land": "NRW", "bezirke": ["Mitte", "Schildesche", "Gadderbaum", "Brackwede", "Dornberg", "Jöllenbeck"]},
    "bonn": {"name": "Bonn", "land": "NRW", "bezirke": ["Zentrum", "Beuel", "Bad Godesberg", "Hardtberg", "Poppelsdorf", "Endenich"]},
    "muenster": {"name": "Münster", "land": "NRW", "bezirke": ["Altstadt", "Aegidii", "Geist", "Hiltrup", "Gievenbeck", "Roxel"]},
    "karlsruhe": {"name": "Karlsruhe", "land": "Baden-Württemberg", "bezirke": ["Innenstadt", "Südstadt", "Weststadt", "Mühlburg", "Durlach"]},
    "mannheim": {"name": "Mannheim", "land": "Baden-Württemberg", "bezirke": ["Innenstadt", "Neckarstadt", "Lindenhof", "Schwetzingerstadt", "Feudenheim"]},
    "augsburg": {"name": "Augsburg", "land": "Bayern", "bezirke": ["Innenstadt", "Lechhausen", "Oberhausen", "Haunstetten", "Göggingen"]},
    "wiesbaden": {"name": "Wiesbaden", "land": "Hessen", "bezirke": ["Mitte", "Biebrich", "Dotzheim", "Schierstein", "Kostheim"]},
    "aachen": {"name": "Aachen", "land": "NRW", "bezirke": ["Mitte", "Burtscheid", "Brand", "Eilendorf", "Haaren"]},
    "braunschweig": {"name": "Braunschweig", "land": "Niedersachsen", "bezirke": ["Innenstadt", "Weststadt", "Östliches Ringgebiet", "Lehndorf"]},
    "kiel": {"name": "Kiel", "land": "Schleswig-Holstein", "bezirke": ["Altstadt", "Gaarden", "Wik", "Düsternbrook", "Hassee"]},
    "chemnitz": {"name": "Chemnitz", "land": "Sachsen", "bezirke": ["Zentrum", "Kaßberg", "Schloßchemnitz", "Sonnenberg"]},
    "magdeburg": {"name": "Magdeburg", "land": "Sachsen-Anhalt", "bezirke": ["Altstadt", "Stadtfeld", "Buckau", "Sudenburg"]},
    "freiburg": {"name": "Freiburg", "land": "Baden-Württemberg", "bezirke": ["Altstadt", "Wiehre", "Herdern", "Stühlinger"]},
    "krefeld": {"name": "Krefeld", "land": "NRW", "bezirke": ["Mitte", "Bockum", "Uerdingen", "Hüls"]},
    "mainz": {"name": "Mainz", "land": "Rheinland-Pfalz", "bezirke": ["Altstadt", "Neustadt", "Oberstadt", "Hartenberg"]},
    "rostock": {"name": "Rostock", "land": "Mecklenburg-Vorpommern", "bezirke": ["Stadtmitte", "Warnemünde", "Lichtenhagen"]},
    "erfurt": {"name": "Erfurt", "land": "Thüringen", "bezirke": ["Altstadt", "Löbervorstadt", "Brühlervorstadt"]},
    "kassel": {"name": "Kassel", "land": "Hessen", "bezirke": ["Mitte", "Vorderer Westen", "Bad Wilhelmshöhe"]},
    "halle": {"name": "Halle", "land": "Sachsen-Anhalt", "bezirke": ["Altstadt", "Neustadt", "Giebichenstein"]},
    "potsdam": {"name": "Potsdam", "land": "Brandenburg", "bezirke": ["Innenstadt", "Babelsberg", "Potsdam West"]},
    "saarbruecken": {"name": "Saarbrücken", "land": "Saarland", "bezirke": ["Alt-Saarbrücken", "St. Johann", "Malstatt"]},
    "oldenburg": {"name": "Oldenburg", "land": "Niedersachsen", "bezirke": ["Innenstadt", "Eversten", "Kreyenbrück"]},
    "osnabrueck": {"name": "Osnabrück", "land": "Niedersachsen", "bezirke": ["Innenstadt", "Wüste", "Schinkel"]},
    "heidelberg": {"name": "Heidelberg", "land": "Baden-Württemberg", "bezirke": ["Altstadt", "Bergheim", "Weststadt"]},
    "darmstadt": {"name": "Darmstadt", "land": "Hessen", "bezirke": ["Mitte", "Bessungen", "Martinsviertel"]},
    "regensburg": {"name": "Regensburg", "land": "Bayern", "bezirke": ["Altstadt", "Stadtamhof", "Steinweg"]},
    "wuerzburg": {"name": "Würzburg", "land": "Bayern", "bezirke": ["Altstadt", "Sanderau", "Grombühl"]},
    "wolfsburg": {"name": "Wolfsburg", "land": "Niedersachsen", "bezirke": ["Stadtmitte", "Nordstadt", "Westhagen"]},
    "ulm": {"name": "Ulm", "land": "Baden-Württemberg", "bezirke": ["Mitte", "Weststadt", "Oststadt"]},
    "heilbronn": {"name": "Heilbronn", "land": "Baden-Württemberg", "bezirke": ["Innenstadt", "Sontheim", "Neckargartach"]},
    "pforzheim": {"name": "Pforzheim", "land": "Baden-Württemberg", "bezirke": ["Innenstadt", "Nordstadt", "Oststadt"]},
    "goettingen": {"name": "Göttingen", "land": "Niedersachsen", "bezirke": ["Innenstadt", "Weende", "Grone"]},
    "reutlingen": {"name": "Reutlingen", "land": "Baden-Württemberg", "bezirke": ["Innenstadt", "Ringelbach", "Gönningen"]},
    "koblenz": {"name": "Koblenz", "land": "Rheinland-Pfalz", "bezirke": ["Altstadt", "Südliche Vorstadt", "Ehrenbreitstein"]},
    "jena": {"name": "Jena", "land": "Thüringen", "bezirke": ["Zentrum", "Jena-Nord", "Jena-Ost"]},
    "trier": {"name": "Trier", "land": "Rheinland-Pfalz", "bezirke": ["Mitte", "Süd", "West"]},
    "erlangen": {"name": "Erlangen", "land": "Bayern", "bezirke": ["Innenstadt", "Röthelheim", "Alterlangen"]},
    "hildesheim": {"name": "Hildesheim", "land": "Niedersachsen", "bezirke": ["Mitte", "Nordstadt", "Oststadt"]},
    "cottbus": {"name": "Cottbus", "land": "Brandenburg", "bezirke": ["Mitte", "Sandow", "Spremberger Vorstadt"]},
    "schwerin": {"name": "Schwerin", "land": "Mecklenburg-Vorpommern", "bezirke": ["Altstadt", "Paulsstadt", "Feldstadt"]},
}

# Import template
from b2b_template import TEMPLATE, slugify

def generate_pages(include_bezirke=False):
    """
    Generiert alle B2B Branchen x Stadt Seiten
    include_bezirke: Wenn True, auch Ortsteil-Seiten generieren
    """
    base_dir = "standorte/gewerbe"
    os.makedirs(base_dir, exist_ok=True)
    
    total_count = 0
    
    for branche_slug, branche_data in BRANCHEN.items():
        branche_name = branche_data["name"]
        icon = branche_data["icon"]
        keywords = branche_data["keywords"]
        intro = branche_data["intro"]
        vorteile = branche_data["vorteile"]
        
        # Erstelle Branche-Ordner
        branche_dir = os.path.join(base_dir, branche_slug)
        os.makedirs(branche_dir, exist_ok=True)
        
        for stadt_slug, stadt_data in STAEDTE.items():
            stadt = stadt_data["name"]
            land = stadt_data["land"]
            bezirke = stadt_data.get("bezirke", [])
            
            # Bezirke HTML generieren
            bezirke_html = ""
            for bezirk in bezirke[:6]:  # Max 6 Bezirke anzeigen
                bezirke_html += f'<div class="feature-card-pro"><h4>{bezirk}</h4><p>Service für {branche_name} verfügbar</p></div>\n'
            
            # Related Branches HTML
            related = list(BRANCHEN.keys())[:8]
            related_html = ""
            for rel in related:
                if rel != branche_slug:
                    rel_name = BRANCHEN[rel]["name"]
                    related_html += f'<li><a href="../{rel}/{stadt_slug}.html" style="color: var(--primary);">→ {rel_name} in {stadt}</a></li>\n'
            
            # Template befüllen
            content = TEMPLATE.format(
                branche_name=branche_name,
                branche_slug=branche_slug,
                stadt=stadt,
                stadt_slug=stadt_slug,
                land=land,
                icon=icon,
                keywords_str=", ".join(keywords),
                intro_text=intro,
                vorteil_1=vorteile[0] if len(vorteile) > 0 else "Professioneller Service",
                vorteil_2=vorteile[1] if len(vorteile) > 1 else "Schnelle Reaktionszeiten",
                vorteil_3=vorteile[2] if len(vorteile) > 2 else "Transparente Preise",
                bezirke_html=bezirke_html,
                related_branches_html=related_html
            )
            
            # Seite speichern
            filepath = os.path.join(branche_dir, f"{stadt_slug}.html")
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            
            total_count += 1
            
            # Optional: Bezirk-Seiten
            if include_bezirke:
                for bezirk in bezirke:
                    bezirk_slug = slugify(bezirk)
                    bezirk_content = content.replace(
                        f"<h1>Rauchmelder für {branche_name} in {stadt}</h1>",
                        f"<h1>Rauchmelder für {branche_name} in {stadt}-{bezirk}</h1>"
                    ).replace(
                        f"Service für {branche_name} in {stadt}",
                        f"Service für {branche_name} in {stadt}-{bezirk}"
                    )
                    
                    bezirk_filepath = os.path.join(branche_dir, f"{stadt_slug}-{bezirk_slug}.html")
                    with open(bezirk_filepath, "w", encoding="utf-8") as f:
                        f.write(bezirk_content)
                    total_count += 1
        
        print(f"✅ {branche_name}: {len(STAEDTE)} Städte")
    
    print(f"\n🎉 Insgesamt {total_count} Seiten generiert!")
    print(f"   Branchen: {len(BRANCHEN)}")
    print(f"   Städte: {len(STAEDTE)}")
    return total_count

if __name__ == "__main__":
    import sys
    include_bezirke = "--bezirke" in sys.argv
    generate_pages(include_bezirke=include_bezirke)
