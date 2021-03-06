from responses.standard_response_body import StandardResponseBody
from starlette.status import HTTP_200_OK
from classrooms import controllers as classroom_controllers
from tokens import controllers as token_controllers
from attendance import controllers as attendance_controllers
from fastapi import status


async def take_attendance(token, classroom_uid):
    tkn = await token_controllers.validate_token(token)

    if tkn:
        tkn = await token_controllers.get_token_by_value(tkn)
        if_creator_bool = await attendance_controllers.check_user_if_creator(user_id=tkn.user_id)

        if if_creator_bool == True:
            '''
                1. Generate unique attendance code
                2. Send code in response
            '''
        else:
            return StandardResponseBody(
            )
