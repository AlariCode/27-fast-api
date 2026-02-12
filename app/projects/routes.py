from fastapi import APIRouter, Depends, HTTPException

from .service import ProjectServiceDeps

from .schema import (
    ProjectCreateRequest,
    ProjectCreateResponse,
    ProjectPath,
    ProjectUpdateRequest,
    ProjectUpdateResponse,
    ProjectGetResponse,
)


router = APIRouter(prefix="/v1/projects", tags=["Projects"])


@router.get(
    "/{project_id}",
    response_model=ProjectGetResponse,
    description="""
    Получает проект по его id, если проекта нет, возвращает ошибку.
            """,
)
async def get_project(
    service: ProjectServiceDeps,
    path: ProjectPath = Depends(),
):
    project = await service.get(path.project_id)
    if project is None:
        raise HTTPException(404, "Project not found")
    return ProjectGetResponse(
        id=project.id,
        key=project.key,
        name=project.name,
        description=project.description
    )


@router.patch("/{project_id}", response_model=ProjectUpdateResponse)
async def update_project(data: ProjectUpdateRequest, service: ProjectServiceDeps, path: ProjectPath = Depends()):
    project = await service.update(path.project_id, data)
    if project is None:
        raise HTTPException(404, "Project not found")
    return ProjectUpdateResponse(
        id=project.id, key=project.key, name=project.name, description=project.description
    )


@router.post("/", response_model=ProjectCreateResponse, status_code=201)
async def create_project(service: ProjectServiceDeps, data: ProjectCreateRequest):
    res = await service.create(data)
    return ProjectCreateResponse(id=res.id, name=res.name)
