from fastapi import FastAPI
from . import models
from .database import engine
from .routers import users,auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#routes
app.include_router(users.router)
app.include_router(auth.router)

#health route
@app.get("/")
def health():
    return {"status":"Success","message":"Server Running Successfully"}

