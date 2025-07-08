from sqlalchemy import Column, Integer, String, DateTime,Time, Date
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
Base = declarative_base()
class User(Base):
    __tablename__ = "users"
    user_id = Column(String, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    registration_date = Column(DateTime,  default=datetime.now())

    
class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True,  autoincrement="auto", index=True)
    title = Column(String)
    description = Column(String)
    catergory = Column(String)
    priority = Column(String)
    status = Column(String)   
    due_date = Column(Date)
    due_time = Column(Time)
    user_id = Column(String)
    created_at = Column(DateTime, default=datetime.now())

class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, autoincrement="auto", index=True)
    title = Column(String)
    description = Column(String)
    user_id = Column(String)
    date_created = Column(DateTime, default=datetime.now())
