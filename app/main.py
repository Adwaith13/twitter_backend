from fastapi import FastAPI
from . import models
from .database import engine
from .routers import users,auth,tweet

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#routes
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(tweet.router)

#health route
@app.get("/")
def health():
    return {"status":"Success","message":"Server Running Successfully"}

