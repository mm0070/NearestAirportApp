FROM python:2

WORKDIR /app
COPY . .

# RUN apk add --no-cache python2 py2-pip
RUN pip install -r requirements.txt