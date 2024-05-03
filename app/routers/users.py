#importing all necessary packages
from fastapi import APIRouter,status,HTTPException,Depends,Response
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import User
from ..schemas import UserCreate,UserOut
from ..utils import hash
from ..oauth2 import get_current_user

#create a router
router = APIRouter(prefix="/users",tags=["Users"])

#user create route
@router.post("/",status_code=status.HTTP_201_CREATED,response_model=UserOut)
def create_user(user:UserCreate,db:Session=Depends(get_db)):
    hashed_password = hash(user.password)
    user.password = hashed_password
    
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user   

#get user by id route
@router.get("/{id}",response_model=UserOut)
def get_user(id:int,db:Session=Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with {id} does not exist")
        
    return user

#delete user
@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id:int,db:Session=Depends(get_db),
                 current_user = Depends(get_current_user)):
    user_query = db.query(User).filter(User.id == id)
    user = user_query.first()
    
    if user == None:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} does not exist")
         
    if user.id != current_user.id:
         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Not authorized to perform requested action")
         
    user_query.delete(synchronize_session = False)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)  
    