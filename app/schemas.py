from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional

#schema to create user
class UserCreate(BaseModel):
    email:EmailStr
    username:str
    password:str

#schema for user output
class UserOut(BaseModel):
    id:int
    email:EmailStr
    username:str
    created_at:datetime
    
    class Config:
        orm_mode = True
 
 #schema for token        
class Token(BaseModel):
    access_token:str
    token_type:str    
class TokenData(BaseModel):
    id:Optional[str] = None