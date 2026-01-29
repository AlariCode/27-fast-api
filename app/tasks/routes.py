from fastapi import APIRouter, Depends

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
    path: TaskPath = Depends(),
):
    return TaskGetResponse(id=path.task_id)
