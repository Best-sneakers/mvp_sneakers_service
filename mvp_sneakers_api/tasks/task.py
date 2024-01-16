import time

from mvp_sneakers_api.services.celery import celery


@celery.task(name="create_task")
def create_task(task_type):
    time.sleep(int(task_type) * 10)
    return True
