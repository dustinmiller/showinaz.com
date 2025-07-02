#!/bin/bash

# Simple show generator that creates basic markdown files
# Usage: ./generate_shows_simple.sh

# Change to script directory
cd "$(dirname "$0")"

# Check if list.txt exists
if [ ! -f "list.txt" ]; then
    echo "list.txt not found"
    exit 1
fi

# Create content/event directory if it doesn't exist
mkdir -p content/event

echo "Generating show files from list.txt..."

generated_count=0

# Read list.txt line by line
while IFS= read -r line || [ -n "$line" ]; do
    # Skip empty lines and lines starting with ---
    [[ -z "$line" || "$line" =~ ^--- ]] && continue
    
    # Parse format: M/D Artist @ Venue
    if [[ $line =~ ^([0-9]{1,2}/[0-9]{1,2})[[:space:]]+(.+)[[:space:]]+@[[:space:]]+(.+)$ ]]; then
        date_part="${BASH_REMATCH[1]}"
        artist="${BASH_REMATCH[2]}"
        venue="${BASH_REMATCH[3]}"
        
        # Convert date to YYYY-MM-DD format (assuming 2025)
        IFS='/' read -r month day <<< "$date_part"
        iso_date=$(printf "2025-%02d-%02d" "$month" "$day")
        
        # Create filename slug
        artist_slug=$(echo "$artist" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g' | sed 's/--*/-/g' | sed 's/^-\|-$//g')
        filename="$iso_date-$artist_slug.md"
        
        # Create markdown content
        cat > "content/event/$filename" << EOF
+++
title = "$artist at $venue"
date = $iso_date
template = "page.html"
slug = "$iso_date-$artist_slug"

[extra]
artist = "$artist"
venue = "$venue"
venue_url = ""
+++
EOF
        
        echo "Generated: $filename"
        ((generated_count++))
    else
        echo "Skipping malformed line: $line"
    fi
done < list.txt

echo
echo "Generated $generated_count show files"
echo "Done!"