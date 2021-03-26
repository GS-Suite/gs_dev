from fastapi import Response, Header, Body
from forum import routes as forum_routes
from main import app

@app.post('/create_forum/')
async def create_forum(classroom_uid: str, token: str = Header(None)):
    return await forum_routes.create_forum(classroom_uid, token)

@app.post('/get_forum_chat/')
async def get_forum_chat():
    pass

@app.post('/send_message/')
async def send_message(classroom_uid: str = Body(...), message: str = Body(...), reply_id: str = Body(None),token: str = Header(None)):
    return await forum_routes.send_message(classroom_uid=classroom_uid, message=message, token=token)
