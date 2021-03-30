from lectures import mongo as lectures_mongo


async def add_classroom_to_lectures_mongo(classroom_uid):
    res = await lectures_mongo.add_classroom_to_lectures_mongo(classroom_uid)
    return res


async def get_classroom_lectures(classroom_uid):
    res = await lectures_mongo.get_classroom_lectures(classroom_uid)
    return res


async def add_lecture(classroom_uid, lecture):
    res = await lectures_mongo.add_lecture(classroom_uid, lecture)
    return res

