from mongo_setup import Mongo_CONN
from datetime import datetime


def create_monogo_class(classroom_id):
    db = Mongo_CONN[classroom_id]
    try:
        for collection in ['Enrolled', 'Attendance']:
            col = db[collection]
            dummy = {'datetime': datetime.now()}
            col.insert_one(dummy)
            col.delete_many({})
        return True
    except Exception as e:
        return False
