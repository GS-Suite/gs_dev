from db_setup.mongo_setup import Mongo_CONN
import datetime


DB_NAME = 'Classrooms'


def attendance_token_mongo(classroom_uid: str, attendance_token: str):
    try:
        Mongo_CONN[DB_NAME][classroom_uid].insert_one(
            {
                'attendance_token': attendance_token,
                'created_time': datetime.datetime.now()
            }
        )
        return True
    except Exception as e:
        print(e)
        return False
