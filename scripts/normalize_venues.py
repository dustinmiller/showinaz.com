#!/usr/bin/env python3
"""
Venue Normalization Script for Shows in AZ

This script normalizes venue names and adds venue URLs to event markdown files.
It handles common variations and typos in venue names.
"""

import os
import re
import glob
from typing import Dict, Tuple

# Venue normalization mapping: {variation: (canonical_name, url)}
VENUE_MAPPING = {
    # Major Venues
    "The Van Buren": ("The Van Buren", "https://www.thevanburen.com/"),
    "Van Buren": ("The Van Buren", "https://www.thevanburen.com/"),
    
    "Valley Bar": ("Valley Bar", "https://www.valleybarphx.com/"),
    
    "The Rebel Lounge": ("The Rebel Lounge", "https://www.rebelphx.com/"),
    "Rebel Lounge": ("The Rebel Lounge", "https://www.rebelphx.com/"),
    "Rebel Lge": ("The Rebel Lounge", "https://www.rebelphx.com/"),
    "Rebel L": ("The Rebel Lounge", "https://www.rebelphx.com/"),
    "Rebel Lg": ("The Rebel Lounge", "https://www.rebelphx.com/"),
    "Rebel Lnge": ("The Rebel Lounge", "https://www.rebelphx.com/"),
    
    "Crescent Ballroom": ("Crescent Ballroom", "https://www.crescentphx.com/"),
    "The Crescent Ballroom": ("Crescent Ballroom", "https://www.crescentphx.com/"),
    "The Crescent": ("Crescent Ballroom", "https://www.crescentphx.com/"),
    "Crescent BR": ("Crescent Ballroom", "https://www.crescentphx.com/"),
    "Crescent Ballrm": ("Crescent Ballroom", "https://www.crescentphx.com/"),
    "Crescent": ("Crescent Ballroom", "https://www.crescentphx.com/"),
    "Crescent B.r.": ("Crescent Ballroom", "https://www.crescentphx.com/"),
    "The Crescent BR": ("Crescent Ballroom", "https://www.crescentphx.com/"),
    "Crescent (2:30)": ("Crescent Ballroom", "https://www.crescentphx.com/"),
    "Crescent Ballroom (7:00)": ("Crescent Ballroom", "https://www.crescentphx.com/"),
    
    "The MIM": ("MIM Music & Instrument Museum", "https://mim.org/"),
    "MIM": ("MIM Music & Instrument Museum", "https://mim.org/"),
    "The MIM": ("MIM Music & Instrument Museum", "https://mim.org/"),
    
    "The Nile Theater": ("The Nile Theater", "https://theniletheatre.com/"),
    "The Nile": ("The Nile Theater", "https://theniletheatre.com/"),
    "Nile": ("The Nile Theater", "https://theniletheatre.com/"),
    "The Nile Theatre": ("The Nile Theater", "https://theniletheatre.com/"),
    "Nile Theater": ("The Nile Theater", "https://theniletheatre.com/"),
    
    "Nile Underground": ("Nile Underground", "https://theniletheatre.com/"),
    "The Nile Underground": ("Nile Underground", "https://theniletheatre.com/"),
    "Nile UG": ("Nile Underground", "https://theniletheatre.com/"),
    "The Nile Undergrnd": ("Nile Underground", "https://theniletheatre.com/"),
    "Nile Undergrnd": ("Nile Underground", "https://theniletheatre.com/"),
    "Nile Thtr": ("The Nile Theater", "https://theniletheatre.com/"),
    
    "Club Congress": ("Club Congress", "https://www.hotelcongress.com/club-congress/"),
    "Congress": ("Club Congress", "https://www.hotelcongress.com/club-congress/"),
    "Club Congrs": ("Club Congress", "https://www.hotelcongress.com/club-congress/"),
    "CluB Congress": ("Club Congress", "https://www.hotelcongress.com/club-congress/"),
    "Congress Plaza Stage": ("Club Congress", "https://www.hotelcongress.com/club-congress/"),
    "Congress Plaza St": ("Club Congress", "https://www.hotelcongress.com/club-congress/"),
    
    "191 Toole": ("191 Toole", "https://www.191toole.com/"),
    "191 Tool": ("191 Toole", "https://www.191toole.com/"),
    "191Tool": ("191 Toole", "https://www.191toole.com/"),
    "191 Tool": ("191 Toole", "https://www.191toole.com/"),
    
    "The Marquee Theater": ("The Marquee Theater", "https://www.luckymanonline.com/venue/marquee-theatre/"),
    "The Marquee": ("The Marquee Theater", "https://www.luckymanonline.com/venue/marquee-theatre/"),
    "Marquee Theater": ("The Marquee Theater", "https://www.luckymanonline.com/venue/marquee-theatre/"),
    "Marquee": ("The Marquee Theater", "https://www.luckymanonline.com/venue/marquee-theatre/"),
    "The Marquee Thtr": ("The Marquee Theater", "https://www.luckymanonline.com/venue/marquee-theatre/"),
    
    "The Rialto Theater": ("The Rialto Theater", "https://www.rialtotheatre.com/"),
    "The Rialto Theatre": ("The Rialto Theater", "https://www.rialtotheatre.com/"),
    "Rialto": ("The Rialto Theater", "https://www.rialtotheatre.com/"),
    "The Rialto": ("The Rialto Theater", "https://www.rialtotheatre.com/"),
    "Rialto Theater": ("The Rialto Theater", "https://www.rialtotheatre.com/"),
    
    "Last Exit Live": ("Last Exit Live", "https://lastexitlive.com/"),
    "Last Exit": ("Last Exit Live", "https://lastexitlive.com/"),
    "Last Exit L": ("Last Exit Live", "https://lastexitlive.com/"),
    "@ast Exit Live": ("Last Exit Live", "https://lastexitlive.com/"),
    
    "Walter Studios": ("Walter Studios", "https://walterstudios.com/"),
    "Walter Wherehouse": ("Walter Studios", "https://walterstudios.com/"),
    "Walter Wherehous": ("Walter Studios", "https://walterstudios.com/"),
    "Walter W?H": ("Walter Studios", "https://walterstudios.com/"),
    "Walter WH": ("Walter Studios", "https://walterstudios.com/"),
    
    "Fox Theater": ("Fox Theater", "https://www.foxtheatretucson.com/"),
    "The Fox Theater": ("Fox Theater", "https://www.foxtheatretucson.com/"),
    
    "PHX Arena": ("Footprint Center", "https://www.footprintcenter.com/"),
    "Footprint Center": ("Footprint Center", "https://www.footprintcenter.com/"),
    
    # Smaller/Alternative Venues
    "Darkstar": ("Darkstar", "https://www.darkstarbar.com/"),
    "Sunbar": ("Sunbar", "https://www.sunbarscottsdale.com/"),
    
    "Yucca Tap Room": ("Yucca Tap Room", "https://www.yuccatap.com/"),
    "Yucca North": ("Yucca Tap Room", "https://www.yuccatap.com/"),
    "Yucca Tap Rm": ("Yucca Tap Room", "https://www.yuccatap.com/"),
    
    "Maya Day Club": ("Maya Day Club", "https://mayadayclub.com/"),
    "Maya Day Club @ Maya Day C": ("Maya Day Club", "https://mayadayclub.com/"),
    
    "The Rhythm Room": ("The Rhythm Room", "http://rhythmroom.com/"),
    "Rhythm Room": ("The Rhythm Room", "http://rhythmroom.com/"),
    "Rhythm Rm": ("The Rhythm Room", "http://rhythmroom.com/"),
    
    "Rockbar": ("Rockbar", "https://rockbarscottsdale.com/"),
    
    # Amphitheaters & Large Venues
    "Talking Stick Amphitheater": ("Talking Stick Resort Amphitheatre", "https://www.talkingstickresortamphitheatre.com/"),
    "Talking Stick Amph": ("Talking Stick Resort Amphitheatre", "https://www.talkingstickresortamphitheatre.com/"),
    "Talking Stick Amphithtr": ("Talking Stick Resort Amphitheatre", "https://www.talkingstickresortamphitheatre.com/"),
    "Talking Stick Resort": ("Talking Stick Resort Amphitheatre", "https://www.talkingstickresortamphitheatre.com/"),
    "Talking Stick Amp": ("Talking Stick Resort Amphitheatre", "https://www.talkingstickresortamphitheatre.com/"),
    
    "Pepsi Amphitheater": ("Ak-Chin Pavilion", "https://www.livenation.com/venue/KovZpZAEAkeA/ak-chin-pavilion-events"),
    "Pepsi Amphithtr": ("Ak-Chin Pavilion", "https://www.livenation.com/venue/KovZpZAEAkeA/ak-chin-pavilion-events"),
    "Ak-Chin Pavilion": ("Ak-Chin Pavilion", "https://www.livenation.com/venue/KovZpZAEAkeA/ak-chin-pavilion-events"),
    
    "Mesa Amphitheater": ("Mesa Amphitheatre", "https://www.mesaamp.com/"),
    "Mesa Arts Center": ("Mesa Arts Center", "https://www.mesaartscenter.com/"),
    "Mesa Amphithtr": ("Mesa Amphitheatre", "https://www.mesaamp.com/"),
    "Mesa Amp": ("Mesa Amphitheatre", "https://www.mesaamp.com/"),
    
    "Arizona Financial Theater": ("Arizona Financial Theatre", "https://www.azfinancialtheatre.com/"),
    "AZ Financial Theater": ("Arizona Financial Theatre", "https://www.azfinancialtheatre.com/"),
    "Arizona Financial Theatr": ("Arizona Financial Theatre", "https://www.azfinancialtheatre.com/"),
    "AZ Financial Thtr": ("Arizona Financial Theatre", "https://www.azfinancialtheatre.com/"),
    "Arizona Financial": ("Arizona Financial Theatre", "https://www.azfinancialtheatre.com/"),
    "Arizona Financial Thtr": ("Arizona Financial Theatre", "https://www.azfinancialtheatre.com/"),
    
    "Celebrity Theater": ("Celebrity Theatre", "https://celebritytheatre.com/"),
    "Celebrity Theatre": ("Celebrity Theatre", "https://celebritytheatre.com/"),
    "Celebrity Theatr": ("Celebrity Theatre", "https://celebritytheatre.com/"),
    "Celebrity": ("Celebrity Theatre", "https://celebritytheatre.com/"),
    
    # Tucson Venues
    "Orpheum Theater Flagstaff": ("Orpheum Theater", "https://www.orpheumflagstaff.com/"),
    "Orpheum Theatre Flagstaff": ("Orpheum Theater", "https://www.orpheumflagstaff.com/"),
    "Orpheum Flagstaff": ("Orpheum Theater", "https://www.orpheumflagstaff.com/"),
    "Orpheum Flg": ("Orpheum Theater", "https://www.orpheumflagstaff.com/"),
    "Orpheum Flagstff": ("Orpheum Theater", "https://www.orpheumflagstaff.com/"),
    
    # Other Common Venues
    "Rawhide": ("Rawhide Event Center", "https://www.rawhide.com/"),
    "Wild Horse Pass Oasis Pool": ("Wild Horse Pass Hotel & Casino", "https://wingilariver.com/"),
    "WHP Oasis Pool": ("Wild Horse Pass Hotel & Casino", "https://wingilariver.com/"),
    "X Phoenix (rooftop pool party)": ("X Phoenix", ""),
    "X Phoenix (rooftop pool)": ("X Phoenix", ""),
    "X Phoenix": ("X Phoenix", ""),
    
    "San Tan Gardens": ("San Tan Gardens", ""),
    "San Tan Grdn": ("San Tan Gardens", ""),
    
    "Dynamite Beer Co": ("Dynamite Beer Co", ""),
    "Dynamite Beer Co- Tatum": ("Dynamite Beer Co", ""),
    "Dynamite Beer Co - Tatum": ("Dynamite Beer Co", ""),
    
    "Cactus Jacks": ("Cactus Jacks", ""),
    
    "The Darkside TFM": ("The Darkside", ""),
    "Darkside": ("The Darkside", ""),
    
    "Pho Cao": ("Pho Cao", ""),
    
    "Wasted Grain (Jay Allan's Birthday show)": ("Wasted Grain", ""),
    "Wasted Grain": ("Wasted Grain", ""),
    
    "Birdcage Saln": ("Birdcage Saloon", ""),
    "Birdcage Saloon": ("Birdcage Saloon", ""),
    
    "Tempe Center For The Arts": ("Tempe Center for the Arts", "https://tempecenterforthearts.com/"),
    "Tempe Center for the Arts": ("Tempe Center for the Arts", "https://tempecenterforthearts.com/"),
    
    # Major unmapped venues (high frequency)
    "Arizona Financial Theatre": ("Arizona Financial Theatre", "https://www.azfinancialtheatre.com/"),
    "Arizona Financial Theater": ("Arizona Financial Theatre", "https://www.azfinancialtheatre.com/"),
    "AZ Financial Theater": ("Arizona Financial Theatre", "https://www.azfinancialtheatre.com/"),
    "AZ Financial Theatre": ("Arizona Financial Theatre", "https://www.azfinancialtheatre.com/"),
    "AZ Financial Th": ("Arizona Financial Theatre", "https://www.azfinancialtheatre.com/"),
    "AZ Financial Tr": ("Arizona Financial Theatre", "https://www.azfinancialtheatre.com/"),
    "Arizona Federal Theater": ("Arizona Financial Theatre", "https://www.azfinancialtheatre.com/"),
    
    "MIM Music & Instrument Museum": ("MIM Music & Instrument Museum", "https://mim.org/"),
    "The MIM Music & Instrument Museum": ("MIM Music & Instrument Museum", "https://mim.org/"),
    
    # Orpheum variations (Phoenix vs Flagstaff)
    "Orpheum Theater": ("Orpheum Theater Phoenix", "https://www.orpheumtheatrephoenix.com/"),
    "The Orpheum Theater": ("Orpheum Theater Phoenix", "https://www.orpheumtheatrephoenix.com/"),
    "Orpheum Theatre": ("Orpheum Theater Phoenix", "https://www.orpheumtheatrephoenix.com/"),
    "The Orpheum Theatre": ("Orpheum Theater Phoenix", "https://www.orpheumtheatrephoenix.com/"),
    
    "The Orpheum Flagstaff": ("Orpheum Theater Flagstaff", "https://www.orpheumflagstaff.com/"),
    "The Orpheum Theater Flagstaff": ("Orpheum Theater Flagstaff", "https://www.orpheumflagstaff.com/"),
    "The Orpheum Theatre Flagstaff": ("Orpheum Theater Flagstaff", "https://www.orpheumflagstaff.com/"),
    "Orpheum Theater Flagstaff": ("Orpheum Theater Flagstaff", "https://www.orpheumflagstaff.com/"),
    "Orpheum Theater Flagstff": ("Orpheum Theater Flagstaff", "https://www.orpheumflagstaff.com/"),
    "Orpheum Flagstaff": ("Orpheum Theater Flagstaff", "https://www.orpheumflagstaff.com/"),
    
    # Rawhide
    "Rawhide Event Center": ("Rawhide Event Center", "https://www.rawhide.com/"),
    
    # Typo fixes - map to existing venues
    "The Crescent Ballrm": ("Crescent Ballroom", "https://www.crescentphx.com/"),
    "Crescent Ballrm": ("Crescent Ballroom", "https://www.crescentphx.com/"),
    "The Ceescent BR": ("Crescent Ballroom", "https://www.crescentphx.com/"),
    "Ceescent BR": ("Crescent Ballroom", "https://www.crescentphx.com/"),
    "Crescent br": ("Crescent Ballroom", "https://www.crescentphx.com/"),
    "Crescent Br": ("Crescent Ballroom", "https://www.crescentphx.com/"),
    
    "Valley B": ("Valley Bar", "https://www.valleybarphx.com/"),
    "Valley Br": ("Valley Bar", "https://www.valleybarphx.com/"),
    
    "The  Marquee Theater": ("The Marquee Theater", "https://www.luckymanonline.com/venue/marquee-theatre/"),
    
    "Celebrity Thtr": ("Celebrity Theatre", "https://celebritytheatre.com/"),
    
    "The Nile Thtr": ("The Nile Theater", "https://theniletheatre.com/"),
    "Nile Thtr": ("The Nile Theater", "https://theniletheatre.com/"),
    
    "The Rebel Loung": ("The Rebel Lounge", "https://www.rebelphx.com/"),
    "Rebel Loung": ("The Rebel Lounge", "https://www.rebelphx.com/"),
    
    "Maya Day C": ("Maya Day Club", "https://mayadayclub.com/"),
    
    "Mesa  Amphitheater": ("Mesa Amphitheatre", "https://www.mesaamp.com/"),
    "Mesa Amphitheater": ("Mesa Amphitheatre", "https://www.mesaamp.com/"),
    
    "Talking Stick Amph.": ("Talking Stick Resort Amphitheatre", "https://www.talkingstickresortamphitheatre.com/"),
    "Talking Stick Amphith": ("Talking Stick Resort Amphitheatre", "https://www.talkingstickresortamphitheatre.com/"),
    
    # Special case venues with no normalization needed
    "TBD": ("TBD", ""),
    "AZ State Fair": ("Arizona State Fair", "https://azstatefair.com/"),
    "Fort Tuthil": ("Fort Tuthill County Park", ""),
    "Fort Tuthill Fairgrounds": ("Fort Tuthill County Park", ""),
    "The Barn at Fort Tuthill Fairgrounds": ("Fort Tuthill County Park", ""),
    "Electric Pickle": ("The Electric Pickle", ""),
    "The Electric Pickle": ("The Electric Pickle", ""),
    
    # Remaining major venues
    "Talking Stick Resort Amphitheatre": ("Talking Stick Resort Amphitheatre", "https://www.talkingstickresortamphitheatre.com/"),
    "Mesa Amphitheatre": ("Mesa Amphitheatre", "https://www.mesaamp.com/"),
    "Orpheum Theater Phoenix": ("Orpheum Theater Phoenix", "https://www.orpheumtheatrephoenix.com/"),
    "Wild Horse Pass Hotel & Casino": ("Wild Horse Pass Hotel & Casino", "https://wingilariver.com/"),
    "Fort Tuthill County Park": ("Fort Tuthill County Park", ""),
    "Arizona State Fair": ("Arizona State Fair", "https://azstatefair.com/"),
    "The Darkside": ("The Darkside", ""),
}

def normalize_venue_name(venue_name: str) -> Tuple[str, str]:
    """
    Normalize a venue name and return (canonical_name, url)
    
    Args:
        venue_name: Raw venue name from event file
        
    Returns:
        Tuple of (normalized_name, venue_url)
    """
    # Remove quotes and strip whitespace
    clean_name = venue_name.strip().strip('"').strip("'")
    
    # Check direct mapping first
    if clean_name in VENUE_MAPPING:
        return VENUE_MAPPING[clean_name]
    
    # Handle special cases with @ symbol (venue @ location)
    if '@' in clean_name:
        parts = clean_name.split('@')
        if len(parts) > 1:
            venue_part = parts[-1].strip()
            if venue_part in VENUE_MAPPING:
                return VENUE_MAPPING[venue_part]
    
    # If no mapping found, return as-is with empty URL
    return clean_name, ""

def escape_toml_string(text: str) -> str:
    """
    Escape special characters in TOML strings
    
    Args:
        text: The string to escape
        
    Returns:
        Escaped string safe for TOML
    """
    # Escape backslashes first
    text = text.replace('\\', '\\\\')
    # Escape quotes
    text = text.replace('"', '\\"')
    # Handle newlines
    text = text.replace('\n', '\\n')
    text = text.replace('\r', '\\r')
    text = text.replace('\t', '\\t')
    return text

