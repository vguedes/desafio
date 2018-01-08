# General
# ----------------------------------------------------------------------------
help:
	@echo "Options"
	@echo
	@echo "runservices: docker-compose up in detached mode"
	@echo "stopservices: docker-compose stop"
	@echo "api_logs: view api logs"
	@echo "----------------------------------------------------"
	@echo "migrate: migrate django api"
	@echo "make_migrations: create migrations for django api"
	@echo "create_superuser: creates admin user"
	@echo "api_shell: start django shell"

runservices:
	docker-compose up -d

stopservices:
	docker-compose stop

api_logs:
	docker logs -f reclameaqui_django_api_1

# Tool belt
# ----------------------------------------------------------------------------
migrate:
	docker-compose run django_api python manage.py migrate

make_migrations:
	docker-compose run django_api python manage.py makemigrations

create_superuser:
	docker-compose run django_api python manage.py createsuperuser --username admin

api_shell:
	docker-compose run django_api python manage.py shell
