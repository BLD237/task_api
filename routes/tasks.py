from fastapi import Depends, HTTPException, status as s, APIRouter
from database import get_db
from models import User, Task
from auth import get_current_user
from datetime import datetime
from base import  Basicreponse, SingleTaskResponseStructure, TaskCreateModel
router = APIRouter()


@router.get("/api/tasks", )
def read_tasks(current_user: User = Depends(get_current_user), db= Depends(get_db)):
      todos = db.query(Task).filter(Task.user_id == current_user.user_id).all()
      if todos:            
        return {"status":"success", "data":todos, "message":"Data fetched successfully"}
      else:
        return {"status":"success", "data": None, "message":"No tasks found."}
      
@router.post("/api/tasks", response_model=SingleTaskResponseStructure)
def create_task(task: TaskCreateModel, current_user: User = Depends(get_current_user), db = Depends(get_db)):
     new_task = Task(title=task.title, description=task.description, catergory=task.category, priority=task.priority,user_id = current_user.user_id, status=task.status,  due_date=task.due_date, due_time = task.due_time )
     db.add(new_task)
     db.commit()
     db.refresh(new_task)
     response_time = datetime.now()
     return {"status":"success", "message":"New Task Created successfuly.", "data":new_task, "response_time":response_time }

@router.get("/api/tasks/{task_id}", response_model=SingleTaskResponseStructure)
def read_task(task_id: int, current_user: User = Depends(get_current_user), db =Depends(get_db)):
     todo = db.query(Task).filter(Task.id == task_id).first()
     response_time = datetime.now()
     if todo is None:
          raise HTTPException(status_code=s.HTTP_404_NOT_FOUND, detail={"status":"failed", "data":None, "message":"Task not found"})
     if todo.user_id != current_user.user_id:
          raise HTTPException(status_code=s.HTTP_403_FORBIDDEN, detail={"status":"failed", "data":None, "message":"You are not authorized to access this task"})
     return {"status":"success", "message":"Data fetched successfuly.", "data":todo, "response_time":response_time }
     

@router.put("/api/tasks/{task_id}", response_model=Basicreponse)
def update_task(task_id: int, title: str =None, description: str = None, category: str = None, priority: str = None, due_date: str = None, due_time: str = None, status: str = None, current_user: User = Depends(get_current_user), db = Depends(get_db)):
     task = db.query(Task).filter(Task.id == task_id).first()
     if task is None:
          raise HTTPException(status_code=s.HTTP_404_NOT_FOUND, detail={"status":"failed", "data":None, "message":"Task not found"})
     if task.user_id != current_user.user_id:
          raise HTTPException(status_code=s.HTTP_403_FORBIDDEN, detail={"status":"failed", "data":None, "message":"You are not authorized to access this task"} )
     if title:
          task.title = title
     if description:
          task.description = description
          
     if category:
          task.catergory = category
          
     if priority:
          task.priority = priority
          
     if due_date:
          task.due_date = due_date
     if due_time:
          task.due_time = due_time
     if status:
          task.status = status
          
     db.commit()
     db.refresh(task)
     return {"status":"success", "data":task, "message":"Task Updated Successfuly"}

@router.delete("/api/tasks/{task_id}", response_model=Basicreponse)
def delete_task(task_id, current_user: User = Depends(get_current_user), db = Depends(get_db)):
     todo = db.query(Task).filter(Task.id == task_id).first()
     if todo is None:
          raise HTTPException(status_code=s.HTTP_404_NOT_FOUND, detail={"status":"failed", "data":None, "message":"Task not found"})
     if todo.user_id != current_user.user_id:
          raise HTTPException(status_code=s.HTTP_403_FORBIDDEN, detail={"status":"failed", "data":None, "message":"You are not authorized to access this task"})
     db.delete(todo)
     db.commit()
     return {"status":"success", "data":None, "message":"Task Deleted Successfuly"}
