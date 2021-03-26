from typing import Optional
from fastapi import Response, BackgroundTasks, Header, Depends, UploadFile, APIRouter
from fastapi.param_functions import File
from user import schemas as user_schemas
from user import routes as user_routes


router = APIRouter()

@router.post("/sign_up/", tags = ["users"])
async def sign_up(user: user_schemas.UserSignUp):
    return await user_routes.sign_up(user)


@router.post("/sign_in/", tags = ["users"])
async def sign_in(user: user_schemas.UserSignIn):
    return await user_routes.sign_in(user)


@router.post("/sign_out/", tags = ["users"])
async def sign_out(background_tasks: BackgroundTasks, token: str = Header(None)):
    return await user_routes.sign_out(token, background_tasks)


@router.post("/update_profile/", tags = ["users"])
async def update_profile(details: user_schemas.UpdateProfileSchema, token: str = Header(None)):
    return await user_routes.update_profile(token, details)


@router.post("/update_password/", tags = ["users"])
async def update_password(details: user_schemas.UpdatePasswordSchema, token: str = Header(None)):
    return await user_routes.update_password(token, details)


@router.post("/delete_account/", tags = ["users"])
async def delete_account(password: user_schemas.DeleteUserSchema, token: str = Header(None)):
    return await user_routes.delete_account(password, token)


@router.post('/get_user_dashboard/', tags = ["users"])
async def get_user_dashboard(token: str = Header(None)):
    return await user_routes.get_user_dashboard(token)


@router.post("/change_profile_picture", tags = ["users"])
async def change_profile_picture(token: str = Header(None), picture: Optional[UploadFile] = File(None)):
    return await user_routes.change_profile_picture(token, picture)