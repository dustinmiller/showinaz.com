const shows = [
    { date: '6/25', artist: 'Bayside', venue: 'The Nile Theater' },
    { date: '6/25', artist: 'Peter Frampton', venue: 'AZ Financial Theater' },
    { date: '6/25', artist: 'LosGothsCo.', venue: 'The Van Buren' },
    { date: '6/25', artist: 'Lyn Lapid', venue: 'Crescent Ballroom' },
    { date: '6/25', artist: 'Howling Giant', venue: 'Rebel Lounge' },
    { date: '6/25', artist: 'Albert Lee', venue: 'The MIM' },
    { date: '6/26', artist: 'Gong', venue: 'Walter Studios' },
    { date: '6/26', artist: 'Lords Of Acid', venue: 'The Nile Theater' },
    { date: '6/26', artist: 'Vana Liya', venue: 'Last Exit Live' },
    { date: '6/26', artist: 'Akeem Ali', venue: 'Rebel Lounge' },
    { date: '6/26', artist: 'Vinyl Station', venue: 'The MIM' },
    { date: '6/26', artist: 'Tommy Newport', venue: 'Orpheum Flagstaff' },
    { date: '6/27', artist: 'Saba', venue: 'The Van Buren' },
    { date: '6/27', artist: 'Mark Knight', venue: 'Sunbar' },
    { date: '6/27', artist: 'Kathy Mattea', venue: 'The MIM' },
    { date: '6/27', artist: 'Weston Smith & Honey Lee', venue: 'Valley Bar' },
    { date: '6/27', artist: 'Ian Munsick', venue: 'Pepsi Amphitheater' },
    { date: '6/27', artist: 'Mickey Avalon', venue: 'The Marquee Theater' },
    { date: '6/28', artist: 'Planck', venue: 'Let It Roll Bowling' },
    { date: '6/28', artist: 'Hypervisor', venue: 'Pho Cao' },
    { date: '6/28', artist: 'Lisa Lisa 40th Anniversary w/ Expose, Color Me Badd, Rob Base, C&C Music Factory, more', venue: 'Footprint Center' },
    { date: '6/28', artist: 'Gong', venue: 'Orpheum Theater Flagstaff' },
    { date: '6/28', artist: 'Lil Mosey', venue: 'The Marquee Theater' },
    { date: '6/28', artist: 'Miles Nielsen, Kelly Steward', venue: 'Rockbar' },
    { date: '6/28', artist: 'Ace Monroe', venue: 'Last Exit Live' },
    { date: '6/28', artist: 'Codd Dubz', venue: 'Darkstar' },
    { date: '6/28', artist: 'Bonnie X Clyde', venue: 'Sunbar' },
    { date: '6/28', artist: 'Elita w/ Maebe', venue: 'Valley Bar' },
    { date: '6/28', artist: 'Broncho', venue: 'Crescent Ballroom' },
    { date: '6/28', artist: 'Giovani Kiyingi & Friends', venue: 'The MIM' },
    { date: '6/28', artist: 'Key Glock', venue: 'Arizona Financial Theater' },
    { date: '6/28', artist: 'Supertask, Daggz, Arboreal', venue: 'Walter Studios' },
    { date: '6/30', artist: 'Paperflower', venue: 'Rebel Lounge' },
    { date: '7/1', artist: 'Parkway Drive, Kill Switch Engage', venue: 'Talking Stick Amphitheater' },
    { date: '7/1', artist: 'Planning For Burial', venue: 'Rebel Lounge' },
    { date: '7/1', artist: 'Betty Who', venue: 'Crescent Ballroom' },
    { date: '7/1', artist: 'Tropical Fuck Storm', venue: 'Club Congress' },
    { date: '7/2', artist: 'Tropical Fuck Storm', venue: 'Van Buren' },
    { date: '7/3', artist: 'Deserts Hearts Festival', venue: 'Various' },
    { date: '7/3', artist: 'The English Beat', venue: 'The Marquee' },
    { date: '7/3', artist: 'The Driver Era', venue: 'AZ Financial Theater' },
    { date: '7/3', artist: 'Nimino', venue: 'Sunbar' },
    { date: '7/3', artist: 'Hotel California (Eagles Tribute)', venue: 'Pepsi Amphitheater' },
    { date: '7/4', artist: 'Tsu Nami', venue: 'Darkstar' },
    { date: '7/4', artist: 'Stone Breed, Jasmine Cain', venue: 'Orpheum Theater Flagstaff' },
    { date: '7/5', artist: 'The Loop Tour', venue: 'Darkstar' },
    { date: '7/5', artist: 'bad tune & Gilligan Moss', venue: 'Darkstar' },
    { date: '7/6', artist: 'Kesha & Scissor Sisters', venue: 'Talking Stick Amphitheater' },
    { date: '7/6', artist: 'Esteban', venue: 'The MIM' },
    { date: '7/7', artist: 'The Band Feel', venue: 'Club Congress' },
    { date: '7/7', artist: 'Honey Revenge', venue: 'The Nile Theater' },
    { date: '7/8', artist: 'Pegboy', venue: 'Rebel Lounge' },
    { date: '7/8', artist: 'This Will Destroy You', venue: 'Crescent Ballroom' },
    { date: '7/9', artist: 'Tiago PZK', venue: 'The Crescent Ballroom' },
    { date: '7/9', artist: '60 Juno', venue: 'Valley Bar' },
    { date: '7/10', artist: 'Brit Floyd', venue: 'AZ Financial Theater' },
    { date: '7/10', artist: 'Death Lens', venue: 'Rebel Lounge' },
    { date: '7/10', artist: 'The Fabulous Thunderbirds', venue: 'The MIM' },
    { date: '7/11', artist: 'Allison Kraus & Union Station w/ Jerry Douglas', venue: 'AZ Financial Theater' },
    { date: '7/11', artist: 'DJ Rum', venue: 'Walter Studios' },
    { date: '7/11', artist: 'Hol!', venue: 'Sunbar' },
    { date: '7/11', artist: 'Necromantix', venue: 'Club Congress' },
    { date: '7/11', artist: 'Vandoliers', venue: 'Rebel Lounge' },
    { date: '7/11', artist: 'Esha Tewari', venue: 'Crescent Ballroom' },
    { date: '7/12', artist: 'Katy Perry', venue: 'Footprint Center' },
    { date: '7/12', artist: 'Tep No', venue: 'Valley Bar' },
    { date: '7/12', artist: 'King Lil G & Young Drummer Boy', venue: 'The Van Buren' },
    { date: '7/12', artist: 'Ae:on Mode', venue: 'Darkstar' },
    { date: '7/12', artist: 'Slushii', venue: 'Sunbar' },
    { date: '7/12', artist: 'Khani Cole', venue: 'The MIM' },
    { date: '7/12', artist: 'Durante', venue: 'Crescent Ballroom' },
    { date: '7/12', artist: 'Rhiannon Giddens & The Old-Time Revue', venue: 'Pepsi Amphitheater' },
    { date: '7/12', artist: 'Shanghai Doom & Detre', venue: 'Walter Studio' },
    { date: '7/13', artist: 'Goo Goo Dolls w/ Dashboard Confessional', venue: 'AZ Financial Theater' },
    { date: '7/13', artist: 'Duane Betts & Palmetto Hotel', venue: 'MIM' },
    { date: '7/13', artist: 'Low Cut Connie', venue: 'Crescent Ballroom' },
    { date: '7/13', artist: 'Gavn! w, Adam Yokum', venue: 'Rebel Lounge' },
    { date: '7/15', artist: 'Caleb Gordon', venue: 'The Crescent Ballroom' },
    { date: '7/15', artist: 'Penelope Road', venue: 'Rebel Lounge' },
    { date: '7/15', artist: 'Mei Semones', venue: 'Valley Bar' },
    { date: '7/15', artist: 'The Church', venue: 'The MIM' },
    { date: '7/16', artist: '311', venue: 'Pepsi Amphitheater' },
    { date: '7/16', artist: 'Mustard Service', venue: 'Rebel Lounge' },
    { date: '7/16', artist: 'The Bombpops', venue: 'Valley Bar' },
    { date: '7/16', artist: 'MC Davo & Sabino', venue: 'Crescent Ballroom' },
    { date: '7/17', artist: 'The Beautiful Mistake', venue: 'Rebel Lounge' },
    { date: '7/17', artist: 'The Paul Thorn Band', venue: 'The MIM' },
    { date: '7/17', artist: 'Sharpie Smile', venue: 'Valley Bar' },
    { date: '7/17', artist: '82 Major', venue: 'The Nile Theater' },
    { date: '7/18', artist: 'Dexter & The Moonrocks', venue: 'Marquee' },
    { date: '7/18', artist: 'Funtcase', venue: 'Sunbar' },
    { date: '7/18', artist: 'Mereba', venue: 'Valley Bar' },
    { date: '7/18', artist: 'Ally Venable', venue: 'The MIM' },
    { date: '7/18', artist: 'Closed Tear', venue: 'Nile Underground' },
    { date: '7/18', artist: 'Escape To Coconino Fest w/ Ganja White Night, Boogie T, Jade Cicada, & more', venue: 'Various' },
    { date: '7/19', artist: 'ADO', venue: 'Footprint Center' },
    { date: '7/19', artist: 'Nekromantix', venue: 'The Marquee Theater' },
    { date: '7/19', artist: 'Badklatt, Dirtysnatcha, Subfiltronik', venue: 'Sunbar' },
    { date: '7/19', artist: 'Dexter & The Moonrocks', venue: 'Orpheum Theater Flagstaff' },
    { date: '7/19', artist: 'Jordan Mitchell', venue: 'Valley Bar' },
    { date: '7/19', artist: 'Aiden Hilton', venue: 'Nile Underground' },
    { date: '7/20', artist: 'Surprise Chef', venue: 'Valley Bar' },
    { date: '7/20', artist: 'Harbour', venue: 'Crescent Ballroom' },
    { date: '7/20', artist: 'Jasiah', venue: 'The Nile Theater' },
    { date: '7/20', artist: 'Street Light Manifesto', venue: 'The Marquee' },
    { date: '7/20', artist: 'Patti Austin', venue: 'The MIM' },
    { date: '7/21', artist: 'Good Sleepy w/ Troubled Minds', venue: 'Valley Bar' },
    { date: '7/22', artist: 'Dayglow Abortions', venue: 'Last Exit Live' },
    { date: '7/22', artist: 'Michael Seyer', venue: 'Rebel Lounge' },
    { date: '7/22', artist: 'Jake Scott', venue: 'Crescent Ballroom' },
    { date: '7/22', artist: 'Tom Rush', venue: 'The MIM' },
    { date: '7/22', artist: 'Orthodox', venue: 'Nile Underground' },
    { date: '7/23', artist: 'BabyMetal', venue: 'Arizona Financial Theater' },
    { date: '7/23', artist: 'Garbage Barbie', venue: 'Rebel Lounge' },
    { date: '7/23', artist: 'Wavves', venue: 'Crescent Ballroom' },
    { date: '7/23', artist: 'Life-Guard', venue: 'Valley Bar' },
    { date: '7/23', artist: 'Ramirez', venue: 'The Nile Theater' },
    { date: '7/23', artist: 'Al Jardine & The Pet Sounds', venue: 'MIM' },
    { date: '7/24', artist: 'Sadgirl', venue: 'The Rebel Lounge' },
    { date: '7/24', artist: 'Sarah & The Safe Word', venue: 'Valley Bar' },
    { date: '7/25', artist: 'Less Than Jake', venue: 'The Van Buren' },
    { date: '7/25', artist: 'Scene Queen', venue: 'The Nile Theater' },
    { date: '7/25', artist: 'Matt Heckler, Joe\'s Truck Stop', venue: 'Last Exit Live' },
    { date: '7/25', artist: 'Gnumb', venue: 'The Rebel Lounge' },
    { date: '7/25', artist: 'Dustbowl Champion', venue: 'Valley Bar' },
    { date: '7/25', artist: 'One Night Of Queen (performed by Gary Mullen & The Works)', venue: 'Celebrity Theater' },
    { date: '7/25', artist: 'Don McLean', venue: 'The MIM' },
    { date: '7/26', artist: 'Andy C', venue: 'Sunbar' },
    { date: '7/26', artist: 'Ben Kweller', venue: 'The Crescent Ballroom' },
    { date: '7/26', artist: 'Ekkstacy', venue: 'The Van Buren' },
    { date: '7/26', artist: 'Giuseppe Ottaviani', venue: 'Darkstar' },
    { date: '7/26', artist: 'Volbeat w/ Salesforce', venue: 'Talking Stick Amphitheater' },
    { date: '7/26', artist: 'Lil Wyte', venue: 'Club Congress' },
    { date: '7/26', artist: 'Iron Priestess', venue: 'Nile Underground' },
    { date: '7/27', artist: 'Isaiah Falls', venue: 'Crescent Ballroom' },
    { date: '7/27', artist: 'Gold Celeste', venue: 'Valley Bar' },
    { date: '7/27', artist: 'Lizz Wright', venue: 'The MIM' },
    { date: '7/27', artist: 'Jessie Murph', venue: 'Arizona Financial Theater' },
    { date: '7/28', artist: 'The Mountain Grass Unit', venue: 'Valley Bar' },
    { date: '7/29', artist: 'Architects', venue: 'The Van Buren' },
    { date: '7/29', artist: 'Charlie Musselwhite', venue: 'The MIM' },
    { date: '7/29', artist: 'Frankie & Witch Fingers', venue: 'Club Congress' },
    { date: '7/30', artist: '40 Watt Sun', venue: 'Last Exit Live' },
    { date: '7/30', artist: 'Mark Battles', venue: 'Nile Underground' },
    { date: '7/30', artist: 'Frankie & The Witch Fingers', venue: 'Rebel Lounge' },
    { date: '7/30', artist: 'Henry Kapono', venue: 'The MIM' },
    { date: '7/31', artist: 'Cha Wa', venue: 'The MIM' },
    { date: '7/31', artist: 'Maye', venue: 'Valley Bar' },
    { date: '7/31', artist: 'Oliver Anthony', venue: 'The Van Buren' },
    { date: '8/1', artist: 'Primus', venue: 'Arizona Federal Theater' },
    { date: '8/1', artist: 'The Polish Ambassador & Late Night Radio', venue: 'Walter Studios' },
    { date: '8/1', artist: 'D4VD', venue: 'The Van Buren' },
    { date: '8/1', artist: 'Couch Dog', venue: 'Valley Bar' }
];

