import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()
from sqlalchemy.orm import sessionmaker
from models import Base

# Use internal URL on Render (same network), external URL when running locally.
# Set DATABASE_URL in Render dashboard or in .env locally.
SQLALCHEMY_DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://task_user:password@localhost:5432/task_api_aqle",
)

# Render and some providers give postgres://; SQLAlchemy 1.4+ expects postgresql://
if SQLALCHEMY_DATABASE_URL.startswith("postgres://"):
    SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=280,
    pool_size=10,
    max_overflow=20,
    pool_timeout=30,
    connect_args={"connect_timeout": 10},
)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

# Tables are created via Alembic migrations; do not create_all here in production.
# Uncomment below only for quick local bootstrap without migrations:
# Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
