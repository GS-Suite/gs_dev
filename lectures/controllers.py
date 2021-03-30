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


async def edit_lecture(classroom_uid, lecture_uid, lecture):
    res = await lectures_mongo.edit_lecture(classroom_uid, lecture_uid, lecture)
    return res


async def delete_lecture(classroom_uid, lecture_uid):
    res = await lectures_mongo.delete_lecture(classroom_uid, lecture_uid)
    return res

