from db_setup.mongo_setup import Mongo_CONN


DB_ENROLLED = 'Enrolled'
DB_ATTENDANCE = 'Attendance'
DB_USERS = "Users"

'''
def create_mongo_classroom(classroom_uid: str):
    try:
        Mongo_CONN[DB_ATTENDANCE][classroom_uid].insert_one(
            {'enrolled': []}
        )
        return True
    except Exception as e:
        print(e)
        return False
'''

async def get_classroom_enrolled(classroom_uid):
    x = Mongo_CONN[DB_ENROLLED][classroom_uid].find()
    y = [{"uid": i["uid"], "username": i["username"]} for i in x]
    if y != []:
        return y
    return []

'''
async def get_classroom_details(classroom_uid):
    return [i for i in Mongo_CONN[][classroom_uid].find()]
'''


async def check_enrolled_in_classroom(classroom_uid, user_id):
    try:
        x = Mongo_CONN[DB_ENROLLED][classroom_uid].find_one(
            {"uid": user_id}
        )
        if x:
            return True
        return False
    except Exception as e:
        print(e)
        return False


async def check_enrolled_in_user_enrolled(classroom_uid, user_id):
    try:
        x = Mongo_CONN['Users'][user_id].find_one()

        if classroom_uid in x['enrolled']:
            return True
    except Exception as e:
        print(e)
        return False


async def get_user_enrolled(user_uid):
    x = Mongo_CONN[DB_USERS][user_uid].find({})
    return x[0]["enrolled"]


async def enroll_user(user_uid, classroom_uid):
    try:
        Mongo_CONN[DB_USERS][user_uid].update(
            {'user_id': user_uid},
                {'$push': {
                    'enrolled': classroom_uid
                }
            }
        )
        return True
    except Exception as e:
        print(e)
        return False


async def enroll_classroom(user_uid, username, classroom_uid):
    try:
        Mongo_CONN[DB_ENROLLED][classroom_uid].insert_one(
            {
                'uid': user_uid,
                "username": username
            }
        )
        return True
    except Exception as e:
        print(e)
        return False

'''
def classroom_add_entry_code(classroom_uid: str, code: str):
    try:
        Mongo_CONN[DB_NAME][classroom_uid].update(
            {"join_code": {"$exists": True}},
            {
                '$set': {
                    "join_code": code
                }
            }
        )
        return True
    except Exception as e:
        print(e)
        return False'''

