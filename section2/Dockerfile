FROM postgres:latest

ENV POSTGRES_USER docker
ENV POSTGRES_PASSWORD docker
ENV POSTGRES_DB sales

COPY sql/create_table.sql /docker-entrypoint-initdb.d/
