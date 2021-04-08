from forum import mongo as forum_mongo
from classrooms import controllers as classroom_controllers
from user import controllers as user_controllers


async def create_forum(classroom_uid):
    '''Returns Bool'''
    return await forum_mongo.create_forum(classroom_uid)


async def send_message(classroom_id, message_id, reply_user_id, reply_username, reply_msg_id, datetimestamp, user_id, username, message):
    '''Returns Bool'''
    return await forum_mongo.post_message_to_forum(classroom_id, message_id, reply_user_id, reply_username, reply_msg_id, datetimestamp, user_id, username, message)


async def get_all_messages(classroom_uid):
    classroom = await classroom_controllers.get_classroom_owner_from_class_uid(classroom_uid=classroom_uid)
    owner_username = await user_controllers.get_user_username(uid=classroom['classroom_owner_id'])
    posts = await forum_mongo.get_all_messages(classroom_uid=classroom_uid)

    if posts == []:
        return {
            'status': False,
            'message': 'There are no messages'
        }
    
    elif posts == False:
        return {
            'status': False,
            'message': 'Failed to get messages'
        }
    
    else:
        send = {
            'classroom_uid': classroom_uid,
            'classroom_owner_uid': classroom['classroom_owner_id'],
            'classroom_owner_username': owner_username,
            'forum_id': classroom_uid + '-F',
            'thread': 'main',
        }
        send['posts'] = posts

        return send

    
async def delete_forum(classroom_uid):
    #return forum_mongo.delete_forum(classroom_uid)
    pass

    
