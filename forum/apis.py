from tokens.controllers import token_validation
from fastapi.param_functions import Depends
from forum import routes as forum_routes
from fastapi import Body, APIRouter


router = APIRouter()

@router.post('/create_forum/')
async def create_forum(classroom_uid: str = Body(..., embed=True), token: dict = Depends(token_validation)):
    return await forum_routes.create_forum(classroom_uid, token)


@router.post('/get_forum_chat/')
async def get_forum_chat(classroom_uid: str = Body(..., embed=True), token: dict = Depends(token_validation)):
    return await forum_routes.get_forum_chat(classroom_uid = classroom_uid, token = token)


@router.post('/send_message/')
async def send_message(classroom_uid: str = Body(...), message: str = Body(...), reply_user_id: str = Body(...), 
                    reply_msg_id: str = Body(...), token: dict = Depends(token_validation)):
    return await forum_routes.send_message(classroom_uid=classroom_uid, message=message, reply_user_id=reply_user_id, 
                    reply_msg_id=reply_msg_id, tkn=token)