def fix_toml_formatting(content: str) -> str:
    """
    Fix common TOML formatting issues in event files
    
    Args:
        content: File content
        
    Returns:
        Fixed content
    """
    lines = content.split('\n')
    fixed_lines = []
    
    for line in lines:
        # Fix title field with unescaped quotes and trailing spaces
        if line.strip().startswith('title = "'):
            title_match = re.match(r'^(\s*title = ")(.*)(")\s*$', line)
            if title_match:
                prefix = title_match.group(1)
                title_content = title_match.group(2)
                suffix = title_match.group(3)
                
                # Remove trailing spaces from title content
                title_content = title_content.rstrip()
                
                # Check if quotes are properly escaped
                if '"' in title_content and '\\"' not in title_content:
                    title_content = escape_toml_string(title_content)
                    line = f"{prefix}{title_content}{suffix}"
        
        # Fix artist field with unescaped quotes
        elif line.strip().startswith('artist = "'):
            artist_match = re.match(r'^(\s*artist = ")(.*)(")\s*$', line)
            if artist_match:
                prefix = artist_match.group(1)
                artist_content = artist_match.group(2)
                suffix = artist_match.group(3)
                
                # Check if quotes are properly escaped
                if '"' in artist_content and '\\"' not in artist_content:
                    artist_content = escape_toml_string(artist_content)
                    line = f"{prefix}{artist_content}{suffix}"
        
        # Fix venue field with unescaped quotes (this will be handled by normalization too)
        elif line.strip().startswith('venue = "'):
            venue_match = re.match(r'^(\s*venue = ")(.*)(")\s*$', line)
            if venue_match:
                prefix = venue_match.group(1)
                venue_content = venue_match.group(2)
                suffix = venue_match.group(3)
                
                # Check if quotes are properly escaped
                if '"' in venue_content and '\\"' not in venue_content:
                    venue_content = escape_toml_string(venue_content)
                    line = f"{prefix}{venue_content}{suffix}"
        
        fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)

