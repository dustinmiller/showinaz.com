# 🎵 Shows in AZ

> Your ultimate guide to live music in Arizona

A sleek, fast, and responsive website showcasing upcoming concerts and live music events across Arizona. Built with modern web technologies for music lovers who want to stay in the loop.

## ✨ Features

🎯 **Smart Filtering** - Find shows by artist, venue, or date with real-time search  
📱 **Mobile-First Design** - Looks amazing on any device  
🌙 **Dark Theme** - Easy on the eyes with a modern aesthetic  
🚀 **Lightning Fast** - Static site generation for optimal performance  
🔄 **Auto-Updates** - Past events automatically cleaned up daily  
🎪 **Venue Links** - Direct links to venue websites and tickets  
📱 **Social Sharing** - Optimized link previews with proper Open Graph tags  
🛠️ **Smart Normalization** - Automatic venue name standardization and URL addition  

## 🏗️ Tech Stack

- **[Zola](https://www.getzola.org/)** - Blazing fast static site generator
- **Vanilla JavaScript** - No frameworks, just pure performance
- **CSS Grid & Flexbox** - Modern responsive layouts
- **GitHub Actions** - Automated content management
- **Bash Scripts** - Portable, dependency-free tooling

## 🚀 Quick Start

```bash
# Clone the repo
git clone https://github.com/dustinmiller/showsinaz.com.git
cd showsinaz.com

# Install Zola (macOS)
brew install zola

# Start development server
zola serve
# → http://127.0.0.1:1111
```

## 📝 Adding Shows

1. **Add shows to `list.txt`** in the format:
   ```
   7/15 The Strokes @ Crescent Ballroom
   7/20 Tame Impala @ The Van Buren
   8/5 Local Natives @ Walter Studios
   ```

2. **Generate and normalize event files:**
   ```bash
   make setup-events
   # Or manually:
   ./scripts/generate_shows.sh
   python3 scripts/normalize_venues.py
   ```

3. **Preview your changes:**
   ```bash
   make serve
   ```

## 🛠️ Development

### Commands
```bash
# See all available commands
make help

# Build for production
make build

# Start development server
make serve

# Generate events from list.txt
make generate

# Normalize venue names and add URLs
make normalize-venues

# Clean up past events
make remove-past

# Complete event setup (generate + normalize)
make setup-events
```

### Project Structure
```
├── content/event/          # Auto-generated event markdown files
├── templates/             # HTML templates
│   ├── base.html         # Main layout with social media tags
│   ├── shows.html        # Event listing page with filtering
│   └── index.html        # Homepage
├── static/               # CSS, images, assets
│   ├── logo.png          # Main logo
│   └── logo-social.png   # Social media optimized logo
├── scripts/              # Automation scripts
│   ├── generate_shows.sh # Event generation from list.txt
│   ├── remove_past_shows.sh # Cleanup past events
│   └── normalize_venues.py # Venue name & URL normalization
├── Makefile              # Self-documenting build commands
└── list.txt             # Show data input file
```

## 🤖 Automation

**Daily Cleanup** - GitHub Actions automatically removes past events every day at 6 AM EST, keeping the site fresh and current.

**Content Generation** - Bash scripts convert plain text show listings into properly formatted markdown files with metadata.

**Venue Normalization** - Python script automatically normalizes venue names, adds official URLs, and fixes TOML formatting issues.

**Social Media Optimization** - Auto-generated Open Graph and Twitter Card tags ensure proper link previews with optimized logos.

## 🎨 Design Philosophy

- **Performance First** - Static generation means lightning-fast loads
- **Mobile-Centric** - Designed for on-the-go music discovery
- **Accessibility** - Semantic HTML and keyboard navigation
- **Simplicity** - Clean, distraction-free interface focused on the music

## 🤝 Contributing

Found a show we missed? Want to improve the site? 

1. Fork the repo
2. Add your shows to `list.txt`
3. Run `./generate_shows.sh`
4. Submit a pull request

## 📄 License

MIT License - feel free to use this code for your own local music scene!

---

**Made with ❤️ for the Arizona music community**

[Visit the site →](https://showsinaz.com)