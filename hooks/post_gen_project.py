import os
import shutil


def remove_celery_files():
    shutil.rmtree("{{cookiecutter.app_name}}/ext/celery/")
    os.remove("worker.py")

def main():
    if "{{cookiecutter.celery_worker}}" == "Do not use Celery":
        remove_celery_files()

if __name__ == "__main__":
    main()