const venueLinks = {
    'Last Exit Live': 'https://lastexitlive.com',
    'Crescent Ballroom': 'https://www.crescentphx.com',
    'The Crescent Ballroom': 'https://www.crescentphx.com',
    'The Van Buren': 'https://www.thevanburenphx.com',
    'Van Buren': 'https://www.thevanburenphx.com',
    'Walter Studios': 'https://walterstudios.com',
    'Walter Wherehouse': 'https://walterwherehouse.com',
    'The Nile Theater': 'https://theniletheatre.com',
    'Rebel Lounge': 'https://rebelbar.com',
    'Valley Bar': 'https://thevalleybar.com',
    'The MIM': 'https://mim.org',
    'Sunbar': 'https://sunbarphx.com',
    'Club Congress': 'https://hotelcongress.com'
};

let currentFilter = 'all';
let currentSearch = '';
let allShows = [...shows];

function isShowUpcoming(show) {
    const today = new Date();
    today.setHours(0, 0, 0, 0); // Reset time to start of day for accurate comparison
    const showDate = getDateObj(show.date);
    return showDate >= today;
}

function getUpcomingShows(showsToFilter = shows) {
    return showsToFilter.filter(isShowUpcoming);
}

function createShowItem(show) {
    const item = document.createElement('div');
    item.className = 'show-item';
    
    const venueHtml = venueLinks[show.venue] 
        ? `<a href="${venueLinks[show.venue]}" class="show-venue" target="_blank" rel="noopener">${show.venue}</a>`
        : `<div class="show-venue">${show.venue}</div>`;
    
    item.innerHTML = `
        <div class="show-date">${show.date}</div>
        <div class="show-artist">${show.artist}</div>
        ${venueHtml}
    `;
    return item;
}

