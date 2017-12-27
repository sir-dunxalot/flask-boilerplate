FROM tiangolo/uwsgi-nginx-flask:python3.6

MAINTAINER Duncan Walker <duncangrahamwalker@gmail.com>

# Place app in container

COPY ./app /app

# Install deps

COPY requirements.txt requirements.txt

RUN pip install --trusted-host pypi.python.org -r requirements.txt
