from fastapi import FastAPI
from .db import create_task, get_tasks, update_task, delete_task, create_table_if_not_exists

app = FastAPI()
create_table_if_not_exists()

@app.get("/")
def home():
    return {"Home Page"}

@app.post("/tasks-add/")
def create_task_endpoint(title: str, description: str):
    create_task(title, description)
    return {"message": "Task created successfully!"}

@app.get("/tasks/")
def get_tasks_endpoint():
    tasks = get_tasks()
    return {"tasks": [dict(task) for task in tasks]}  # Convert rows to dicts

@app.put("/tasks/{task_id}")
def update_task_endpoint(task_id: int, status: str):
    update_task(task_id, status)
    return {"message": "Task updated successfully!"}

@app.delete("/tasks/{task_id}")
def delete_task_endpoint(task_id: int):
    delete_task(task_id)
    return {"message": "Task deleted successfully!"}
