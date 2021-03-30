from tokens.controllers import token_validation
from responses.not_owner_response_body import NotOwnerResponseBody
from responses.standard_response_body import StandardResponseBody
from classrooms import controllers as classroom_controllers
from lectures import controllers as lecture_controllers
from lectures import mongo as lectures_mongo



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