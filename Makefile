run:
	./manage.py runserver
migrate:
	./manage.py makemigrations
	./manage.py migrate
user:
	./manage.py createsuperuser
celery:
	celery -A config worker -l debug