function renderShows(showsToRender = shows) {
    const showsList = document.getElementById('showsList');
    showsList.innerHTML = '';
    
    if (showsToRender.length === 0) {
        const noResults = document.createElement('div');
        noResults.className = 'no-results';
        noResults.innerHTML = currentSearch 
            ? `No shows found matching "${currentSearch}"` 
            : 'No shows found for the selected filter';
        showsList.appendChild(noResults);
        return;
    }
    
    const resultsCount = document.createElement('div');
    resultsCount.className = 'results-count';
    resultsCount.textContent = `Showing ${showsToRender.length} show${showsToRender.length !== 1 ? 's' : ''}`;
    showsList.appendChild(resultsCount);
    
    showsToRender.forEach((show, index) => {
        const item = createShowItem(show);
        item.style.animationDelay = `${index * 0.03}s`;
        showsList.appendChild(item);
    });
}

function getDateObj(dateStr) {
    const [month, day] = dateStr.split('/').map(Number);
    const currentYear = new Date().getFullYear();
    return new Date(currentYear, month - 1, day);
}

function getWeekendDates() {
    const today = new Date();
    const currentDay = today.getDay();
    const weekendDates = [];
    
    if (currentDay <= 1) {
        const saturday = new Date(today);
        saturday.setDate(today.getDate() + (6 - currentDay));
        const sunday = new Date(saturday);
        sunday.setDate(saturday.getDate() + 1);
        
        weekendDates.push(
            `${saturday.getMonth() + 1}/${saturday.getDate()}`,
            `${sunday.getMonth() + 1}/${sunday.getDate()}`
        );
    } else {
        const nextSaturday = new Date(today);
        nextSaturday.setDate(today.getDate() + (6 - currentDay + 7));
        const nextSunday = new Date(nextSaturday);
        nextSunday.setDate(nextSaturday.getDate() + 1);
        
        weekendDates.push(
            `${nextSaturday.getMonth() + 1}/${nextSaturday.getDate()}`,
            `${nextSunday.getMonth() + 1}/${nextSunday.getDate()}`
        );
    }
    
    return weekendDates;
}

