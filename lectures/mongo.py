from db_setup.mongo_setup import Mongo_CONN
from bson.objectid import ObjectId
from pymongo import DESCENDING, ASCENDING
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
        lecture
    )
    if res.acknowledged:
        return True
    else:
        return False


async def get_classroom_lecture_videos(classroom_uid):
    res = Mongo_CONN[DB_LECTURES][classroom_uid].find().sort(
        'date', ASCENDING
    )
    x = json.loads(json_util.dumps(res))
    return x


async def get_classroom_lecture_playlists(classroom_uid):
    playlists = set()
    res = Mongo_CONN[DB_LECTURES][classroom_uid].find()
    x = json.loads(json_util.dumps(res))
    for lec in x:
        for p in lec["playlists"]:
            playlists.add(p)
    return playlists


async def get_classroom_playlist_videos(classroom_uid, playlist_name):
    res = Mongo_CONN[DB_LECTURES][classroom_uid].find(
        {"playlists": {"$in":[playlist_name]}}
    ).sort("date_created", DESCENDING)
    x = json.loads(json_util.dumps(res))
    return x


async def edit_lecture(classroom_uid, lecture_uid, lecture):
    print(lecture.__dict__)
    res = Mongo_CONN[DB_LECTURES][classroom_uid].update_one(
        {"_id": ObjectId(lecture_uid)}, {"$set": lecture.__dict__}
    )
    if res.acknowledged:
        return True
    else:
        return False


async def delete_lecture(classroom_uid, lecture_uid):
    res = Mongo_CONN[DB_LECTURES][classroom_uid].delete_one(
        {"_id": ObjectId(lecture_uid)}
    )
    print(res.acknowledged)
    return res.acknowledged