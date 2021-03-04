from pydantic import Field
from classrooms import schemas as classroom_schemas
from classrooms import routes as classroom_routes
from fastapi import Response, Header
from main import app


@app.post("/create_classroom/")
async def create_classroom(classroom: classroom_schemas.CreateClassroomSchema, token: str = Header(None)):
    return await classroom_routes.create_classroom(classroom, token)


@app.post("/get_user_classrooms/")
async def get_user_classrooms(token: str = Header(None)):
    return await classroom_routes.get_user_classrooms(token)


@app.post("/get_user_enrolled/")
async def get_user_enrolled(token: str = Header(None)):
    return await classroom_routes.get_user_enrolled(token)


@app.post("/get_classroom_details/")
async def get_classroom_details(classroom: classroom_schemas.ClassroomUidSchema, token: str = Header(None)):
    return await classroom_routes.get_classroom_details(classroom.classroom_uid, token)


@app.post('/enroll/')
async def course_enroll(classroom: classroom_schemas.ClassroomUidSchema, token: str = Header(None)):
    return await classroom_routes.course_enroll(token, classroom.classroom_uid)