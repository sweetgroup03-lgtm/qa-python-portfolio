# Project 2: API Test Automation

## Stack

- FastAPI (local API)
- pytest
- requests

## What this project demonstrates

- API smoke checks
- CRUD-like endpoint checks
- Status code and response body assertions

## Run

```powershell
cd project_2_api_pytest
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Start API in terminal 1:

```powershell
uvicorn app.main:app --reload
```

Run tests in terminal 2:

```powershell
cd project_2_api_pytest
.venv\Scripts\Activate.ps1
pytest -v
```

