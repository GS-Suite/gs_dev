from discover import routes as discover_routes
from fastapi import Header, APIRouter
from typing import Optional


router = APIRouter()

@router.post("/search/", tags = ["discover"])
async def search(query: str, filter: Optional[str] = None, token: str = Header(None)):
    return await discover_routes.search(token, query, filter)