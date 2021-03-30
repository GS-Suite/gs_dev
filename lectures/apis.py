from tokens.controllers import token_validation
from lectures import routes as lecture_routes
from fastapi.param_functions import Depends
from fastapi import APIRouter
from pydantic import Field


router = APIRouter()

''' TEACHER APIS '''

@router.post("/add_section/")
async def add_section(classroom_uid: str = Field(...), section_name: str = Field(...), token: dict = Depends(token_validation)):
    return await lecture_routes.add_section(token, classroom_uid, section_name)