#!/bin/bash
secret_key = dhbj32g8f2uzwbhjg7z
database_name = whatMemeAmI
sql_user = whatMeme
sql_password = whatMemeAmI

echo "[bringing down old container]"
docker-compose -f whatMemeAmI.yml down

echo "[starting docker new container & download container that are not here yet]"
# start new setup / with same login credentials as last time / if not db connection does not work
SECRET_KEY=$secret_key DATABASE_NAME=$database_name SQL_USER=$sql_user SQL_PASSWORD=$sql_password docker-compose -f whatMemeAmI.yml up -d
echo "[docker container started]"
echo "[migrate new database scheme]"
docker-compose -f whatMemeAmI.yml exec memeapp python manage.py migrate --noinput

echo "[collection all staticfiles so the website looks beautiful]"
docker-compose -f whatMemeAmI.yml exec memeapp python manage.py collectstatic --no-input --clear

exec "$@"
