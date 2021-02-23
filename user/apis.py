from fastapi import Response, BackgroundTasks, Header, Depends
from user import schemas as user_schemas
from user import routes as user_routes
from main import app


@app.post("/sign_up/")
async def sign_up(user: user_schemas.UserSignUp, response: Response):
    return await user_routes.sign_up(user, response)


@app.post("/sign_in/")
async def sign_in(user: user_schemas.UserSignIn, response: Response):
    return await user_routes.sign_in(user, response)


@app.post("/sign_out/")
async def sign_out(token: str, response: Response, background_tasks: BackgroundTasks):
    return await user_routes.sign_out(token, response, background_tasks)


@app.post("/delete_account/")
async def delete_account(response: Response, password: user_schemas.DeleteUserSchema, token: str = Header(None)):
    return await user_routes.delete_account(password, token, response)


@app.post('/enroll/')
async def course_enroll(token: str, enroll: user_schemas.UserCourseEnroll, response: Response):
    return await user_routes.course_enroll(token, enroll)
