# GET Query rnd_from и rnd_to, возвращающий случайный int
# в этом диапазоне

from fastapi import APIRouter

from .schema import ProjectCreateRequest


router = APIRouter(
    prefix="/projects"
)


@router.post("/")
async def create_project(data: ProjectCreateRequest):
    return data
