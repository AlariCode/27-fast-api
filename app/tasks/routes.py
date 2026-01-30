from fastapi import APIRouter, Depends

from app.core.settings import SettingsDeps

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
    settings: SettingsDeps,
    path: TaskPath = Depends(),
):
    res = service.get(path.task_id)
    print(settings.db.url)
    return TaskGetResponse(id=res)
