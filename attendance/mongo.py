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
                    "students": {},
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


async def give_attendance(classroom_uid, username, attendance_token):
    try:

        x = Mongo_CONN[DB_NAME][classroom_uid].update(
                {'token': attendance_token},
                { 
                    '$set': {
                        f'students.{username}': datetime.datetime.now()
                    }
                }
            )
        return True
    except Exception as e:
        print(e)
        return False


async def view_student_attendance(classroom_uid, username):
    #print(classroom_uid, user_uid)
    results = {
        "attended_count": 0,
        "total_count": 0,
        "details": {}
    }
    x = Mongo_CONN[DB_NAME][classroom_uid].find()
    for i in x:
        if username in i["students"]:
            results["details"][i["created_timestamp"]] = True
            results["attended_count"] += 1
        else:
            results["details"][i["created_timestamp"]] = False
        results["total_count"] += 1
    return results


async def view_classroom_attendance(classroom_uid):
    total_count = Mongo_CONN[DB_ENROLLED][classroom_uid].count()
    
    x = Mongo_CONN[DB_NAME][classroom_uid].find()

    results = {}
    for i in x:
        #print(i)
        results[i["created_timestamp"]] = {
            "attended_count": len(i["students"]),
            "total_count": total_count,
            "students": i["students"],
            "token": i["token"]
        }

    return results


async def delete_classroom_attendance(classroom_uid: str):
    try:
        mongo_resp = Mongo_CONN[DB_NAME]
        if mongo_resp:
            mongo_resp.drop_collection(classroom_uid)
        return True
    except Exception as e:
        # print(e)
        return False