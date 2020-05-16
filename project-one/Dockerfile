# pull official base image
FROM python:3.7-slim

# set work directory
WORKDIR /usr/src/app/web

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apt-get update && apt-get -y install gcc python3-dev musl-dev postgresql-server-dev-11 netcat
RUN pip install --upgrade pip
COPY requirements.txt /usr/src/app/web/requirements.txt
RUN pip install -r requirements.txt

COPY entrypoint.sh /usr/src/app/web/entrypoint.sh
# copy project
COPY . /usr/src/app/web

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/web/entrypoint.sh"]