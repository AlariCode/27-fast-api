from random import random
from fastapi import FastAPI, Response, HTTPException

app = FastAPI()


class UnauthHTTPException(HTTPException):
    def __init__(self) -> None:
        super().__init__(401, "Не авторизиован")


@app.get("/")
def root(response: Response):
    num = random()
    if num > 0.5:
        raise UnauthHTTPException()
    response.status_code = 201
    return {"Score": num}
