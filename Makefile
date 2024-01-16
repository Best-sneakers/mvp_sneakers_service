.PHONY: dev pre-commit isort black mypy flake8 pylint lint

dev: pre-commit

pre-commit:
	pre-commit install
	pre-commit autoupdate

isort:
	isort . --profile black

flake8:
	flake8 .

black:
	black .

mypy:
	mypy -p app

pylint:
	pylint app



lint: isort black mypy  pylint flake8

check_and_rename_env:
	  @if [ -e ".env" ]; then \
        echo "env file exists."; \
      else \
      	cp .env.example .env | \
        echo "File does not exist."; \
      fi

build_front:
	docker-compose -f frontend/docker-compose.yml build

run_front:
	docker-compose -f frontend/docker-compose.yml up


build_docker_metrics: check_and_rename_env
	docker-compose -f docker-compose.metrics.yml build

build_docker_dev:check_and_rename_env
	docker compose -f docker-compose.dev.yml build

run_metrics:
	docker compose -f docker-compose.metrics.yml up

metrics_stop:
	docker compose -f docker-compose.metrics.yml down

run_dev:
	docker compose -f docker-compose.dev.yml up

dev_stop:
	docker compose -f docker-compose.dev.yml down
