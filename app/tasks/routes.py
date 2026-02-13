import logging
from fastapi import APIRouter, Depends, HTTPException

from .service import TaskServiceDeps

from .schema import TaskCreateRequest, TaskCreateResponse, TaskGetResponse, TaskPath


router = APIRouter(prefix="/v1/tasks", tags=["Tasks"])
logger = logging.getLogger(__name__)


@router.get(
    "/{task_id}",
    response_model=TaskGetResponse,
    description="""
    Получает задачу по его id, если задачи нет, возвращает ошибку.
            """,
)
async def get_task(
    service: TaskServiceDeps,
    path: TaskPath = Depends(),
):
    res = await service.get(path.task_id)
    return TaskGetResponse(id=res.id, title=res.title, description=res.description, is_completed=res.is_completed, project_id=res.project_id)


@router.post("/", response_model=TaskCreateResponse, status_code=201)
async def create_task(service: TaskServiceDeps, data: TaskCreateRequest):
    res = await service.create(data)
    return TaskCreateResponse(id=res.id, title=res.title, description=res.description, is_completed=res.is_completed, project_id=res.project_id)
