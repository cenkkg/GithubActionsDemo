# syntax=docker/dockerfile:1

FROM python:alpine
WORKDIR .
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD gunicorn --bind 0.0.0.0:3000 wsgi:app