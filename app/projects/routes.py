# GET Query rnd_from и rnd_to, возвращающий случайный int
# в этом диапазоне

from fastapi import APIRouter, Depends

from .schema import (
    ProjectCreateRequest,
    ProjectCreateResponse,
    ProjectPath,
    ProjectUpdateRequest,
    ProjectUpdateResponse,
    ProjectGetResponse,
)


router = APIRouter(prefix="/v1/projects", tags=["Projects"])


@router.get("/{project_id}", response_model=ProjectGetResponse, description="""
    Получает проект по его id, если проекта нет, возвращает ошибку.
            """)
def get_project(path: ProjectPath = Depends()):
    return ProjectGetResponse(id=path.project_id)


@router.patch("/{project_id}", response_model=ProjectUpdateResponse)
def update_project(data: ProjectUpdateRequest, path: ProjectPath = Depends()):
    # работы с БД
    return ProjectUpdateResponse(
        id=path.project_id, key="123", name=data.name, description=data.description
    )


@router.post("/", response_model=ProjectCreateResponse, status_code=201)
async def create_project(data: ProjectCreateRequest):
    return ProjectCreateResponse(id=1, name=data.name)
