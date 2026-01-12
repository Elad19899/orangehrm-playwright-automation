# OrangeHRM Playwright Animation

## Purpose
Build a reliable, maintainable UI automation framework using Playwright with Python to validate the core, business critical flows of the OrangeHRM Demo site.

## Tech Stack
- Python 3.11+
- Playwright for Python
- pytest
- python-dotenv

## Setup
1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Install Playwright browsers:
   ```bash
   playwright install
   ```
4. Configure `.env`:
   - Copy `.env.example` to `.env`
   - Adjust variables if needed.

## Running Tests
Run all tests:
```bash
pytest
```

Run smoke tests:
```bash
pytest -m smoke
```

Run with headed mode (visible browser):
```bash
pytest --headed
```

Linting:
```bash
ruff check .
```

Formatting:
```bash
black .
```
