from typing import Annotated

from fastapi import Depends


class TaskRepository():
    def get_by_id(self, task_id: int):
        if task_id > 100:
            raise ValueError("Больше 100")
        return task_id


def get_task_repository():
    return TaskRepository()


TaskRepositoryDeps = Annotated[
    TaskRepository,
    Depends(get_task_repository)
]
