from random import random
from fastapi import FastAPI, Response, HTTPException
from fastapi.responses import JSONResponse, PlainTextResponse, HTMLResponse

app = FastAPI()


class UnauthHTTPException(HTTPException):
    def __init__(self) -> None:
        super().__init__(401, "Не авторизиован")


@app.get("/")
def root():
    num = random()
    return {"score": num}
