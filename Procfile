release: python manage.py collectstatic --noinput
release: python manage.py makemigrations
release: python manage.py migrate
release: python manage.py loaddata pokemon.json
web: gunicorn webdev.wsgi --log-file -
