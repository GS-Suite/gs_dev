from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql.sqltypes import Boolean
from db_setup.pg_setup import SessionLocal, Base
from user import mongo
import datetime


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
    verified = Column(Boolean, default = False)
    profile_picture_link = Column(String)


async def create_user(user: dict, uid: str):
    db_user = User(
        **user.__dict__,
        uid = uid,
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


async def get_user_by_email(username: str, email: str):
    return db.query(User).filter(
        User.username == username,
        User.email == email
    ).first()


async def get_user_for_dashboard(uid: str):
    return db.query(User).filter(
        User.uid == uid
    ).first()


async def update_profile(user: User, details):
    try:
        user.first_name = details.first_name
        user.last_name = details.last_name
        user.email = details.email
        db.commit()
        return user
    except Exception as e:
        print(e)
        db.rollback()
        return False


async def update_password(user: User, new_password):
    try:
        user.password = new_password
        db.commit()
        return True
    except Exception as e:
        print(e)
        db.rollback()
        return False

async def delete_user(user: User):
    try:
        db.delete(user)
        db.commit()
        return True
    except Exception as e:
        print(e)
        db.rollback()
        return False


async def set_verified(email):
    try:
        x = db.query(User).filter(
            User.email == email
        ).first()
        x.verified = True
        db.commit()
        return True
    except Exception as e:
        print(e)
        db.rollback()
        return False


async def update_profile_picture(uid, link):
    try:
        user = db.query(User).filter(
            User.uid == uid
        ).first()
        user.profile_picture_link = link
        db.commit()
        return True
    except Exception as e:
        print(e)
        return False