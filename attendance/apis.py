from attendance import schemas as attendance_schemas
from attendance import routes as attendance_routes
from tokens.controllers import token_validation
from fastapi.param_functions import Depends
from fastapi import APIRouter, Body
from typing import Optional


''' TEACHER API '''
ATTENDANCE_DEFAULT_TOKEN_TIMEOUT = 30 * 60


router = APIRouter()

@router.post('/take_attendance/', tags = ["attendance_teacher"])
async def take_attendance(classroom_uid: str = Body(...), timeout_minutes: Optional[int] = Body(30), token: dict = Depends(token_validation)):
    if timeout_minutes == "" or not timeout_minutes:
        timeout_minutes = ATTENDANCE_DEFAULT_TOKEN_TIMEOUT
    else:
        timeout_minutes = timeout_minutes * 60
    return await attendance_routes.take_attendance(token = token, classroom_uid=classroom_uid, timeout = timeout_minutes)


@router.post('/stop_attendance/', tags = ["attendance_teacher"])
async def stop_attendance(classroom_uid: str = Body(...), attendance_token: str = Body(...), token: dict = Depends(token_validation)):
    return await attendance_routes.stop_attendance(token=token, classroom_uid=classroom_uid, attendance_token=attendance_token)


@router.post('/delete_attendance/', tags = ["attendance_teacher"])
async def delete_attendance(classroom_uid: str = Body(...), attendance_token: str = Body(...), token: dict = Depends(token_validation)):
    return await attendance_routes.delete_attendance(token=token, classroom_uid=classroom_uid.classroom_uid, attendance_token=attendance_token)


@router.post("/view_classroom_attendance/", tags = ["attendance_teacher"])
async def view_classroom_attendance(classroom_uid: str = Body(..., embed=True), token: dict = Depends(token_validation)):
    return await attendance_routes.view_classroom_attendance(token = token, classroom_uid = classroom_uid)

''' Student APIs '''

@router.post('/give_attendance/', tags = ["attendance_student"])
async def give_attendance(classroom_uid: str = Body(...), attendance_token: str = Body(...), token: dict = Depends(token_validation)):
    return await attendance_routes.give_attendance(token=token, classroom_uid=classroom_uid, attendance_token=attendance_token)

''' Common APIs '''

@router.post("/view_student_attendance", tags = ["attendance_teacher", "attendance_student"])
async def view_student_attendance(classroom_uid: str = Body(..., embed=True), token: dict = Depends(token_validation)):
    return await attendance_routes.view_student_attendance(token = token, classroom_uid = classroom_uid)