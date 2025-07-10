from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://u150585579_taskplus:ONLYmore!112@srv1847.hstgr.io/u150585579_taskplus_db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True,          
    pool_recycle=280,             
    pool_timeout=30,               
    connect_args={
        "connect_timeout": 10       
    }
)
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
