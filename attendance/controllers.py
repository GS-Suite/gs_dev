from classrooms import models as classroom_models
from attendance import mongo as attendance_mongo


async def check_user_if_creator(classroom_id, user_id):
    classroom_obj = await classroom_models.get_classroom_by_uid(classroom_id)
    if user_id == classroom_obj.creator_uid:
        return True
    else:
        return False


def add_attendance_token_mongo(classroom_uid: str, attendance_token: str):
    attendance_mongo_resp = attendance_mongo.attendance_token_mongo(
        classroom_uid=classroom_uid, attendance_token=attendance_token)
    return attendance_mongo_resp

def delete_attendance_token_from_mongo(classroom_uid: str):
    delete_token_rep = attendance_mongo.delete_attendance_token_mongo(classroom_uid=classroom_uid)
    return delete_token_rep


def if_user_enrolled(classroom_uid, user_id):
    classroom_enrolled_resp = attendance_mongo.check_enrolled_in_classroom(classroom_uid, user_id)
    user_enrolled_resp = attendance_mongo.check_enrolled_in_user_enrolled(classroom_uid, user_id)

    print('classroom_enrolled_resp: ', classroom_enrolled_resp)
    print('user_enrolled_resp: ', user_enrolled_resp)

    if classroom_enrolled_resp ==  True and user_enrolled_resp == True:
        return True
    
    return False

def log_attendance(classroom_uid, user_id, attendance_token):
    logged_attendance_resp = attendance_mongo.give_attendance(classroom_uid, user_id, attendance_token)

    if logged_attendance_resp ==  True:
        return True
    return False

