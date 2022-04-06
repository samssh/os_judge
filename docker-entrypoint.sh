#!/bin/bash

exec python manage.py collectstatic --noinput --clear &
echo "Running gunicorn..."
exec gunicorn os_judge.wsgi \
    --pythonpath "/home/software" \
    --name os_judge-gunicorn \
    --bind 0.0.0.0:8000 \
    --workers 5 \
    --timeout 30 \
    --log-level=info \
    --worker-class=sync \
    --graceful-timeout 40 \
    --reload