from responses.invalid_token_response_body import InvalidTokenResponseBody
from responses.standard_response_body import StandardResponseBody
from classrooms import controllers as classroom_controllers


async def create_classroom(classroom, token):
    res, cls = await classroom_controllers.create_class(token, classroom.class_name)
    if res == True:
        return StandardResponseBody(
            True, "Classroom created", token.token_value, cls
        )
    elif res == "exists":
        return StandardResponseBody(
            False, "Classroom already exists", token.token_value, cls
        )
    return StandardResponseBody(
        False, "Classroom not created"
    )



async def get_user_classrooms(token):
    res = await classroom_controllers.get_user_classrooms(token.user_id)
    if res == []:
        return StandardResponseBody(
            False, "You haven't created any classrooms", token.token_value
        )
    elif res:
        return StandardResponseBody(
            True, "User classrooms", token.token_value, res
        )
    else:
        return StandardResponseBody(
            False, "Could not retrieve data", token.token_value
        )


async def get_user_enrolled(token):
    res = await classroom_controllers.get_user_enrolled(token.user_id)
    #print(res)
    if res == []:
        return StandardResponseBody(
            True, "You aren't enrolled in any classroom", token.token_value
        )
    elif res:
        return StandardResponseBody(
            True, "User Enrolled in", token.token_value, res
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
            True, "Enrolled students", token.token_value, {"enrolled" : res}
        )
    else:
        return StandardResponseBody(
            False, "Could not retrieve data"
        )


async def get_classroom_details(uid, token):
    res = await classroom_controllers.get_classroom_details(token.user_id, uid)
    #print(res)
    if res:
        return StandardResponseBody(
            True, "Classroom details retrieved", token.token_value, res
        )
    else:
        return StandardResponseBody(
            False, "Could not retrieve data", token.token_value
        )



async def generate_classroom_entry_code(uid, token):
    res = await classroom_controllers.generate_classroom_entry_code(token.user_id, uid)
    if res:
        return StandardResponseBody(
            True, "Entry code generated", token.token_value, res
        )
    return StandardResponseBody(
        False, "Sorry! Couldn't generate entry code", token.token_value
    )



async def course_enroll(token, entry_code):
    res = await classroom_controllers.enroll_user(token.user_id, token, entry_code)
    print(token.username)
    if res == True:
        return StandardResponseBody(
            True, "You have been enrolled successfully", token.token_value
        )
    elif res == "exists":
        return StandardResponseBody(
            False, "User already enrolled", token.token_value
        )
    elif res == "code_error":
        return StandardResponseBody(
            False, "Invalid entry code", token.token_value
        )
    return StandardResponseBody(
        False, "Sorry! Couldn't enroll", token.token_value
    )


async def get_classroom_uid_by_entry_code(entry_code, token):
    res = await classroom_controllers.getClassroomUid(entry_code)

    if res['status'] == True:
        return StandardResponseBody(
            True, "Classroom ID aquired", token.token_value, {"classroom_uid": res['classroom_uid'], "classroom_name": res['classroom_name']}
        )
    else:
        return StandardResponseBody(
            False, "Could not get classroom ID", token.token_value
        )


async def get_classroom_owner_from_class_uid(classroom_uid, token):
    res = await classroom_controllers.get_classroom_owner_from_class_uid(classroom_uid)

    if res['status'] == True:
        return StandardResponseBody(
            True, "Classroom owner ID aquired", token.token_value, {
                'classroom_uid': res['classroom_uid'],
                'classroom_name': res['classroom_name'],
                'classroom_owner_id': res['classroom_owner_id']
            }
        )
    else:
        return StandardResponseBody(
            False, "Could not get classroom owner ID", token.token_value
        )
