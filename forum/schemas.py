from pydantic import BaseModel, Field


class Forum(BaseModel):
    forum_id: str = Field(...)
    classroom_uid: str = Field(...)

    class Config:
        orm_mode = True