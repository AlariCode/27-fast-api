from fastapi import APIRouter, Depends

from .service import TaskServiceDeps

from .schema import TaskGetResponse, TaskPath


router = APIRouter(prefix="/v1/tasks", tags=["Tasks"])


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
    return TaskGetResponse(id=res)
