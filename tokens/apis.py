from user import routes
from tokens import routes as token_routes
from fastapi import Header, APIRouter


router = APIRouter()

@router.post("/validate_token/", tags = ["tokens"])
async def validate_token(token: str = Header(None)):
    return await token_routes.validate_token(token)


@router.post("/refresh_token/", tags = ["tokens"])
async def refresh_token(token: str = Header(None)):
    return await token_routes.refresh_token(token)
