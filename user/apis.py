from fastapi import Response, BackgroundTasks, Header, Depends
from user import schemas as user_schemas
from user import routes as user_routes
from main import app


@app.post("/sign_up/")
async def sign_up(user: user_schemas.UserSignUp):
    return await user_routes.sign_up(user)


@app.post("/sign_in/")
async def sign_in(user: user_schemas.UserSignIn):
    return await user_routes.sign_in(user)


@app.post("/sign_out/")
async def sign_out(background_tasks: BackgroundTasks, token: str = Header(None)):
    return await user_routes.sign_out(token, background_tasks)


@app.post("/update_profile/")
async def update_profile(details: user_schemas.UpdateProfileSchema, token: str = Header(None)):
    return await user_routes.update_profile(token, details)


@app.post("/update_password/")
async def update_password(details: user_schemas.UpdatePasswordSchema, token: str = Header(None)):
    return await user_routes.update_password(token, details)


@app.post("/delete_account/")
async def delete_account(password: user_schemas.DeleteUserSchema, token: str = Header(None)):
    return await user_routes.delete_account(password, token)


@app.post('/get_user_dashboard/')
async def get_user_dashboard(token: str = Header(None)):
    return await user_routes.get_user_dashboard(token)