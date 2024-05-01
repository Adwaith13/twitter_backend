#importing all necessary packages
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

#import base from database
from .database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer,primary_key=True,nullable=False)
    email = Column(String,nullable=False,unique=True)
    username = Column(String,nullable=False,unique=True)
    password = Column(String,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False, server_default=text('now()'))
    

