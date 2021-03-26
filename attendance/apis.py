from attendance import schemas as attendance_schemas
from attendance import routes as attendance_routes
from fastapi import Response, Header, APIRouter
from typing import Optional


''' TEACHER API '''
ATTENDANCE_DEFAULT_TOKEN_TIMEOUT = 30 * 60


router = APIRouter()

@router.post('/take_attendance/', tags = ["attendance"])
async def take_attendance(classroom_uid: attendance_schemas.TakeAttendance, timeout_minutes: Optional[int] = 30, token: str = Header(None)):
    if timeout_minutes == "" or not timeout_minutes:
        timeout_minutes = ATTENDANCE_DEFAULT_TOKEN_TIMEOUT
    else:
        timeout_minutes = timeout_minutes * 60
    return await attendance_routes.take_attendance(token = token, classroom_uid=classroom_uid.classroom_uid, timeout = timeout_minutes)


@router.post('/stop_attendance/', tags = ["attendance"])
async def stop_attendance(classroom_uid: attendance_schemas.TakeAttendance, attendance_token: str, token:str = Header(None)):
    return await attendance_routes.stop_attendance(token=token, classroom_uid=classroom_uid.classroom_uid, attendance_token=attendance_token)


@router.post('/delete_attendance/', tags = ["attendance"])
async def delete_attendance(classroom_uid: attendance_schemas.TakeAttendance, attendance_token: str, token:str = Header(None)):
    return await attendance_routes.delete_attendance(token=token, classroom_uid=classroom_uid.classroom_uid, attendance_token=attendance_token)


''' Student API '''

@router.post('/give_attendance/', tags = ["attendance"])
async def give_attendance(classroom_uid: attendance_schemas.TakeAttendance, attendance_token: str, token:str = Header(None)):
    return await attendance_routes.give_attendance(token=token, classroom_uid=classroom_uid, attendance_token=attendance_token)

