# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Shows in AZ is a static website for listing live music events in Arizona. It's built using Zola static site generator with Python utilities for content management.

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

### Bash Utilities

- `generate_shows.sh` - Generates event markdown files from `list.txt`
  - Parses format: `6/25 Artist @ Venue`
  - Creates properly formatted markdown files with frontmatter
  - No external dependencies, portable across environments
- `remove_past_shows.sh` - Removes past event files to keep content current
  - Uses filename pattern matching for date comparison
  - Automatically runs daily via GitHub Actions
- `list.txt` - Plain text file with show listings in M/D format

## Common Development Commands

### Build and Serve
- `zola build` - Build the static site to `public/` directory
- `zola serve` - Start development server at http://127.0.0.1:1111
- `zola check` - Validate site structure and links

### Content Management
- `./generate_shows.sh` - Generate event files from list.txt
- `./remove_past_shows.sh` - Clean up past events

### Sass Compilation
Zola automatically compiles Sass files from `sass/` to `static/` when `compile_sass = true` in config.toml.

## Key Features

### Frontend Functionality (`templates/shows.html`)
- **Live Search**: Filters events by artist, venue, or date (`script.js:138-160`)
- **Date Filters**: "All Events", "Today", "This Weekend", "Next 7 Days" (`script.js:80-129`)
- **Responsive Design**: CSS Grid layout adapting to screen size
- **Venue Links**: Clickable venue names linking to venue websites
- **Auto-hide Past Events**: JavaScript automatically hides past shows (`script.js:180-201`)

### Content Generation
The `generate_shows.sh` script processes show data with:
- Date parsing from M/D to ISO format (assumes 2025)
- Filename slugification for SEO-friendly URLs
- Automatic frontmatter generation

### Automated Cleanup
GitHub Actions workflow runs daily at 6 AM EST to automatically remove past events:
- Triggered by cron schedule: `0 11 * * *` (UTC)
- Can be manually triggered via GitHub web interface
- Uses `remove_past_shows.sh` for cleanup logic

## File Organization

Events are organized with date-prefixed filenames: `YYYY-MM-DD-artist-name.md`
This ensures proper chronological sorting and prevents filename conflicts.

## Development Workflow

1. Add new shows to `list.txt` in format: `M/D Artist @ Venue`
2. Run `./generate_shows.sh` to create markdown files
3. Use `zola serve` to preview changes locally
4. Past events are automatically cleaned up via GitHub Actions daily
5. Build for production with `zola build`

The site uses Zola's built-in features for RSS feeds, HTML minification, and Sass compilation as configured in `config.toml`.

## Architecture Notes

### Template Structure
- `base.html` provides the main layout with header/footer and logo
- `shows.html` contains the main event listing with inline JavaScript for filtering
- All JavaScript functionality is embedded directly in the template (no external JS files)
- CSS uses a dark theme with responsive design patterns

### Static Assets
- Logo image served from `static/logo.png` 
- CSS uses responsive sizing with viewport units and media queries
- Mobile-first approach with breakpoint at 768px