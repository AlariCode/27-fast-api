from typing import Annotated

from fastapi import Depends

from app.core.db import DbSessionDeps
from app.tasks.models import Task


class TaskRepository():
    def __init__(self, session: DbSessionDeps):
        self.session = session

    def get_by_id(self, task_id: int):
        if task_id > 100:
            raise ValueError("Больше 100")
        return task_id

    async def save(self, task: Task):
        self.session.add(task)
        await self.session.commit()
        await self.session.refresh(task)
        return task


def get_task_repository(session: DbSessionDeps):
    return TaskRepository(session)


TaskRepositoryDeps = Annotated[
    TaskRepository,
    Depends(get_task_repository)
]
