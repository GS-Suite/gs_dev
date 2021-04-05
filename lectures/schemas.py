from datetime import datetime
from pydantic import BaseModel, Field


class CreateLectureSchema(BaseModel):
    lecture_name: str = Field(...)
    lecture_link: str = Field(...)
    playlists: list = []
    lecture_description: str = Field(...)
    lecture_resources: str = Field(...)

    class Config:
        orm_mode = True

class UpdateLectureSchema(BaseModel):
    lecture_uid: str = Field(...)
    lecture_name: str = Field(...)
    lecture_link: str = Field(...)
    sections: list = []
    lecture_description: str = Field(...)
    lecture_resources: str = Field(...)

    class Config:
        orm_mode = True