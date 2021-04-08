from classrooms import schemas as classroom_schemas
from classrooms import routes as classroom_routes
from tokens.controllers import token_validation
from fastapi.param_functions import Depends
from fastapi import APIRouter, Body


router = APIRouter()

''' TEACHER APIS '''

@router.post("/create_classroom/", tags = ["classrooms : teacher"])
async def create_classroom(classroom: classroom_schemas.CreateClassroomSchema, token: dict = Depends(token_validation)):
    return await classroom_routes.create_classroom(classroom, token)


@router.post("/get_user_classrooms/", tags = ["classrooms : teacher"])
async def get_user_classrooms(token: dict = Depends(token_validation)):
    return await classroom_routes.get_user_classrooms(token)


@router.post("/get_classroom_details/", tags = ["classrooms : teacher"])
async def get_classroom_details(classroom: classroom_schemas.ClassroomUidSchema, token: dict = Depends(token_validation)):
    return await classroom_routes.get_classroom_details(classroom.classroom_uid, token)


@router.post("/generate_classroom_join_code", tags = ["classrooms : teacher"])
async def generate_classroom_entry_code(classroom_uid: classroom_schemas.ClassroomUidSchema, token: dict = Depends(token_validation)):
    return await classroom_routes.generate_classroom_entry_code(classroom_uid.classroom_uid, token)

@router.post('/unenroll_user/', tags = ['classrooms : teacher'])
async def unenroll_user(classroom_uid: str = Body(...), user_id: str = Body(...), token: dict = Depends(token_validation)):
    return await classroom_routes.unenroll_user(classroom_uid = classroom_uid, user_id = user_id, token = token)


@router.post("/delete_classroom/", tags = ["classroom : teacher"])
async def delete_classroom(classroom_uid: str = Body(...), token: dict = Depends(token_validation)):
    return await classroom_routes.delete_classroom(classroom_uid = classroom_uid, token = token)


''' STUDENT APIS '''

@router.post('/enroll/', tags = ["classrooms : student"])
async def course_enroll(entry_code: str = Body(..., embed=True), token: dict = Depends(token_validation)):
    return await classroom_routes.course_enroll(token, entry_code)


@router.post('/unenroll/', tags = ['classrooms : student'])
async def unenroll(classroom_uid: str = Body(..., embed=True), token: dict = Depends(token_validation)):
    return await classroom_routes.unenroll(classroom_uid = classroom_uid, token = token)


@router.post("/get_user_enrolled/", tags = ["classrooms : student"])
async def get_user_enrolled(token: dict = Depends(token_validation)):
    return await classroom_routes.get_user_enrolled(token)


''' COMMON APIS '''

@router.post("/get_classroom_enrolled/", tags = ["classrooms : data"])
async def get_classroom_enrolled(classroom_uid: classroom_schemas.ClassroomUidSchema, token: dict = Depends(token_validation)):
    return await classroom_routes.get_classroom_enrolled(classroom_uid.classroom_uid, token)


@router.post("/get_classroom_uid_from_entry_code/", tags = ["classrooms : data"])
async def get_classroom_uid(entry_code: str = Body(..., embed=True), token: dict = Depends(token_validation)):
    return await classroom_routes.get_classroom_uid_by_entry_code(entry_code, token)


@router.post('/get_classroom_owner_from_class_uid/', tags = ["classrooms : data"])
async def get_classroom_owner_from_class_uid(classroom_uid: str = Body(..., embed=True), token: dict = Depends(token_validation)):
    return await classroom_routes.get_classroom_owner_from_class_uid(classroom_uid, token)
