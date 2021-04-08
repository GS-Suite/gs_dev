from starlette.responses import RedirectResponse
from responses.standard_response_body import StandardResponseBody
from user import controllers as user_controllers
from fastapi.responses import HTMLResponse

from classrooms import controllers as classroom_controllers


async def sign_up(user, url, bg):
    res = await user_controllers.sign_up(user, url, bg)
    if res == True:
        return StandardResponseBody(
            True, "Your account has been created"
        )
    elif res == "exists":
        return StandardResponseBody(
            False, "An account with that username already exists"
        )
    return StandardResponseBody(
        False, "Account not created"
    )


async def sign_in(user):
    token = await user_controllers.sign_in(user)
    if token:
        #print(res)
        return StandardResponseBody(
                True, "Successfully logged in", token.token_value
            )
    return StandardResponseBody(
        False, "Invalid username or password"
    )


async def sign_out(token, background_tasks):
    background_tasks.add_task(user_controllers.sign_out, token = token)
    return StandardResponseBody(
        True, "Successfully logged out"
    )


async def update_profile(token, details):
    res = await user_controllers.update_profile(token.user_id, details)
    if res:
        return StandardResponseBody(
            True, "Profile updated", token.token_value, res
        )
    return StandardResponseBody(False, "Profile not updated")


async def update_password(token, details):
    res = await user_controllers.update_password(token.user_id, details)
    if res == True:
        return StandardResponseBody(
            True, "Password updated", token.token_value
        )
    elif res == "invalid_password":
        return StandardResponseBody(False, "Invalid current password")
    return StandardResponseBody(False, "Profile not updated")


async def delete_account(password, token):
    #print(password.password)
    status = await user_controllers.delete_account(password.password, token)
    if status:
        return StandardResponseBody(True, "Your account has been deleted, along with all your data, and classrooms")
    return StandardResponseBody(False, "Error. Could not delete account")


async def get_user_dashboard(token):
    user_data = await user_controllers.get_user_dashboard(token.user_id)
    if user_data:
        return StandardResponseBody(
            True, "Details fetched", token.token_value, user_data
        )
    return StandardResponseBody(False, "Details not fetched")


async def change_profile_picture(token, picture):
    resp = await user_controllers.change_profile_picture(token.user_id, picture)
    if resp == "deleted":
        return StandardResponseBody(
            True, "Profile picture deleted", token.token_value
        )
    elif resp:
        return StandardResponseBody(
            True, "Profile picture updated", token.token_value
        )
    return StandardResponseBody(False, "Could not update profile picture")


async def get_username_from_user_id(user_uid, token):
    resp = await user_controllers.get_user_username(uid=user_uid)

    if resp:
        return StandardResponseBody(
            True, 'Username acquired from given user uid', token.token_value, {
                'user_uid': user_uid,
                'username': resp
            }
        )
    else:
       return StandardResponseBody(
            False, 'Username could not be aquired from given user uid', token.token_value
        )


async def verify_email(token):
    res = await user_controllers.verify_email(token)
    if res:
        return HTMLResponse(
            "<p>Email Verified</p>"
        )
    return HTMLResponse(
            "<p>Token already used, or email could not be verified</p>"
        )


async def send_reset_password(username, email, url, bg):
    ''' check if user exists '''
    user = await user_controllers.get_user_from_email(username, email)
    if user:
        res = False
        #res = await user_controllers.send_reset_password(user, url, bg)
        if res:
            return StandardResponseBody(
                True, "Email to reset password sent successfully.", token = None
            )
        return StandardResponseBody(
            False, "Failed to send email.", token = None
        )
    return StandardResponseBody(
        False, "No account found with that email and username.", token = None
    )


async def reset_password(reset):
    res = await user_controllers.reset_password(reset)
    if res:
        return StandardResponseBody(
            True, "Your password has been changed.", token = None
        )
    return StandardResponseBody(
        False, "Could not reset password.", token = None
    )

''' this function does not need some special controller code since it's just organising data (as of yet)'''
async def get_any_user_profile_from_user_id(user_id, token):

    ''' User ID validation '''
    if user_id == '':
        return StandardResponseBody(
            False, 'User ID cannot be empty', token.token_value
        )
    
    ''' Get (any) User Profile aka Dashboard '''
    user_profile = await user_controllers.get_user_dashboard(user_id)

    if user_profile == False:
        return StandardResponseBody(
            False, 'The user you are searching for does not exist', token.token_value
        )

    ''' Get the searched user's created classrooms, if any '''
    user_created_classrooms = await classroom_controllers.get_user_classrooms(user_uid = user_id)

    ''' Get the searched user's enrolled classrooms, if any '''
    user_enrolled_classrooms = await classroom_controllers.get_user_enrolled(user_uid = user_id)
    
    if user_created_classrooms == [] and user_enrolled_classrooms == []:
        return StandardResponseBody(
            True, 'User profile could be procured', token.token_value, {
                'user_profile': user_profile,
                'user_created_classrooms': [],
                'user_enrolled_classrooms': []
            }
        )
    elif user_created_classrooms != [] and user_enrolled_classrooms == []:
        return StandardResponseBody(
            True, 'User Profile and user\'s created classrooms could be procured', token.token_value, {
                'user_profile': user_profile, 
                'user_created_classrooms': user_created_classrooms,
                'user_enrolled_classrooms': []
            }
        )
    elif user_created_classrooms == [] and user_enrolled_classrooms != []:
        return StandardResponseBody(
            True, 'User Profile and user\'s enrolled classrooms could be procured', token.token_value, {
                'user_profile': user_profile, 
                'user_created_classrooms': [],
                'user_enrolled_classrooms': user_enrolled_classrooms
            }
        )
    elif user_created_classrooms != [] and user_enrolled_classrooms != []:
        return StandardResponseBody(
            True, 'User Profile, User\'s enrolled and created classrooms could be procured', token.token_value, {
                'user_profile': user_profile, 
                'user_created_classrooms': user_created_classrooms,
                'user_enrolled_classrooms': user_enrolled_classrooms
            }
        )
    else:
        return StandardResponseBody(
            False, 'We have no clue why this would should up, it\'s an error', token.token_value
        )


async def get_any_user_profile_from_username(username, token):
    if username == '':
        return StandardResponseBody(
            False, 'Username cannot be left empty', token.token_value
        )
    user_id = await user_controllers.get_userid_from_username(username = username)
    if user_id:
        return await get_any_user_profile_from_user_id(user_id = user_id, token = token)
    return StandardResponseBody(
        False, 'Could not get userid from username', token.token_value
    )