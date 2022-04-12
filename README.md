# Cookiecutter Flask RESTful

## Default Project
By default the project generated with this cookiecutter gives a simple RESTful login manager, as shown below.

### Home Page
![cookiecutter-flask-restful.png](https://cdn.discordapp.com/attachments/955441956731887616/963511388934909982/cookiecutter-flask-restful.png)

### Login page
![cookiecutter-flask-restful-login.png](https://cdn.discordapp.com/attachments/955441956731887616/963511346568257646/cookiecutter-flask-restful-login.png)

* * *

## Usage

To use this cookiecutter template you need to have cookiecutter installed in your machine, you can do this by typing:
```
$ pip install cookiecutter
```

After install cookiecutter, run the command below to start to download and configure your project.
```
$ cookiecutter https://github.com/AndreAmorim05/cookiecutter-flask-restful
```

Another recomendation to use this project is to have Poetry in your machine, you can install it using the documentation that is precise on how to do this [Poetry install](https://python-poetry.org/docs/)
Or a not so recommended way is using pip
```
$ pip install --user poetry
```

After run the above command you will see that some questions appear in your shell, enter the project specifications as asked, below you can see an example how it works.
```
root_app_name [My Project Name]: Flask App
app_name [flask_app]:
description [Some description to my project]:
author_name [André Amorim]:
email [andré-amorim@example.com]:
admin_access_email [andré-amorim@example.com]:
admin_access_password [admin]:
version [0.1.0]: 1.0.0
Select open_source_license:
1 - MIT
2 - BSD
3 - GPLv3
4 - Apache Software License 2.0
5 - Not open source
Choose from 1, 2, 3, 4, 5 [1]: 3
Select postgresql_version:
1 - 14.2
2 - 13.5
3 - 12.9
4 - 11.14
5 - 10.19
Choose from 1, 2, 3, 4, 5 [1]: 1
Select celery_worker:
1 - Redis
2 - Rabbitmq
3 - Do not use Celery
Choose from 1, 2, 3 [1]: 2
```

Then, your project is set, now you can develop as you want, just need to change the directory
```
$ cd flask_app
$ ls -ll
```

To get the dependencies and activate the .venv using poetry:
```
$ poetry shell
$ poetry install
```

Take your project versionated with git
```
$ git init
$ git add .
$ git commit -m "First commit"
```

Get everything up with docker compose:
```
$ docker-compose up -d
```

The same commando can be simplified with the command presente in the Makefile
```
$ make upd
```

If you want to use PostgreSQL already populated with the credentials provided in the poject setup, to access the admin routes. The command below creates the first migration and populate the database. 
```
$ make inidb
```

Finaly to run the flask application use the command:
```
$ make run
```

[OPTIONAL] If you choose some celery worker, to run the worker open another shell at the same directory and run:
```
$ make worker
```
