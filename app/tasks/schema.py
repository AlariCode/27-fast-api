from pydantic import BaseModel, Field


class TaskPath(BaseModel):
    task_id: int = Field(gt=0)


class TaskGetResponse(BaseModel):
    id: int
