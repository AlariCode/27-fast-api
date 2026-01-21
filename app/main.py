from fastapi import FastAPI
from projects.routes import router as project_router

app = FastAPI()

app.include_router(project_router)
