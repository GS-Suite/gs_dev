from fastapi import BackgroundTasks, Depends, UploadFile, APIRouter
from tokens.controllers import token_validation
from fastapi.param_functions import File
from user import schemas as user_schemas
from user import routes as user_routes
from typing import Optional


router = APIRouter()

@router.post("/sign_up/")
async def sign_up(user: user_schemas.UserSignUp):
    return await user_routes.sign_up(user)


@router.post("/sign_in/")
async def sign_in(user: user_schemas.UserSignIn):
    return await user_routes.sign_in(user)


@router.post("/sign_out/")
async def sign_out(background_tasks: BackgroundTasks, token: dict = Depends(token_validation)):
    return await user_routes.sign_out(token, background_tasks)


@router.post("/update_profile/")
async def update_profile(details: user_schemas.UpdateProfileSchema, token: dict = Depends(token_validation)):
    return await user_routes.update_profile(token, details)


@router.post("/update_password/")
async def update_password(details: user_schemas.UpdatePasswordSchema, token: dict = Depends(token_validation)):
    return await user_routes.update_password(token, details)


@router.post("/delete_account/")
async def delete_account(password: user_schemas.DeleteUserSchema, token: dict = Depends(token_validation)):
    return await user_routes.delete_account(password, token)


@router.post('/get_user_dashboard/')
async def get_user_dashboard(token: dict = Depends(token_validation)):
    return await user_routes.get_user_dashboard(token)


@router.post("/change_profile_picture")
async def change_profile_picture(token: dict = Depends(token_validation), picture: Optional[UploadFile] = File(None)):
    return await user_routes.change_profile_picture(token, picture)