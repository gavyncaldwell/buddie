.PHONY: setup format lint typecheck test clean

# Install dependencies
setup:
	python -m venv venv
	. venv/bin/activate && pip install --upgrade pip
	. venv/bin/activate && pip install --no-build-isolation -r requirements-dev.txt
	. venv/bin/activate && pre-commit install

# Format code
format:
	. venv/bin/activate && black .
	. venv/bin/activate && isort .

# Lint code
lint:
	. venv/bin/activate && flake8 .

# Type check
typecheck:
	. venv/bin/activate && mypy app

# Run tests
test:
	. venv/bin/activate && pytest

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