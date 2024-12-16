#!/bin/sh

# This script will install brainuploader locally via docker compose.
# While this script works as-is, you should really see the documentation!

docker compose up -d
docker compose exec api-server python manage.py makemigrations brainuploader
docker compose exec api-server python manage.py migrate
docker compose exec api-server python manage.py createsuperuser
docker compose exec api-server python generate_sample_flashcards.py

echo "Now go to http://localhost:8000/ to see the prototype."
echo "Not everything is working yet, but you can create and edit cards at"
echo "http://localhost:8000/admin/"

echo "Note: frontend server is running at http://localhost:3000/"
