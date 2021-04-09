# import requests


# import requests

# response = requests.post("https://gs-suite-dev.herokuapp.com/sign_in/", json = {"username": "keane_pereira", "password": "K3@n3P3r3ir@"})
# print(response.status_code)
# print()

'''
import pymongo

m = pymongo.MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false')'''
# print(m.list_database_names())
# m.drop_database('Enrolled')
# print(m.list_database_names())

''' Check if the deleted obj is not the last one, if it is, then insert new collection then delete the collection you want'''
# client = m['DemoDB']['DemoCol']
# client.drop()
# print(client.find_one({}))


'''demo insert'''
# client = m['Enrolled']['Clsuid']
# client.insert_one(
#     {
#         'user_id': 'abc',
#         'username': 'keane',
#         'enrolled': ['abc', 'welfhi24hro2', 'lol']
#     }
# )

''' to unenroll step 2'''
# client = m['Enrolled']['Clsuid']
# client.delete_one(
#     {'user_id': 'abc'}
# )

# client = m['Enrolled']['Clsuid']
# client.update_one(
#     {'user_id': 'abc'},
#     { '$pull': { 'enrolled': { '$in': ['lol'] }} },
#     False
# )
# print(client.find_one({}))

from db_setup.mongo_setup import Mongo_CONN

DB_LECTURES = 'Lectures'
classroom_uid = '39c6e81c1a47463f96ed9d7d443efca2'


playlists = set()
res = Mongo_CONN[DB_LECTURES][classroom_uid].find({})
# print(res)
for j in res:
    if 'sections' in j.keys():
        for p in j['sections']:
            playlists.add(p)
    else:
        for p in j['playlists']:
            playlists.add(p)

playlists.remove('')





# x = json.loads(json_util.dumps(res))
# for lec in x:
#     for p in lec["playlists"]:
#         playlists.add(p)
print(playlists)

