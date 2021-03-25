from responses.standard_response_body import StandardResponseBody
from starlette.status import HTTP_200_OK

from tokens import controllers as token_controllers
from attendance import controllers as attendance_controllers
from attendance import helpers as attendance_helpers
from fastapi import status


async def take_attendance(token, classroom_uid, timeout):
    tkn = await token_controllers.validate_token(token)
    if tkn:
        if_creator_bool = await attendance_controllers.check_user_if_creator(
            classroom_id = classroom_uid,
            user_id=tkn.user_id
        )

        if if_creator_bool == True:
            '''
                1. Generate unique attendance code
                2. Add code to Mongo
                3. Send code in response
            '''
            attendance_token = attendance_helpers.generate_attendance_code()

            ### add token to redis
            response = attendance_controllers.add_attendance_token_redis(
                classroom_uid = classroom_uid, 
                token = attendance_token,
                timeout = timeout
            )
            
            ### add object to mongo
            if response:
                response = attendance_controllers.add_attendance_mongo(
                    classroom_uid = classroom_uid,
                    token = attendance_token
                )

            
            if response == True:
                return StandardResponseBody(
                    True, 'Attendance code generated', tkn.token_value, {'attendance_token': attendance_token}
                )
            elif response == "exists":
                return StandardResponseBody(
                    False, 'Exists', tkn.token_value, {'attendance_token': attendance_token}
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


async def stop_attendance(token, attendance_token, classroom_uid):
    tkn = await token_controllers.validate_token(token)

    if tkn:
        creator_bool = await attendance_controllers.check_user_if_creator(
            classroom_id=classroom_uid,
            user_id=tkn.user_id
        )

        if creator_bool:
                '''
                    1. Delete attendance token document from Mongo
                    2. Send response
                '''

                response = attendance_controllers.delete_attendance_token_redis(
                    token = attendance_token
                )

                if response ==  True:
                    return StandardResponseBody(
                        True, 'Attendance has been stopped', tkn.token_value
                    )
                else:
                    return StandardResponseBody(
                        False, 'Could not stop attendance', tkn.token_value
                    )
        else:
            return StandardResponseBody(
                False, 'You are not the owner of the classroom', tkn.token_value
            )
    else:
        return StandardResponseBody(
            False, 'Invalid user'
        )


async def delete_attendance(token, attendance_token, classroom_uid):
    tkn = await token_controllers.validate_token(token)

    if tkn:
        if_creator_bool = await attendance_controllers.check_user_if_creator(classroom_id=classroom_uid,
                                                                             user_id=tkn.user_id)

        if if_creator_bool == True:
                '''
                    1. Delete attendance token document from Mongo
                    2. Send response
                '''

                response = attendance_controllers.delete_attendance_token_redis(
                    token = attendance_token
                )

                if response:
                    response = attendance_controllers.delete_attendance_mongo(
                        classroom_uid, attendance_token
                    )

                if response ==  True:
                    return StandardResponseBody(
                        True, 'Attendance has been deleted', tkn.token_value
                    )
                else:
                    return StandardResponseBody(
                        False, 'Could not delete attendance', tkn.token_value
                    )
        else:
            return StandardResponseBody(
                False, 'You are not the owner of the classroom', tkn.token_value
            )
    else:
        return StandardResponseBody(
            False, 'Invalid user'
        )


async def give_attendance(token, classroom_uid, attendance_token):
    tkn = await token_controllers.validate_token(token)

    if tkn:
        if_user_enrolled = attendance_controllers.if_user_enrolled(classroom_uid=classroom_uid.classroom_uid, user_id=tkn.user_id)

        if if_user_enrolled:

            response = attendance_controllers.log_attendance(
                classroom_uid = classroom_uid.classroom_uid, 
                user_id = tkn.user_id,
                attendance_token = attendance_token)
            
            if response == True:
                return StandardResponseBody(
                    True, 'Your attendance has been logged!', tkn.token_value
                )
            else:
                return StandardResponseBody(
                    False, 'Your attendance could not be logged.', tkn.token_value
                )
        else:
            return StandardResponseBody(
                    False, 'You have not enrolled in this classroom', tkn.token_value
                )
    else:
        return StandardResponseBody(
            False, 'Chal bhak hacker!'
        )
