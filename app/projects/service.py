from typing import Annotated

from fastapi import Depends

from .repository import ProjectRepository, ProjectRepositoryDeps


def get_project_service(repo: ProjectRepositoryDeps):
    return ProjectService(repo)


class ProjectService:
    def __init__(self, repo: ProjectRepository):
        self.repo = repo

    def get_project(self, project_id: int):
        return self.repo.get_by_id(project_id)


ProjectServiceDeps = Annotated[
    ProjectService,
    Depends(get_project_service)
]
