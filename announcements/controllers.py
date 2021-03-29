from announcements import mongo as announcement_mongo



def create_announcement_pane(classroom_uid):
    '''Returns Bool'''
    return announcement_mongo.create_announcement_pane(classroom_uid)