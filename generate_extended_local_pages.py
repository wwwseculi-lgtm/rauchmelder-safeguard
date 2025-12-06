#!/usr/bin/env python3
"""
Erweiterte lokale SEO-Seiten für Deutschland
Generiert zusätzliche Seiten für Stadtteile, Bezirke, Vororte und Kleinstädte
"""

import os
import random
from pathlib import Path

OUTPUT_DIR = Path("/Users/neslihanakdeniz/Desktop/Rauchmelder/standorte/deutschland")

# Erweiterte Daten: Großstädte mit Stadtteilen
CITY_DISTRICTS = {
    "Berlin": {
        "bundesland": "Berlin",
        "stadtteile": [
            "Mitte", "Prenzlauer Berg", "Pankow", "Weißensee", "Friedrichshain", 
            "Kreuzberg", "Neukölln", "Treptow", "Köpenick", "Lichtenberg",
            "Hohenschönhausen", "Marzahn", "Hellersdorf", "Charlottenburg",
            "Wilmersdorf", "Spandau", "Steglitz", "Zehlendorf", "Tempelhof",
            "Schöneberg", "Reinickendorf", "Wedding", "Moabit", "Tiergarten",
            "Grunewald", "Dahlem", "Wannsee", "Frohnau", "Hermsdorf", "Tegel",
            "Lübars", "Waidmannslust", "Wittenau", "Borsigwalde", "Märkisches Viertel",
            "Rosenthal", "Blankenburg", "Heinersdorf", "Karow", "Buch", "Französisch Buchholz",
            "Niederschönhausen", "Wilhelmsruh", "Schönholz", "Blankenfelde", "Malchow"
        ]
    },
    "Hamburg": {
        "bundesland": "Hamburg",
        "stadtteile": [
            "Altona", "Eimsbüttel", "Hamburg-Nord", "Wandsbek", "Bergedorf",
            "Harburg", "St. Pauli", "St. Georg", "Ottensen", "Eppendorf",
            "Winterhude", "Barmbek", "Blankenese", "Nienstedten", "Finkenwerder",
            "Wilhelmsburg", "Veddel", "Rothenburgsort", "Billstedt", "Horn",
            "Hamm", "Borgfelde", "Hohenfelde", "Uhlenhorst", "Eilbek",
            "Marienthal", "Jenfeld", "Tonndorf", "Farmsen", "Bramfeld",
            "Steilshoop", "Ohlsdorf", "Fuhlsbüttel", "Langenhorn", "Schnelsen",
            "Niendorf", "Lokstedt", "Stellingen", "Bahrenfeld", "Lurup",
            "Osdorf", "Iserbrook", "Sülldorf", "Rissen"
        ]
    },
    "München": {
        "bundesland": "Bayern",
        "stadtteile": [
            "Altstadt-Lehel", "Ludwigsvorstadt-Isarvorstadt", "Maxvorstadt", "Schwabing-West",
            "Au-Haidhausen", "Sendling", "Sendling-Westpark", "Schwanthalerhöhe",
            "Neuhausen-Nymphenburg", "Moosach", "Milbertshofen-Am Hart", "Schwabing-Freimann",
            "Bogenhausen", "Berg am Laim", "Trudering-Riem", "Ramersdorf-Perlach",
            "Obergiesing-Fasangarten", "Untergiesing-Harlaching", "Thalkirchen-Obersendling",
            "Hadern", "Pasing-Obermenzing", "Aubing-Lochhausen-Langwied", "Allach-Untermenzing",
            "Feldmoching-Hasenbergl", "Laim", "Giesing", "Haidhausen", "Bogenhausen"
        ]
    },
    "Köln": {
        "bundesland": "NRW",
        "stadtteile": [
            "Innenstadt", "Rodenkirchen", "Lindenthal", "Ehrenfeld", "Nippes",
            "Chorweiler", "Porz", "Kalk", "Mülheim", "Deutz", "Poll", "Westhoven",
            "Zündorf", "Langel", "Godorf", "Rondorf", "Hahnwald", "Marienburg",
            "Bayenthal", "Sülz", "Klettenberg", "Lövenich", "Müngersdorf", "Braunsfeld",
            "Bickendorf", "Ossendorf", "Neuehrenfeld", "Nippes", "Bilderstöckchen",
            "Mauenheim", "Niehl", "Riehl", "Weidenpesch", "Longerich"
        ]
    },
    "Frankfurt": {
        "bundesland": "Hessen",
        "stadtteile": [
            "Altstadt", "Innenstadt", "Bahnhofsviertel", "Westend", "Nordend",
            "Ostend", "Bornheim", "Sachsenhausen", "Oberrad", "Niederrad",
            "Schwanheim", "Goldstein", "Griesheim", "Nied", "Höchst",
            "Unterliederbach", "Zeilsheim", "Sindlingen", "Rödelheim", "Hausen",
            "Praunheim", "Heddernheim", "Niederursel", "Ginnheim", "Dornbusch",
            "Eschersheim", "Eckenheim", "Preungesheim", "Bonames", "Nieder-Eschbach",
            "Nieder-Erlenbach", "Harheim", "Kalbach-Riedberg", "Berkersheim", "Riederwald",
            "Fechenheim", "Enkheim", "Seckbach", "Bergen"
        ]
    },
    "Stuttgart": {
        "bundesland": "Baden-Württemberg",
        "stadtteile": [
            "Mitte", "Nord", "Ost", "Süd", "West", "Bad Cannstatt", "Birkach",
            "Botnang", "Degerloch", "Feuerbach", "Hedelfingen", "Möhringen",
            "Mühlhausen", "Münster", "Obertürkheim", "Plieningen", "Sillenbuch",
            "Stammheim", "Untertürkheim", "Vaihingen", "Wangen", "Weilimdorf",
            "Zuffenhausen"
        ]
    },
    "Düsseldorf": {
        "bundesland": "NRW",
        "stadtteile": [
            "Altstadt", "Carlstadt", "Stadtmitte", "Pempelfort", "Derendorf",
            "Golzheim", "Flingern", "Düsseltal", "Mörsenbroich", "Rath",
            "Unterrath", "Lichtenbroich", "Lohausen", "Stockum", "Oberkassel",
            "Niederkassel", "Heerdt", "Lörick", "Bilk", "Unterbilk",
            "Hafen", "Hamm", "Flehe", "Volmerswerth", "Oberbilk",
            "Eller", "Lierenfeld", "Vennhausen", "Unterbach", "Gerresheim",
            "Grafenberg", "Ludenberg", "Hubbelrath", "Knittkuhl", "Benrath",
            "Urdenbach", "Wersten", "Himmelgeist", "Holthausen", "Reisholz",
            "Hassels", "Garath", "Hellerhof"
        ]
    },
    "Dortmund": {
        "bundesland": "NRW",
        "stadtteile": [
            "Innenstadt", "Hörde", "Hombruch", "Lütgendortmund", "Eving",
            "Scharnhorst", "Brackel", "Aplerbeck", "Mengede", "Huckarde",
            "Dorstfeld", "Westerfilde", "Bodelschwingh", "Nette", "Oestrich"
        ]
    },
    "Essen": {
        "bundesland": "NRW",
        "stadtteile": [
            "Stadtmitte", "Rüttenscheid", "Werden", "Kettwig", "Bredeney",
            "Margarethenhöhe", "Holsterhausen", "Frohnhausen", "Altendorf",
            "Borbeck", "Bergeborbeck", "Bochold", "Steele", "Kray",
            "Horst", "Burgaltendorf", "Überruhr", "Kupferdreh", "Fischlaken",
            "Heisingen"
        ]
    },
    "Leipzig": {
        "bundesland": "Sachsen",
        "stadtteile": [
            "Mitte", "Zentrum", "Schönefeld", "Volkmarsdorf", "Sellerhausen",
            "Stötteritz", "Probstheida", "Connewitz", "Plagwitz", "Lindenau",
            "Leutzsch", "Böhlitz-Ehrenberg", "Grünau", "Schleußig", "Gohlis",
            "Eutritzsch", "Mockau", "Thekla", "Wiederitzsch", "Lindenthal",
            "Paunsdorf", "Engelsdorf", "Mölkau"
        ]
    },
    "Bremen": {
        "bundesland": "Bremen",
        "stadtteile": [
            "Mitte", "Süd", "Ost", "West", "Nord", "Schwachhausen", "Vahr",
            "Horn-Lehe", "Borgfeld", "Oberneuland", "Osterholz", "Hemelingen",
            "Neustadt", "Obervieland", "Huchting", "Woltmershausen", "Gröpelingen",
            "Walle", "Findorff", "Burglesum", "Vegesack", "Blumenthal"
        ]
    },
    "Dresden": {
        "bundesland": "Sachsen",
        "stadtteile": [
            "Altstadt", "Neustadt", "Blasewitz", "Loschwitz", "Weißer Hirsch",
            "Striesen", "Gruna", "Seidnitz", "Tolkewitz", "Laubegast",
            "Kleinzschachwitz", "Pillnitz", "Plauen", "Mockritz", "Coschütz",
            "Gittersee", "Prohlis", "Reick", "Strehlen", "Südvorstadt",
            "Cotta", "Löbtau", "Naußlitz", "Gorbitz", "Briesnitz",
            "Pieschen", "Trachau", "Mickten", "Kaditz", "Übigau"
        ]
    },
    "Hannover": {
        "bundesland": "Niedersachsen",
        "stadtteile": [
            "Mitte", "Calenberger Neustadt", "Nordstadt", "Südstadt", "Bult",
            "Zoo", "Oststadt", "List", "Vahrenwald", "Vahrenheide", "Sahlkamp",
            "Bothfeld", "Isernhagen-Süd", "Lahe", "Groß-Buchholz", "Kleefeld",
            "Heideviertel", "Kirchrode", "Döhren", "Wülfel", "Mittelfeld",
            "Seelhorst", "Bemerode", "Anderten", "Misburg", "Stöcken",
            "Marienwerder", "Ledeburg", "Burg", "Leinhausen", "Herrenhausen",
            "Linden", "Limmer", "Davenstedt", "Badenstedt", "Bornum",
            "Ricklingen", "Oberricklingen", "Mühlenberg", "Wettbergen"
        ]
    },
    "Nürnberg": {
        "bundesland": "Bayern",
        "stadtteile": [
            "Altstadt", "St. Lorenz", "St. Sebald", "Wöhrd", "Gostenhof",
            "Steinbühl", "Südstadt", "Schweinau", "Gibitzenhof", "Sandreuth",
            "Langwasser", "Hasenbuck", "Rangierbahnhof-Siedlung", "Katzwang",
            "Kornburg", "Worzeldorf", "Herpersdorf", "Eibach", "Maiach",
            "Röthenbach", "Reichelsdorf", "Krottenbach", "Mühlhof", "Gebersdorf",
            "Großreuth", "Kleinreuth", "Höfen", "Gaismannshof", "Buch",
            "Thon", "Almoshof", "Lohe", "Kraftshof", "Neunhof",
            "Boxdorf", "Großgründlach", "Kleingründlach", "Schnepfenreuth",
            "Fischbach", "Brunn", "Altenfurt", "Moorenbrunn", "Zerzabelshof"
        ]
    }
}

