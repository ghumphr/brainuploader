#!/bin/sh

# This script will install brainuploader locally via docker compose.
# While this script works as-is, you should really see the documentation!

docker compose up -d
docker compose exec brainuploader python manage.py makemigrations brainuploader
docker compose exec brainuploader python manage.py migrate
docker compose exec brainuploader python manage.py createsuperuser
docker compose exec brainuploader python generate_sample_flashcards.py

echo "Now go to http://localhost:8000/static/cardviewer.html to see the prototype."
echo "Not everything is working yet, but you can create and edit cards at"
echo "http://localhost:8000/admin/"
