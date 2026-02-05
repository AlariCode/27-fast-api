import logging
from fastapi import APIRouter, Depends

from .service import TaskServiceDeps

from .schema import TaskGetResponse, TaskPath


router = APIRouter(prefix="/v1/tasks", tags=["Tasks"])
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.propagate = False

handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(
    "[TASKS] %(levelname)s:%(name)s:%(message)s"
))
logger.addHandler(handler)


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
    # logger.warning(f"ID: {res}")
    logger.warning("ID: %s", res)
    logger.info("ID: %s", res)
    return TaskGetResponse(id=res)
