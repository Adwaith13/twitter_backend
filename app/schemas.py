from pydantic import BaseModel,EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    email:EmailStr
    username:str
    password:str