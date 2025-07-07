from pydantic import BaseModel
from datetime import datetime
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
    user_id  : str
    created_at : datetime
    due_at: datetime
class ResponseStructure(BaseModel):
    status: str
    data: list[TodoModel]
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
     data: None
class SingleTaskResponseStructure(BaseModel):
    status: str
    data: TodoModel
    message: str
   
