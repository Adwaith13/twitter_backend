#importing all necessary packages
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#connection string with local db
DATABASE_URL = "postgresql://postgres:adwaith1310@localhost/twitter"

#creating sql engine for db connection
engine = create_engine(DATABASE_URL)

#creating session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
     