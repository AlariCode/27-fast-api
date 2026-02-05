import logging
import sys
from fastapi import FastAPI
from app.core.settings import Settings
from app.projects.routes import router as project_router
from app.tasks.routes import router as task_router


def create_app() -> FastAPI:
    settings = Settings()  # type: ignore[call-arg]
    new_app = FastAPI(
        title=settings.app.name,
        description="API для работы приложения аналога Jira",
        version="0.1.1",
        openapi_tags=[
            {"name": "Projects", "description": "Управление проектам"},
            {"name": "Tasks", "description": "Управление задачами"},
        ],
    )

    new_app.state.settings = settings

    new_app.include_router(project_router)
    new_app.include_router(task_router)
    return new_app


app = create_app()
