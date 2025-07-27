# Venue Mapping Status

## Summary
- **Total unique venues**: 42
- **Total events**: 714  
- **Venues mapped**: 42 (100%)
- **Venues with URLs**: 31 (74%)
- **Major venues covered**: ✅ All top 10 venues have URLs

## ✅ Fully Mapped (31 venues with URLs)
All major performance venues in Arizona are properly mapped with official URLs:

### Major Venues (10+ events)
- Crescent Ballroom (71 events) 
- Valley Bar (69 events)
- The Van Buren (64 events) 
- The Rebel Lounge (60 events)
- The Nile Theater (38 events)
- Arizona Financial Theatre (38 events)
- MIM Music & Instrument Museum (35 events)
- The Marquee Theater (35 events)
- Club Congress (32 events)
- 191 Toole (25 events)
- Talking Stick Resort Amphitheatre (16 events)
- Orpheum Theater Phoenix (15 events)
- Celebrity Theatre (11 events)
- Yucca Tap Room (11 events)

### Medium Venues (5-10 events)
- Darkstar, Last Exit Live, Walter Studios, Sunbar, The Rialto Theater, Nile Underground, Fox Theater, Footprint Center, Mesa Amphitheatre, Ak-Chin Pavilion

### Smaller Venues (1-4 events)
- Maya Day Club, Rawhide Event Center, Rockbar, Orpheum Theater Flagstaff, Mesa Arts Center, The Rhythm Room, Wild Horse Pass Hotel & Casino, Tempe Center for the Arts, Arizona State Fair

## ❌ Missing URLs (11 venues)
These venues are mapped but lack official website URLs:

### Bars/Restaurants (likely no official websites)
- Pho Cao (1 event) - Vietnamese restaurant
- Wasted Grain (1 event) - Bar/venue
- Cactus Jacks (1 event) - Bar
- The Electric Pickle (1 event) - Bar
- Birdcage Saloon (1 event) - Bar

### Event Spaces/Centers
- San Tan Gardens (4 events) - Shopping center events
- X Phoenix (3 events) - Rooftop pool party venue
- Dynamite Beer Co (2 events) - Brewery
- The Darkside (1 event) - Alternative venue
- Fort Tuthill County Park (1 event) - County park
- TBD (placeholder) - Events not yet confirmed

## Impact
- **714 events** now have consistent, standardized venue names
- **31 major venues** provide direct links to official websites for tickets
- **100% coverage** means no more unmapped venue variations
- **TOML formatting** issues automatically resolved

## Automation Tools
- `make audit-venues` - Show current venue mapping status
- `make normalize-venues` - Apply venue standardization and URL addition
- `make normalize-venues-dry` - Preview changes before applying
- `scripts/audit_venues.py --create-reference` - Generate research file for new venues