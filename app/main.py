from fastapi import FastAPI
from app.core.settings import Settings
from app.projects.routes import router as project_router
from app.tasks.routes import router as task_router
from app.users.routes import router as user_router


def create_app() -> FastAPI:
    settings = Settings()  # type: ignore[call-arg]
    new_app = FastAPI(
        title=settings.app.name,
        description="API для работы приложения аналога Jira",
        version="0.1.1",
        openapi_tags=[
            {"name": "Projects", "description": "Управление проектам"},
            {"name": "Tasks", "description": "Управление задачами"},
            {"name": "Auth", "description": "Авторизация пользователя"},
        ],
    )

    new_app.state.settings = settings

    new_app.include_router(project_router)
    new_app.include_router(task_router)
    new_app.include_router(user_router)
    return new_app


app = create_app()
