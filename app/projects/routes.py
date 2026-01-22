# GET Query rnd_from и rnd_to, возвращающий случайный int
# в этом диапазоне

from fastapi import APIRouter, Depends

from .schema import ProjectCreateRequest, ProjectCreateResponse, ProjectPath


router = APIRouter(
    prefix="/projects"
)


@router.get("/{project_id}")
def get_project(
    path: ProjectPath = Depends()
):
    return {"id": path.project_id}


@router.post("/", response_model=ProjectCreateResponse)
async def create_project(data: ProjectCreateRequest):
    # создали проект
    # return {**data.model_dump(), "id": 1}
    print(data)
    return ProjectCreateResponse(
        id=1,
        name=data.name
    )
