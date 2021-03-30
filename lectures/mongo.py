from db_setup.mongo_setup import Mongo_CONN
from bson import json_util
import json


DB_LECTURES = "Lectures"

async def add_classroom_to_lectures_mongo(classroom_uid):
    if classroom_uid not in Mongo_CONN[DB_LECTURES].list_collection_names():
        Mongo_CONN[DB_LECTURES].create_collection(classroom_uid)
        return True
    else:
        return False


async def add_lecture(classroom_uid, lecture):
    res = Mongo_CONN[DB_LECTURES][classroom_uid].insert_one(
        lecture.__dict__
    )
    if res.acknowledged:
        return True
    else:
        return False


async def get_classroom_lectures(classroom_uid):
    res = Mongo_CONN[DB_LECTURES][classroom_uid].find()
    x = json.loads(json_util.dumps(res))
    return x