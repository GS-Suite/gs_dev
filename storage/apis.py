from typing import Optional

from fastapi.datastructures import UploadFile
from fastapi.params import File
from tokens.controllers import token_validation
from storage import routes as storage_routes
from fastapi.param_functions import Depends
from fastapi import APIRouter, Body


router = APIRouter()

@router.post("/create_folder/")
async def create_storage_folder(
    classroom_uid: str = Body(..., embed = True), 
    folder_name: str = Body(..., embed = True), 
    path: str = Body(..., embed = True), 
    token: dict = Depends(token_validation)):
    return await storage_routes.create_folder(classroom_uid, folder_name, path, token)


@router.post("/upload_file/")
async def upload_file(
    classroom_uid: str = Body(..., embed = True),
    path: str = Body(..., embed = True),    
    token: dict = Depends(token_validation),
    file: Optional[UploadFile] = File(None)):
    return await storage_routes.upload_file(token, classroom_uid, path, file)


@router.post("/get_files_and_folders/")
async def get_storage_files_and_folders(
    classroom_uid: str = Body(..., embed = True),
    path: str = Body(..., embed = True), 
    token: dict = Depends(token_validation)):
    return await storage_routes.get_files_and_folders(classroom_uid, path, token)


@router.post("/get_file_download_link/")
async def get_file_download_link(
    classroom_uid: str = Body(..., embed = True),
    path: str = Body(..., embed = True), 
    token: dict = Depends(token_validation)):
    return await storage_routes.get_file_download_link(classroom_uid, path, token)


@router.post("/delete_folder/")
async def delete_storage_folder(
    classroom_uid: str = Body(..., embed = True),
    path: str = Body(..., embed = True), 
    token: dict = Depends(token_validation)):
    return await storage_routes.delete_file(classroom_uid, path, token)
