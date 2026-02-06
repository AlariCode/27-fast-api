import logging
from fastapi import APIRouter, Depends, HTTPException

from .service import TaskServiceDeps

from .schema import TaskGetResponse, TaskPath


router = APIRouter(prefix="/v1/tasks", tags=["Tasks"])
logger = logging.getLogger(__name__)


@router.get(
    "/{task_id}",
    response_model=TaskGetResponse,
    description="""
    Получает задачу по его id, если задачи нет, возвращает ошибку.
            """,
)
def get_task(
    service: TaskServiceDeps,
    path: TaskPath = Depends(),
):
    res = service.get(path.task_id)
    if not res:
        raise HTTPException(500, "Ошибка чтения ID")
    logger.info("ID: %s", res, extra={"user_id": 1})
    return TaskGetResponse(id=res)
