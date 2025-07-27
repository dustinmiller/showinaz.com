.PHONY: help build serve check generate clean remove-past lint test deploy

help: ## @@ Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## @@.*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## @@"}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

build: ## @@ Build the static site to public/ directory
	zola build

serve: ## @@ Start development server at http://127.0.0.1:1111
	zola serve

check: ## @@ Validate site structure and links
	zola check

generate: ## @@ Generate event files from list.txt
	./generate_shows.sh

clean: ## @@ Remove build artifacts and generated files
	rm -rf public/
	@echo "Cleaned build artifacts"

remove-past: ## @@ Remove past event files (automated cleanup)
	./remove_past_shows.sh

lint: ## @@ Check code formatting and style
	@echo "No specific linting configured for Zola sites"
	@echo "Consider adding HTML/CSS validators if needed"

test: ## @@ Run tests (placeholder for future testing)
	@echo "No tests configured yet"
	@echo "Consider adding link checking or content validation"

deploy: build ## @@ Build and prepare for deployment
	@echo "Site built successfully in public/"
	@echo "Deploy public/ directory to your hosting provider"

dev: serve ## @@ Alias for serve - start development server

new-events: generate ## @@ Alias for generate - create events from list.txt

cleanup: remove-past ## @@ Alias for remove-past - clean up old events

all: clean build ## @@ Clean and build the site

watch: ## @@ Watch for changes and rebuild (development mode)
	zola serve --watch

init: ## @@ Initialize development environment
	@echo "Checking dependencies..."
	@command -v zola >/dev/null 2>&1 || { echo "Zola not found. Install from https://www.getzola.org/"; exit 1; }
	@echo "Development environment ready!"
	@echo "Run 'make serve' to start development server"

status: ## @@ Show git status and upcoming events count
	@echo "=== Git Status ==="
	@git status --short
	@echo ""
	@echo "=== Event Count ==="
	@echo "Total events: $$(find content/event -name '*.md' 2>/dev/null | wc -l)"
	@echo "Upcoming events: $$(find content/event -name '2025-*.md' 2>/dev/null | wc -l)"

social-logo: ## @@ Create optimized social media logo (1200x630)
	@python3 -c "from PIL import Image; img = Image.open('static/logo.png'); social = Image.new('RGBA', (1200, 630), (0,0,0,0)); size = min(630, 600); resized = img.resize((size, size), Image.Resampling.LANCZOS); social.paste(resized, ((1200-size)//2, (630-size)//2), resized); social.save('static/logo-social.png'); print('Created logo-social.png')"

commit: ## @@ Stage and commit changes with descriptive message
	@echo "Staging changes..."
	@git add .
	@echo "Enter commit message:"
	@read -p "> " msg; git commit -m "$$msg"

push: ## @@ Push commits to remote repository
	git push origin main

full-deploy: all commit push ## @@ Complete deployment: build, commit, and push

update-events: generate remove-past ## @@ Update events: generate new ones and remove past ones
	@echo "Events updated successfully!"