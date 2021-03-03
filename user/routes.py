from user import controllers as user_controllers
from tokens import controllers as token_controllers
from fastapi import status
from responses.standard_response_body import StandardResponseBody
from responses.token_response_body import TokenResponseBody
from responses.dashboard_response_body import DashboardResponseBody


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
    res = await user_controllers.sign_in(user)
    if res:
        #print(res)
        return TokenResponseBody(
            True, "Successfully logged in", res
        )
    return StandardResponseBody(
        False, "Invalid username or password"
    )


async def sign_out(token, background_tasks):
    background_tasks.add_task(user_controllers.sign_out, token_value = token)
    return StandardResponseBody(
        True, "Successfully logged out"
    )


async def delete_account(password, token):
    token = await token_controllers.get_token_by_value(token)
    if token == None:
        return StandardResponseBody(False, "Invalid token")

    print(password.password)
    status = await user_controllers.delete_account(password.password, token)
    if status:
        return StandardResponseBody(True, "Your account has been deleted")
    return StandardResponseBody(False, "Error. Could not delete account")


async def get_user_dashboard(token):
    tkn = await token_controllers.validate_token(token)
    if tkn:
        tkn = await token_controllers.get_token_by_value(tkn)
        
        user_data = await user_controllers.get_user_dashboard(tkn.user_id)
        if user_data:
            return DashboardResponseBody(
                True, "Details fetched", user_data
            )
        return StandardResponseBody(False, "Details not fetched")
    else:
        return StandardResponseBody(False, "Non-existent user")