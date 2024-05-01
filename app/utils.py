from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

#password hash function
def hash(password:str):
    return pwd_context.hash(password)
    