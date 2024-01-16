from celery import Celery

celery = Celery("worker")

celery.config_from_object("mvp_sneakers_api.settings.celery_config")
