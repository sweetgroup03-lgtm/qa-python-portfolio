# Project 3: UI Test Automation (Playwright + Python)

## Stack

- Playwright for Python
- pytest
- Page Object pattern

## What this project demonstrates

- UI functional checks
- Form validation checks
- Reusable page object

## Run

```powershell
cd project_3_ui_playwright
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
playwright install
```

Start local static server in terminal 1:

```powershell
cd project_3_ui_playwright
python -m http.server 5500 -d app
```

Run tests in terminal 2:

```powershell
cd project_3_ui_playwright
.venv\Scripts\Activate.ps1
pytest -v
```

