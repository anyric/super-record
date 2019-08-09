#!/bin/bash

# wait for 5 seconds for database to be ready
sleep 5

# run migrations
python manage.py migrate

# starts server
gunicorn --workers 4 --bind 0.0.0.0:8000 superrecord.wsgi
