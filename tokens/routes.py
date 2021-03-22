from responses.standard_response_body import StandardResponseBody
from tokens import controllers as token_controllers
from fastapi import status


async def validate_token(token):
    token = await token_controllers.validate_token(token)
    if token:
        return StandardResponseBody(
            True, "Valid token", token.token_value
            )
    return StandardResponseBody(
        False, "Invalid token"
        )


async def refresh_token(token):
    res = await token_controllers.refresh_token_by_token(token)
    print(res)
    if res:
        return StandardResponseBody(
            True, "Token refreshed", res.token_value
        )
    return StandardResponseBody(
        False, "Token not refreshed"
    )