# General
# ----------------------------------------------------------------------------
help:
	@echo "Options"
	@echo
	@echo "build: build project"
	@echo "run: docker-compose up in atached mode"
	@echo "daemon: docker-compose up in daemon mode"
	@echo "stop: docker-compose stop"
	@echo "api_logs: view api logs"
	@echo "----------------------------------------------------"
	@echo "migrate: migrate django api"
	@echo "test: test django api"
	@echo "make_migrations: create migrations for django api"
	@echo "create_superuser: creates admin user"
	@echo "api_shell: start django shell"

build:
	docker-compose build

run:
	docker-compose up --scale django_api=5

daemon:
	docker-compose up -d --scale django_api=5

stop:
	docker-compose stop

api_logs:
	docker logs -f reclameaqui_django_api_1

# Tool belt
# ----------------------------------------------------------------------------
migrate:
	docker-compose run django_api python manage.py migrate

test:
	docker-compose run django_api python manage.py test

make_migrations:
	docker-compose run django_api python manage.py makemigrations

create_superuser:
	docker-compose run django_api python manage.py createsuperuser --username admin

api_shell:
	docker-compose run django_api python manage.py shell
