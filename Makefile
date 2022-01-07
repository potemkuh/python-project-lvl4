install:
	poetry install

migrate:
	poetry run python manage.py migrate

makemigrations:
	poetry run python manage.py makemigrations

run:
	poetry run python manage.py runserver 0.0.0.0:8000

lint:
	poetry run flake8 .

makemessages:
	django-admin makemessages -l ru

compilemessages:
	django-admin compilemessages

test:
	poetry run python manage.py test