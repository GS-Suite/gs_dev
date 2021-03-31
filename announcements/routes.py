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
        if_announcement_pane_exists = forum_mongo.check_if_forum_exists(classroom_uid)

        if if_announcement_pane_exists['forum_exists'] == True:
            return StandardResponseBody(
                False, 'Announcement Pane already exists', token.token_value
            )
        else:
            announcement_pane_creation_status = announcement_controllers.create_announcement_pane(classroom_uid)
            if announcement_pane_creation_status == True:
                return StandardResponseBody(
                    True, 'Announcement Pane has been created', token.token_value
                )
            else:
                return StandardResponseBody(
                    True, 'Announcement Pane could not be created', token.token_value
                )
    else:
        return NotOwnerResponseBody(token.token_value)


async def post_announcement(classroom_uid, announcement, background_tasks,token):
    if_user_creator = await classroom_controllers.check_user_if_creator(classroom_id=classroom_uid, user_id=token.user_id)
    # get_enrolled_peeps = 
    pass