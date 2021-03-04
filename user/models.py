from sqlalchemy import Column, Integer, String, DateTime, ARRAY
from pg_setup import SessionLocal, Base
from sqlalchemy.orm import load_only
import datetime

from user import mongo

db = SessionLocal()


class User(Base):

    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    uid = Column(String, unique=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    date_joined = Column(DateTime)


async def create_user(user: dict, uid: str):
    db_user = User(
        uid=uid,
        username=user.username,
        password=user.password,
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        date_joined=datetime.datetime.now()
    )
    try:
        db.add(db_user)
        '''
            Create Mongo User id insert
        '''
        if mongo.create_user_mongo(uid=uid): ### returns True
            db.commit()
            db.refresh(db_user)
            return True
    except Exception as e:
        print(e)
    db.rollback()
    return False


async def get_user_by_username(username: str):
    return db.query(User).filter(
        User.username == username
    ).first()


async def get_user_by_uid(uid: str):
    return db.query(User).filter(
        User.uid == uid
    ).first()


async def get_user_for_dashboard(uid: str):
    return db.query(User).filter(
        User.uid == uid
    ).first()


async def delete_user(user: User):
    try:
        db.delete(user)
        db.commit()
        return True
    except Exception as e:
        print(e)
        db.rollback()
        return False
