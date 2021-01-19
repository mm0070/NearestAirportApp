FROM python:2.7.11-alpine

WORKDIR /app
COPY . .

RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 apk add --no-cache nodejs && \
 pip install -r requirements.txt --no-cache-dir && \
 npm install -g less && \
 apk --purge del .build-deps

RUN pip install -r requirements.txt
