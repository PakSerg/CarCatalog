#!/bin/sh

echo "Waiting for PostgreSQL..."
while ! nc -z database 5432; do
  sleep 0.5
done
echo "Wait a bit..."
sleep 5
echo "PostgreSQL is up!"

python manage.py migrate
python manage.py loaddata fixtures/user.json 

python manage.py runserver 0.0.0.0:8000