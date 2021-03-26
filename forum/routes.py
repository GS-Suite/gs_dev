from responses.standard_response_body import StandardResponseBody

from attendance import controllers as attendance_controllers
from forum import controllers as forum_controllers
from forum import mongo as forum_mongo


async def create_forum(classroom_uid, token):
    '''
        1. Validate token
        2. Check if user_id is classroom owner
        3. Check if forum already exits, if true, return forum id, name, 'Already created for your classroom'
            message
        4. Create forum if does not exist, return forum id, name, 'Forum created' message
    '''
    if_user_creator = await attendance_controllers.check_user_if_creator(classroom_id=classroom_uid, user_id=token.user_id)

    if if_user_creator == True:
        if_forum_exists = forum_mongo.check_if_forum_exists(classroom_uid)

        if if_forum_exists['forum_exists'] == True:
            return StandardResponseBody(
                False, 'Forum already exists', token.token_value
            )
        else:
            forum_creation_status = forum_controllers.create_forum(classroom_uid)
            if forum_creation_status == True:
                return StandardResponseBody(
                    True, 'Forum has been created', token.token_value
                )
            else:
                return StandardResponseBody(
                    True, 'Forum could not be created', token.token_value
                )
    else:
        return StandardResponseBody(
        False, 'You are not the creator of the classroom', token.token_value
    )


async def send_message(classroom_uid, message, token):
    pass
