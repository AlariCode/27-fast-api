from enum import Enum
from random import random
from fastapi import Body, FastAPI, Path, Query, Request, Response, HTTPException
from fastapi.responses import JSONResponse, PlainTextResponse, HTMLResponse

app = FastAPI()


class SortOrder(str, Enum):
    asc = "asc"
    desc = "desc"


class UnauthHTTPException(HTTPException):
    def __init__(self) -> None:
        super().__init__(401, "Не авторизиован")


@app.get("/posts/{post_id}")
def get_post(post_id: int):
    return {"id": post_id}


@app.get("/posts")
def get_posts(
    limit: int = 10,
    offset: int = Query(0, ge=0),
    tags: list[str] = Query([]),
    order: SortOrder = SortOrder.asc
):
    return {"limit": limit, "offset": offset, "tags": tags, "order": order}


@app.post("/posts")
async def create_post(
    request: Request
    # body: dict = Body()
):
    data = await request.json()
    return data
