from fastapi import Response, BackgroundTasks, Header
from tokens import schemas as token_schemas
from tokens import routes as token_routes
from main import app


@app.post("/validate_token/")
async def validate_token(token: token_schemas.TokenValidate, response: Response):
    return await token_routes.validate_token(token, response)


@app.post("/refresh_token/")
async def refresh_token(token: token_schemas.TokenValidate, response: Response):
    return await token_routes.refresh_token(token, response)
