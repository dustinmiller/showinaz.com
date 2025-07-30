# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Shows in AZ is a static website for listing live music events in Arizona. It's built using Zola static site generator with bash utilities for content management.

## Architecture

The site uses Zola (https://www.getzola.org/) as the static site generator with the following structure:

- `config.toml` - Zola configuration with site metadata and build settings
- `content/` - Markdown content files organized by section
  - `content/_index.md` - Homepage content configuration
  - `content/event/` - Individual event markdown files (auto-generated)
- `templates/` - Zola HTML templates using Tera templating
  - `base.html` - Base template with common layout
  - `shows.html` - Main events listing page with filtering and search
  - `index.html` - Homepage template
  - `page.html` - Individual event page template
- `static/` - Static assets (CSS, images, etc.)
- `sass/` - Sass stylesheets (compiled by Zola)

## Content Management

### Event Data Structure
Each event is stored as a markdown file in `content/event/` with this frontmatter format:
```toml
+++
title = "Artist Name at Venue Name"
date = 2025-07-01
template = "page.html"
slug = "2025-07-01-artist-name"

[extra]
artist = "Artist Name"
venue = "Venue Name"
venue_url = "https://venue-website.com"
+++
```

### Automation Scripts

#### Bash Scripts (`scripts/`)
- `generate_shows.sh` - Generates event markdown files from `list.txt`
  - Parses format: `6/25 Artist @ Venue`
  - Creates properly formatted markdown files with frontmatter
  - No external dependencies, portable across environments
- `remove_past_shows.sh` - Removes past event files to keep content current
  - Uses filename pattern matching for date comparison
  - Automatically runs daily via GitHub Actions

#### Python Scripts (`scripts/`)
- `normalize_venues.py` - Normalizes venue names and adds official URLs
  - Maps 80+ Arizona venue variations to canonical names
  - Adds official venue websites for ticket links
  - Automatically fixes TOML formatting issues (quote escaping)
  - Supports dry-run mode for preview
  - Handles special cases like venue @ location format

#### Input Files
- `list.txt` - Plain text file with show listings in M/D format

## Common Development Commands

### Makefile Commands (Recommended)
- `make help` - Show all available commands with descriptions
- `make serve` - Start development server at http://127.0.0.1:1111
- `make build` - Build the static site to `public/` directory
- `make check` - Validate site structure and links
- `make generate` - Generate event files from list.txt
- `make normalize-venues` - Normalize venue names and add URLs
- `make normalize-venues-dry` - Preview venue normalization changes
- `make remove-past` - Clean up past events
- `make setup-events` - Complete event setup (generate + normalize)
- `make update-events` - Update events (generate new + remove past)
- `make social-logo` - Create optimized social media logo
- `make status` - Show git status and event counts

### Direct Commands
- `zola build` - Build the static site to `public/` directory
- `zola serve` - Start development server at http://127.0.0.1:1111
- `zola check` - Validate site structure and links
- `python3 scripts/normalize_venues.py` - Normalize venues
- `python3 scripts/normalize_venues.py --dry-run` - Preview changes
- `python3 scripts/normalize_venues.py --file path/to/event.md` - Process single file

### Sass Compilation
Zola automatically compiles Sass files from `sass/` to `static/` when `compile_sass = true` in config.toml.

## Key Features

### Frontend Functionality (`templates/shows.html`)
- **Live Search**: Filters events by artist, venue, or date with inline JavaScript
- **Date Filters**: "All Events", "Today", "This Weekend", "Next 7 Days" 
- **Responsive Design**: CSS Grid layout adapting to screen size
- **Venue Links**: Clickable venue names linking to venue websites
- **Auto-hide Past Events**: JavaScript automatically hides past shows
- **No external JS dependencies**: All functionality embedded in HTML templates

### Content Generation
The `scripts/generate_shows.sh` script processes show data with:
- Date parsing from M/D to ISO format (assumes 2025)
- Filename slugification for SEO-friendly URLs
- Automatic frontmatter generation

### Venue Normalization (`scripts/normalize_venues.py`)
- **Comprehensive Mapping**: 80+ Arizona venue variations mapped to canonical names
- **URL Integration**: Automatic addition of official venue websites
- **TOML Validation**: Fixes formatting issues like unescaped quotes
- **Error Prevention**: Prevents build failures from malformed frontmatter
- **Smart Processing**: Handles special formats like "Artist @ Venue @ Location"

### Social Media Optimization (`templates/base.html`)
- **Open Graph Tags**: Rich previews on Facebook, LinkedIn, and other platforms
- **Twitter Cards**: Optimized sharing experience on Twitter
- **Logo Optimization**: 1200x630 social media logo for proper aspect ratios
- **Dynamic Metadata**: Page-specific titles and descriptions

### Automated Cleanup
GitHub Actions workflow runs daily at 6 AM EST to automatically remove past events:
- Triggered by cron schedule: `0 11 * * *` (UTC)
- Can be manually triggered via GitHub web interface
- Uses `scripts/remove_past_shows.sh` for cleanup logic

### HTML Validation
The repository includes a pre-commit hook that automatically validates HTML using the W3C validator:
- **Location**: `.git/hooks/pre-commit`
- **Trigger**: Runs when HTML or Markdown files are staged for commit
- **Process**: 
  1. Builds the site with `make build`
  2. Validates all HTML files in `public/` directory using Docker
  3. Blocks commit if validation fails
- **Requirements**: Docker must be installed
- **Bypass**: Use `git commit --no-verify` to skip validation if needed
- **Docker Command**: Uses `ghcr.io/validator/validator:latest` image

## File Organization

Events are organized with date-prefixed filenames: `YYYY-MM-DD-artist-name.md`
This ensures proper chronological sorting and prevents filename conflicts.

## Development Workflow

### Standard Workflow
1. Add new shows to `list.txt` in format: `M/D Artist @ Venue`
2. Run `make setup-events` to generate and normalize events
3. Use `make serve` to preview changes locally
4. Past events are automatically cleaned up via GitHub Actions daily
5. Build for production with `make build`

### Venue Management
- The `normalize_venues.py` script handles 80+ Arizona venue mappings
- Automatically fixes common TOML formatting issues like unescaped quotes
- Adds official venue URLs for better user experience
- Use `make normalize-venues-dry` to preview changes before applying

### TOML Formatting
The normalization script automatically handles:
- Unescaped quotes in titles (e.g., album names like "Fragile")
- Special characters in artist and venue names
- Proper TOML string escaping for reliable parsing

The site uses Zola's built-in features for RSS feeds, HTML minification, and Sass compilation as configured in `config.toml`.

## Architecture Notes

### Template Structure
- `base.html` provides the main layout with header/footer, logo, and social media meta tags
- `shows.html` contains the main event listing with inline JavaScript for filtering
- All JavaScript functionality is embedded directly in the template (no external JS files)
- CSS uses a dark theme with responsive design patterns

### Static Assets
- Main logo: `static/logo.png` with responsive sizing
- Social logo: `static/logo-social.png` (1200x630 for optimal sharing)
- CSS uses viewport units and media queries for fluid scaling
- Mobile-first approach with breakpoint at 768px
- Dark theme with custom color palette (#282a36 background, #f8f8f2 text)

### Content Processing Pipeline
1. **Input**: Simple format in `list.txt` - `M/D Artist @ Venue`
2. **Generation**: `scripts/generate_shows.sh` creates markdown files with TOML frontmatter
3. **Normalization**: `scripts/normalize_venues.py` standardizes venue names and adds URLs
4. **Validation**: Automatic TOML formatting fixes prevent build failures
5. **Build**: Zola processes everything into static HTML

### Quality Assurance
- **TOML Validation**: Automatic quote escaping and formatting fixes
- **Venue Consistency**: Standardized venue names across all events
- **URL Verification**: Official venue websites for better user experience
- **Build Safety**: Scripts prevent malformed files that break site generation

### Content Input Format
Shows are added via `list.txt` using simple format: `M/D Artist @ Venue`
- Example: `7/15 The Strokes @ Crescent Ballroom`
- Date assumes current year (2025)
- Artist and venue names are automatically slugified for URLs
- Venue normalization handles variations and adds official URLs
- No manual markdown file creation needed

## Common Troubleshooting

### TOML Parsing Errors
If `make serve` fails with TOML parsing errors:
1. Run `make normalize-venues` to automatically fix formatting issues
2. Check for unescaped quotes in event titles or venue names
3. The normalize script handles these automatically going forward

### Venue Name Inconsistencies
- Use `make normalize-venues-dry` to preview venue standardization
- Add new venue mappings to `scripts/normalize_venues.py` VENUE_MAPPING
- Run `make normalize-venues` after adding new venues to apply changes

### Missing Venue URLs
- Check if venue is in the VENUE_MAPPING dictionary
- Add new venues with official URLs to the mapping
- Run normalization to apply URL additions