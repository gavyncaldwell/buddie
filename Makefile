.PHONY: setup-frontend setup-backend format-frontend format-backend lint-frontend lint-backend test-frontend test-backend dev build deploy clean

# Setup
setup-frontend:
	cd frontend && npm install && npm run prepare

setup-backend:
	@echo "Backend will be set up via Docker - use 'make dev' to start the containers"

setup: setup-frontend setup-backend

# Formatting
format-frontend:
	cd frontend && npm run format

format-backend:
	docker compose exec backend bash -c "cd /app && black . && isort ."

format: format-frontend format-backend

# Linting
lint-frontend:
	cd frontend && npm run lint

lint-backend:
	docker compose exec backend bash -c "cd /app && flake8 ."

lint: lint-frontend lint-backend

# Testing
test-frontend:
	cd frontend && npm run check

test-backend:
	docker compose exec backend bash -c "cd /app && pytest"

test: test-frontend test-backend

# Development
dev:
	docker compose up

# Build
build:
	docker build -t buddie .

# Deploy
deploy:
	fly deploy

# Clean
clean:
	docker compose down -v
	rm -rf frontend/node_modules
	rm -rf frontend/.svelte-kit 