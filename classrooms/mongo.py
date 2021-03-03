from re import T
from mongo_setup import Mongo_CONN
from datetime import datetime
from classrooms import mongo


DB_NAME = 'Classrooms'


def create_mongo_classroom(classroom_uid: str):
    try:
        Mongo_CONN[DB_NAME][classroom_uid].insert_one(
            {
                'classroom_uid': classroom_uid,
                'enrolled': [],
                'attendance': {},
                "join_code": None
            }
        )
        return True
    except Exception as e:
        print(e)
        return False


async def get_classroom_enrolled(classroom_uid):
    x = Mongo_CONN[DB_NAME][classroom_uid].find()
    y = [i for i in x]
    if y != []:
        return y[0]["enrolled"]
    return []


async def get_classroom_details(classroom_uid):
    return [i for i in Mongo_CONN[DB_NAME][classroom_uid].find()]



async def get_user_enrolled(user_uid):
    x = Mongo_CONN["Users"][user_uid].find({})
    return x[0]["enrolled"]


def enroll_user(user_uid, classroom_uid):
    try:
        Mongo_CONN['Users'][user_uid].update(
            {'user_id': user_uid},
            {'$push': {'enrolled': classroom_uid}
             }
        )
        return True
    except Exception as e:
        print(e)
        return False



def enroll_classroom(user_uid, classroom_uid):
    try:
        Mongo_CONN[DB_NAME][classroom_uid].update(
            {'classroom_uid': classroom_uid},
            {'$push': {'enrolled': user_uid}
             }
        )
        return True
    except Exception as e:
        print(e)
        return False
