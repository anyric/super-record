release: pip install django==2.2.4 django-easy-pdf && python src/manage.py migrate
web: pip install django==2.2.4 django-easy-pdf && gunicorn --chdir src/ superrecord.wsgi:application