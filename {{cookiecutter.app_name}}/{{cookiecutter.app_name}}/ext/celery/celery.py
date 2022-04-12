from celery import Celery

celery = Celery("{{cookiecutter.app_name}}", include=[])
celery.autodiscover_tasks(["{{cookiecutter.app_name}}.ext.celery.tasks"], force=True)


@celery.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))
