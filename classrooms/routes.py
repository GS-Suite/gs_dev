from re import T
from responses.standard_response_body import StandardResponseBody
from starlette.status import HTTP_200_OK
from classrooms import controllers as classroom_controllers
from tokens import controllers as token_controllers
from fastapi import status


async def create_classroom(classroom, token):
    tkn = await token_controllers.validate_token(token)
    if tkn:

        tkn = await token_controllers.get_token_by_value(tkn)
        if tkn:       
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
    else:
        return StandardResponseBody(
            False, "Non-existent user"
        )


async def get_user_classrooms(token):
    tkn = await token_controllers.validate_token(token)

    if tkn:
        tkn = await token_controllers.get_token_by_value(tkn)

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
    else:
        return {"success": False, "message": "Non-existent user"}


async def get_user_enrolled(token):
    tkn = await token_controllers.validate_token(token)

    if tkn:
        tkn = await token_controllers.get_token_by_value(tkn)

        res = await classroom_controllers.get_user_enrolled(tkn.user_id)
        print(res)
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
    return StandardResponseBody(
        False, "Non-existent user"
    )


async def get_classroom_details(uid, token):
    tkn = await token_controllers.validate_token(token)

    if tkn:
        tkn = await token_controllers.get_token_by_value(tkn)
        
        #print(tkn)
        res = await classroom_controllers.get_classroom_details(tkn.user_id, uid)
        print(res)
        if res:
            return StandardResponseBody(
                True, "Classroom details retrieved", tkn.token_value, res
            )
        else:
            return StandardResponseBody(
                False, "Could not retrieve data", tkn.token_value
            )
    else:
        return StandardResponseBody(
            False, "Non-existent user"
        )


async def generate_classroom_entry_code(uid, token):
    val_token = await token_controllers.validate_token(token)

    if val_token:
        tkn = await token_controllers.get_token_by_value(token)

        res = await classroom_controllers.generate_classroom_entry_code(tkn.user_id, uid)
        if res:
            return StandardResponseBody(
                True, "Entry code generated", tkn.token_value, res
            )
        return StandardResponseBody(
            False, "Sorry! Couldn't generate entry code", tkn.token_value
        )
    else:
        return StandardResponseBody (
            False, "Your account is invalid"
        )


async def course_enroll(token, classroom_uid, entry_code):
    val_token = await token_controllers.validate_token(token)

    if val_token:
        tkn = await token_controllers.get_token_by_value(token)

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
    else:
        return StandardResponseBody (
            False, "Your account is invalid"
        )