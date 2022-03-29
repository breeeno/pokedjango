release: python manage.py collectstatic --noinput && python manage.py migrate && python manage.py loaddata pokemon.json
web: gunicorn primeirageracao.wsgi --log-file -
