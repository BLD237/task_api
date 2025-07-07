from fastapi import FastAPI
from pydantic import BaseModel
import sqlalchemy as sql
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Task App API", 
              version="1.0.0",
                description="Fast Task API is a restful API used for task management. With All the CRUD operations on tasks using SQLITE database",
                servers=[{"DeepXlabs Servers"}],
                contact= ["MUFOR BELMOND, muforbelmond20@gmail.com"]
                )

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


# Input model for creating a task (no id)
class TaskCreate(BaseModel):
    title: str
    description: str
    done: bool

# Full Task model (includes id)
class Task(TaskCreate):
    id: int
tasks = [
    {"id": 1, "title": "Task 1", "description": "Description 1", "done": False},
    {"id": 2, "title": "Task 2", "description": "Description 2", "done": False},
    {"id": 3, "title": "Task 3", "description": "Description 3", "done": False},
]

@app.get("/tasks/")
async def read_tasks():
    return {"code": 200, "status": "success", "data": tasks}

@app.post("/tasks/", response_model=Task)
async def create_task(task: TaskCreate):
    # Generate new ID (max id + 1)
    new_id = max([t["id"] for t in tasks], default=0) + 1
    new_task = task.dict()
    new_task["id"] = new_id
    tasks.append(new_task)
    return new_task

@app.get("/tasks/{task_id}", response_model=Task)
async def read_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return {"error": "Task Not Found"}

@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, task: TaskCreate):
    for existing_task in tasks:
        if existing_task['id'] == task_id:
            existing_task['title'] = task.title
            existing_task['description'] = task.description
            existing_task['done'] = task.done
            return existing_task
    return {"error": "Task Not Found"}

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            return {"status": "Success", "message": "task deleted", "data": []}
    return {"error": "Task Not Found"}

