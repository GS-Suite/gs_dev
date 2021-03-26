from tokens.controllers import token_validation
from fastapi.param_functions import Depends
from tokens import routes as token_routes
from fastapi import APIRouter


router = APIRouter()

@router.post("/validate_token/")
async def validate_token(token: dict = Depends(token_validation)):
    return await token_routes.validate_token(token)


@router.post("/refresh_token/")
async def refresh_token(token: dict = Depends(token_validation)):
    return await token_routes.refresh_token(token)