# Weitere Kleinstädte und Gemeinden nach Bundesland
SMALL_TOWNS = {
    "Bayern": [
        "Erding", "Freising", "Dachau", "Starnberg", "Fürstenfeldbruck", "Ebersberg",
        "Bad Aibling", "Rosenheim Stadt", "Wasserburg am Inn", "Mühldorf am Inn",
        "Altötting", "Burghausen", "Traunreut", "Traunstein", "Bad Reichenhall",
        "Berchtesgaden", "Prien am Chiemsee", "Wolfratshausen", "Geretsried",
        "Bad Tölz", "Lenggries", "Miesbach", "Holzkirchen", "Garmisch-Partenkirchen",
        "Mittenwald", "Murnau am Staffelsee", "Weilheim", "Penzberg", "Tutzing",
        "Herrsching am Ammersee", "Landsberg am Lech", "Schongau", "Marktoberdorf",
        "Kaufbeuren", "Buchloe", "Mindelheim", "Bad Wörishofen", "Krumbach",
        "Günzburg", "Dillingen an der Donau", "Donauwörth", "Nördlingen", "Rain",
        "Neuburg an der Donau", "Schrobenhausen", "Aichach", "Friedberg", "Mering"
    ],
    "Baden-Württemberg": [
        "Ludwigsburg Stadt", "Kornwestheim", "Bietigheim-Bissingen", "Leonberg",
        "Sindelfingen", "Böblingen", "Herrenberg", "Nagold", "Calw", "Pforzheim Stadt",
        "Mühlacker", "Vaihingen an der Enz", "Bretten", "Bruchsal", "Ettlingen",
        "Rastatt", "Bühl", "Achern", "Kehl", "Offenburg Stadt", "Lahr",
        "Emmendingen", "Waldkirch", "Titisee-Neustadt", "Lörrach", "Weil am Rhein",
        "Rheinfelden", "Bad Säckingen", "Waldshut-Tiengen", "Konstanz Stadt",
        "Radolfzell", "Singen", "Stockach", "Überlingen", "Friedrichshafen",
        "Ravensburg Stadt", "Weingarten", "Biberach an der Riß", "Laupheim",
        "Ehingen", "Ulm Innenstadt", "Ulm Söflingen", "Ulm Wiblingen",
        "Göppingen Stadt", "Geislingen an der Steige", "Schwäbisch Gmünd",
        "Aalen", "Ellwangen", "Heidenheim an der Brenz", "Neckarsulm",
        "Heilbronn Stadt", "Weinsberg", "Öhringen", "Künzelsau", "Schwäbisch Hall"
    ],
    "NRW": [
        "Aachen Stadt", "Stolberg", "Eschweiler", "Düren", "Jülich", "Erkelenz",
        "Heinsberg", "Geilenkirchen", "Mönchengladbach Stadt", "Rheydt", "Wickrath",
        "Viersen", "Nettetal", "Kempen", "Krefeld Stadt", "Willich", "Tönisvorst",
        "Neuss Stadt", "Dormagen", "Grevenbroich", "Korschenbroich", "Meerbusch",
        "Remscheid", "Solingen Stadt", "Wuppertal Elberfeld", "Wuppertal Barmen",
        "Velbert", "Wülfrath", "Mettmann", "Erkrath", "Hilden", "Haan", "Langenfeld",
        "Monheim am Rhein", "Leverkusen Stadt", "Bergisch Gladbach", "Overath",
        "Rösrath", "Siegburg", "Sankt Augustin", "Troisdorf", "Hennef", "Königswinter",
        "Bad Honnef", "Bonn Beuel", "Bonn Bad Godesberg", "Bonn Innenstadt",
        "Meckenheim", "Rheinbach", "Euskirchen", "Erftstadt", "Kerpen", "Bergheim",
        "Bedburg", "Pulheim", "Frechen", "Hürth", "Brühl", "Wesseling",
        "Bochum Stadt", "Herne", "Castrop-Rauxel", "Recklinghausen", "Marl",
        "Haltern am See", "Dorsten", "Gladbeck", "Bottrop", "Oberhausen",
        "Mülheim an der Ruhr", "Ratingen", "Duisburg Meiderich", "Duisburg Hamborn",
        "Duisburg Homberg", "Dinslaken", "Moers", "Kamp-Lintfort", "Neukirchen-Vluyn",
        "Wesel", "Xanten", "Kleve", "Emmerich am Rhein", "Geldern", "Kevelaer"
    ],
    "Niedersachsen": [
        "Braunschweig Stadt", "Wolfsburg Stadt", "Salzgitter", "Gifhorn", "Peine",
        "Helmstedt", "Wolfenbüttel", "Goslar", "Bad Harzburg", "Clausthal-Zellerfeld",
        "Osterode am Harz", "Northeim", "Einbeck", "Göttingen Stadt", "Duderstadt",
        "Holzminden", "Hameln", "Bad Pyrmont", "Rinteln", "Bückeburg", "Stadthagen",
        "Minden", "Bad Oeynhausen", "Herford", "Löhne", "Vlotho", "Bad Salzuflen",
        "Lemgo", "Detmold", "Lage", "Blomberg", "Schieder-Schwalenberg",
        "Hildesheim Stadt", "Sarstedt", "Alfeld", "Elze", "Gronau", "Burgdorf",
        "Lehrte", "Sehnde", "Laatzen", "Ronnenberg", "Gehrden", "Barsinghausen",
        "Wunstorf", "Neustadt am Rübenberge", "Garbsen", "Langenhagen", "Isernhagen",
        "Burgwedel", "Wedemark", "Celle", "Bergen", "Soltau", "Munster",
        "Uelzen", "Bad Bevensen", "Lüneburg Stadt", "Winsen an der Luhe", "Buchholz",
        "Tostedt", "Buxtehude", "Stade", "Bremervörde", "Zeven", "Rotenburg Wümme",
        "Verden", "Achim", "Delmenhorst", "Wildeshausen", "Cloppenburg", "Vechta",
        "Diepholz", "Sulingen", "Nienburg", "Loccum", "Stolzenau"
    ],
    "Hessen": [
        "Darmstadt Stadt", "Bensheim", "Heppenheim", "Viernheim", "Lampertheim",
        "Lorsch", "Mörlenbach", "Rimbach", "Fürth", "Michelstadt", "Erbach",
        "Bad König", "Groß-Umstadt", "Dieburg", "Babenhausen", "Seligenstadt",
        "Hanau Stadt", "Maintal", "Bruchköbel", "Langenselbold", "Gelnhausen",
        "Schlüchtern", "Steinau an der Straße", "Bad Soden-Salmünster", "Wächtersbach",
        "Offenbach am Main", "Obertshausen", "Heusenstamm", "Dietzenbach", "Dreieich",
        "Langen", "Egelsbach", "Neu-Isenburg", "Mörfelden-Walldorf", "Rüsselsheim",
        "Groß-Gerau", "Raunheim", "Kelsterbach", "Bad Vilbel", "Karben",
        "Bad Homburg vor der Höhe", "Oberursel", "Kronberg im Taunus", "Königstein",
        "Friedberg Hessen", "Bad Nauheim", "Butzbach", "Lich", "Hungen",
        "Gießen Stadt", "Wetzlar", "Herborn", "Dillenburg", "Haiger",
        "Marburg Stadt", "Kirchhain", "Stadtallendorf", "Gladenbach", "Biedenkopf",
        "Fulda Stadt", "Hünfeld", "Eiterfeld", "Bebra", "Bad Hersfeld",
        "Alsfeld", "Lauterbach", "Schlitz", "Homberg Efze", "Fritzlar",
        "Bad Wildungen", "Frankenberg Eder", "Korbach", "Bad Arolsen", "Volkmarsen",
        "Hofgeismar", "Wolfhagen", "Baunatal", "Vellmar", "Kassel Stadt"
    ],
    "Rheinland-Pfalz": [
        "Mainz Stadt", "Ingelheim am Rhein", "Bingen am Rhein", "Bad Kreuznach",
        "Idar-Oberstein", "Birkenfeld", "Kirn", "Simmern", "Kirchberg", "Kastellaun",
        "Boppard", "St. Goar", "St. Goarshausen", "Koblenz Stadt", "Lahnstein",
        "Bendorf", "Neuwied", "Andernach", "Mayen", "Mendig", "Polch",
        "Cochem", "Zell Mosel", "Traben-Trarbach", "Bernkastel-Kues", "Wittlich",
        "Trier Stadt", "Konz", "Saarburg", "Hermeskeil", "Bitburg", "Prüm",
        "Worms", "Alzey", "Kirchheimbolanden", "Rockenhausen", "Kaiserslautern Stadt",
        "Landstuhl", "Ramstein-Miesenbach", "Kusel", "Lauterecken", "Pirmasens",
        "Zweibrücken", "Homburg", "Bexbach", "Neunkirchen Saar", "Spiesen-Elversberg",
        "Ludwigshafen am Rhein", "Frankenthal Pfalz", "Speyer", "Neustadt an der Weinstraße",
        "Landau in der Pfalz", "Bad Bergzabern", "Germersheim"
    ],
    "Schleswig-Holstein": [
        "Kiel Stadt", "Kronshagen", "Altenholz", "Mettenhof", "Wellsee",
        "Neumünster", "Rendsburg", "Eckernförde", "Schleswig", "Flensburg Stadt",
        "Harrislee", "Glücksburg", "Husum", "Tönning", "Friedrichstadt", "Heide",
        "Meldorf", "Brunsbüttel", "Itzehoe", "Elmshorn", "Pinneberg", "Uetersen",
        "Wedel", "Quickborn", "Norderstedt", "Ahrensburg", "Bargteheide", "Bad Oldesloe",
        "Reinbek", "Geesthacht", "Lauenburg Elbe", "Schwarzenbek", "Ratzeburg",
        "Mölln", "Bad Segeberg", "Kaltenkirchen", "Henstedt-Ulzburg", "Bad Bramstedt",
        "Neumünster", "Bordesholm", "Plön", "Preetz", "Lübeck Stadt", "Travemünde",
        "Bad Schwartau", "Stockelsdorf", "Eutin", "Bad Malente", "Timmendorfer Strand",
        "Scharbeutz", "Neustadt in Holstein", "Oldenburg in Holstein", "Heiligenhafen"
    ],
    "Sachsen": [
        "Chemnitz Stadt", "Freiberg", "Mittweida", "Döbeln", "Riesa", "Großenhain",
        "Meißen", "Radebeul", "Coswig", "Freital", "Pirna", "Heidenau",
        "Dippoldiswalde", "Altenberg", "Bautzen", "Kamenz", "Radeberg", "Bischofswerda",
        "Neustadt in Sachsen", "Sebnitz", "Bad Schandau", "Königstein", "Görlitz Stadt",
        "Zittau", "Löbau", "Niesky", "Weißwasser", "Hoyerswerda", "Schwarzheide",
        "Senftenberg", "Spremberg", "Forst Lausitz", "Cottbus Stadt", "Guben",
        "Zwickau Stadt", "Werdau", "Crimmitschau", "Glauchau", "Meerane", "Limbach-Oberfrohna",
        "Stollberg", "Aue", "Schwarzenberg", "Annaberg-Buchholz", "Marienberg",
        "Freiberg", "Brand-Erbisdorf", "Frankenberg Sachsen", "Flöha", "Oederan",
        "Plauen", "Reichenbach im Vogtland", "Auerbach", "Oelsnitz Vogtland", "Klingenthal"
    ],
    "Thüringen": [
        "Erfurt Stadt", "Weimar", "Jena", "Gera", "Gotha", "Eisenach",
        "Mühlhausen", "Nordhausen", "Sondershausen", "Artern", "Sangerhausen",
        "Schmalkalden", "Meiningen", "Suhl", "Zella-Mehlis", "Ilmenau",
        "Arnstadt", "Bad Langensalza", "Bad Salzungen", "Waltershausen", "Friedrichroda",
        "Saalfeld", "Rudolstadt", "Bad Blankenburg", "Pößneck", "Neustadt an der Orla",
        "Greiz", "Zeulenroda-Triebes", "Schleiz", "Sonneberg", "Neuhaus am Rennweg",
        "Hildburghausen", "Eisfeld", "Altenburg", "Schmölln", "Meuselwitz", "Gößnitz"
    ],
    "Sachsen-Anhalt": [
        "Magdeburg Stadt", "Schönebeck", "Staßfurt", "Bernburg", "Köthen Anhalt",
        "Dessau-Roßlau", "Zerbst Anhalt", "Bitterfeld-Wolfen", "Wittenberg",
        "Halle Stadt", "Merseburg", "Weißenfels", "Naumburg", "Zeitz", "Eisleben",
        "Hettstedt", "Sangerhausen", "Quedlinburg", "Wernigerode", "Halberstadt",
        "Aschersleben", "Stendal", "Salzwedel", "Gardelegen", "Havelberg", "Burg"
    ],
    "Brandenburg": [
        "Potsdam Stadt", "Werder Havel", "Brandenburg an der Havel", "Rathenow",
        "Nauen", "Falkensee", "Dallgow-Döberitz", "Oranienburg", "Bernau bei Berlin",
        "Eberswalde", "Bad Freienwalde", "Strausberg", "Rüdersdorf bei Berlin",
        "Erkner", "Fürstenwalde Spree", "Beeskow", "Eisenhüttenstadt", "Frankfurt Oder",
        "Schwedt Oder", "Templin", "Prenzlau", "Angermünde", "Neuruppin",
        "Wittstock Dosse", "Kyritz", "Perleberg", "Wittenberge", "Pritzwalk",
        "Lübben Spreewald", "Lübbenau Spreewald", "Cottbus Stadt", "Spremberg", "Senftenberg",
        "Finsterwalde", "Elsterwerda", "Bad Liebenwerda", "Herzberg Elster", "Jüterbog",
        "Luckenwalde", "Ludwigsfelde", "Zossen", "Königs Wusterhausen", "Wildau"
    ],
    "Mecklenburg-Vorpommern": [
        "Schwerin Stadt", "Wismar", "Grevesmühlen", "Bad Kleinen", "Gadebusch",
        "Rostock Stadt", "Warnemünde", "Bad Doberan", "Kühlungsborn", "Güstrow",
        "Teterow", "Malchin", "Waren Müritz", "Röbel Müritz", "Malchow",
        "Neubrandenburg", "Neustrelitz", "Mirow", "Wesenberg", "Friedland",
        "Anklam", "Usedom", "Wolgast", "Greifswald", "Stralsund", "Bergen auf Rügen",
        "Sassnitz", "Binz", "Putbus", "Barth", "Ribnitz-Damgarten", "Grimmen",
        "Demmin", "Pasewalk", "Prenzlau", "Templin", "Parchim", "Plau am See",
        "Ludwigslust", "Hagenow", "Boizenburg Elbe", "Lauenburg", "Zarrentin am Schaalsee"
    ],
    "Saarland": [
        "Saarbrücken Stadt", "Völklingen", "Püttlingen", "Sulzbach Saar", "Quierschied",
        "Heusweiler", "Riegelsberg", "Wadgassen", "Schwalbach Saar", "Dillingen Saar",
        "Saarlouis", "Lebach", "Schmelz", "Wadern", "Losheim am See", "Merzig",
        "Mettlach", "Perl", "Beckingen", "Rehlingen-Siersburg", "Überherrn",
        "Bous", "Ensdorf", "Schiffweiler", "Neunkirchen Saar", "Spiesen-Elversberg",
        "Ottweiler", "Schiffweiler", "Illingen", "Merchweiler", "Friedrichsthal",
        "Homburg Stadt", "Bexbach", "Kirkel", "Blieskastel", "Gersheim", "Mandelbachtal",
        "St. Ingbert", "Rohrbach", "St. Wendel", "Tholey", "Marpingen", "Nohfelden",
        "Nonnweiler", "Freisen", "Namborn", "Oberthal"
    ]
}

