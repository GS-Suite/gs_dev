from responses.standard_response_body import StandardResponseBody
from user import controllers as user_controllers
from fastapi.responses import HTMLResponse


async def sign_up(user):
    res = await user_controllers.sign_up(user)
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
    background_tasks.add_task(user_controllers.sign_out, token_value = token)
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
        return StandardResponseBody(True, "Your account has been deleted")
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
            "<p>Email could not be verified</p>"
        )