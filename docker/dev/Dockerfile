FROM python:3.7-alpine

LABEL application='superrecord'

LABEL maintainer='Anyama Richard'

WORKDIR /app

# update system and install dependencies
RUN apk update && apk add --no-cache bash git openssh \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk del build-deps \
    && pip install pipenv 

#copy source code to app dir
COPY src/ /app/
ADD Pipfile /app/

ADD scripts/start.sh /app/

# add execute permission
RUN chmod +x start.sh

# install app dependencies from the pipfile
RUN pipenv install --skip-lock --system && \
    apk --update --upgrade add gcc musl-dev jpeg-dev zlib-dev \
    libffi-dev cairo-dev pango-dev gdk-pixbuf-dev && \
    pip install -U django-easy-pdf

CMD bash -c "source start.sh"