# Textvariationen für einzigartigen Content
def get_intro_text(ort, bundesland, variant):
    texts = [
        f"Professionelle Rauchmelder-Installation in {ort} ({bundesland}). Unsere zertifizierten Techniker sorgen für Ihren Schutz nach DIN 14676. Schnell, zuverlässig, günstig.",
        f"Rauchmelder-Service in {ort}: Ob Neuinstallation, Wartung oder Austausch - wir sind Ihr kompetenter Partner in {bundesland}. Jetzt unverbindlich anfragen!",
        f"Suchen Sie einen Rauchmelder-Fachbetrieb in {ort}? Wir bieten professionelle Installation und Wartung in ganz {bundesland}. TÜV-geprüft und normgerecht.",
        f"Brandschutz für {ort} und Umgebung: Unser erfahrenes Team installiert und wartet Ihre Rauchmelder nach den neuesten Standards. Faire Preise, Top-Qualität.",
        f"Ihr Rauchmelder-Experte in {ort}, {bundesland}. Von der Beratung bis zur Installation - alles aus einer Hand. Kontaktieren Sie uns noch heute!",
        f"Rauchwarnmelder für {ort}: Fachgerechte Montage, jährliche Wartung und zuverlässiger Service. Wir schützen Ihr Zuhause in {bundesland}.",
        f"In {ort} setzen Sie auf Qualität: Unsere Rauchmelder-Profis garantieren normgerechte Installation nach DIN 14676. Kostenlose Erstberatung!",
        f"Brandschutz hat in {ort} höchste Priorität. Vertrauen Sie auf unseren erfahrenen Service für Rauchmelder-Installation und Wartung in {bundesland}."
    ]
    return texts[variant % len(texts)]

