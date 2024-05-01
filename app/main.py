from fastapi import FastAPI
from . import models
from .database import engine
from .routers import users

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)

#health route
@app.get("/")
def health():
    return {"status":"Success","message":"Server Running Successfully"}

