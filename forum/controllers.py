from forum import mongo as forum_mongo


def create_forum(classroom_uid):
    '''Returns Bool'''
    return forum_mongo.create_forum(classroom_uid)








