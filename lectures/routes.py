from tokens.controllers import token_validation
from responses.not_owner_response_body import NotOwnerResponseBody
from responses.standard_response_body import StandardResponseBody
from classrooms import controllers as classroom_controllers
from lectures import controllers as lecture_controllers
from lectures import mongo as lectures_mongo


async def get_classroom_lectures(token, classroom_uid):
    check_creator = await classroom_controllers.check_user_if_creator(classroom_id=classroom_uid, user_id=token.user_id)
    is_user_enrolled = await classroom_controllers.if_user_enrolled(classroom_uid, token.user_id)
    if check_creator or is_user_enrolled:
        response = await lecture_controllers.get_classroom_lectures(classroom_uid)
        if response:
            return StandardResponseBody(
                True, 'Lectures retrieved.', token.token_value, response
            )
        else:
            return StandardResponseBody(
                False, 'Lecture could not be retrieved.', token.token_value
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