

## Project setup
docker-compose up -d --build
docker exe dvrpdb_backend python manage.py makemigrations
docker exe dvrpdb_backend python manage.py migrate
docker exec dvrpdb_backend python manage.py collectstatic
docker exec -it dvrpdb_backend python manage.py createsuperuser

