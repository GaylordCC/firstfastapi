from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL
SQLALCHEMY_DATABASE_URL = 'sqlite:///./blog.db'

# Creating the Engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Creating the Session Local
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False, )

# Declrative Base
Base = declarative_base()


def get_db():
    db = SessionLocal()  # Create an instance of SessionLocal
    
    try:
        yield db
    finally:
        db.close()
