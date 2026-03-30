#!/usr/bin/env python3
"""
Replace [forrás](keyword_pattern&t=XXs) with actual video URLs.

Usage:
    python3 scripts/add_source_links.py

This script replaces all keyword patterns in markdown files with actual 
URLs including timestamps. The mapping is defined in SOURCES dict below.
"""

import re
from pathlib import Path

# Source mapping from 0000-home.md
SOURCES = {
    "direkt36_szabo_bence": "https://www.youtube.com/watch?v=IXmuE2TX9yE",
    "partizan_laczo_adrienn": "https://www.youtube.com/watch?v=2GLvrjKpKRY",
    "partizan_szabo_bence": "https://www.youtube.com/watch?v=roI9C9zraLE",
    "magyar_kormany_gundalf": "https://www.youtube.com/watch?v=2tqZZL_Bv1w",
    "gundalf_444": "https://www.youtube.com/watch?v=xdlMnQsK_f0",
}

def replace_source_links(content):
    """Replace [forrás](pattern&t=XXs) with actual URLs."""
    
    def replacer(match):
        pattern = match.group(1)
        timestamp = match.group(2)
        
        # Find matching source
        for key, url in SOURCES.items():
            if key in pattern:
                return f"[forrás]({url}&t={timestamp})"
        
        # If no match found, return original
        return match.group(0)
    
    # Match [forrás](keyword_pattern&t=XXs) or [forrás](keyword_pattern&t=XXs)
    return re.sub(
        r'\[forrás\]\(([^&]+)&t=(\d+)s?\)',
        replacer,
        content
    )

def main():
    content_dir = Path("content")
    updated_count = 0
    
    for md_file in sorted(content_dir.glob("*.md")):
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        updated_content = replace_source_links(content)
        
        if updated_content != content:
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"✓ Updated: {md_file.name}")
            updated_count += 1
        else:
            print(f"  No changes: {md_file.name}")
    
    print(f"\nTotal files updated: {updated_count}")

if __name__ == "__main__":
    main()
