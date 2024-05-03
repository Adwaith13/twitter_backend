from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from ..models import Tweets
from ..oauth2 import get_current_user
from ..schemas import CreateTweet,TweetGet
from ..database import get_db
from typing import List

router = APIRouter(prefix="/tweets", tags=["Tweets"])

#create new tweet
@router.post("/",response_model=TweetGet,status_code=status.HTTP_201_CREATED)
def create_tweet(tweet:CreateTweet,db:Session=Depends(get_db),
                 current_user_id:int = Depends(get_current_user)):
    new_tweet = Tweets(owner_id = current_user_id.id,**tweet.dict())
    db.add(new_tweet)
    db.commit()
    db.refresh(new_tweet)
    
    return new_tweet
    
#get tweet by id
@router.get("/{id}",response_model=TweetGet,status_code=status.HTTP_200_OK)
def get_tweet_by_id(id:int,db:Session=Depends(get_db),
                    current_user:int=Depends(get_current_user)):
    tweet = db.query(Tweets).filter(Tweets.owner_id == id).first()
    if not tweet:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Tweet with owner id {id} not found")
    
    return tweet
    
#get all tweets
@router.get("/",response_model=List[TweetGet],status_code=status.HTTP_200_OK)
def get_all_tweets(db:Session=Depends(get_db)):
    tweet = db.query(Tweets).all()
    return tweet

