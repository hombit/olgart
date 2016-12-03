#!/bin/bash

if [ -z "$DJANGOSECRETKEY" ]; then
    exit 1  
fi

python3 wait_postgres.py

python3 ./manage.py syncdb --noinput

if [ -f /backup/olgart.json ]; then
    python3 ./manage.py loaddata /backup/olgart.json
fi

if [ -d /backup/media ]; then
    cp -r /backup/media/* /www/media
fi

python3 ./manage.py makemessages --all


gunicorn \
    --workers 3 \
    --bind 0.0.0.0:8000 \
    --proxy-allow-from proxy \
    olgart.wsgi
