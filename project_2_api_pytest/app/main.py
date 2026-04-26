from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Task API for QA Practice")

tasks: dict[int, dict] = {}
next_id = 1


class TaskCreate(BaseModel):
    title: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/tasks", status_code=201)
def create_task(payload: TaskCreate):
    global next_id
    task = {"id": next_id, "title": payload.title, "completed": False}
    tasks[next_id] = task
    next_id += 1
    return task


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = tasks.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.patch("/tasks/{task_id}/complete")
def complete_task(task_id: int):
    task = tasks.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task["completed"] = True
    return task

