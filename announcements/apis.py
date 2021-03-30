from tokens.controllers import token_validation
from fastapi.param_functions import Depends

from announcements import routes as announcement_routes

from fastapi import Body, APIRouter, BackgroundTasks


router = APIRouter()

@router.post('/create_announcement_pane/')
async def create_annonuncement_pane(classroom_uid: str = Body(..., embed=True), token: dict = Depends(token_validation)):
    return await announcement_routes.create_announcement_pane(classroom_uid, token)

@router.post('/post_announcement/')
async def post_announcement(classroom_uid: str = Body(...), announcement: str = Body(...), 
                background_tasks: BackgroundTasks, token: dict = Depends(token_validation)):
    return await announcement_routes.post_announcement(classroom_uid, announcement, background_tasks, token)