function filterShows(filter) {
    currentFilter = filter;
    const today = new Date();
    today.setHours(0, 0, 0, 0);
    const todayStr = `${today.getMonth() + 1}/${today.getDate()}`;
    
    // Start with only upcoming shows
    let filteredShows = getUpcomingShows(allShows);
    
    switch(filter) {
        case 'today':
            filteredShows = filteredShows.filter(show => show.date === todayStr);
            break;
        case 'weekend':
            const weekendDates = getWeekendDates();
            filteredShows = filteredShows.filter(show => weekendDates.includes(show.date));
            break;
        case 'upcoming':
            const nextWeek = new Date(today);
            nextWeek.setDate(today.getDate() + 7);
            filteredShows = filteredShows.filter(show => {
                const showDate = getDateObj(show.date);
                return showDate <= nextWeek;
            });
            break;
        default:
            // 'all' case - already filtered to upcoming shows only
            break;
    }
    
    if (currentSearch) {
        filteredShows = searchShows(filteredShows, currentSearch);
    }
    
    renderShows(filteredShows);
}

function searchShows(showsToSearch, query) {
    if (!query.trim()) return showsToSearch;
    
    const searchTerm = query.toLowerCase().trim();
    return showsToSearch.filter(show => 
        show.artist.toLowerCase().includes(searchTerm) ||
        show.venue.toLowerCase().includes(searchTerm) ||
        show.date.includes(searchTerm)
    );
}

