from fastapi import Response, Header
from attendance import schemas as attendance_schemas
from attendance import routes as attendance_routes
from main import app


@app.post('/take_attendance/')
async def take_attendance(token: str = Header(None), classroom_uid: attendance_schemas.TakeAttendance):
    return await attendance_routes.take_attendance(token=token, classroom_uid=classroom_uid)
