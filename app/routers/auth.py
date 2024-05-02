from fastapi import APIRouter,status,HTTPException,Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import User
from ..oauth2 import create_token
from ..utils import verify
from ..schemas import Token

router = APIRouter(tags=['Authentication'])

@router.post("/login",response_model=Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    user = db.query(User).filter(User.email == user_credentials.username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    if not verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    # create a token
    access_token = create_token(data={"user_id": user.id})
    
    # return token
    return {"access_token": access_token, "token_type": "bearer"}
