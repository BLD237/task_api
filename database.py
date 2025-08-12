from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

SQLALCHEMY_DATABASE_URL = "mysql+pymysql:/username:password@provider/database"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True,        # ✅ Fixes "MySQL server has gone away"
    pool_recycle=280,          # ✅ Prevents dropped stale connections
    pool_size=10,              # ✅ Default is 5 — increase to avoid bottlenecks
    max_overflow=20,           # ✅ Allow temporary extra connections
    pool_timeout=30,           # ✅ How long to wait for a free connection
    connect_args={
        "connect_timeout": 10  # ✅ Connect timeout for initial handshake
    }
)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

# This should ideally not be run on import in production
# Better to handle migrations via Alembic
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()  # ✅ Always release connection
