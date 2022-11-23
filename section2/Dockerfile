FROM postgres

ENV POSTGRES_USER docker
ENV POSTGRES_PASSWORD docker
ENV POSTGRES_DB sales

COPY sql/create_table.sql /docker-entrypoint-initdb.d/

RUN /docker-entrypoint-initdb.d/create_table.sql
