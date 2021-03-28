from tokens.controllers import token_validation
from discover import routes as discover_routes
from fastapi.param_functions import Depends
from fastapi import APIRouter, Body
from typing import Optional


router = APIRouter()

@router.post("/search/")
async def search(query: str = Body(...), filter: Optional[str] = Body(None), token: dict = Depends(token_validation)):
    return await discover_routes.search(token, query, filter)