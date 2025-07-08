from fastapi import Depends, HTTPException, status, APIRouter
from database import get_db
from models import User
from auth import get_current_user, oauth2_scheme, create_access_token, authenticate_user, security, hash_password
from datetime import timedelta
from base import UserCreate, LoginUser,  LoginResponse, Basicreponse
import uuid
router = APIRouter()

@router.post("/api/auth/register", response_model=Basicreponse)
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

@router.post("/api/auth/login", response_model=LoginResponse)
def login(user: LoginUser, db=Depends(get_db)):
      usr = authenticate_user(db, user.email, user.password)
      if not usr:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail={"status":"failed", "data":None, "message":"Invalid email or password"})
      access_token_expires = timedelta(days=30)
      access_token = create_access_token(data={"sub": user.email}, expires_delta=access_token_expires)
      return {"status":"success","access_token": access_token, "token_type": "bearer", "data":None, "message":"Login Successful" }

