from db_setup.mongo_setup import FORUM_MONGO_CONN


def create_announcement_pane(classroom_uid):
    try:
        resp = FORUM_MONGO_CONN[classroom_uid + '-F']['announcements']
        resp.insert_one({"first": "first announcement"})
        resp.delete_many({})
        return True
    
    except Exception as e:
        print(e)
        return False