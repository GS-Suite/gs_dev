from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from db_setup.pg_setup import Base, engine
from fastapi import FastAPI
import uvicorn

from announcements.apis import router as announcement_router
from attendance.apis import router as attendance_router
from classrooms.apis import router as classroom_router
from discover.apis import router as discover_router
from lectures.apis import router as lecture_router
from storage.apis import router as storage_router
from tokens.apis import router as token_router
from forum.apis import router as forum_router
from user.apis import router as user_router

from user import controllers as user_controllers
from classrooms import controllers as classroom_controllers

from dotenv import load_dotenv
load_dotenv()

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://127.0.0.1",
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://gs-suite.herokuapp.com",
    "https://gs-suite.herokuapp.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/", include_in_schema = False)
async def home_to_doc():
    return RedirectResponse("/docs")


app.include_router(user_router,         tags = [])
app.include_router(token_router,        tags = ["tokens"])
app.include_router(classroom_router,    tags = [])
app.include_router(lecture_router,      tags = ["lectures"])
app.include_router(attendance_router,       tags = [])
app.include_router(storage_router,              tags = ["resources"],       prefix="/resources")
app.include_router(forum_router,                tags = ["forums"])
app.include_router(announcement_router,         tags = ["announcement"])
app.include_router(discover_router,             tags = ["discover"])


@app.get("/public/get_total_counts/", include_in_schema = False)
async def get_total_counts():
    user_count = await user_controllers.get_total_user_count()
    classroom_count = await classroom_controllers.get_total_classroom_count()
    return {
        "user_count": user_count,
        "classroom_count": classroom_count
    }


if __name__ == "__main__":
    uvicorn.run(
        "main:app", host="127.0.0.1", port=8000
    )
