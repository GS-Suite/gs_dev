from fastapi.param_functions import Body
from tokens.controllers import token_validation
from lectures import schemas as lecture_schemas
from lectures import routes as lecture_routes
from fastapi import APIRouter, Depends


router = APIRouter()

''' TEACHER APIS '''

@router.post("/get_classroom_lectures/")
async def get_classroom_lectures(classroom_uid: str = Body(..., embed = True), token: dict = Depends(token_validation)):
    return await lecture_routes.get_classroom_lectures(token, classroom_uid)


@router.post("/add_lecture/")
async def add_lecture(lecture: lecture_schemas.CreateLectureSchema, classroom_uid: str = Body(..., embed = True), token: dict = Depends(token_validation)):
    return await lecture_routes.add_lecture(token, classroom_uid, lecture)