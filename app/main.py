from random import random
from fastapi import FastAPI, Path, Response, HTTPException
from fastapi.responses import JSONResponse, PlainTextResponse, HTMLResponse

app = FastAPI()


class UnauthHTTPException(HTTPException):
    def __init__(self) -> None:
        super().__init__(401, "Не авторизиован")


@app.get("/posts/{post_id}")
def get_post(post_id: int):
    return {"id": post_id}
