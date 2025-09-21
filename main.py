from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, List

app = FastAPI(title="Task Manager (Mini FastAPI Demo)")


# pydantic model for creating task
class TaskCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=120, example="Pray")
    completed: bool = Field(False, description="Is the task completed?")
    priority: Optional[int] = Field(
        None, ge=1, le=5, description="Priority 1 (low) to 5 (high)", example=1
    )


class Task(TaskCreate):
    id: int


# in-memory storage
tasks: List[dict] = []
_next_id = 1


@app.get("/", tags=["root"])
def get_root():
    return {"message": "Hello, FastAPI! 🎉"}


@app.post("/tasks", response_model=Task, status_code=201, tags=["tasks"])
def create_task(payload: TaskCreate):
    """
    Create a task.
    FastAPI will validate the incoming JSON against TaskCreate automatically.
    """
    global _next_id
    task_data = payload.dict()
    task_data["id"] = _next_id
    _next_id += 1
    tasks.append(task_data)
    return task_data


@app.get("/tasks", response_model=List[Task], status_code=200, tags=["tasks"])
def list_tasks():
    return tasks
