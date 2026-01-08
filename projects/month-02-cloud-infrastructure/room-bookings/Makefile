.PHONY: help dev-build dev-up dev-down dev-rebuild dev-logs build push release clean

help:  ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

# Development commands
dev-build:  ## Build development image without starting
	docker compose -f compose.dev.yml build

dev-up:  ## Start development environment
	docker compose -f compose.dev.yml up -d

dev-down:  ## Stop development environment
	docker compose -f compose.dev.yml down

dev-rebuild:  ## Rebuild and start dev environment
	docker compose -f compose.dev.yml up -d --build

dev-logs:  ## Tail development logs
	docker compose -f compose.dev.yml logs -f

# Production build/push commands
build:  ## Build Docker image with version tag (usage: make build VERSION=v1.0)
	docker build -t stillron/libcal-bookings:$(VERSION) -t stillron/libcal-bookings:latest .

build-clean:  ## Build without cache - use after dependency updates (usage: make build-clean VERSION=v1.0)
	docker build --no-cache -t stillron/libcal-bookings:$(VERSION) -t stillron/libcal-bookings:latest .

push:  ## Push Docker image to Docker Hub (usage: make push VERSION=v1.0)
	docker push stillron/libcal-bookings:$(VERSION)
	docker push stillron/libcal-bookings:latest

release: build push  ## Build and push new version (usage: make release VERSION=v1.0)

release-clean: build-clean push  ## Build without cache and push (usage: make release-clean VERSION=v1.0)

# Cleanup
clean:  ## Remove stopped containers and dangling images
	docker compose -f compose.dev.yml down -v
	docker image prune -f