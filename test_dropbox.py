# import dropbox


# access_token = ""
# dbx = dropbox.Dropbox(access_token)
'''x = dbx.users_get_current_account()
print(x)'''

'''for entry in dbx.files_list_folder('').entries:
    print(entry)'''


# db_path = "/upload test/test.jpg"
# file_path = "C:/Users/keane/Desktop/test.jpg"
# download_path = "C:/Users/keane/Desktop/download_test.jpg"

# dbx.files_upload(
#     open(file_path, "rb").read(), 
#     db_path
# )

# with open(download_path, "wb") as f:
#     metadata, res = dbx.files_download(path = db_path)
#     f.write(res.content)



# from db_setup.mongo_setup import Mongo_CONN
# from bson import ObjectId
# import datetime

# from typing import NamedTuple

# DB_NAME = 'Classrooms'

# classroom_uid = '334de992305740f7ad29a9bf9bc493cf'



# x = Mongo_CONN[DB_NAME][classroom_uid].update_one(
#         {'classroom_uid': classroom_uid},
#         {
#             '$set': {
#                 'attendance': {
#                 str(datetime.datetime.today()): {
#                         '491e0381-aecf-4ab2-b8d4-229f56c0bdb6': str(datetime.datetime.today())
#                     }
#                 }
#             }
#         }
#     )

# y = Mongo_CONN.list_database_names()
# print(y)


import pymongo

forum = pymongo.MongoClient("mongodb+srv://gs_suite:Keanebish123@forumcluster.1ossz.mongodb.net/")
c = forum['yoyo_db']['some_coll']
c.insert_one({"dummy": "dummy"})
print(c.find())
# forum["yoyo_db"]['some_coll'].delete_many({})






