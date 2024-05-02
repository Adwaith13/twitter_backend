from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

#password hash function
def hash(password:str):
    return pwd_context.hash(password)

#verify password
def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
    