#!/bin/bash
# Check production environment variables

export WSGI_ENV=prod

# Prepare log files and start outputting logs to stdout
mkdir -p /var/log/gunicorn/
touch /var/log/gunicorn/gunicorn.error.log
touch /var/log/gunicorn/gunicorn.access.log

#tail -n 0 -f /var/log/gunicorn/*.log &
# Start Gunicorn processes
exec gunicorn --bind 0.0.0.0:8000 recruiting_analytics_backend.wsgi
