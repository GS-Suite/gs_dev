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