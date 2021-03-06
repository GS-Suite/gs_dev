from pydantic import BaseModel, Field


class TakeAttendance(BaseModel):
    classroom_uid: str = Field(...)

    class Config:
        orm_mode = True

