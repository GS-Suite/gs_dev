from starlette.responses import JSONResponse
from user import controllers as user_controllers
from tokens import controllers as token_controllers
from fastapi import status
from responses.standard_response_body import StandardResponseBody


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
    tkn = await token_controllers.validate_token(token)
    if tkn:
        res = await user_controllers.update_profile(tkn.user_id, details)
        if res:
            return StandardResponseBody(
                True, "Profile updated", tkn.token_value, res
            )
        return StandardResponseBody(False, "Profile not updated")
    return StandardResponseBody(False, "Invalid token")


async def update_password(token, details):
    tkn = await token_controllers.validate_token(token)
    if tkn:
        res = await user_controllers.update_password(tkn.user_id, details)
        if res == True:
            return StandardResponseBody(
                True, "Password updated", tkn.token_value
            )
        elif res == "invalid_password":
            return StandardResponseBody(False, "Invalid current password")
        return StandardResponseBody(False, "Profile not updated")
    return StandardResponseBody(False, "Invalid token")


async def delete_account(password, token):
    token = await token_controllers.validate_token(token)
    if token:
        #print(password.password)
        status = await user_controllers.delete_account(password.password, token)
        if status:
            return StandardResponseBody(True, "Your account has been deleted")
        return StandardResponseBody(False, "Error. Could not delete account")
    return StandardResponseBody(False, "Invalid token")


async def get_user_dashboard(token):
    tkn = await token_controllers.validate_token(token)
    if tkn:
        user_data = await user_controllers.get_user_dashboard(tkn.user_id)
        if user_data:
            return StandardResponseBody(
                True, "Details fetched", tkn.token_value, user_data
            )
        return StandardResponseBody(False, "Details not fetched")
    return StandardResponseBody(False, "Non-existent user")


async def change_profile_picture(token, picture):
    tkn = await token_controllers.validate_token(token)
    if tkn:
        resp = await user_controllers.change_profile_picture(tkn.user_id, picture)
        if resp == "deleted":
            return StandardResponseBody(
                True, "Profile picture deleted", tkn.token_value
            )
        elif resp:
            return StandardResponseBody(
                True, "Profile picture updated", tkn.token_value
            )
        return StandardResponseBody(False, "Could not update profile picture")
    return StandardResponseBody(False, "Non-existent user")
