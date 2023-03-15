web: gunicorn oc_lettings_site.wsgi
release: python manage.py migrate
web: python manage.py collectstatic
web: python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@email.com', 'Abc1234!')"