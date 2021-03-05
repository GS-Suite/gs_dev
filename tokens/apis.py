from fastapi import Header
from tokens import routes as token_routes
from main import app


@app.post("/validate_token/")
async def validate_token(token: str = Header(None)):
    return await token_routes.validate_token(token)

'''
@app.post("/refresh_token/")
async def refresh_token(token: str = Header(None)):
    return await token_routes.refresh_token(token)
'''