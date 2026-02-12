from fastapi import APIRouter, Depends

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
def get_project(
    service: ProjectServiceDeps,
    path: ProjectPath = Depends(),
):
    res = service.get(path.project_id)
    return ProjectGetResponse(id=res)


@router.patch("/{project_id}", response_model=ProjectUpdateResponse)
def update_project(data: ProjectUpdateRequest, path: ProjectPath = Depends()):
    # работы с БД
    return ProjectUpdateResponse(
        id=path.project_id, key="123", name=data.name, description=data.description
    )


@router.post("/", response_model=ProjectCreateResponse, status_code=201)
async def create_project(service: ProjectServiceDeps, data: ProjectCreateRequest):
    res = await service.create(data)
    return ProjectCreateResponse(id=res.id, name=res.name)
