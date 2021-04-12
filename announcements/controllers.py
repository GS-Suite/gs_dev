from announcements import mongo as announcement_mongo
from classrooms import mongo as classroom_mongo
from classrooms import models as classroom_models
from user import models as user_models
from announcements import helpers as announcement_helpers
from classrooms import controllers as classroom_controllers
from user import controllers as user_controllers
import datetime


async def create_announcement_pane(classroom_uid):
    '''Returns Bool'''
    return await announcement_mongo.create_announcement_pane(classroom_uid)


async def send_notif(classroom_uid, announcement, tasks):
    classroom_enrolled = await classroom_mongo.get_classroom_enrolled(classroom_uid=classroom_uid)
    classroom_info = await classroom_models.get_classroom_by_uid(uid=classroom_uid)
    creator_info = await user_models.get_user_by_uid(uid=classroom_info.creator_uid)

    datetimestamp = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    
    enrolled_mailing_list = []

    mongo_ann_struc = {
        'announcement_id': announcement_helpers.generate_message_code(),
        'announcement': announcement,
        'datetime': datetimestamp,
        'creator': creator_info.username,
        'creator_uid': classroom_info.creator_uid
    }

    email_struc = {
        'announcement': announcement,
        'datetime': datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    }

    post_announcement_mongo = await announcement_mongo.post_announcement(mongo_ann_struc, classroom_uid)

    if post_announcement_mongo ==  True:
        ###
        return True
        
        if classroom_enrolled != []:
            ''' Prepping mailing list'''
            for enrolled_user in classroom_enrolled:
                user = await user_models.get_user_by_uid(uid=enrolled_user['uid'])
                user_info = {
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'username': user.username,
                    'email': user.email
                }
                enrolled_mailing_list.append(user_info)
            
            
            mail_status = await announcement_helpers.send_announcement_email(
                 enrolled_mailing_list=enrolled_mailing_list,
                 classroom_info=classroom_info,
                 creator_info = creator_info,
                 email_struc=email_struc,
                 bg = tasks
            )
            if mail_status:
                 return True
        else:
            ''' which is empty obv '''
            return False



async def get_all_announcements(classroom_uid):
    classroom = await classroom_controllers.get_classroom_owner_from_class_uid(classroom_uid=classroom_uid)
    owner_username = await user_controllers.get_user_username(uid=classroom['classroom_owner_id'])
    posts = await announcement_mongo.get_all_announcements(classroom_uid=classroom_uid)

    if posts == []:
        return {
            'status': True,
            'message': 'There are no announcements'
        }

    elif posts == False:
        return {
            'status': False,
            'message': 'Failed to get announcements'
        }  
    elif type(posts) == list:
        send = {
            'classroom_uid': classroom_uid,
            'classroom_owner_uid': classroom['classroom_owner_id'],
            'classroom_owner_username': owner_username,
            'forum_id': classroom_uid + '-F',
            'thread': 'announcements',
            "posts": posts 
        }
        
        return send

async def delete_announcement(classroom_uid, announcement_id):
    resp = await announcement_mongo.delete_announcement(classroom_uid, announcement_id)

    if resp ==  True:
        return True
    else:
        return False
        