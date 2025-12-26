from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/")
def root(response: Response):
    if False:
        response.status_code = 400
    response.status_code = 204
    return {"Score": 10}
