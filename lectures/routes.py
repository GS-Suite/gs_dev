from tokens.controllers import token_validation
from responses.not_owner_response_body import NotOwnerResponseBody
from responses.standard_response_body import StandardResponseBody
from classrooms import controllers as classroom_controllers
from lectures import controllers as lecture_controllers
from lectures import mongo as lectures_mongo


async def get_classroom_lecture_videos(token, classroom_uid):
    check_creator = await classroom_controllers.check_user_if_creator(classroom_id=classroom_uid, user_id=token.user_id)
    is_user_enrolled = await classroom_controllers.if_user_enrolled(classroom_uid, token.user_id)
    if check_creator or is_user_enrolled:
        response = await lecture_controllers.get_classroom_lecture_videos(classroom_uid)
        if response:
            return StandardResponseBody(
                True, 'Lecture videos retrieved.', token.token_value, response
            )
        elif response == []:
            return StandardResponseBody(
                False, 'There are no lectures to retrieve', token.token_value
            )
        else:
            return StandardResponseBody(
                False, 'Lecture videos could not be retrieved.', token.token_value
            )
    else:
        return StandardResponseBody(
            success=False, message="You are not authorized to view this data", token=token.token_value
        )


async def get_classroom_lecture_playlists(token, classroom_uid):
    check_creator = await classroom_controllers.check_user_if_creator(classroom_id=classroom_uid, user_id=token.user_id)
    is_user_enrolled = await classroom_controllers.if_user_enrolled(classroom_uid, token.user_id)
    if check_creator or is_user_enrolled:
        response = await lecture_controllers.get_classroom_lecture_playlists(classroom_uid)
        if response:
            return StandardResponseBody(
                True, 'Classroom playlists retrieved.', token.token_value, response
            )
        else:
            return StandardResponseBody(
                False, 'Classroom playlists could not be retrieved.', token.token_value
            )
    else:
        return StandardResponseBody(
            success=False, message="You are not authorized to view this data", token=token.token_value
        )


async def get_classroom_playlist_videos(token, classroom_uid, playlist_name):
    check_creator = await classroom_controllers.check_user_if_creator(classroom_id=classroom_uid, user_id=token.user_id)
    is_user_enrolled = await classroom_controllers.if_user_enrolled(classroom_uid, token.user_id)
    if check_creator or is_user_enrolled:
        response = await lecture_controllers.get_classroom_playlist_videos(classroom_uid, playlist_name)
        if response:
            return StandardResponseBody(
                True, 'Classroom playlist videos retrieved.', token.token_value, response
            )
        else:
            return StandardResponseBody(
                False, 'Classroom playlist videos could not be retrieved.', token.token_value
            )
    else:
        return StandardResponseBody(
            success=False, message="You are not authorized to view this data", token=token.token_value
        )


async def add_lecture(token, classroom_uid, lecture):
    check_creator = await classroom_controllers.check_user_if_creator(classroom_id=classroom_uid, user_id=token.user_id)

    if check_creator:
        ### check if collection in mongo exists, else create
        await lecture_controllers.add_classroom_to_lectures_mongo(classroom_uid)

        response = await lecture_controllers.add_lecture(classroom_uid, lecture)
        if response:
            return StandardResponseBody(
                True, 'Lecture added.', token.token_value, response
            )
        else:
            return StandardResponseBody(
                False, 'Lecture could not be added.', token.token_value
            )
    else:
        return NotOwnerResponseBody(token.token_value)


async def edit_lecture(token, classroom_uid, lecture_uid, lecture):
    check_creator = await classroom_controllers.check_user_if_creator(classroom_id=classroom_uid, user_id=token.user_id)

    if check_creator:
        ### check if collection in mongo exists, else create
        await lecture_controllers.add_classroom_to_lectures_mongo(classroom_uid)

        response = await lecture_controllers.edit_lecture(classroom_uid, lecture_uid, lecture)
        if response:
            return StandardResponseBody(
                True, 'Lecture changes saved.', token.token_value
            )
        else:
            return StandardResponseBody(
                False, 'Lecture changes could not be saved.', token.token_value
            )
    else:
        return NotOwnerResponseBody(token.token_value)


async def delete_lecture(token, classroom_uid, lecture_uid):
    check_creator = await classroom_controllers.check_user_if_creator(classroom_id=classroom_uid, user_id=token.user_id)

    if check_creator:
        response = await lecture_controllers.delete_lecture(classroom_uid, lecture_uid)
        if response:
            return StandardResponseBody(
                True, 'Lecture deleted.', token.token_value
            )
        else:
            return StandardResponseBody(
                False, 'Lecture could not be deleted.', token.token_value
            )
    else:
        return NotOwnerResponseBody(token.token_value)