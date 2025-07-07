from fastapi import FastAPI, Depends, HTTPException, status, WebSocket, WebSocketDisconnect
from fastapi.security import HTTPBasicCredentials
from fastapi.middleware.cors import CORSMiddleware
from database import get_db
from models import User, Todo
from auth import get_current_user, oauth2_scheme, create_access_token, authenticate_user, security, hash_password
from datetime import timedelta, datetime
from typing import List
from apscheduler.schedulers.background import BackgroundScheduler
import hashlib
from base import UserCreate, LoginUser, TodoModel, ResponseStructure, LoginResponse, Basicreponse, SingleTaskResponseStructure
import uuid
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)
class WebsocketManager:
    def __init__(self):
        self.active_connections = {}
    async def connect(self, websocket: WebSocket, user_id: str):
            await websocket.accept()
            self.active_connections[user_id] = websocket
    def disconnect(self, user_id: str):
            if user_id in self.active_connections:
                del self.active_connections[user_id]
    async def send_message(self, user_id: str, message: str):
            if user_id in self.active_connections:
                  await self.active_connections[user_id].send_text(message)

ws_manager = WebsocketManager()
@app.post("/api/auth/register", response_model=Basicreponse)
def resgister_user(user: UserCreate, db=Depends(get_db)):
      existing_user = db.query(User).filter(User.email == user.email).first()
      user_id = str(uuid.uuid1())
      if existing_user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"status":"failed", "data":None, "message":"Email already exist"})
      new_user = User(user_id=user_id, name = user.name, email= user.email, hashed_password = hash_password(password=user.password))
      db.add(new_user)
      db.commit()
      db.refresh(new_user)
      return {"status":"success", "message":"User created successfully"}
@app.post("/api/auth/login", response_model=LoginResponse)
def login(user: LoginUser, db=Depends(get_db)):
      usr = authenticate_user(db, user.email, user.password)
      if not usr:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail={"status":"failed", "data":None, "message":"Invalid email or password"})
      access_token_expires = timedelta(minutes=2)
      access_token = create_access_token(data={"sub": user.email}, expires_delta=access_token_expires)
      return {"status":"success","access_token": access_token, "token_type": "bearer", "data":None, "message":"Login Successful" }

@app.get("/api/tasks")
def read_tasks(current_user: User = Depends(get_current_user), db= Depends(get_db)):
      todos = db.query(Todo).filter(Todo.user_id == current_user.user_id).all()
      if todos:            
        return {"status":"success", "data":todos, "message":"Data fetched successfully"}
      else:
        return {"status":"success", "data": None, "message":"Data fetched successfully"}
@app.post("/api/tasks", response_model=Basicreponse)
def create_task():
     pass
@app.get("/tasks/{task_id}", response_model=SingleTaskResponseStructure)
def read_task():
     pass
@app.put("tasks/{task_id}", response_model=Basicreponse)
def update_task():
     pass
@app.delete("/tasks/{todo_id}", response_model=Basicreponse)
def delete_task():
     pass

@app.websocket("/ws")
async def websocket_enpoint(websocket: WebSocket, current_user: User = Depends(get_current_user)):
     await ws_manager.connect(websocket, current_user.user_id)
     try: 
          while True:
               message = await websocket.receive_text()
               await ws_manager.send_message(current_user.user_id, f"Recieved message: {message}")
     except WebSocketDisconnect:
          ws_manager.disconnect(current_user.user_id)
          print("Client Disconnected")
     except Exception as e:
          ws_manager.disconnect(current_user.user_id)
          print(f"Error occured: {e}")
     pass
            
     
# scheduler = BackgroundScheduler()
# def send_notification(todo_id: int):
#       db = next(get_db())
#       todo = db.query(Todo).filter(Todo.id == todo_id).first()
#       db.close()