function initializeSearch() {
    const searchInput = document.getElementById('searchInput');
    const clearBtn = document.getElementById('clearSearch');
    
    searchInput.addEventListener('input', (e) => {
        currentSearch = e.target.value;
        clearBtn.classList.toggle('visible', currentSearch.length > 0);
        
        let filteredShows = allShows;
        
        if (currentFilter !== 'all') {
            filterShows(currentFilter);
            return;
        }
        
        // Start with upcoming shows only
        filteredShows = getUpcomingShows(allShows);
        
        if (currentSearch) {
            filteredShows = searchShows(filteredShows, currentSearch);
        }
        
        renderShows(filteredShows);
    });
    
    clearBtn.addEventListener('click', () => {
        searchInput.value = '';
        currentSearch = '';
        clearBtn.classList.remove('visible');
        filterShows(currentFilter);
    });
    
    searchInput.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            searchInput.blur();
        }
    });
}

function initializeFilters() {
    const filterButtons = document.querySelectorAll('.filter-btn');
    
    filterButtons.forEach(button => {
        button.addEventListener('click', (e) => {
            filterButtons.forEach(btn => {
                btn.classList.remove('active');
                btn.setAttribute('aria-pressed', 'false');
            });
            e.target.classList.add('active');
            e.target.setAttribute('aria-pressed', 'true');
            
            const filter = e.target.getAttribute('data-filter');
            filterShows(filter);
        });
    });
}

function sortShowsByDate(showsToSort) {
    return showsToSort.sort((a, b) => {
        const dateA = getDateObj(a.date);
        const dateB = getDateObj(b.date);
        return dateA - dateB;
    });
}

function init() {
    allShows = sortShowsByDate([...shows]);
    // Initialize with upcoming shows only
    const upcomingShows = getUpcomingShows(allShows);
    renderShows(upcomingShows);
    initializeFilters();
    initializeSearch();
}

document.addEventListener('DOMContentLoaded', init);