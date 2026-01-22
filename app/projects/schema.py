from fastapi import HTTPException
from pydantic import BaseModel, Field, field_validator


class ProjectPath(BaseModel):
    project_id: int = Field(gt=0)


class ProjectCreateRequest(BaseModel):
    key: str
    name: str
    description: str | None = None

    model_config = {
        "extra": "forbid"
    }

    @field_validator("key")
    @classmethod
    def key_not_empty(cls, value):
        if not value.strip():
            raise HTTPException(400, "key must be valid string")
        return value


class ProjectCreateResponse(BaseModel):
    id: int
    name: str
