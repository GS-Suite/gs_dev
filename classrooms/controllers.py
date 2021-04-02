from classrooms import helpers as classroom_helpers
from classrooms import models as classroom_model
from classrooms import mongo as classroom_mongo
from user import models as user_model


async def check_user_if_creator(classroom_id, user_id):
    classroom_obj = await classroom_model.get_classroom_by_uid(uid = classroom_id)
    if classroom_obj:
        if user_id == classroom_obj.creator_uid:
            return True
    return False


async def if_user_enrolled(classroom_uid, user_id):
    classroom_enrolled_resp = await classroom_mongo.check_enrolled_in_classroom(classroom_uid, user_id)
    user_enrolled_resp = await classroom_mongo.check_enrolled_in_user_enrolled(classroom_uid, user_id)

    # print('classroom_enrolled_resp: ', classroom_enrolled_resp)
    # print('user_enrolled_resp: ', user_enrolled_resp)

    if classroom_enrolled_resp ==  True and user_enrolled_resp == True:
        return True
    
    return False


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
    #print(user_uid)
    classrooms = await classroom_mongo.get_user_enrolled(user_uid)
    print(classrooms)
    results = []
    for uid in classrooms:
        C = await classroom_model.get_classroom_by_uid(uid)
        teacher = await user_model.get_user_by_uid(C.creator_uid)
        results.append({
            "uid": uid,
            "name": C.name,
            "teacher": {
                "username": teacher.username,
                "name": f"{teacher.first_name} {teacher.last_name}"
            }
        })
    return results


async def get_classroom_enrolled(classroom_uid):
    enrolled = await classroom_mongo.get_classroom_enrolled(classroom_uid)
    return enrolled


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
        "entry_code": classroom.entry_code,
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
        ''' 
            Add Code to Mongo entry

        '''
        #mongo_resp = mongo.classroom_add_entry_code(classroom_uid = classroom_uid, code = code)
        #if mongo_resp:
        if classroom:
            classroom = {
                "name": classroom.name,
                "uid": classroom.uid,
                "entry_code": classroom.entry_code,
                "classroom_owner_id": user_uid
            }
            return classroom

    return False


async def enroll_user(user_uid, token, entry_code):
    '''
    1. Get user_id from token model
    2. pass to mongo.course.enroll
    '''

    ### check code for validity
    classroom = await classroom_model.get_classroom_by_entry_code(entry_code)
    if not classroom:
        return "code_error"
    
    ### check if user already enrolled
    x = await classroom_mongo.get_classroom_enrolled(classroom.uid)
    for user in x:
        if user["username"] == token.username:
            return "exists"
    else:
        ### enroll user
        try:
            ### Updating user's enrolled array in mongo
            await classroom_mongo.enroll_user(user_uid, classroom.uid)
            ### Updating classroom enrolled array in mongo
            await classroom_mongo.enroll_classroom(user_uid, token.username, classroom.uid)
            return True
        ### undo stuff
            #
            #
            #
        except Exception as e:
            print(e)
            return False

async def getClassroomUid(entry_code):
    try:
        classroom_uid = await classroom_model.get_classroom_by_entry_code(entry_code)
        return {
            'status': True,
            'classroom_uid': classroom_uid.uid,
            'classroom_name': classroom_uid.name,
        }
    except Exception as e:
        print(e)
        return {'status': False}


async def delete_user_classrooms(uid):
    return await classroom_model.delete_user_classrooms(uid)


async def get_classroom_owner_from_class_uid(classroom_uid):
    try:
        classroom = await classroom_model.get_classroom_by_uid(uid=classroom_uid)
        return {
            'status': True,
            'classroom_uid': classroom.uid,
            'classroom_name': classroom.name,
            'classroom_owner_id': classroom.creator_uid
        }
    except Exception as e:
        print(e)
        return {'status': False}



'''
async def generate_join_link():
    return x'''