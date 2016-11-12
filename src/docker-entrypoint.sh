#!/bin/bash

if [ -z "$DJANGOSECRETKEY" ]; then
    exit 1  
fi


python3 ./manage.py syncdb --noinput

if [ -f /olgart.json ]; then
    python3 ./manage.py loaddata /olgart.json
fi

if [ -f /media_backup ]; then
    cp -r /media_backup/ /media
fi

python3 ./manage.py makemessages --all


gunicorn \
    --workers 3 \
    --bind 0.0.0.0:8000 \
    --proxy-allow-from 0.0.0.0 \
    olgart.wsgi
