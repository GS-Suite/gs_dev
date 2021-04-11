# # from db_setup.mongo_setup import FORUM_MONGO_CONN

# import pymongo
# import datetime
# import pytz



# FORUM_MONGO_CONN = pymongo.MongoClient('')

# forum_id = '' + '-F'
# msgs = []


# resp = FORUM_MONGO_CONN[forum_id]['main'].find({})

# # for i in resp:
# #     i
# #     print(i)
# for i in resp:
#     i.pop('_id')
#     i['datetime'] = i['datetimestamp'].astimezone(pytz.timezone("Asia/Kolkata")).strftime('%d-%m-%Y %H:%M:%S')
#     i.pop('datetimestamp')
#     msgs.append(i)
# #     # i['time'] = i['datetimestamp'].strftime('%H:%M:%S')
# #     # i.pop('datetimestamp')

# print(msgs)  
