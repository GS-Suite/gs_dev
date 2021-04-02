from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from db_setup.pg_setup import Base, SessionLocal
from user.models import User
import datetime


db = SessionLocal()
class Classroom(Base):

    __tablename__ = "classrooms"

    id = Column(Integer, primary_key=True, index=True)
    uid = Column(String, unique=True, index=True)
    creator_uid = Column(String, ForeignKey(User.uid))
    name = Column(String)
    date_created = Column(DateTime)
    entry_code = Column(String, default = None)
    

async def get_classrooms_by_user(uid: str):
    x = db.query(Classroom).filter(
        Classroom.creator_uid == uid
    ).all()
    return x


async def get_classroom_by_uid(uid: str):
    return db.query(Classroom).filter(
        Classroom.uid == uid
    ).first()


async def get_classroom_by_entry_code(code):
    return db.query(Classroom).filter(
        Classroom.entry_code == code
    ).first()
    

async def get_classroom_by_name(uid: str, name: str):
    return db.query(Classroom).filter(
        Classroom.creator_uid == uid,
        Classroom.name == name
    ).first()


async def create_classroom(creator_uid: str, name: str, uid: str):
    classroom = Classroom(
        uid=uid,
        creator_uid=creator_uid,
        name=name,
        date_created=datetime.datetime.now()
    )
    try:
        db.add(classroom)
        db.commit()
        '''
            Creating Mongo classroom
        '''
        #mongo_resp = mongo.create_mongo_classroom(uid)

        db.refresh(classroom)
        return True, classroom
    except Exception as e:
        print(e)
        db.rollback()
        return False, False


async def delete_classroom(classroom: Classroom):
    try:
        db.delete(classroom)
        db.commit()
        db.refresh(classroom)
        return True
    except Exception as e:
        print(e)
        db.rollback()
        return False


async def delete_user_classrooms(user_uid: str):
    try:
        db.query(Classroom).filter(
            Classroom.creator_uid == user_uid
        ).delete()
        db.commit()
        return True
    except Exception as e:
        print(e)
        db.rollback()
        return False


async def generate_entry_code(classroom, code):
    try:
        classroom.entry_code = code
        db.commit()
        return classroom
    except Exception as e:
        print(e)
        db.rollback()
        return False