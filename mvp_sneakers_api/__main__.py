import uvicorn

from mvp_sneakers_api import app
from mvp_sneakers_api.settings.settings import settings

uvicorn.run(app, host=settings.api.host, port=int(settings.api.port))
