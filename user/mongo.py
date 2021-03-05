from db_setup.mongo_setup import Mongo_CONN


DB_NAME = 'Users'

def create_user_mongo(uid: str):

    try:
        Mongo_CONN[DB_NAME][uid].insert_one(
            {
                'user_id': uid,
                'enrolled': [],
            }
        )
        return True
    except Exception as e:
        raise e