#!/bin/sh
set -e
python3 manage.py migrate
python3 manage.py collectstatic --no-input
uwsgi --socket :8000 wsgiSetting.ini
exec "$@"
