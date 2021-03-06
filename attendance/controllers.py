from classrooms import models as classroom_models
from attendance import mongo as attendance_mongo


async def check_user_if_creator(classroom_id, user_id):
    classroom_obj = await classroom_models.get_classroom_by_uid(classroom_id)
    if user_id == classroom_obj.creator_uid:
        return True
    else:
        return False


async def add_attendance_token_mongo(classroom_uid: str, attendance_token: str):
    attendance_mongo_resp = attendance_mongo.attendance_token_mongo(
        classroom_uid=classroom_uid, attendance_token=attendance_token)
    return attendance_mongo_resp
