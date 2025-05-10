# Buddie

A personal cannabis concierge application that helps users track, rate, and discover cannabis products.

## Project Structure

- **backend**: Python FastAPI backend with modules for:
  - API endpoints
  - Database models
  - Authentication
  - Web scrapers
  - ML recommendation engine
- **frontend**: SvelteKit PWA with:
  - Components
  - Routes
  - Stores
  - API clients

## Tech Stack

- **Frontend**: SvelteKit + TypeScript + PWA
- **Backend**: Python FastAPI + SQLModel
- **Database**: PostgreSQL on fly.io
- **Authentication**: JWT + OAuth (Google, etc.)
- **Infrastructure**: Docker, fly.io

## Development Tools

### Code Quality Tools

- **Backend**:
  - **Black**: Python code formatter
  - **isort**: Import sorter
  - **flake8**: Linter
  - **mypy**: Type checking
  - **pre-commit**: Git hooks
- **Frontend**:
  - **ESLint**: JavaScript/TypeScript linter
  - **Prettier**: Code formatter
  - **svelte-check**: Type checking for Svelte
  - **husky**: Git hooks
  - **lint-staged**: Run linters on staged files
  - **commitlint**: Enforce commit message format

### Development Workflow

The project provides various commands to ease development:

```bash
# Set up development environment
make setup

# Format code
make format

# Lint code
make lint

# Run tests
make test

# Start development servers with docker
make dev

# Build for production
make build

# Deploy to fly.io
make deploy
```

### Git Workflow

The repository uses git hooks to ensure code quality:

1. **Pre-commit**: Automatically formats and lints code before commit
2. **Commit messages**: Must follow the [Conventional Commits](https://www.conventionalcommits.org/) format

Example commit messages:

- `feat: add user profile page`
- `fix: correct authentication flow`
- `docs: update API documentation`
- `style: format code according to guidelines`

## Getting Started

1. Clone this repository
2. Run `make setup` to install dependencies
3. Run `make dev` to start the development environment
4. Frontend will be available at: http://localhost:3001
5. Backend API will be available at: http://localhost:8001
6. API docs will be available at: http://localhost:8001/docs
7. Adminer (database admin) will be available at: http://localhost:8082

## VSCode Configuration

This repository includes VSCode configuration for optimal development experience:

1. Install recommended extensions when prompted
2. Use the included debugging configurations
3. Enjoy automatic formatting and linting
