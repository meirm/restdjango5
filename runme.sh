mkdir -p data
docker run -d --name deleteme -p 8000:8000 -v data:/data restdjango5 python manage.py runserver 0.0.0.0:8000
docker exec -ti deleteme python manage.py makemigrations
docker exec -ti deleteme python manage.py migrate
docker exec -ti deleteme python manage.py createsuperuser
