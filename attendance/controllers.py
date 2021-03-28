from classrooms import models as classroom_models
from attendance import mongo as attendance_mongo
from attendance import redis as attendance_redis


async def check_user_if_creator(classroom_id, user_id):
    classroom_obj = await classroom_models.get_classroom_by_uid(classroom_id)
    if user_id == classroom_obj.creator_uid:
        return True
    return False


async def add_attendance_token_redis(classroom_uid, token, timeout):
    resp = await attendance_redis.set_token(
        token, classroom_uid, timeout
    )
    return resp


async def add_attendance_mongo(classroom_uid, token):
    resp = await attendance_mongo.add_attendance_mongo(
        classroom_uid, token
    )
    return resp


async def delete_attendance_token_redis(token):
    delete_token_rep = await attendance_redis.delete_token(token)
    return delete_token_rep


async def delete_attendance_mongo(classroom_uid, token):
    delete_resp = await attendance_mongo.delete_attendance_mongo(
        classroom_uid, token
    )
    return delete_resp


async def if_user_enrolled(classroom_uid, user_id):
    classroom_enrolled_resp = await attendance_mongo.check_enrolled_in_classroom(classroom_uid, user_id)
    user_enrolled_resp = await attendance_mongo.check_enrolled_in_user_enrolled(classroom_uid, user_id)

    # print('classroom_enrolled_resp: ', classroom_enrolled_resp)
    # print('user_enrolled_resp: ', user_enrolled_resp)

    if classroom_enrolled_resp ==  True and user_enrolled_resp == True:
        return True
    
    return False


async def log_attendance(classroom_uid, user_id, attendance_token):
    ### check if token in redis
    valid = await attendance_redis.get_token(attendance_token)
    print(valid)

    if valid:
        logged_attendance_resp = await attendance_mongo.give_attendance(classroom_uid, user_id, attendance_token)

        if logged_attendance_resp ==  True:
            return True
    return False


async def view_student_attendance(classroom_uid, user_uid):
    ### calculate student attendance mongo
    res = await attendance_mongo.view_student_attendance(classroom_uid, user_uid)
    return res