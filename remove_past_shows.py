#!/usr/bin/env python3

import os
import re
from datetime import datetime
from pathlib import Path

def parse_date_from_file(file_path):
    """Parse the date from a markdown file's frontmatter"""
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Extract date from frontmatter
        date_match = re.search(r'date = (\d{4}-\d{2}-\d{2})', content)
        if date_match:
            date_str = date_match.group(1)
            return datetime.strptime(date_str, '%Y-%m-%d').date()
    except Exception as e:
        print(f"Error parsing {file_path}: {e}")
    
    return None

def remove_past_shows():
    """Remove show files that have already passed"""
    event_dir = Path('/home/dustin/showsinaz-com/content/event')
    today = datetime.now().date()
    
    if not event_dir.exists():
        print(f"Event directory {event_dir} does not exist")
        return
    
    removed_files = []
    kept_files = []
    
    # Get all markdown files in the event directory
    for file_path in event_dir.glob('*.md'):
        # Skip the _index.md file
        if file_path.name == '_index.md':
            continue
            
        show_date = parse_date_from_file(file_path)
        
        if show_date is None:
            print(f"Could not parse date from {file_path.name}, keeping file")
            kept_files.append(file_path.name)
            continue
        
        if show_date < today:
            # Show has passed, remove the file
            try:
                file_path.unlink()
                removed_files.append(f"{file_path.name} ({show_date})")
                print(f"Removed: {file_path.name} ({show_date})")
            except Exception as e:
                print(f"Error removing {file_path.name}: {e}")
        else:
            # Show is in the future, keep it
            kept_files.append(f"{file_path.name} ({show_date})")
    
    print(f"\nSummary:")
    print(f"Removed {len(removed_files)} past show files")
    print(f"Kept {len(kept_files)} upcoming show files")
    
    if removed_files:
        print(f"\nRemoved files:")
        for file_info in removed_files:
            print(f"  - {file_info}")

if __name__ == "__main__":
    print("Removing past show files...")
    remove_past_shows()
    print("Done!")