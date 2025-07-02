#!/bin/bash

# Create shows directory
mkdir -p content/shows

# Clean up existing generated files (optional)
# rm -f content/shows/2024-*.md

# Function to create filename slug
create_slug() {
    echo "$1" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g' | sed 's/--*/-/g' | sed 's/^-\|-$//g'
}

# Function to clean venue name
clean_venue() {
    echo "$1" | sed 's/Thtr/Theater/g' | sed 's/Ballrm/Ballroom/g' | sed 's/Amph/Amphitheater/g' | sed 's/Amphithtr/Amphitheater/g' | sed 's/B\.r\./Ballroom/g' | sed 's/B\.R\./Ballroom/g' | sed 's/crescent ballroom/Crescent Ballroom/gi' | sed 's/van buren/Van Buren/gi' | sed 's/[[:space:]]*$//'
}

# Function to get venue URL
get_venue_url() {
    # Remove trailing spaces and normalize
    local venue_clean=$(echo "$1" | sed 's/[[:space:]]*$//')
    case "$venue_clean" in
        "Last Exit Live") echo "https://lastexitlive.com" ;;
        "Crescent Ballroom"|"The Crescent Ballroom"|"Crescent Ballrm"|"Crescent B.R."|"Crescent BR") echo "https://www.crescentphx.com" ;;
        "The Van Buren"|"Van Buren") echo "https://www.thevanburenphx.com" ;;
        "Walter Studios") echo "https://walterstudios.com" ;;
        "Walter Wherehouse"|"Walter Wherehous") echo "https://walterwherehouse.com" ;;
        *) echo "" ;;
    esac
}

# Function to escape quotes in TOML strings
escape_toml() {
    echo "$1" | sed 's/"/\\"/g'
}

# Process each line
count=0
while IFS= read -r line; do
    # Skip empty lines and separator lines
    [[ -z "$line" || "$line" =~ ^-+$ ]] && continue
    
    # Extract date from beginning of line
    if [[ $line =~ ^([0-9]{1,2}/[0-9]{1,2}) ]]; then
        date_str="${BASH_REMATCH[1]}"
        remainder="${line#$date_str }"
        
        # Split by @
        if [[ $remainder =~ ^(.+)\ @\ (.+)$ ]]; then
            artist="${BASH_REMATCH[1]}"
            venue="${BASH_REMATCH[2]}"
            
            # Clean up venue name
            venue_clean=$(clean_venue "$venue")
            
            # Create ISO date (assuming 2025)
            month=$(echo "$date_str" | cut -d'/' -f1)
            day=$(echo "$date_str" | cut -d'/' -f2)
            iso_date=$(printf "2025-%02d-%02d" "$month" "$day")
            
            # Create filename and slug
            artist_slug=$(create_slug "$artist")
            filename="$iso_date-$artist_slug.md"
            page_slug="$iso_date-$artist_slug"
            
            # Get venue URL
            venue_url=$(get_venue_url "$venue_clean")
            
            # Escape strings for TOML
            title_escaped=$(escape_toml "$artist at $venue_clean")
            artist_escaped=$(escape_toml "$artist")
            venue_escaped=$(escape_toml "$venue_clean")
            
            # Create markdown file
            cat > "content/shows/$filename" << EOF
+++
title = "$title_escaped"
date = $iso_date
template = "page.html"
slug = "$page_slug"

[extra]
artist = "$artist_escaped"
venue = "$venue_escaped"
venue_url = "$venue_url"
+++

$artist performs at $venue_clean.
EOF
            
            echo "Generated: $filename"
            ((count++))
        fi
    fi
done < list.txt

echo
echo "Generated $count show files in content/shows"