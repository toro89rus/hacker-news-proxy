-include .env

install:
	uv sync

lint:
	uv run ruff check proxy

test:
	uv run pytest --cov=proxy --cov-report=term-missing

start-dev:
	uv run flask --app proxy.app --debug run --port 8232


start:
	uv run  gunicorn -w 5 -b 0.0.0.0:$(PORT) proxy.app:app

