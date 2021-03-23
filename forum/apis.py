from fastapi import Response, Header
from forum import schemas as forum_schemas
from forum import routes as forum_routes
from main import app

@app.post('/create_forum/')
async def create_forum(forum: forum_schemas.Forum):
    pass

@app.post('/get_forum_chat/')
async def get_forum_chat():
    pass

@app.post('/send_message/'):
async def post():
    pass
