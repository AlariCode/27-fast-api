# GET Query rnd_from и rnd_to, возвращающий случайный int
# в этом диапазоне

from fastapi import APIRouter

from .schema import ProjectCreateRequest, ProjectCreateResponse


router = APIRouter(
    prefix="/projects"
)


@router.post("/", response_model=ProjectCreateResponse)
async def create_project(data: ProjectCreateRequest):
    # создали проект
    # return {**data.model_dump(), "id": 1}
    return ProjectCreateResponse(
        id=1,
        name=data.name
    )
