from db_setup.mongo_setup import Mongo_CONN
from bson import ObjectId
import datetime


DB_NAME = 'Classrooms'


def attendance_token_mongo(classroom_uid: str, attendance_token: str):
    try:
        mongo_resp = Mongo_CONN[DB_NAME][classroom_uid].find(
                {
                'attendance_token': {'$exists': True}
                }
        )
        mongo_obj_list = [i for i in mongo_resp]

        if len(mongo_obj_list) >= 1:
            return [True, mongo_obj_list[0]['attendance_token']]
        else:
            # Creating current datetime dict inside mongo.classroom.attenance dictionary
            Mongo_CONN[DB_NAME][classroom_uid].update(
                {'classroom_uid': classroom_uid},
                {
                    '$set': {
                        'attendance': {
                        str(datetime.datetime.today()): {}
                        }
                    }
                }
            )
            # Inserting attendance_token in mongo
            Mongo_CONN[DB_NAME][classroom_uid].insert_one(
                {
                    'attendance_token': attendance_token,
                    'created_time': datetime.datetime.now()
                }
            )
            return True
    except Exception as e:
        print(e)
        return False

def delete_attendance_token_mongo(classroom_uid: str):
    try:
        mongo_resp = Mongo_CONN[DB_NAME][classroom_uid].find(
                {
                'attendance_token': {'$exists': True}
                }
            )
        mongo_obj_list = [i for i in mongo_resp]
        for i in range(len(mongo_obj_list)):
            Mongo_CONN[DB_NAME][classroom_uid].delete_one(
                {
                    '_id': ObjectId(mongo_obj_list[i]['_id'])}
                )
        return True
    except Exception as e:
        # print(e)
        return False


def check_enrolled_in_classroom(classroom_uid, user_id):
    try:
        x = Mongo_CONN[DB_NAME][classroom_uid].find_one()
        if user_id in x['enrolled']:
            return True
    except Exception as e:
        print(e)
        return False

def check_enrolled_in_user_enrolled(classroom_uid, user_id):
    try:
        x = Mongo_CONN['Users'][user_id].find_one()

        if classroom_uid in x['enrolled']:
            return True
    except Exception as e:
        print(e)
        return False

def give_attendance(classroom_uid, user_id, attendance_token):

    try:
        get_attendance_token_from_mongo = Mongo_CONN[DB_NAME][classroom_uid].find_one({'attendance_token': {'$exists': True}})
        print(get_attendance_token_from_mongo['attendance_token'])

        if attendance_token == get_attendance_token_from_mongo['attendance_token']:
            print(attendance_token, user_id)
            x = Mongo_CONN[DB_NAME][classroom_uid].update_one(
                {'attendance': {'$exists': True}},
                { 
                    '$set': {
                        'attendance': {   
                        str(datetime.datetime.today()): {
                            '$set': {
                                str(user_id): str(datetime.datetime.today())
                            }}
                        }
                        
                    }
                }
            )
        
        return True
    except Exception as e:
        print(e)
        return False