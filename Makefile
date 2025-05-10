.PHONY: setup-frontend setup-backend format-frontend format-backend lint-frontend lint-backend test-frontend test-backend dev build deploy clean

# Setup
setup-frontend:
	cd frontend && npm install && npm run prepare

setup-backend:
	cd backend && make setup

setup: setup-frontend setup-backend

# Formatting
format-frontend:
	cd frontend && npm run format

format-backend:
	cd backend && make format

format: format-frontend format-backend

# Linting
lint-frontend:
	cd frontend && npm run lint

lint-backend:
	cd backend && make lint

lint: lint-frontend lint-backend

# Testing
test-frontend:
	cd frontend && npm run check

test-backend:
	cd backend && make test

test: test-frontend test-backend

# Development
dev:
	docker-compose up

# Build
build:
	docker build -t buddie .

# Deploy
deploy:
	fly deploy

# Clean
clean:
	cd backend && make clean
	rm -rf frontend/node_modules
	rm -rf frontend/.svelte-kit 