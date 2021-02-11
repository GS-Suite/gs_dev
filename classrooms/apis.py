from classrooms import schemas as classroom_schemas
from classrooms import routes as classroom_routes
from fastapi import Response, Header
from main import app


@app.post("/create_classroom/")
async def create_classroom(classroom: classroom_schemas.CreateClassroomSchema, response: Response, token: str = Header(None)):
    return await classroom_routes.create_classroom(classroom, response, token)

@app.post("/get_classrooms/")
async def get_classrooms(response: Response, token: str = Header(None)):
    return await classroom_routes.get_classrooms(token, response)
