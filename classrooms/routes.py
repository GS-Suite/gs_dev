from starlette.status import HTTP_200_OK
from classrooms import controllers as classroom_controllers
from tokens import controllers as token_controllers
from fastapi import status


async def create_classroom(classroom, response, token):
    tkn_validation_resp = await token_controllers.validate_token(token)

    if tkn_validation_resp:
        tkn = tkn_validation_resp['token']
        #print(tkn)
        res = await classroom_controllers.create_class(tkn, classroom.class_name)
        response.status_code = res
        if res == status.HTTP_200_OK:
            return {"success": True, "message": "Classroom created", "classroom_name": classroom.class_name}, res
        elif res == status.HTTP_409_CONFLICT:
            return {"success": False, "message": "Classroom already exists"}, res
        return {"success": False, "message": "Classroom not created"}, res
    else:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"success": False, "message": "Non-existent user"}, status.HTTP_401_UNAUTHORIZED


async def get_classrooms(token, response):
    tkn_validation_resp = await token_controllers.validate_token(token)

    if tkn_validation_resp:
        tkn = await token_controllers.get_token_by_value(tkn_validation_resp["token"])
        
        res = await classroom_controllers.get_classrooms_by_user(tkn.user_id)
        print(res)
        if res:
            return {"success": True, "message": "Classrooms retrieved", "data": res}, status.HTTP_200_OK
        else:
            return {"success": False, "message": "Could not retrieve data"}, status.HTTP_400_BAD_REQUEST
    else:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"success": False, "message": "Non-existent user"}, status.HTTP_401_UNAUTHORIZED
