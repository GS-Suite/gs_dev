from pydantic import Field
from classrooms import schemas as classroom_schemas
from classrooms import routes as classroom_routes
from fastapi import Response, Header
from main import app


''' TEACHER APIS '''

@app.post("/create_classroom/")
async def create_classroom(classroom: classroom_schemas.CreateClassroomSchema, token: str = Header(None)):
    return await classroom_routes.create_classroom(classroom, token)


@app.post("/get_user_classrooms/")
async def get_user_classrooms(token: str = Header(None)):
    return await classroom_routes.get_user_classrooms(token)


@app.post("/get_classroom_details/")
async def get_classroom_details(classroom: classroom_schemas.ClassroomUidSchema, token: str = Header(None)):
    return await classroom_routes.get_classroom_details(classroom.classroom_uid, token)


@app.post("/generate_classroom_join_code")
async def generate_classroom_entry_code(classroom_uid: classroom_schemas.ClassroomUidSchema, token: str = Header(None)):
    return await classroom_routes.generate_classroom_entry_code(classroom_uid.classroom_uid, token)


''' STUDENT APIS '''

@app.post('/enroll/')
async def course_enroll(classroom: classroom_schemas.UserClassroomEnroll, token: str = Header(None)):
    return await classroom_routes.course_enroll(token, classroom.classroom_uid, classroom.entry_code)


@app.post("/get_user_enrolled/")
async def get_user_enrolled(token: str = Header(None)):
    return await classroom_routes.get_user_enrolled(token)


@app.post("/get_classroom_enrolled/")
async def get_classroom_enrolled(classroom_uid: classroom_schemas.ClassroomUidSchema, token: str = Header(None)):
    return await classroom_routes.get_classroom_enrolled(classroom_uid.classroom_uid, token)


@app.post("/get_classroom_uid/")
async def get_classroom_uid(entry_code: str, token: str = Header(None)):
    return await classroom_routes.get_classroom_uid_by_entry_code(entry_code, token)
