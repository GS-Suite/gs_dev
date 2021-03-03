from classrooms import helpers as classroom_helpers
from tokens import controllers as token_controllers
from classrooms import models as classroom_model
from user import models as user_models
from classrooms import mongo
from fastapi import status


async def get_user_classrooms(user_uid):
    classrooms = await classroom_model.get_classrooms_by_user(user_uid)
    return classrooms


async def get_user_enrolled(user_uid):
    print(user_uid)
    classrooms = await mongo.get_user_enrolled(user_uid)
    return classrooms


async def create_class(token, class_name):
    # GET USER FROM TOKEN, PASS user id while creating class
    
    # check if classroom with same name exists
    classrooms = await classroom_model.get_classrooms_by_user(token.user_id)
    for c in classrooms:
        # print(c.name)
        if c.name == class_name:
            return "exists", c

    uid = await classroom_helpers.generate_uid()
    return await classroom_model.create_classroom(token.user_id, class_name, uid)


async def get_classroom_details(user_id, name):
    ### check user role (teacher, student, owner, etc)
    ### accordingly retrieve data
    classroom = await classroom_model.get_classroom_by_name(user_id, name)
    
    ### get mongo rows, check users and classrooms
    role = await classroom_helpers.get_user_role(user_id, classroom.uid)

    if role == "teacher":
        creator = await user_models.get_user_by_uid(classroom.creator_uid)
        cls = {
            "name": classroom.name,
            "created_by": creator.username
        }
    elif role == "student":
        creator = await user_models.get_user_by_uid(classroom.creator_uid)
        cls = {
            "name": classroom.name,
            "created_by": creator.username
        }
    else:
        return False
    return cls


async def delete_classroom(token, classroom_name):
    pass


async def enroll_user(user_uid, classroom_uid):
    '''
    1. Get user_id from token model
    2. pass to mongo.course.enroll
    '''
    
    ### check if user already enrolled
    x = await mongo.get_classroom_enrolled(classroom_uid)
    if user_uid in x:
        return "exists"
    else:
        ### enroll user
        try:
            ### Updating user's enrolled array in mongo
            if mongo.enroll_user(user_uid, classroom_uid):
                ### Updating classroom enrolled array in mongo
                if mongo.enroll_classroom(user_uid, classroom_uid):
                    return True
            ### undo stuff
            #
            #
            #
            return False
        except Exception as e:
            return False