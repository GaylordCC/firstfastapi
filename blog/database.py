from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# DataBase URL
SQLALCHAMY_DATABASE_URL = 'sqlite:/// ./blog.db'

# Creating the Engine
engine = create_engine(SQLALCHAMY_DATABASE_URL,connect_args={"check_same_thread": False})

# Creating the Session Local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declrative Base
Base = declarative_base()
