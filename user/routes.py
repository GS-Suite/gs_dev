from user import controllers as user_controllers
from tokens import controllers as token_controllers
from fastapi import status


async def sign_up(user, response):
    stts = await user_controllers.sign_up(user)
    response.status_code = stts
    if stts == 200:
        return {"success": True, "message": "Your account has been created"}
    elif stts == 409:
        return {"success": False, "message": "An account with that username already exists"}
    else:
        return {"success": False, "message": "Account not created"}


async def sign_in(user, response):
    res = await user_controllers.sign_in(user)
    if res:
        #print(res)
        response.status_code = status.HTTP_200_OK
        return {"success": True, "message": "Successfully logged in", "data": {"token": res}}

    response.status_code = status.HTTP_401_UNAUTHORIZED
    return {"success": False, "message": "Invalid username or password"}


async def sign_out(token, response, background_tasks):
    background_tasks.add_task(user_controllers.sign_out, token_value = token)
    response.status_code = 200
    return {"success": True, "message": "Successfully logged out"}


async def delete_account(password, token, response):
    if token == None:
        return {"success": False, "message": "'token' is a required header"}

    status = await user_controllers.delete_account(password, token)
    response.status_code = status
    
    if status == 200:
        return {"success": True, "message": "Your account has been deleted"}
    elif status == 401:
        return {"success": False, "message": "Invalid token or password"}
    return {"success": False, "message": "Error. Could not delete account"}

async def course_enroll(token, enroll):
    val_token = await token_controllers.validate_token(token)
    if type(val_token) == bool and val_token == True:
        status = await user_controllers.enroll_user(token = token, course_uid = enroll.course_uid)
        if status == 200:
            return {"success": True, "message": "You have been enrolled successfully"}
        else:
            return {"success": False, "message": "Sorry! Couldn't enroll"}
    elif type(val_token) == bool and val_token == False:
        return {
            "success": False, "message": "Your account is invalid"
        }
    elif type(val_token) == str:
        status = await user_controllers.enroll_user(token = val_token, course_uid = enroll.course_uid)
        if status == 200:
            return {"success": True, "message": "You have been enrolled successfully"}
        else:
            return {"success": False, "message": "Sorry! Couldn't enroll"}
    else:
        return {
            "success": False, "message": "Oops! "
        }
        
