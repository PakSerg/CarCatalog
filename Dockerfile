FROM python:3.10-slim 

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get -y install netcat-openbsd postgresql-client 

COPY requirements.txt requirements.txt 
RUN pip install -r requirements.txt 

COPY . . 

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh