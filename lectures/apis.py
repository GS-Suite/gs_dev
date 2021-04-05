from fastapi.param_functions import Body
from tokens.controllers import token_validation
from lectures import schemas as lecture_schemas
from lectures import routes as lecture_routes
from fastapi import APIRouter, Depends


router = APIRouter()


@router.post("/get_classroom_lecture_videos/")
async def get_classroom_lecture_videos(classroom_uid: str = Body(..., embed = True), token: dict = Depends(token_validation)):
    return await lecture_routes.get_classroom_lecture_videos(token, classroom_uid)


@router.post("/get_classroom_lecture_playlists/")
async def get_classroom_lecture_playlists(classroom_uid: str = Body(..., embed = True), token: dict = Depends(token_validation)):
    return await lecture_routes.get_classroom_lecture_playlists(token, classroom_uid)


@router.post("/get_classroom_playlist_videos/")
async def get_classroom_playlist_videos(classroom_uid: str = Body(..., embed = True), playlist_name: str = Body(..., embed = True), token: dict = Depends(token_validation)):
    return await lecture_routes.get_classroom_playlist_videos(token, classroom_uid, playlist_name)


''' TEACHER APIS '''

@router.post("/add_lecture/")
async def add_lecture(lecture: lecture_schemas.CreateLectureSchema, classroom_uid: str = Body(..., embed = True), token: dict = Depends(token_validation)):
    return await lecture_routes.add_lecture(token, classroom_uid, lecture)


@router.post("/edit_lecture/")
async def add_lecture(lecture: lecture_schemas.CreateLectureSchema, lecture_uid: str = Body(..., embed = True), classroom_uid: str = Body(..., embed = True), token: dict = Depends(token_validation)):
    return await lecture_routes.edit_lecture(token, classroom_uid, lecture_uid, lecture)


@router.post("/delete_lecture/")
async def delete_lecture(classroom_uid: str = Body(..., embed = True), lecture_uid: str = Body(..., embed = True), token: dict = Depends(token_validation)):
    return await lecture_routes.delete_lecture(token, classroom_uid, lecture_uid)