#!/bin/bash

# Get today's date in YYYY-MM-DD format
today=$(date +%Y-%m-%d)

# Change to project root directory (one level up from script directory)
cd "$(dirname "$0")/.."

# Check if content/event directory exists
if [ ! -d "content/event" ]; then
    echo "Event directory content/event does not exist"
    exit 1
fi

# Create archive directory if it doesn't exist
if [ ! -d "content/archive" ]; then
    mkdir -p "content/archive"
    echo "Created archive directory"
fi

echo "Archiving past show files..."

archived_count=0
kept_count=0

# Process each markdown file in the event directory
for file in content/event/*.md; do
    # Skip if no files match or if it's _index.md
    [ -f "$file" ] || continue
    [ "$(basename "$file")" = "_index.md" ] && continue
    
    # Extract date from the filename (assumes YYYY-MM-DD format at start)
    filename=$(basename "$file")
    if [[ $filename =~ ^([0-9]{4}-[0-9]{2}-[0-9]{2}) ]]; then
        file_date="${BASH_REMATCH[1]}"
        
        # Compare dates (string comparison works for YYYY-MM-DD format)
        if [[ "$file_date" < "$today" ]]; then
            echo "Archiving: $filename ($file_date)"
            mv "$file" "content/archive/"
            ((archived_count++))
        else
            ((kept_count++))
        fi
    else
        echo "Could not parse date from $filename, keeping file"
        ((kept_count++))
    fi
done

echo
echo "Summary:"
echo "Archived $archived_count past show files to content/archive/"
echo "Kept $kept_count upcoming show files in content/event/"
echo "Done!"