def update_event_file(file_path: str, dry_run: bool = False) -> bool:
    """
    Update a single event file with normalized venue data and fix TOML formatting
    
    Args:
        file_path: Path to the event markdown file
        dry_run: If True, only show what would be changed
        
    Returns:
        True if file was modified (or would be modified in dry run)
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # First fix any TOML formatting issues
        original_content = content
        content = fix_toml_formatting(content)
        toml_fixed = content != original_content
        
        # Extract current venue and venue_url (after TOML fixes)
        venue_match = re.search(r'^venue = "([^"\\]*(?:\\.[^"\\]*)*)"', content, re.MULTILINE)
        venue_url_match = re.search(r'^venue_url = "([^"\\]*(?:\\.[^"\\]*)*)"', content, re.MULTILINE)
        
        if not venue_match:
            print(f"Warning: No venue found in {file_path}")
            return toml_fixed
        
        current_venue = venue_match.group(1)
        current_url = venue_url_match.group(1) if venue_url_match else ""
        
        # Unescape for normalization processing
        current_venue_unescaped = current_venue.replace('\\"', '"').replace('\\\\', '\\')
        
        # Normalize venue
        normalized_venue, normalized_url = normalize_venue_name(current_venue_unescaped)
        
        # Re-escape the normalized venue for TOML
        normalized_venue_escaped = escape_toml_string(normalized_venue)
        
        # Check if changes are needed
        venue_changed = current_venue != normalized_venue_escaped
        url_changed = current_url != normalized_url
        
        if not venue_changed and not url_changed and not toml_fixed:
            return False
        
        if dry_run:
            print(f"\n{file_path}:")
            if venue_changed:
                print(f"  Venue: '{current_venue}' → '{normalized_venue}'")
            if url_changed:
                print(f"  URL: '{current_url}' → '{normalized_url}'")
            return True
        
        # Apply changes
        new_content = content
        if venue_changed:
            new_content = re.sub(
                r'^venue = "([^"]*)"',
                f'venue = "{normalized_venue}"',
                new_content,
                flags=re.MULTILINE
            )
        
        if venue_url_match and url_changed:
            new_content = re.sub(
                r'^venue_url = "([^"]*)"',
                f'venue_url = "{normalized_url}"',
                new_content,
                flags=re.MULTILINE
            )
        elif not venue_url_match and normalized_url:
            # Add venue_url line after venue line
            new_content = re.sub(
                r'^(venue = "[^"]*")$',
                f'\\1\nvenue_url = "{normalized_url}"',
                new_content,
                flags=re.MULTILINE
            )
        
        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"Updated: {os.path.basename(file_path)}")
        if venue_changed:
            print(f"  Venue: '{current_venue}' → '{normalized_venue}'")
        if url_changed:
            print(f"  URL: '{current_url}' → '{normalized_url}'")
        
        return True
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    """Main function to process all event files"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Normalize venue names and add URLs')
    parser.add_argument('--dry-run', action='store_true', 
                       help='Show what would be changed without making changes')
    parser.add_argument('--file', help='Process a specific file instead of all files')
    args = parser.parse_args()
    
    if args.file:
        files = [args.file]
    else:
        files = glob.glob('content/event/*.md')
    
    if not files:
        print("No event files found")
        return
    
    print(f"Processing {len(files)} event files...")
    if args.dry_run:
        print("DRY RUN - No changes will be made\n")
    
    changed_count = 0
    for file_path in sorted(files):
        if update_event_file(file_path, args.dry_run):
            changed_count += 1
    
    print(f"\n{'Would change' if args.dry_run else 'Changed'} {changed_count} files")
    
    if args.dry_run:
        print("\nRun without --dry-run to apply changes")

if __name__ == '__main__':
    main()