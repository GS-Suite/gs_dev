from mongo_setup import Mongo_CONN
from datetime import datetime


DB_NAME = 'Classrooms'


def create_monogo_class(classroom_uid: str):
    try:
        for collection in ['Enrolled', 'Attendance']:
            if collection != 'Attendance':
                Mongo_CONN[DB_NAME][classroom_uid].insert_one(
                    {
                        'classroom_uid': classroom_uid,
                        'enrolled': []
                    }
                )
            else:
                col.insert_one({'datetime': datetime.now()})
                col.delete_many({})
        return True
    except Exception as e:
        raise e


def enroll_classroom(user_uid: str, course_uid: str):
    try:
        '''
            Updating classroom enrolled array in mongo
        '''
        Mongo_CONN[DB_NAME][course_uid].update_one(
            {'user_id': user_uid},
            {'$push': {'enrolled': user_uid}
             }
        )
        return True
    except Exception as e:
        raise e
