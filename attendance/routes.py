from responses.standard_response_body import StandardResponseBody
from starlette.status import HTTP_200_OK

from tokens import controllers as token_controllers
from attendance import controllers as attendance_controllers
from attendance import helpers as attendance_helpers
from fastapi import status


async def take_attendance(token, classroom_id):
    tkn = await token_controllers.validate_token(token)
    if tkn:
        if_creator_bool = await attendance_controllers.check_user_if_creator(classroom_id=classroom_id.classroom_uid,
                                                                             user_id=tkn.user_id)

        if if_creator_bool == True:
            '''
                1. Generate unique attendance code
                2. Add code to Mongo
                3. Send code in response
            '''
            attendance_token = attendance_helpers.generate_attendance_code()

            response = await attendance_controllers.add_attendance_token_mongo(
                classroom_uid=classroom_id.classroom_uid, attendance_token=attendance_token)

            if response:
                return StandardResponseBody(
                    True, 'Attendance code generated', tkn.token_value, attendance_token
                )
            else:
                return StandardResponseBody(
                    False, 'Could not generate attendance token for classroom', tkn.token_value
                )
        else:
            return StandardResponseBody(
                False, 'You are not the owner of the classroom', tkn.token_value
            )
    else:
        return StandardResponseBody(
            False, 'Invalid user'
        )
