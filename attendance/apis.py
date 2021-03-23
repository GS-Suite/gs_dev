from fastapi import Response, Header
from attendance import schemas as attendance_schemas
from attendance import routes as attendance_routes
from main import app


''' TEACHER API '''


@app.post('/take_attendance/')
async def take_attendance(classroom_uid: attendance_schemas.TakeAttendance, token: str = Header(None)):
    return await attendance_routes.take_attendance(token=token, classroom_id=classroom_uid)

@app.post('/stop_attendance/')
async def stop_attendance(classroom_uid: attendance_schemas.TakeAttendance, token:str = Header(None)):
    return await attendance_routes.stop_attendance(token=token, classroom_id=classroom_uid)


''' Student API '''

@app.post('/give_attendance/')
async def give_attendance(classroom_uid: attendance_schemas.TakeAttendance, attendance_token: str, token:str = Header(None)):
    return await attendance_routes.give_attendance(token=token, classroom_uid=classroom_uid, attendance_token=attendance_token)

