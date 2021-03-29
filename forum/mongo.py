from db_setup.mongo_setup import FORUM_MONGO_CONN


def check_if_forum_exists(classroom_uid):
    try:
        list_of_forums = FORUM_MONGO_CONN.list_database_names()
        if classroom_uid+'-F' in list_of_forums:
            return {'forum_exists': True, 'status': 'Successful'}
        else:
            return {'forum_exists': False, 'status': 'Successful'}
    except Exception as e:
        print(e)
        ''' When mongo fails '''
        return {'forum_exists': False, 'status': 'Failed'}


def create_forum(classroom_uid):
    try:
        resp = FORUM_MONGO_CONN[classroom_uid + '-F']['main']
        resp.insert_one({"first": "firstmessage"})
        resp.delete_many({})
        return True
    
    except Exception as e:
        print(e)
        return False


def post_message_to_forum(classroom_id, message_id, reply_user_id, reply_username, reply_msg_id, datetimestamp, user_id, username, message):
    forum_id = classroom_id + '-F'
    try:
        resp = FORUM_MONGO_CONN[forum_id]['main']
        resp.insert_one(
                {
                    "message_id": message_id,
                    "reply_user_id": reply_user_id,
                    "reply_username": reply_username,
                    "reply_msg_id": reply_msg_id,
                    "datetimestamp": datetimestamp,
                    "user_id": user_id,
                    "username": username,
                    "message": message
                }
            )
        return True
    except Exception as e:
        print(e)
        return False


def get_all_messages(classroom_uid):
    forum_id = classroom_id + '-F'
    msgs = []
    
    try:
        resp = FORUM_MONGO_CONN[forum_id]['main'].find()
        
        if len([i for i in resp]) >= 1:

            for i in resp:
                i.pop('_id')
                i['date'] = i['datetimestamp'].strftime('%d-%m-%Y')
                i['time'] = i['datetimestamp'].strftime('%H:%M:%S')
                i.pop('datetimestamp')
                msgs.append(i)
        
            return msgs
        else:
            return []
    
    except Exception as e:
        print(e)
        return False