from pydantic import BaseModel
from datetime import datetime, time
from models import Task
class UserCreate(BaseModel):
    name: str
    email: str
    password: str
class LoginUser(BaseModel):
    email: str
    password: str
class TodoModel(BaseModel):
    id: int
    title: str
    description: str
    catergory: str
    priority : str
    due_date: datetime
    due_time: time
    status: str
    user_id  : str
    created_at : datetime
 

class ResponseStructure(BaseModel):
    status: str
    data: TodoModel
    message: str
   
class LoginResponse(BaseModel):
        status: str
        data: None
        access_token:str
        token_type:str
        message: str     

class Basicreponse(BaseModel):
     status: str
     message: str
     data: TodoModel | None

class Response(BaseModel):
     status: str
     message: str
     data: TodoModel | None
class SingleTaskResponseStructure(BaseModel):
    status: str
    message: str
    message: str
    data: TodoModel | None
    response_time: datetime = datetime.now()

class TaskCreateModel(BaseModel):   
    title: str
    description: str
    category: str
    priority : str   
    due_date: datetime
    due_time: time
    status: str
class CategoryCreate(BaseModel):
    title : str
    description : str
class CategoryResponse(BaseModel):
    status : str
    message : str
    data: CategoryCreate | None
class CategorySchema(BaseModel):
    id : int
    title: str
    description: str
    user_id : str
    date_created : datetime
class CategoryFetch(BaseModel):
     status: str
     message: str
     data: list[CategorySchema] | None



   
