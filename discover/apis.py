from typing import Optional
from discover import routes as discover_routes
from pydantic import Field
from fastapi import Header
from main import app


@app.post("/search/")
async def search(query: str, filter: Optional[str] = None, token: str = Header(None)):
    return await discover_routes.search(token, query, filter)