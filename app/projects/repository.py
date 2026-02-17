import logging
from typing import Annotated

from fastapi import Depends

from app.core.db import DbSessionDeps
from app.projects.model import Project

logger = logging.getLogger(__name__)


class ProjectRepository:
    def __init__(self, session: DbSessionDeps):
        self.session = session

    async def get_by_id(self, project_id: int):
        return await self.session.get(Project, project_id)

    async def save(self, project: Project):
        self.session.add(project)
        await self.session.commit()
        await self.session.refresh(project)
        return project

    async def delete(self, project: Project):
        await self.session.delete(project)
        await self.session.commit()


def get_project_repository(session: DbSessionDeps):
    return ProjectRepository(session)


ProjectRepositoryDeps = Annotated[ProjectRepository, Depends(get_project_repository)]
