run-dev:
	gunicorn app.app:app

run:
	gunicorn --config config.py app.app:app