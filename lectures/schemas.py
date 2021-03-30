from typing import Optional
from pydantic import BaseModel, Field, validator
import re


class CreateLectureSchema(BaseModel):
    lecture_name: str = Field(...)
    lecture_link: str = Field(...)
    sections: list = []
    lecture_description: str = Field(...)
    lecture_resources: str = Field(...)

    class Config:
        orm_mode = True