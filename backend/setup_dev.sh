#!/bin/bash

# Set up Python virtual environment for development
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
python -m playwright install chromium

# Display success message
echo "Development environment set up successfully!"
echo "To activate the virtual environment, run: source venv/bin/activate" 