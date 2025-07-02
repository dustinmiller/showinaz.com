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

2. **Generate event files:**
   ```bash
   ./generate_shows.sh
   ```

3. **Preview your changes:**
   ```bash
   zola serve
   ```

## 🛠️ Development

### Commands
```bash
# Build for production
zola build

# Validate site
zola check

# Clean up past events
./remove_past_shows.sh
```

### Project Structure
```
├── content/event/          # Auto-generated event markdown files
├── templates/             # HTML templates
│   ├── base.html         # Main layout
│   ├── shows.html        # Event listing page
│   └── index.html        # Homepage
├── static/               # CSS, images, assets
├── generate_shows.sh     # Event generation script
├── remove_past_shows.sh  # Cleanup script
└── list.txt             # Show data input
```

## 🤖 Automation

**Daily Cleanup** - GitHub Actions automatically removes past events every day at 6 AM EST, keeping the site fresh and current.

**Content Generation** - Simple bash scripts convert plain text show listings into properly formatted markdown files with metadata.

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