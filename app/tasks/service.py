
from typing import Annotated

from fastapi import Depends

from .repository import TaskRepositoryDeps, TaskRepository


def get_task_service(repo: TaskRepositoryDeps):
    return TaskService(repo)


class TaskService:
    def __init__(self, repo: TaskRepository):
        self.repo = repo

    def get(self, project_id: int):
        return self.repo.get_by_id(project_id)


TaskServiceDeps = Annotated[
    TaskService,
    Depends(get_task_service)
]
