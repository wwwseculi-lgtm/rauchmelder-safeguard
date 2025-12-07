#!/usr/bin/env python3
"""
Entfernt Scroll Progress Indicator von allen Seiten
"""

import re
from pathlib import Path

BASE_DIR = Path("/Users/neslihanakdeniz/Desktop/Rauchmelder")

def remove_scroll_progress(filepath):
    content = filepath.read_text(encoding='utf-8')
    
    if 'scroll-progress' not in content:
        return False
    
    # CSS entfernen
    content = re.sub(
        r'/\* Scroll Progress Indicator \*/\s*\.scroll-progress \{[^}]+\}\s*',
        '',
        content,
        flags=re.DOTALL
    )
    
    # JavaScript entfernen
    content = re.sub(
        r"// Scroll Progress Indicator\s*if \(!document\.querySelector\('\.scroll-progress'\)\) \{[^}]+\}\s*window\.addEventListener\('scroll', \(\) => \{[^}]+\}\);\s*\}",
        '',
        content,
        flags=re.DOTALL
    )
    
    filepath.write_text(content, encoding='utf-8')
    return True

def main():
    removed = 0
    for html_file in BASE_DIR.rglob("*.html"):
        if any(skip in str(html_file) for skip in ['node_modules', '.git']):
            continue
        if remove_scroll_progress(html_file):
            removed += 1
            if removed % 100 == 0:
                print(f"✅ {removed} Seiten bearbeitet...")
    
    print(f"\n✅ Scroll Progress von {removed} Seiten entfernt!")

if __name__ == "__main__":
    main()
