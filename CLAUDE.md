# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Shows in AZ is a static website for listing live music events in Arizona. It's a client-side only application with no build process or dependencies beyond the browser.

## Architecture

The site uses a simple three-file architecture:

- `index.html` - Main HTML structure with semantic layout
- `styles.css` - Complete CSS styling with glassmorphism design and responsive layout
- `script.js` - Vanilla JavaScript for show data management and filtering

### Data Structure

Show data is stored as a JavaScript array in `script.js:1-39` with the format:
```javascript
{ date: '6/25', artist: 'Artist Name', venue: 'Venue Name' }
```

### Key Components

- **Show Cards**: Dynamically generated DOM elements displaying individual shows
- **Filter System**: Buttons that filter shows by "all", "today", or "weekend"
- **Responsive Grid**: CSS Grid layout that adapts from multi-column to single column

## Development

Since this is a static site with no build process:

- Open `index.html` directly in a web browser to test
- No compilation, bundling, or package management required
- Changes to any file are immediately visible on browser refresh

## Adding New Shows

To add shows, modify the `shows` array in `script.js:1-39`. Each show object requires:
- `date`: String in M/D format (e.g., "6/25")
- `artist`: String with artist/band name
- `venue`: String with venue name

## Styling Architecture

The CSS uses:
- CSS Grid for responsive layout (`styles.css:89-94`)
- Glassmorphism effects with `backdrop-filter` and transparency
- CSS custom properties could be added for theme consistency
- Mobile-first responsive design with breakpoint at 768px (`styles.css:160-182`)

## Filter Logic

The filtering system (`script.js:63-82`) supports:
- "today": Matches current date using JavaScript Date object
- "weekend": Hardcoded weekend dates (currently 6/26-6/29)
- "all": Shows all events

Weekend filter dates may need updating for different date ranges.