from celery import Celery
from celery.app.task import Task as CeleryTask
from flask import Flask

from .celery import celery


def init_celery(app: Flask) -> Celery:
    TaskBase: CeleryTask = celery.Task
    # Initialization of instance is not here anymore
    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    # Configuration of placeholder happens here
    celery.conf.update(
        broker_url=app.config["CELERY_BROKER_URL"],
        # Rest of configuration
    )
    celery.Task = ContextTask
    return celery
