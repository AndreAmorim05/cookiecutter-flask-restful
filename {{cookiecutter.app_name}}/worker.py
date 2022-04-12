from {{cookiecutter.app_name}}.app import create_app
from {{cookiecutter.app_name}}.ext.celery import init_celery

celery = init_celery(create_app())