def get_service_text(ort, bundesland, variant):
    texts = [
        f"Unser Rauchmelder-Service für {ort} umfasst die komplette Installation, regelmäßige Wartung und den rechtzeitigen Austausch aller Geräte.",
        f"Von der ersten Beratung bis zur Dokumentation: Wir begleiten Kunden in {ort} durch den gesamten Prozess der Rauchmelderinstallation.",
        f"Für Privathaushalte und Vermieter in {ort}: Wir bieten maßgeschneiderte Lösungen für jeden Bedarf - vom Einfamilienhaus bis zum Mehrfamilienhaus.",
        f"Schnelle Terminvergabe in {ort} und {bundesland}: Unsere Techniker sind flexibel und kommen zum vereinbarten Zeitpunkt zu Ihnen.",
        f"Dokumentation inklusive: Jeder Kunde in {ort} erhält ein vollständiges Installationsprotokoll für seine Unterlagen.",
        f"Wartungsverträge für {ort}: Wir erinnern Sie automatisch an die jährliche Prüfung und kümmern uns um alles Weitere."
    ]
    return texts[variant % len(texts)]

def create_page(ort, bundesland, slug, variant):
    """Erstellt eine SEO-optimierte Seite für einen Ort"""
    
    intro = get_intro_text(ort, bundesland, variant)
    service = get_service_text(ort, bundesland, variant + 1)
    
    html_content = f'''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{intro[:155]}">
    <title>Rauchmelder {ort} | Installation & Wartung | Secu.li</title>
    <link rel="canonical" href="https://secu.li/standorte/deutschland/{slug}.html">
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
            <span class="hero-badge-top">📍 {bundesland}</span>
            <h1>Rauchmelder-Service in {ort}</h1>
            <p>{intro}</p>
            <div style="margin-top: 20px; display: flex; gap: 10px; justify-content: center; flex-wrap: wrap;">
                <a href="#kontakt" class="btn btn-primary">Jetzt anfragen</a>
                <a href="tel:+4915778631120" class="btn btn-outline">📞 Anrufen</a>
            </div>
        </div>
    </section>

    <section class="local-content">
        <h2>Rauchmelder-Installation in {ort}</h2>
        <p>{service}</p>
        
        <h2>Warum Secu.li in {ort}?</h2>
        <ul>
            <li>✓ DIN 14676 zertifizierte Installation</li>
            <li>✓ Erfahrene Techniker aus der Region {bundesland}</li>
            <li>✓ Schnelle Terminvergabe in {ort}</li>
            <li>✓ Faire Festpreise ohne versteckte Kosten</li>
            <li>✓ Vollständige Dokumentation für Vermieter</li>
        </ul>

        <h2>Rauchmelderpflicht in {bundesland}</h2>
        <p>In {bundesland} gilt die gesetzliche Rauchmelderpflicht. Rauchmelder müssen in Schlafräumen, Kinderzimmern und Fluren installiert werden. Als Ihr Partner in {ort} sorgen wir für die normgerechte Umsetzung.</p>

        <div class="local-cta">
            <h3>Kostenlose Beratung für {ort}</h3>
            <p>Rufen Sie uns an oder nutzen Sie unser Kontaktformular!</p>
            <a href="tel:+4915778631120" class="btn btn-primary">📞 +49 157 78631120</a>
        </div>

        <div class="local-form" id="kontakt">
            <h3>Anfrage für {ort}</h3>
            <form action="https://formspree.io/f/xrbnlwal" method="POST">
                <input type="hidden" name="_subject" value="Anfrage aus {ort} - secu.li">
                <input type="hidden" name="standort" value="{ort}, {bundesland}">
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
    </section>

    <footer class="footer">
        <div class="container" style="text-align: center; padding: 30px;">
            <p>&copy; 2024 Secu.li - Rauchmelder {ort}</p>
            <a href="../../impressum.html">Impressum</a> | <a href="../../datenschutz.html">Datenschutz</a>
        </div>
    </footer>
</body>
</html>'''
    return html_content

