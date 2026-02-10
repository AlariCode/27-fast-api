import logging
from fastapi import APIRouter, Depends, HTTPException

from app.core.db import DbSessionDeps, check_db

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
async def get_task(
    service: TaskServiceDeps,
    db_session: DbSessionDeps,
    path: TaskPath = Depends(),
):
    data = await check_db(db_session)
    logger.info("DB check: %s", data)
    res = service.get(path.task_id)
    if not res:
        raise HTTPException(500, "Ошибка чтения ID")
    logger.info("ID: %s", res, extra={"user_id": 1})
    return TaskGetResponse(id=res)
