from fastapi import FastAPI
from . import models
from .database import engine
from .routers import blog, user


app = FastAPI()

# Create the database tables
models.Base.metadata.create_all(engine)

# Include the routers
app.include_router(blog.router)
app.include_router(user.router)



