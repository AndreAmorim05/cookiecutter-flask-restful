testv:
	poetry run pytest -v

push:
	git push -u origin HEAD

inidb:
	FLASK_APP={{cookiecutter.app_name}}.app poetry run flask db init
	FLASK_APP={{cookiecutter.app_name}}.app poetry run flask db migrate -m "First commit"
	FLASK_APP={{cookiecutter.app_name}}.app poetry run flask db upgrade
	FLASK_APP={{cookiecutter.app_name}}.app poetry run flask populate-db

test-cov:
	FLASK_ENV=test pytest tests/ -v --cov=base

upd:
	docker-compose up -d

down:
	docker-compose down

run:
	FLASK_APP={{cookiecutter.app_name}}.app FLASK_ENV=development poetry run flask run -h 0.0.0.0

worker:
	celery -A worker worker --loglevel=info --pool=solo
