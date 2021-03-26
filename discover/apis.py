from tokens.controllers import token_validation
from discover import routes as discover_routes
from fastapi.param_functions import Depends
from fastapi import APIRouter
from typing import Optional


router = APIRouter()

@router.post("/search/")
async def search(query: str, filter: Optional[str] = None, token: dict = Depends(token_validation)):
    return await discover_routes.search(token, query, filter)