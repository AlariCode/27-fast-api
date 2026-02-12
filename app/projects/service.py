from typing import Annotated

from fastapi import Depends

from app.projects.model import Project
from app.projects.schema import ProjectCreateRequest

from .repository import ProjectRepository, ProjectRepositoryDeps


def get_project_service(repo: ProjectRepositoryDeps):
    return ProjectService(repo)


class ProjectService:
    def __init__(self, repo: ProjectRepository):
        self.repo = repo

    async def get(self, project_id: int):
        return await self.repo.get_by_id(project_id)

    async def create(self, data: ProjectCreateRequest):
        project = Project(
            key=data.key,
            name=data.name,
            description=data.description
        )
        return await self.repo.create(project)


ProjectServiceDeps = Annotated[
    ProjectService,
    Depends(get_project_service)
]
