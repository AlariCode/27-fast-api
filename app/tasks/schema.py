from pydantic import BaseModel, Field


class TaskPath(BaseModel):
    task_id: int = Field(gt=0)


class TaskGetResponse(BaseModel):
    id: int
    title: str
    description: str | None = None
    project_id: int
    is_completed: bool


class TaskCreateRequest(BaseModel):
    title: str
    description: str | None = None
    project_id: int

    model_config = {"extra": "forbid"}


class TaskCreateResponse(BaseModel):
    id: int
    title: str
    description: str | None = None
    project_id: int
    is_completed: bool
