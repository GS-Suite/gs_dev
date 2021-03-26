from db_setup.mongo_setup import Mongo_CONN
from bson import ObjectId
import datetime


DB_NAME = 'Attendance'
DB_ENROLLED = "Enrolled"

async def add_attendance_mongo(classroom_uid: str, attendance_token: str):
    try:
        mongo_resp = Mongo_CONN[DB_NAME][classroom_uid].find_one(
                {
                'attendance_token': attendance_token
                }
        )
        if mongo_resp:
            return "exists"
        else:
            # Creating current datetime dict inside mongo.classroom.attenance dictionary
            Mongo_CONN[DB_NAME][classroom_uid].insert_one(
                {
                    "classroom_uid": classroom_uid,
                    "token": attendance_token,
                    "students": [],
                    "created_timestamp": datetime.datetime.now()
                }
            )
            return True
    except Exception as e:
        print(e)
        return False


async def delete_attendance_mongo(classroom_uid: str, token: str):
    try:
        mongo_resp = Mongo_CONN[DB_NAME][classroom_uid]
        if mongo_resp:
            mongo_resp.delete_one(
                {"token": token}
            )
        return True
    except Exception as e:
        # print(e)
        return False


async def check_enrolled_in_classroom(classroom_uid, user_id):
    try:
        x = Mongo_CONN[DB_ENROLLED][classroom_uid].find_one(
            {"uid": user_id}
        )
        if x:
            return True
        return False
    except Exception as e:
        print(e)
        return False


async def check_enrolled_in_user_enrolled(classroom_uid, user_id):
    try:
        x = Mongo_CONN['Users'][user_id].find_one()

        if classroom_uid in x['enrolled']:
            return True
    except Exception as e:
        print(e)
        return False


async def give_attendance(classroom_uid, user_id, attendance_token):
    try:

        x = Mongo_CONN[DB_NAME][classroom_uid].update_one(
                {'token': attendance_token},
                { 
                    '$push': {
                        'students': {user_id: datetime.datetime.now()}                        
                    }
                }
            )
        return True
    except Exception as e:
        print(e)
        return False
