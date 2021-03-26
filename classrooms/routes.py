from responses.invalid_token_response_body import InvalidTokenResponseBody
from responses.standard_response_body import StandardResponseBody
from classrooms import controllers as classroom_controllers


async def create_classroom(classroom, tkn):
    res, cls = await classroom_controllers.create_class(tkn, classroom.class_name)
    if res == True:
        return StandardResponseBody(
            True, "Classroom created", tkn.token_value, cls
        )
    elif res == "exists":
        return StandardResponseBody(
            False, "Classroom already exists", tkn.token_value, cls
        )
    return StandardResponseBody(
        False, "Classroom not created"
    )



async def get_user_classrooms(tkn):
    res = await classroom_controllers.get_user_classrooms(tkn.user_id)
    if res == []:
        return StandardResponseBody(
            False, "You haven't created any classrooms", tkn.token_value
        )
    elif res:
        return StandardResponseBody(
            True, "User classrooms", tkn.token_value, res
        )
    else:
        return StandardResponseBody(
            False, "Could not retrieve data", tkn.token_value
        )


async def get_user_enrolled(token):
    res = await classroom_controllers.get_user_enrolled(tkn.user_id)
    #print(res)
    if res == []:
        return StandardResponseBody(
            True, "You aren't enrolled in any classroom", tkn.token_value
        )
    elif res:
        return StandardResponseBody(
            True, "User Enrolled in", tkn.token_value, res
        )
    else:
        return StandardResponseBody(
            False, "Could not retrieve data"
        )


async def get_classroom_enrolled(classroom_uid, token):
    res = await classroom_controllers.get_classroom_enrolled(classroom_uid)
    #print(res)
    if res:
        return StandardResponseBody(
            True, "Enrolled students", tkn.token_value, {"enrolled" : res}
        )
    else:
        return StandardResponseBody(
            False, "Could not retrieve data"
        )


async def get_classroom_details(uid, tkn):
    res = await classroom_controllers.get_classroom_details(tkn.user_id, uid)
    #print(res)
    if res:
        return StandardResponseBody(
            True, "Classroom details retrieved", tkn.token_value, res
        )
    else:
        return StandardResponseBody(
            False, "Could not retrieve data", tkn.token_value
        )



async def generate_classroom_entry_code(uid, token):
    res = await classroom_controllers.generate_classroom_entry_code(tkn.user_id, uid)
    if res:
        return StandardResponseBody(
            True, "Entry code generated", tkn.token_value, res
        )
    return StandardResponseBody(
        False, "Sorry! Couldn't generate entry code", tkn.token_value
    )



async def course_enroll(token, classroom_uid, entry_code):
    res = await classroom_controllers.enroll_user(tkn.user_id, classroom_uid, entry_code)
    if res == True:
        return StandardResponseBody(
            True, "You have been enrolled successfully", tkn.token_value
        )
    elif res == "exists":
        return StandardResponseBody(
            False, "User already enrolled", tkn.token_value
        )
    elif res == "code_error":
        return StandardResponseBody(
            False, "Invalid entry code", tkn.token_value
        )
    return StandardResponseBody(
        False, "Sorry! Couldn't enroll", tkn.token_value
    )


async def get_classroom_uid_by_entry_code(entry_code, token):
    res = await classroom_controllers.getClassroomUid(entry_code)

    if res['status'] == True:
        return StandardResponseBody(
            True, "Classroom ID aquired", tkn.token_value, {"classroom_uid": res['classroom_uid'], "classroom_name": res['classroom_name']}
        )
    else:
        return StandardResponseBody(
            False, "Could not get classroom ID", tkn.token_value
        )
