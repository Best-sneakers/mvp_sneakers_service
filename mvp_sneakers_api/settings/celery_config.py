from mvp_sneakers_api.settings.settings import settings

BROKER_URL = (
    f"amqp://{settings.rabbit.username}"
    f":{settings.rabbit.password}@{settings.rabbit.host}:"
    f"{settings.rabbit.port}/"
)

CELERY_RESULT_BACKEND = (
    f"redis://{settings.redis.host}:{settings.redis.port}"
    f"/{settings.redis.db}"
)

CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TIMEZONE = "UTC"
CELERY_ENABLE_UTC = True
CELERY_DEFAULT_QUEUE = settings.project.project_name
CELERY_DEFAULT_EXCHANGE = settings.project.project_name
CELERY_DEFAULT_ROUTING_KEY = settings.project.project_name
