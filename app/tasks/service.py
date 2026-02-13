
import logging
from typing import Annotated

from fastapi import Depends, HTTPException

from app.projects.repository import ProjectRepository, ProjectRepositoryDeps
from app.tasks.models import Task
from app.tasks.schema import TaskCreateRequest

from .repository import TaskRepositoryDeps, TaskRepository
logger = logging.getLogger(__name__)


def get_task_service(task_repo: TaskRepositoryDeps, project_repo: ProjectRepositoryDeps):
    return TaskService(task_repo, project_repo)


class TaskService:
    def __init__(self, task_repo: TaskRepository, project_repo: ProjectRepository):
        self.task_repo = task_repo
        self.project_repo = project_repo

    async def get(self, task_id: int):
        task = await self.task_repo.get_by_id(task_id)
        if task is None:
            raise HTTPException(404, "Task not found")
        return task

    async def create(self, data: TaskCreateRequest):
        project = await self.project_repo.get_by_id(data.project_id)
        if project is None:
            raise HTTPException(404, "Project not found")
        task = Task(**data.model_dump(), is_completed=False)
        return await self.task_repo.save(task)


TaskServiceDeps = Annotated[
    TaskService,
    Depends(get_task_service)
]
