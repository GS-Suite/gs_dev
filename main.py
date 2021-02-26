import os, sys
from dotenv import load_dotenv
load_dotenv()

from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from fastapi import FastAPI
from models import Base, engine
import uvicorn

Base.metadata.create_all(bind = engine)

app = FastAPI()

origins = [
    "*",
    "127.0.0.1",
    "localhost",
    "127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)


@app.get("/", include_in_schema = False)
async def home_to_doc():
    return RedirectResponse("/docs")


from user.apis import *
from tokens.apis import *
from classrooms.apis import *


if __name__ == "__main__":
    uvicorn.run(
        "main:app", host="127.0.0.1", port=8000
    )
