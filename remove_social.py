#!/usr/bin/env python3
"""
Entfernt Social Sharing Buttons von allen Seiten
"""

import re
from pathlib import Path

BASE_DIR = Path("/Users/neslihanakdeniz/Desktop/Rauchmelder")

def remove_social_sharing(filepath):
    """Entfernt Social Sharing Buttons"""
    
    content = filepath.read_text(encoding='utf-8')
    
    if 'social-share' not in content:
        return False
    
    # Social Sharing HTML Block entfernen
    content = re.sub(
        r'\n?<div class="social-share">.*?</div>\s*',
        '',
        content,
        flags=re.DOTALL
    )
    
    # Social Sharing CSS entfernen
    content = re.sub(
        r'/\* Social Sharing \*/.*?\.share-email \{ background: #6B7280; color: white; \}\s*',
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
        
        if remove_social_sharing(html_file):
            removed += 1
            if removed % 100 == 0:
                print(f"✅ {removed} Seiten bearbeitet...")
    
    print(f"\n✅ Social Sharing Buttons von {removed} Seiten entfernt!")

if __name__ == "__main__":
    main()
