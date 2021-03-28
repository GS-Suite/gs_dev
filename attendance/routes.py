from responses.standard_response_body import StandardResponseBody

from attendance import controllers as attendance_controllers
from attendance import helpers as attendance_helpers


async def take_attendance(token, classroom_uid, timeout):
    if_creator_bool = await attendance_controllers.check_user_if_creator(
        classroom_id = classroom_uid,
        user_id=token.user_id
    )

    if if_creator_bool == True:
        '''
            1. Generate unique attendance code
            2. Add code to Mongo
            3. Send code in response
        '''
        attendance_token = await attendance_helpers.generate_attendance_code()

        ### add token to redis
        response = await attendance_controllers.add_attendance_token_redis(
            classroom_uid = classroom_uid, 
            token = attendance_token,
            timeout = timeout
        )
        
        ### add object to mongo
        if response:
            response = await attendance_controllers.add_attendance_mongo(
                classroom_uid = classroom_uid,
                token = attendance_token
            )

        
        if response == True:
            return StandardResponseBody(
                True, 'Attendance code generated', token.token_value, {'attendance_token': attendance_token}
            )
        elif response == "exists":
            return StandardResponseBody(
                False, 'Exists', token.token_value, {'attendance_token': attendance_token}
            )
        else:
            return StandardResponseBody(
                False, 'Could not generate attendance token for classroom', token.token_value
            )
    else:
        return StandardResponseBody(
            False, 'You are not the owner of the classroom', token.token_value
        )


async def stop_attendance(token, attendance_token, classroom_uid):
    creator_bool = await attendance_controllers.check_user_if_creator(
        classroom_id=classroom_uid,
        user_id=token.user_id
    )

    if creator_bool:
        '''
            1. Delete attendance token document from Mongo
            2. Send response
        '''
        response = await attendance_controllers.delete_attendance_token_redis(
            token = attendance_token
        )

        if response ==  True:
            return StandardResponseBody(
                True, 'Attendance has been stopped', token.token_value
            )
        else:
            return StandardResponseBody(
                False, 'Could not stop attendance', token.token_value
            )
    else:
        return StandardResponseBody(
            False, 'You are not the owner of the classroom', token.token_value
        )


async def delete_attendance(token, attendance_token, classroom_uid):
    if_creator_bool = await attendance_controllers.check_user_if_creator(classroom_id=classroom_uid,
                                                                            user_id=token.user_id)

    if if_creator_bool == True:
            '''
                1. Delete attendance token document from Mongo
                2. Send response
            '''

            response = await attendance_controllers.delete_attendance_token_redis(
                token = attendance_token
            )

            if response:
                response = await attendance_controllers.delete_attendance_mongo(
                    classroom_uid, attendance_token
                )

            if response ==  True:
                return StandardResponseBody(
                    True, 'Attendance has been deleted', token.token_value
                )
            else:
                return StandardResponseBody(
                    False, 'Could not delete attendance', token.token_value
                )
    else:
        return StandardResponseBody(
            False, 'You are not the owner of the classroom', token.token_value
        )


async def give_attendance(token, classroom_uid, attendance_token):
    if_user_enrolled = await attendance_controllers.if_user_enrolled(classroom_uid=classroom_uid.classroom_uid, user_id=token.user_id)

    if if_user_enrolled:

        response = await attendance_controllers.log_attendance(
            classroom_uid = classroom_uid.classroom_uid, 
            user_id = token.user_id,
            attendance_token = attendance_token)
        
        if response == True:
            return StandardResponseBody(
                True, 'Your attendance has been logged!', token.token_value
            )
        else:
            return StandardResponseBody(
                False, 'Your attendance could not be logged.', token.token_value
            )
    else:
        return StandardResponseBody(
                False, 'You have not enrolled in this classroom', token.token_value
            )

async def view_student_attendance(token, classroom_uid):
    if_user_enrolled = await attendance_controllers.if_user_enrolled(classroom_uid=classroom_uid.classroom_uid, user_id=token.user_id)

    if if_user_enrolled:

        response = await attendance_controllers.view_student_attendance(
            classroom_uid = classroom_uid.classroom_uid,
            user_uid = token.user_id
        )
        
        if response:
            return StandardResponseBody(
                True, 'Your attendance', token.token_value, response
            )
        else:
            return StandardResponseBody(
                False, 'Your attendance could not be retrieved.', token.token_value
            )
    else:
        return StandardResponseBody(
                False, 'You have not enrolled in this classroom', token.token_value
            )

