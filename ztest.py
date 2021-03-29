from db_setup.mongo_setup import FORUM_MONGO_CONN
import datetime

forum_id = '737c056eaa3d4179915b97d0fe5a1f37-F'

thread = 'main'


x = FORUM_MONGO_CONN[forum_id][thread].find()

# print([i for i in x])


send = {'forum_id': forum_id, 'thread': thread}

msgs = []

for i in x:
    i.pop('_id')
    # print(i['datetimestamp'].strftime('%d-%m-%Y %H:%M%S'))
    i['date'] = i['datetimestamp'].strftime('%d-%m-%Y')
    i['time'] = i['datetimestamp'].strftime('%H:%M:%S')
    i.pop('datetimestamp')
    msgs.append(i)

send['classroom_id'] = forum_id[:-2]
send['posts'] = msgs

if 'wowo' in send.keys():
    print(send)
else:
    print('not there')