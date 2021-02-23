import pymongo
from mongo_setup import Mongo_CONN

from classrooms import mongo


DB_NAME = 'Users'


def create_user_mongo(uid: str):

    try:
        Mongo_CONN[DB_NAME][uid].insert_one(
            {
                'user_id': uid,
                'enrolledIn': []
            }
        )
        return True
    except Exception as e:
        raise e


def course_enroll(user_uid: str, course_uid: str):
    try:
        '''
            Updating user enrolled array in mongo
        '''
        Mongo_CONN[DB_NAME][user_uid].update_one(
            {'user_id': user_uid},
            {'$push': {'enrolledIn': course_uid}
             }
        )
        '''
            Updating classroom enrolled array in mongo
        '''
        mongo.enroll_classroom(user_uid=user_uid, course_uid=course_uid)
        return True
    except Exception as e:
        raise e
