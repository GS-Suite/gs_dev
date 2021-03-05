from classrooms import helpers as classroom_helpers
from tokens import controllers as token_controllers
from classrooms import models as classroom_model
from user import models as user_models
from classrooms import mongo
from fastapi import status


async def get_user_classrooms(user_uid):
    classrooms = await classroom_model.get_classrooms_by_user(user_uid)
    c = [
        {
            "name": i.name,
            "uid": i.uid
        } for i in classrooms
    ]
    return c


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
            return "exists", {
                "name": c.name,
                "uid": c.uid
            }

    uid = await classroom_helpers.generate_uid()
    res, c = await classroom_model.create_classroom(token.user_id, class_name, uid)
    if c:
        c = {
            "name": c.name,
            "uid": c.uid
        }
    return res, c


async def get_classroom_details(user_id, uid):
    ### check user role (teacher, student, owner, etc)
    ### accordingly retrieve data
    classroom = await classroom_model.get_classroom_by_uid(uid)
    
    cls = {
        "name": classroom.name,
        "uid": classroom.uid,
        "entry_code": classroom.entry_code
    }
    return cls


async def delete_classroom(token, classroom_name):
    pass


async def generate_classroom_entry_code(user_uid, classroom_uid):
    print(user_uid, classroom_uid)
    ### get classroom, check if user authorized
    classroom = await classroom_model.get_classroom_by_uid(classroom_uid)
    
    if classroom.creator_uid == user_uid:
        ### generate code, store it
        code = await classroom_helpers.generate_entry_code()
        classroom = await classroom_model.generate_entry_code(classroom, code)
        if classroom:
            classroom = {
                "name": classroom.name,
                "uid": classroom.uid,
                "entry_code": classroom.entry_code
            }
            return classroom
    return False


async def enroll_user(user_uid, classroom_uid, entry_code):
    '''
    1. Get user_id from token model
    2. pass to mongo.course.enroll
    '''

    ### check code for validity
    if not await classroom_model.get_classroom_by_entry_code(entry_code):
        return "code_error"
    
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


async def delete_user_classrooms(uid):
    return await classroom_model.delete_user_classrooms(uid)



async def generate_join_link():
    return x