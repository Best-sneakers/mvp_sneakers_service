.PHONY: dev pre-commit isort black mypy  pylint lint

dev: pre-commit

pre-commit:
	pre-commit install
	pre-commit autoupdate

isort:
	isort . --profile black

black:
	black .

mypy:
	mypy -p src

pylint:
	pylint src


check_and_rename_env:
	  @if [ -e ".env" ]; then \
        echo "env file exists."; \
      else \
      	cp .env.example .env | \
        echo "File does not exist."; \
      fi

build: check_and_rename_env
	docker compose build
	@echo "Waiting for 15 seconds..."
	@sleep 15

lint: isort black mypy  pylint

