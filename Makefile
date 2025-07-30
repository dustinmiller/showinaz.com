.PHONY: help build serve check generate clean remove-past lint test deploy normalize-venues normalize-venues-dry update-events setup-events audit-venues audit-venues-reference check-links check-venue-links check-content-links

help: ## @@ Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## @@.*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## @@"}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

build: ## @@ Build the static site to public/ directory
	zola build

serve: ## @@ Start development server at http://127.0.0.1:1111
	zola serve

check: ## @@ Validate site structure and links
	zola check

generate: ## @@ Generate event files from list.txt
	./scripts/generate_shows.sh

clean: ## @@ Remove build artifacts and generated files
	rm -rf public/
	@echo "Cleaned build artifacts"

remove-past: ## @@ Archive past event files (preserves URLs)
	./scripts/remove_past_shows.sh

archive-past: remove-past ## @@ Alias for remove-past - archive old events

lint: build ## @@ Check code formatting and validate HTML
	@echo "Validating HTML..."
	docker run --rm -v "$$(pwd)/public:/public:ro" ghcr.io/validator/validator:latest vnu --skip-non-html /public/

test: ## @@ Run tests and validation checks
	@echo "Running link checks..."
	-python3 scripts/check_links.py --venue-urls-only --max-workers 5
	@echo "Note: Connection errors are normal as many venues block automated requests"

deploy: build ## @@ Build and prepare for deployment
	@echo "Site built successfully in public/"
	@echo "Deploy public/ directory to your hosting provider"

dev: serve ## @@ Alias for serve - start development server

new-events: generate ## @@ Alias for generate - create events from list.txt

cleanup: remove-past ## @@ Alias for remove-past - archive old events

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

normalize-venues: ## @@ Normalize venue names and add URLs (events + archive)
	python3 scripts/normalize_venues.py

normalize-venues-dry: ## @@ Preview venue normalization changes (dry run)
	python3 scripts/normalize_venues.py --dry-run

update-events: generate remove-past ## @@ Update events: generate new ones and archive past ones
	@echo "Events updated successfully!"

setup-events: generate normalize-venues ## @@ Complete event setup: generate and normalize venues
	@echo "Events generated and venues normalized!"

audit-venues: ## @@ Audit venue mappings and show missing URLs
	python3 scripts/audit_venues.py

audit-venues-reference: ## @@ Create venue reference file for URL research
	python3 scripts/audit_venues.py --create-reference

check-links: ## @@ Check for broken venue URLs and content links
	python3 scripts/check_links.py

check-venue-links: ## @@ Check only venue URLs for broken links
	python3 scripts/check_links.py --venue-urls-only

check-content-links: ## @@ Check only content links for broken links
	python3 scripts/check_links.py --content-links-only