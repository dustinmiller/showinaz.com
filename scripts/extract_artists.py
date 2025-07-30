#!/usr/bin/env python3
"""
Extract unique artists from event markdown files.
Creates a list of all unique artists for the artist reference system.
"""

import os
import re
import json
from pathlib import Path

def extract_artist_from_frontmatter(content):
    """Extract artist name from TOML frontmatter."""
    match = re.search(r'artist\s*=\s*"([^"]+)"', content)
    if match:
        return match.group(1)
    return None

def main():
    """Extract all unique artists from event files."""
    event_dir = Path("content/event")
    unique_artists = set()
    
    if not event_dir.exists():
        print("Event directory not found!")
        return
    
    for md_file in event_dir.glob("*.md"):
        if md_file.name == "_index.md":
            continue
            
        try:
            content = md_file.read_text(encoding='utf-8')
            artist = extract_artist_from_frontmatter(content)
            if artist:
                unique_artists.add(artist)
        except Exception as e:
            print(f"Error processing {md_file}: {e}")
    
    # Sort artists alphabetically
    sorted_artists = sorted(unique_artists)
    
    print(f"Found {len(sorted_artists)} unique artists:")
    print("-" * 50)
    
    # Create JSON structure for artists.json
    artists_data = {
        "artists": {}
    }
    
    for artist in sorted_artists:
        print(artist)
        artists_data["artists"][artist] = {
            "name": artist,
            "youtube": "",
            "genre": [],
            "website": "",
            "spotify": "",
            "instagram": ""
        }
    
    # Write to artists_template.json for manual completion
    with open("artists_template.json", "w", encoding='utf-8') as f:
        json.dump(artists_data, f, indent=2, ensure_ascii=False)
    
    print(f"\nTemplate created: artists_template.json")
    print(f"You can populate the YouTube links and other data in this file.")

if __name__ == "__main__":
    main()