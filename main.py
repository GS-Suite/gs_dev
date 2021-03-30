from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from db_setup.pg_setup import Base, engine
from fastapi import FastAPI
import uvicorn

from attendance.apis import router as attendance_router
from classrooms.apis import router as classroom_router
from discover.apis import router as discover_router
from lectures.apis import router as lecture_router
from tokens.apis import router as token_router
from forum.apis import router as forum_router
from user.apis import router as user_router


Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "*",
    "http://localhost",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", include_in_schema = False)
async def home_to_doc():
    return RedirectResponse("/docs")


app.include_router(user_router,         tags = ["users"])
app.include_router(token_router,        tags = ["tokens"])
app.include_router(classroom_router,    tags = ["classrooms"])
app.include_router(lecture_router,    tags = ["lectures"])
app.include_router(attendance_router)
app.include_router(forum_router,        tags = ["forums"])
app.include_router(discover_router,     tags = ["discover"])


if __name__ == "__main__":
    uvicorn.run(
        "main:app", host="127.0.0.1", port=8000
    )
