from sqlalchemy import Column, Integer, String, DateTime,Time, Date
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
Base = declarative_base()
class User(Base):
    __tablename__ = "users"
    user_id = Column(String(500), primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100), unique=True)
    hashed_password = Column(String(500))
    registration_date = Column(DateTime,  default=datetime.now())

    
class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True,  autoincrement="auto", index=True)
    title = Column(String(500))
    description = Column(String(500))
    catergory = Column(String(100))
    priority = Column(String(100))
    status = Column(String(100))   
    due_date = Column(Date)
    due_time = Column(Time)
    user_id = Column(String(500))
    created_at = Column(DateTime, default=datetime.now())

class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, autoincrement="auto", index=True)
    title = Column(String(100))
    description = Column(String(100))
    user_id = Column(String(500))
    date_created = Column(DateTime, default=datetime.now())
