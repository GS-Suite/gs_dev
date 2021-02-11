from tokens import controllers as token_controllers
from fastapi import status


async def validate_token(token, response):
    #print(token.token)
    res = await token_controllers.validate_token(token.token)
    if res:
        return {
            "success": True,
            "message": "Valid token",
            "data": res
        }, status.HTTP_200_OK
    return {
        "success": False,
        "message": "Invalid token"
    }, status.HTTP_401_UNAUTHORIZED


async def refresh_token(token, response):
    #print(token.token)
    res = await token_controllers.refresh_token_by_token(token.token)
    if res:
        return {
            "success": True,
            "message": "Token refreshed",
            "data": res
        }, status.HTTP_200_OK
    return {
        "success": False,
        "message": "Invalid token"
    }, status.HTTP_401_UNAUTHORIZED