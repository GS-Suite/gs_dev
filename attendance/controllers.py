from classrooms import models as classroom_models
from attendance import mongo as attendance_mongo
from attendance import redis as attendance_redis


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


async def view_classroom_attendance(classroom_uid):
    ### calculate classroom attendance mongo
    res = await attendance_mongo.view_classroom_attendance(classroom_uid)
    return res


async def delete_classroom_attendance(classroom_uid):
    delete_resp = await attendance_mongo.delete_classroom_attendance(classroom_uid)
    return delete_resp