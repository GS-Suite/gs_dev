from responses.standard_response_body import StandardResponseBody

from attendance import controllers as attendance_controllers
from announcements import controllers as announcement_controllers
from forum import mongo as forum_mongo


async def create_announcement_pane(classroom_uid, token):
    if_user_creator = await attendance_controllers.check_user_if_creator(classroom_id=classroom_uid, user_id=token.user_id)

    if if_user_creator == True:
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
        return StandardResponseBody(
        False, 'You are not the creator of the classroom', token.token_value
    )


async def post_announcement(classroom_uid, announcement, background_tasks,token):
    pass