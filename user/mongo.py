import pymongo
from mongo_setup import Mongo_CONN

from classrooms import mongo


DB_NAME = 'Users'


def create_user_mongo(uid: str):

    try:
        Mongo_CONN[DB_NAME][uid].insert_one(
            {
                'user_id': uid,
                'enrolled': [],
            }
        )
        return True
    except Exception as e:
        raise e