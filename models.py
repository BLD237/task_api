from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
Base = declarative_base()
class User(Base):
    __tablename__ = "users"
    user_id = Column(String, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    registration_date = Column(DateTime,  default=datetime.utcnow)

    
class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True,  autoincrement="auto", index=True)
    title = Column(String)
    description = Column(String)
    catergory = Column(String)
    priority = Column(String)
    user_id = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    due_at = Column(DateTime)


