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