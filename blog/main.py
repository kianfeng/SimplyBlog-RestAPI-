from fastapi import FastAPI
from . import models, crud
from .database import engine
from .routers import blogs, users, authentications

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(blogs.router)
app.include_router(users.router)
app.include_router(authentications.router)






