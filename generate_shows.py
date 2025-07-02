#!/usr/bin/env python3
import re
import os
from datetime import datetime
from pathlib import Path

# Venue URL mapping
venue_links = {
    'Last Exit Live': 'https://lastexitlive.com',
    'Crescent Ballroom': 'https://www.crescentphx.com',
    'The Crescent Ballroom': 'https://www.crescentphx.com',
    'Crescent Ballrm': 'https://www.crescentphx.com',
    'Crescent B.R.': 'https://www.crescentphx.com',
    'Crescent BR': 'https://www.crescentphx.com',
    'The Van Buren': 'https://www.thevanburenphx.com',
    'Van Buren': 'https://www.thevanburenphx.com',
    'Walter Studios': 'https://walterstudios.com',
    'Walter Wherehouse': 'https://walterwherehouse.com',
    'Walter Wherehous': 'https://walterwherehouse.com'
}

def clean_filename(text):
    """Convert text to a safe filename"""
    # Remove special characters and replace spaces with hyphens
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.lower().strip('-')

def parse_show_line(line):
    """Parse a line like '6/25 Artist @ Venue' into components"""
    line = line.strip()
    if not line or line.startswith('---'):
        return None
    
    # Match date pattern at start of line
    date_match = re.match(r'^(\d{1,2}/\d{1,2})', line)
    if not date_match:
        return None
    
    date_str = date_match.group(1)
    remainder = line[len(date_str):].strip()
    
    # Split by @ to get artist and venue
    if ' @ ' in remainder:
        artist, venue = remainder.split(' @ ', 1)
        artist = artist.strip()
        venue = venue.strip()
        
        # Clean up common venue name variations
        venue = venue.replace('Thtr', 'Theater')
        venue = venue.replace('Ballrm', 'Ballroom')
        venue = venue.replace('Amph', 'Amphitheater')
        venue = venue.replace('Amphithtr', 'Amphitheater')
        venue = venue.replace('B.r.', 'Ballroom')
        venue = venue.replace('B.R.', 'Ballroom')
        
        return {
            'date': date_str,
            'artist': artist,
            'venue': venue
        }
    
    return None

def date_to_iso(date_str):
    """Convert M/D format to YYYY-MM-DD"""
    month, day = date_str.split('/')
    year = '2024'  # Assuming 2024 for now
    return f"{year}-{int(month):02d}-{int(day):02d}"

def generate_markdown(show):
    """Generate markdown content for a show"""
    venue_url = venue_links.get(show['venue'], '')
    venue_url_line = f'venue_url = "{venue_url}"' if venue_url else 'venue_url = ""'
    
    # Clean up artist name for title
    artist_clean = show['artist'].replace('&', 'and')
    
    content = f"""+++
title = "{artist_clean} at {show['venue']}"
date = {date_to_iso(show['date'])}
template = "page.html"

[extra]
artist = "{show['artist']}"
venue = "{show['venue']}"
{venue_url_line}
+++

{show['artist']} performs at {show['venue']}.
"""
    return content

def main():
    # Read the list.txt file
    with open('list.txt', 'r') as f:
        lines = f.readlines()
    
    # Create shows directory if it doesn't exist
    shows_dir = Path('content/shows')
    shows_dir.mkdir(parents=True, exist_ok=True)
    
    generated_count = 0
    
    for line in lines:
        show = parse_show_line(line)
        if not show:
            continue
        
        # Generate filename
        iso_date = date_to_iso(show['date'])
        artist_slug = clean_filename(show['artist'])
        filename = f"{iso_date}-{artist_slug}.md"
        
        # Generate markdown content
        markdown_content = generate_markdown(show)
        
        # Write to file
        file_path = shows_dir / filename
        with open(file_path, 'w') as f:
            f.write(markdown_content)
        
        generated_count += 1
        print(f"Generated: {filename}")
    
    print(f"\nGenerated {generated_count} show files in {shows_dir}")

if __name__ == '__main__':
    main()