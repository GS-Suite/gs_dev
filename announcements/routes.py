from responses.not_owner_response_body import NotOwnerResponseBody
from responses.standard_response_body import StandardResponseBody
from announcements import controllers as announcement_controllers
from classrooms import controllers as classroom_controllers
from classrooms import models as classroom_models
from forum import mongo as forum_mongo


async def create_announcement_pane(classroom_uid, token):
    
    classroom_exist_status = await classroom_models.get_classroom_by_uid(uid = classroom_uid)
    if not classroom_exist_status:
        return StandardResponseBody(
            False, 'Create classroom before creating announcement pane', token.token_value
        )
    if_user_creator = await classroom_controllers.check_user_if_creator(classroom_id=classroom_uid, user_id=token.user_id)

    if if_user_creator == True:
        ''' forum and announcements are in the same mongo database, just separate threads'''
        if_announcement_pane_exists = await forum_mongo.check_if_forum_exists(classroom_uid)

        if if_announcement_pane_exists['forum_exists'] == True:
            return StandardResponseBody(
                True, 'Announcement Pane already exists', token.token_value
            )
        else:
            announcement_pane_creation_status = await announcement_controllers.create_announcement_pane(classroom_uid)
            if announcement_pane_creation_status == True:
                return StandardResponseBody(
                    True, 'Announcement Pane has been created', token.token_value
                )
            else:
                return StandardResponseBody(
                    False, 'Announcement Pane could not be created', token.token_value
                )
    else:
        return NotOwnerResponseBody(token.token_value)


async def post_announcement(classroom_uid, announcement, background_tasks, token):
    if_user_creator = await classroom_controllers.check_user_if_creator(classroom_id=classroom_uid, user_id=token.user_id)

    if if_user_creator ==  True:
        if_announcement_pane_exists = await forum_mongo.check_if_forum_exists(classroom_uid)

        if if_announcement_pane_exists['forum_exists'] ==  True:
    
            announcement_email_notif_status = await announcement_controllers.send_notif(classroom_uid = classroom_uid, announcement = announcement, tasks = background_tasks)

            if announcement_email_notif_status ==  True:
                return StandardResponseBody(
                    True, 'Announcement has been posted', token.token_value
                )
            else:
                return StandardResponseBody(
                    False, 'Announcement could not be posted', token.token_value
                )
            
        else:
            return StandardResponseBody(
                False, 'Create Announcement Pane', token.token_value
            )
    else:
        return NotOwnerResponseBody(token.token_value)


async def get_all_announcements(classroom_uid, token):
    user_enrolled_status = await classroom_controllers.if_user_enrolled(classroom_uid=classroom_uid, user_id=token.user_id)
    if_user_is_creator = await classroom_controllers.check_user_if_creator(classroom_id=classroom_uid, user_id=token.user_id)

    if user_enrolled_status == True or if_user_is_creator == True:
        if_forum_exists = await forum_mongo.check_if_forum_exists(classroom_uid=classroom_uid)

        if if_forum_exists['forum_exists'] == True:
            get_all_announcements_response_dict = await announcement_controllers.get_all_announcements(classroom_uid = classroom_uid)
            if 'status' in get_all_announcements_response_dict.keys():
                '''if status exists then mongo failed'''
                return StandardResponseBody(
                    False, get_all_announcements_response_dict['message'], token.token_value
                )
            else:
                return StandardResponseBody(
                    True, 'Announcements have been acquired', token.token_value, {'forum_stuff': get_all_announcements_response_dict}
                )
        
        else:
            return StandardResponseBody(
                False, 'Announcements do not exist', token.token_value
            )
    else:
        return NotOwnerResponseBody(token.token_value)


async def delete_announcement(classroom_uid, announcement_id, token):
    if_user_creator = await classroom_controllers.check_user_if_creator(classroom_id = classroom_uid, user_id = token.user_id)

    if if_user_creator == True:
        resp = await announcement_controllers.delete_announcement(classroom_uid = classroom_uid, announcement_id = announcement_id)

        if resp == True:
            return StandardResponseBody(
                True, 'Announcement has been deleted', token.token_value
            )
        else:
            return StandardResponseBody(
                False, 'Announcemement could not be deleted', token.token_value
            )
    
    else:
        return NotOwnerResponseBody(token = token.token_value)

