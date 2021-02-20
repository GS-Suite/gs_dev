from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from user.models import User
from sqlalchemy.orm import Session
from models import Base, SessionLocal
import datetime


db = SessionLocal()

class Token(Base):

    __tablename__ = "token"
    
    id = Column(Integer, primary_key = True, index = True)
    user_id = Column(String, ForeignKey(User.uid))
    token_value = Column(String)
    date_issued = Column(DateTime, default = datetime.datetime.now())


async def get_token_by_value(token: str):
    return db.query(Token).filter(
        Token.token_value == token,
    ).first()


async def get_token_by_user(user_id: int):
    return db.query(Token).filter(
        Token.user_id == user_id,
    ).first()


async def create_token(user_id: int, token_value: str):
    token = Token(
        user_id = user_id,
        token_value = token_value,
        date_issued = datetime.datetime.now()
    )
    try:
        db.add(token)
        db.commit()
        db.refresh(token)
        return token
    except Exception as e:
        print(e)
        return False


async def delete_token(token):
    try:
        db.delete(token)
        db.commit()
        db.refresh(token)
        return True
    except Exception as e:
        print(e)
        db.rollback()
        return False


async def refresh_token(user_id, new_token_value):
    ''' delete tokens '''
    tokens = db.query(Token).filter(
        Token.user_id == user_id,
    ).all()
    #print(tokens)
    for i in tokens:
        db.delete(i)
    new_token = Token(
        user_id = user_id,
        token_value = new_token_value,
        date_issued = datetime.datetime.now()
    )
    ''' add tokens '''
    try:
        db.add(new_token)
        db.commit()
        return new_token
    except Exception as e:
        db.rollback()
        print(e)
        return False