.PHONY: setup format lint typecheck test clean

# Install dependencies
setup:
	pip install -r requirements-dev.txt
	pre-commit install

# Format code
format:
	black .
	isort .

# Lint code
lint:
	flake8 .

# Type check
typecheck:
	mypy app

# Run tests
test:
	pytest

# Run all code quality tools
check: format lint typecheck test

# Clean up temporary files
clean:
	rm -rf .mypy_cache/
	rm -rf .pytest_cache/
	rm -rf __pycache__/
	rm -rf app/__pycache__/
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete 