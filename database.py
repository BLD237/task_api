from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
SQLALCHEMY_DATABASE_URL = "sqlite:///uptodo.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base.metadata.create_all(bind=engine)
def get_db():
    db = SessionLocal()    
    try:
        yield db
    finally:
        db.close()