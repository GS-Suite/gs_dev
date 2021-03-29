from forum import mongo as forum_mongo
from classrooms import controllers as classroom_controllers
from user import controllers as user_controllers


def create_forum(classroom_uid):
    '''Returns Bool'''
    return forum_mongo.create_forum(classroom_uid)


def send_message(classroom_id, message_id, reply_user_id, reply_username, reply_msg_id, datetimestamp, user_id, username, message):
    '''Returns Bool'''
    return forum_mongo.post_message_to_forum(classroom_id, message_id, reply_user_id, reply_username, reply_msg_id, datetimestamp, user_id, username, message)


async def get_all_messages(classroom_uid):
    classroom = await classroom_controllers.get_classroom_owner_from_class_uid(classroom_uid=classroom_uid)
    owner_username = await user_controllers.get_user_username(uid=classroom.creator_uid)
    posts = forum_mongo.get_all_messages(classroom_uid=classroom_uid)

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
            'classroom_owner_uid': classroom.creator_uid,
            'classroom_owner_username': owner_username,
            'forum_id': classroom_uid + '-F',
            'thread': 'main',
        }
        send['posts'] = posts

        return send

    

    
