from fastapi import FastAPI
from projects.routes import router as project_router

app = FastAPI(
    title="KanbanBoard API",
    description="API для работы приложения аналога Jira",
    version="0.1.1",
    openapi_tags=[
        {
            "name": "Projects",
            "description": "Управление проектам"
        }
    ]
)

app.include_router(project_router)
