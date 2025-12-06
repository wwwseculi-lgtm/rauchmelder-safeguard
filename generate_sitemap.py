#!/usr/bin/env python3
"""
Sitemap Generator für secu.li
Erstellt eine XML-Sitemap mit allen Seiten
"""

import os
from pathlib import Path
from datetime import datetime

BASE_URL = "https://secu.li"
OUTPUT_FILE = "/Users/neslihanakdeniz/Desktop/Rauchmelder/sitemap.xml"
ROOT_DIR = Path("/Users/neslihanakdeniz/Desktop/Rauchmelder")

# Dateien die ignoriert werden sollen
IGNORE_FILES = {
    'generate_languages.py', 'generate_local_pages.py', 'generate_unique_local_pages.py',
    'generate_sitemap.py', 'manifest.json', 'service-worker.js', '.DS_Store'
}

IGNORE_DIRS = {'icons', '.git', 'node_modules', '.gemini'}

def get_priority(filepath):
    """Bestimmt die Priorität basierend auf dem Dateipfad"""
    path_str = str(filepath)
    if path_str.endswith('index.html') and 'standorte' not in path_str:
        return "1.0"  # Hauptseite
    elif any(x in path_str for x in ['kontakt', 'service', 'produkte', 'ueber-uns']):
        return "0.9"  # Hauptnavigation
    elif 'standorte/deutschland/index' in path_str:
        return "0.8"  # Deutschland Übersicht
    elif 'standorte/deutschland/' in path_str:
        return "0.7"  # Städteseiten
    else:
        return "0.5"

def get_changefreq(filepath):
    """Bestimmt die Update-Häufigkeit"""
    path_str = str(filepath)
    if 'index.html' in path_str:
        return "weekly"
    elif 'standorte' in path_str:
        return "monthly"
    else:
        return "monthly"

def find_html_files(root_dir):
    """Findet alle HTML-Dateien"""
    html_files = []
    
    for root, dirs, files in os.walk(root_dir):
        # Ignoriere bestimmte Verzeichnisse
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        
        for file in files:
            if file.endswith('.html') and file not in IGNORE_FILES:
                filepath = Path(root) / file
                rel_path = filepath.relative_to(root_dir)
                html_files.append(rel_path)
    
    return html_files

def generate_sitemap():
    """Generiert die sitemap.xml"""
    html_files = find_html_files(ROOT_DIR)
    today = datetime.now().strftime("%Y-%m-%d")
    
    xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    for filepath in sorted(html_files):
        # URL erstellen
        url_path = str(filepath).replace('\\', '/')
        if url_path == 'index.html':
            url = BASE_URL + "/"
        else:
            url = f"{BASE_URL}/{url_path}"
        
        priority = get_priority(filepath)
        changefreq = get_changefreq(filepath)
        
        xml_content += f'''  <url>
    <loc>{url}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>{changefreq}</changefreq>
    <priority>{priority}</priority>
  </url>
'''
    
    xml_content += '</urlset>'
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(xml_content)
    
    print(f"✅ Sitemap erstellt mit {len(html_files)} URLs!")
    print(f"📁 Gespeichert unter: {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_sitemap()