def slugify(text):
    """Erstellt URL-freundlichen Slug"""
    replacements = {
        'ä': 'ae', 'ö': 'oe', 'ü': 'ue', 'ß': 'ss',
        ' ': '-', '/': '-', '.': '', '(': '', ')': ''
    }
    slug = text.lower()
    for old, new in replacements.items():
        slug = slug.replace(old, new)
    return slug

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Zähler für Varianten
    variant_counter = 0
    pages_created = 0
    
    # Stadtteile der Großstädte
    for city, data in CITY_DISTRICTS.items():
        bundesland = data["bundesland"]
        for stadtteil in data["stadtteile"]:
            ort_name = f"{city} {stadtteil}"
            slug = slugify(ort_name)
            filepath = OUTPUT_DIR / f"{slug}.html"
            
            if not filepath.exists():
                content = create_page(ort_name, bundesland, slug, variant_counter)
                filepath.write_text(content, encoding='utf-8')
                pages_created += 1
                variant_counter += 1
    
    # Kleinstädte
    for bundesland, towns in SMALL_TOWNS.items():
        for town in towns:
            slug = slugify(town)
            filepath = OUTPUT_DIR / f"{slug}.html"
            
            if not filepath.exists():
                content = create_page(town, bundesland, slug, variant_counter)
                filepath.write_text(content, encoding='utf-8')
                pages_created += 1
                variant_counter += 1
    
    print(f"✅ {pages_created} neue Seiten erstellt!")
    print(f"📁 Gespeichert in: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
