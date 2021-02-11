from pydantic import BaseModel, Field, validator
import re

class CreateClassroomSchema(BaseModel):
    class_name: str = Field(...)

    class Config:
        orm_mode = True

    @validator('class_name')
    def class_name_check(cls, v):
        assert re.match("^[A-Za-z0-9_ ]*$", v), 'Class name must contain alphabets, numbers, spaces and underscores only'
        assert len(v) >= 5, 'Class name must contain 5 characters or more'
        return v