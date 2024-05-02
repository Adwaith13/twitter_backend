from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    db_username : str
    db_password : str
    db_hostname : str
    db_dbname : str
    secret_key : str
    algorithm : str
    expire_minutes : int
    
    class Config:
        env_file = ".env"
        

settings = Settings()