from enum import Enum

from fastapi import APIRouter, Query, Request

router = APIRouter(
    prefix="/posts"
)


class SortOrder(str, Enum):
    asc = "asc"
    desc = "desc"


@router.get("/{post_id}")
def get_post(post_id: int):
    return {"id": post_id}


@router.get("/")
def get_posts(
    limit: int = 10,
    offset: int = Query(0, ge=0),
    tags: list[str] = Query([]),
    order: SortOrder = SortOrder.asc
):
    return {"limit": limit, "offset": offset, "tags": tags, "order": order}


@router.post("/")
async def create_post(
    request: Request
    # body: dict = Body()
):
    data = await request.json()
    return data
