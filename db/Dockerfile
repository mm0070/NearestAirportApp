FROM postgres:13

WORKDIR /db
COPY . .

COPY init.sql /docker-entrypoint-initdb.d/

