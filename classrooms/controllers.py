from classrooms import helpers as classroom_helpers
from tokens import controllers as token_controllers
from classrooms import models as classroom_model
from fastapi import status


async def create_class(token, class_name):
    # GET USER FROM TOKEN, PASS user id while creating class
    res = await token_controllers.get_token_by_value(token)
    if res != None:
        # check if classroom with same name exists
        classrooms = await classroom_model.get_classrooms_by_user(res.user_id)
        for c in classrooms:
            # print(c.name)
            if c.name == class_name:
                return status.HTTP_409_CONFLICT

        uid = await classroom_helpers.generate_uid()
        resp = await classroom_model.create_classroom(res.user_id, class_name, uid)
        # print(resp)
        if resp:
            return status.HTTP_200_OK
        else:
            return status.HTTP_400_BAD_REQUEST
    else:
        # invalid token
        return status.HTTP_401_UNAUTHORIZED


async def get_classrooms_by_user(user_uid):
    classrooms = await classroom_model.get_classrooms_by_user(user_uid)
    return classrooms


async def get_classroom_by_name(user_id, name):
    classroom = await classroom_model.get_classroom_by_name(user_id, name)
    return classroom


async def delete_classroom(token, classroom_name):
    pass