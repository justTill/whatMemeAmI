#!/bin/bash


echo "[bringing down old container]"
docker-compose -f whatMemeAmI.yml down

echo "[starting docker new container & download container that are not here yet]"
# start new setup / with same login credentials as last time / if not db connection does not work
SECRET_KEY=dhbj32g8f2uzwbhjg7z DATABASE_NAME=whatMemeAmI SQL_USER=whatMeme SQL_PASSWORD=whatMemeAmI docker-compose -f whatMemeAmI.yml up -d
echo "[docker container started]"
echo "[migrate new database scheme]"
docker-compose -f whatMemeAmI.yml exec memeapp python manage.py migrate --noinput

echo "[collection all staticfiles so the website looks beautiful]"
docker-compose -f whatMemeAmI.yml exec memeapp python manage.py migrate --noinput

exec "$@"
