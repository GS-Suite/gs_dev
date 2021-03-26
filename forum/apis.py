from fastapi import Response, Header, Body, APIRouter
from tokens.controllers import token_validation
from fastapi.param_functions import Depends
from forum import routes as forum_routes


router = APIRouter()

@router.post('/create_forum/')
async def create_forum(classroom_uid: str, token: dict = Depends(token_validation)):
    return await forum_routes.create_forum(classroom_uid, token)

@router.post('/get_forum_chat/')
async def get_forum_chat():
    pass

@router.post('/send_message/')
async def send_message(classroom_uid: str = Body(...), message: str = Body(...), token: dict = Depends(token_validation):
    return await forum_routes.send_message(classroom_uid=classroom_uid, message=message, token=token)
