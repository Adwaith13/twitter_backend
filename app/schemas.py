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
    
#schema for tweet
class CreateTweet(BaseModel):
    tweet:str
    
class TweetGet(BaseModel):
    id:int
    tweet:str
    created_at:datetime
    owner_id:int
    owner:UserOut    
    class Config:
        orm_mode = True
    