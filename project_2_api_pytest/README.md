# Project 2: API Test Automation

## Stack

- FastAPI (local API)
- pytest
- requests

## What this project demonstrates

- API smoke checks
- CRUD-like endpoint checks
- Status code and response body assertions

## What I tested

- `GET /health`: API доступно и возвращает `{"status": "ok"}`
- `POST /tasks`: создание задачи, проверка структуры ответа и типов полей
- `POST /tasks` с пустым `title`: валидационная ошибка `422`
- `GET /tasks/{id}`: получение ранее созданной задачи по идентификатору
- `GET /tasks/{id}` для несуществующей задачи: корректный `404`
- `PATCH /tasks/{id}/complete`: изменение статуса задачи на `completed = true`
- `PATCH /tasks/{id}/complete` для несуществующей задачи: корректный `404`

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
