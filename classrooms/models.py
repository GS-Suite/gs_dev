from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, ARRAY
from models import Base, SessionLocal
from user.models import User
import datetime

db = SessionLocal()


class Classroom(Base):

    __tablename__ = "classrooms"

    id = Column(Integer, primary_key=True, index=True)
    uid = Column(String, unique=True, index=True)
    creator_uid = Column(String, ForeignKey(User.uid))
    name = Column(String)
    enrolled = Column(ARRAY(String), default = [])
    date_created = Column(DateTime)


async def get_classrooms_by_user(uid: str):
    return db.query(Classroom).filter(
        Classroom.creator_uid == uid
    ).with_entities(
        Classroom.name
    ).all()


async def get_classroom_by_uid(uid: str):
    return db.query(Classroom).filter(
        Classroom.uid == uid
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
        db.refresh(classroom)
        return True
    except Exception as e:
        print(e)
        db.rollback()
        return False


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
