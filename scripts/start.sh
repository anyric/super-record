#!/bin/bash

apk --update --upgrade add gcc musl-dev jpeg-dev zlib-dev \
libffi-dev cairo-dev pango-dev gdk-pixbuf-dev

pip install -U django-easy-pdf

# wait for 5 seconds for database to be ready
sleep 5

# run migrations
python manage.py migrate

# starts server
python manage.py runserver 0.0.0.0:8000
