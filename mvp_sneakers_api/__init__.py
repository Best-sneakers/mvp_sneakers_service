from logging import config as logging_config

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from mvp_sneakers_api.api.v1 import classificator
from mvp_sneakers_api.settings.logger import LOGGING
from mvp_sneakers_api.settings.settings import settings

app = FastAPI(
    title=settings.project.project_name,
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
)


@app.get("/")
async def root():
    return {"message": "Server running"}


@app.on_event("startup")
async def startup():
    if settings.project.log_file:
        logging_config.dictConfig(LOGGING)


app.include_router(classificator.router, prefix="/api/v1/classificator",
                   tags=["cat&dog"])
