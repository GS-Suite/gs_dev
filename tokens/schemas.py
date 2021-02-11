from pydantic import BaseModel, Field, validator


class TokenValidate(BaseModel):
    token: str = Field(...)

    class Config:
        orm_mode = True

    @validator('token')
    def validate_token(cls, v):
        assert len(v) == 64, "'token' must be of length 64"
        assert len(v) >= 5, 'Username must contain 5 characters or more'
        return v