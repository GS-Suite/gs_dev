from responses.standard_response_body import StandardResponseBody
from starlette.status import HTTP_200_OK

from tokens import controllers as token_controllers
from forum import controllers as forum_controllers
from forum import mongo as forum_mongo
from attendance import controllers as attendance_controllers

from fastapi import status
import datetime
from user import controllers as user_controllers
from forum import helpers as forum_helpers




async def create_forum(classroom_uid, token):
    '''
        1. Validate token
        2. Check if user_id is classroom owner
        3. Check if forum already exits, if true, return forum id, name, 'Already created for your classroom'
            message
        4. Create forum if does not exist, return forum id, name, 'Forum created' message
    '''
    tkn = await token_controllers.validate_token(token)

    if tkn:

        if_user_creator = await attendance_controllers.check_user_if_creator(classroom_id=classroom_uid, user_id=tkn.user_id)

        if if_user_creator == True:
            if_forum_exists = forum_mongo.check_if_forum_exists(classroom_uid)
    
            if if_forum_exists['forum_exists'] == True:
                return StandardResponseBody(
                    False, 'Forum already exists', tkn.token_value
                )
            else:
                forum_creation_status = forum_controllers.create_forum(classroom_uid)
                if forum_creation_status == True:
                    return StandardResponseBody(
                        True, 'Forum has been created', tkn.token_value
                    )
                else:
                    return StandardResponseBody(
                        True, 'Forum could not be created', tkn.token_value
                    )
        else:
            return StandardResponseBody(
            False, 'You are not the creator of the classroom', tkn.token_value
        )
    else:
        return StandardResponseBody(
            False, 'Invalid user'
        )


async def send_message(classroom_uid, message, token):
    tkn = await token_controllers.validate_token(token)

    if tkn:
        user_enrolled_status = attendance_controllers.if_user_enrolled(classroom_uid=classroom_uid, user_id=tkn.user_id)
        if_user_is_creator = await attendance_controllers.check_user_if_creator(classroom_id=classroom_uid, user_id=tkn.user_id)
        
        if user_enrolled_status == True or if_user_is_creator ==  True:

            '''Check if forum exists'''
            if_forum_exists = forum_mongo.check_if_forum_exists(classroom_uid=classroom_uid)
    
            if if_forum_exists['forum_exists'] == True:

                ''' to get username '''
                user_info = await user_controllers.get_user_dashboard(uid=tkn.user_id)


                message_id = forum_helpers.generate_message_code()

                send_message_status = forum_controllers.send_message(
                    classroom_id=classroom_uid,
                    message_id = message_id,
                    date = datetime.datetime.now().strftime("%d-%m-%Y"),
                    time = datetime.datetime.now().strftime("%H:%M:%S"),
                    user_id = tkn.user_id,
                    username = user_info["username"],
                    message = message
                )

                if send_message_status ==  True:
                    return StandardResponseBody(
                        True, 'Message has been posted to forum', tkn.token_value, {'message_id': message_id}
                    )
                else:
                  return StandardResponseBody(
                        False, 'Message could not be posted to forum', tkn.token_value
                    )
            else:
                return StandardResponseBody(
                    False, 'Forum has not been created', tkn.token_value
                )  
        else:
            return StandardResponseBody(
                False, 'You cannot send messsages to this forum', tkn.token_value
            )
            
    else:
        return StandardResponseBody(
            False, 'Invalid User'
        )