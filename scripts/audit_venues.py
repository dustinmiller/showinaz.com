#!/usr/bin/env python3
"""
Venue Audit Script for Shows in AZ

This script audits all venues in event files and shows:
- Which venues are mapped vs unmapped
- Missing URLs for venues
- Frequency of venue usage
- Suggestions for new venue mappings
"""

import os
import re
import glob
from collections import Counter
from typing import Dict, Set, Tuple

# Import the venue mapping from normalize_venues.py
import sys
sys.path.append(os.path.dirname(__file__))
from normalize_venues import VENUE_MAPPING, normalize_venue_name

def extract_venues_from_events() -> Dict[str, int]:
    """Extract all venues from event files with usage counts"""
    venues = Counter()
    
    for file_path in glob.glob('content/event/*.md'):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract venue from frontmatter
            venue_match = re.search(r'^venue = "([^"\\]*(?:\\.[^"\\]*)*)"', content, re.MULTILINE)
            if venue_match:
                venue_raw = venue_match.group(1)
                # Unescape for analysis
                venue = venue_raw.replace('\\"', '"').replace('\\\\', '\\')
                venues[venue] += 1
                
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
    
    return dict(venues)

def analyze_venue_mapping(venues: Dict[str, int]) -> Tuple[Dict[str, Tuple[str, str, int]], Set[str]]:
    """Analyze which venues are mapped and which aren't"""
    mapped_venues = {}
    unmapped_venues = set()
    
    for venue, count in venues.items():
        normalized_venue, url = normalize_venue_name(venue)
        
        if venue in VENUE_MAPPING or normalized_venue != venue:
            # Venue is mapped
            mapped_venues[venue] = (normalized_venue, url, count)
        else:
            # Venue is not mapped
            unmapped_venues.add(venue)
    
    return mapped_venues, unmapped_venues

def get_venues_without_urls() -> Set[str]:
    """Get venues that are mapped but don't have URLs"""
    no_url_venues = set()
    
    for venue_variation, (canonical_name, url) in VENUE_MAPPING.items():
        if not url or url.strip() == "":
            no_url_venues.add(canonical_name)
    
    return no_url_venues

def print_venue_audit():
    """Print comprehensive venue audit report"""
    print("🎵 VENUE AUDIT REPORT")
    print("=" * 50)
    
    # Extract venues from all events
    venues = extract_venues_from_events()
    total_events = sum(venues.values())
    
    print(f"\n📊 SUMMARY")
    print(f"Total unique venues: {len(venues)}")
    print(f"Total events: {total_events}")
    print(f"Venues in mapping: {len(set(canonical for canonical, url in VENUE_MAPPING.values()))}")
    
    # Analyze mapping status
    mapped_venues, unmapped_venues = analyze_venue_mapping(venues)
    venues_without_urls = get_venues_without_urls()
    
    print(f"\n✅ MAPPED VENUES ({len(mapped_venues)})")
    print("-" * 30)
    for venue, (canonical, url, count) in sorted(mapped_venues.items(), key=lambda x: x[1][2], reverse=True):
        url_status = "✓" if url else "❌ NO URL"
        if venue != canonical:
            print(f"{venue} → {canonical} ({count} events) {url_status}")
        else:
            print(f"{venue} ({count} events) {url_status}")
    
    print(f"\n❌ UNMAPPED VENUES ({len(unmapped_venues)})")
    print("-" * 30)
    for venue in sorted(unmapped_venues, key=lambda x: venues[x], reverse=True):
        count = venues[venue]
        print(f"{venue} ({count} events)")
    
    print(f"\n🔗 VENUES MISSING URLs ({len(venues_without_urls)})")
    print("-" * 30)
    for venue in sorted(venues_without_urls):
        print(f"{venue}")
    
    # Top venues by frequency
    print(f"\n🔥 TOP 10 MOST FREQUENT VENUES")
    print("-" * 30)
    top_venues = sorted(venues.items(), key=lambda x: x[1], reverse=True)[:10]
    for venue, count in top_venues:
        normalized, url, _ = mapped_venues.get(venue, (venue, "", count))
        status = "✓" if url else "❌"
        print(f"{venue}: {count} events {status}")
    
    # Suggestions for new mappings
    if unmapped_venues:
        print(f"\n💡 SUGGESTED VENUE MAPPINGS TO ADD")
        print("-" * 30)
        print("Add these to VENUE_MAPPING in normalize_venues.py:")
        print()
        
        for venue in sorted(unmapped_venues, key=lambda x: venues[x], reverse=True):
            count = venues[venue]
            # Suggest some common variations
            variations = [venue]
            
            # Add common abbreviations
            if "Ballroom" in venue:
                variations.append(venue.replace("Ballroom", "BR"))
            if "Theater" in venue:
                variations.append(venue.replace("Theater", "Theatre"))
                variations.append(venue.replace("Theater", "Thtr"))
            if "The " in venue:
                variations.append(venue.replace("The ", ""))
            
            print(f'    # {venue} ({count} events)')
            for var in variations:
                print(f'    "{var}": ("{venue}", ""),')
            print()

def create_venue_reference_file():
    """Create a reference file with all venues for easy editing"""
    venues = extract_venues_from_events()
    mapped_venues, unmapped_venues = analyze_venue_mapping(venues)
    venues_without_urls = get_venues_without_urls()
    
    with open('venue_reference.txt', 'w') as f:
        f.write("# VENUE REFERENCE FILE\n")
        f.write("# Use this file to research and add missing venue URLs\n")
        f.write("# Format: Venue Name | Current URL | Suggested URL | Notes\n\n")
        
        f.write("## VENUES MISSING URLs\n")
        f.write("# These venues are mapped but need official website URLs\n\n")
        for venue in sorted(venues_without_urls):
            f.write(f"{venue} | | | \n")
        
        f.write("\n## UNMAPPED VENUES\n")
        f.write("# These venues need to be added to the mapping\n\n")
        for venue in sorted(unmapped_venues, key=lambda x: venues[x], reverse=True):
            count = venues[venue]
            f.write(f"{venue} ({count} events) | | | \n")
    
    print(f"\n📝 Created venue_reference.txt for easy editing")

if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='Audit venue mappings and URLs')
    parser.add_argument('--create-reference', action='store_true',
                       help='Create venue_reference.txt file for easy editing')
    args = parser.parse_args()
    
    print_venue_audit()
    
    if args.create_reference:
        create_venue_reference_file()