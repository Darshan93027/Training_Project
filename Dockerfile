FROM python:3.11-slim

ENV POSTGRES_DB=myapp
ENV POSTGRES_USER=myuserapp
ENV POSTGRES_PASSWORD=User123

RUN apt-get update && apt-get install -y \
    postgresql \
    postgresql-contrib \
    gcc \
    libpq-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

USER postgres
RUN /etc/init.d/postgresql start && \
    psql -c "CREATE DATABASE ${POSTGRES_DB};" && \
    psql -c "CREATE USER ${POSTGRES_USER} WITH PASSWORD '${POSTGRES_PASSWORD}';" && \
    psql -c "ALTER DATABASE ${POSTGRES_DB} OWNER TO ${POSTGRES_USER};" && \
    psql -d ${POSTGRES_DB} -c "ALTER SCHEMA public OWNER TO ${POSTGRES_USER};" && \
    psql -d ${POSTGRES_DB} -c "GRANT ALL ON SCHEMA public TO ${POSTGRES_USER};"

USER root

EXPOSE 8000 5432

CMD bash -c "\
service postgresql start && \
python manage.py migrate && \
python manage.py runserver 0.0.0.0:8000"
