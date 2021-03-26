from forum import mongo as forum_mongo


def create_forum(classroom_uid):
    '''Returns Bool'''
    return forum_mongo.create_forum(classroom_uid)


def send_message(classroom_id, message_id, reply_user_id, reply_username, reply_msg_id, datetimestamp, user_id, username, message):
    '''Returns Bool'''
    return forum_mongo.post_message_to_forum(classroom_id, message_id, reply_user_id, reply_username, reply_msg_id, datetimestamp, user_id, username, message)

