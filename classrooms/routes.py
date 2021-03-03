from re import T
from responses.classroom_response_body import ClassroomsResponseBody
from responses.user_classrooms_response_body import UserClassroomsResponseBody
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
                return ClassroomsResponseBody(
                    True, "Classroom created", cls
                )
            elif res == "exists":
                return ClassroomsResponseBody(
                    False, "Classroom already exists", cls
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
                False, "You haven't created any classrooms"
            )
        elif res:
            return UserClassroomsResponseBody(
                True, "User classrooms", res
            )
        else:
            return StandardResponseBody(
                False, "Could not retrieve data"
            )
    else:
        return {"success": False, "message": "Non-existent user"}, status.HTTP_401_UNAUTHORIZED


async def get_user_enrolled(token):
    tkn = await token_controllers.validate_token(token)

    if tkn:
        tkn = await token_controllers.get_token_by_value(tkn)

        res = await classroom_controllers.get_user_enrolled(tkn.user_id)
        print(res)
        if res == []:
            return StandardResponseBody(
                True, "You aren't enrolled in any classroom"
            )
        elif res:
            return StandardResponseBody(
                True, "User Enrolled in", res
            )
        else:
            return StandardResponseBody(
                False, "Could not retrieve data"
            )
    return StandardResponseBody(
        False, "Non-existent user"
    )


async def get_classroom_details(classroom, token):
    tkn = await token_controllers.validate_token(token)

    if tkn:
        tkn = await token_controllers.get_token_by_value(tkn)
        
        #print(tkn)
        res = await classroom_controllers.get_classroom_details(tkn.user_id, classroom.class_name)
        print(res)
        if res:
            return StandardResponseBody(
                True, "Classroom details retrieved", res
            )
        else:
            return StandardResponseBody(
                False, "Could not retrieve data"
            )
    else:
        return StandardResponseBody(
            False, "Non-existent user"
        )


async def course_enroll(token, classroom_uid):
    val_token = await token_controllers.validate_token(token)

    if val_token:
        tkn = await token_controllers.get_token_by_value(token)

        res = await classroom_controllers.enroll_user(tkn.user_id, classroom_uid.classroom_uid)
        if res == True:
            return StandardResponseBody(
                True, "You have been enrolled successfully"
            )
        elif res == "exists":
            return StandardResponseBody(
                False, "User already enrolled"
            )
        return StandardResponseBody(
            False, "Sorry! Couldn't enroll"
        )
    else:
        return StandardResponseBody (
            False, "Your account is invalid"
        )