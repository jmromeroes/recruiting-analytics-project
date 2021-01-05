#!/bin/bash
# Check production environment variables

export WSGI_ENV=prod

source "/home/ubuntu/recruiting-analytics-project/env/bin/activate"

# Prepare log files and start outputting logs to stdout
mkdir -p /var/log/gunicorn/
touch /var/log/gunicorn/gunicorn.error.log
touch /var/log/gunicorn/gunicorn.access.log

#tail -n 0 -f /var/log/gunicorn/*.log &
# Start Gunicorn processes
exec gunicorn -c /home/ubuntu/recruiting-analytics-project/recruiting_analytics_backend/deployment/gunicorn/gunicorn.py.ini recruiting_analytics_backend.wsgi