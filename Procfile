release: pip install -U django-easy-pdf && python src/manage.py migrate
web: pip install -U django-easy-pdf && gunicorn --chdir src/ superrecord.wsgi:application