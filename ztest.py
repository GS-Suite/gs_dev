from db_setup.mongo_setup import FORUM_MONGO_CONN

forum_id = '737c056eaa3d4179915b97d0fe5a1f37-F'

thread = 'main'


x = FORUM_MONGO_CONN[forum_id][main].find({})