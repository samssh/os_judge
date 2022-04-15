source venv/bin/activate
source set-env.sh
export DB_NAME=$db_name
export DB_USER=$db_user
export DB_PASS=$db_password
export DB_PORT=$db_port
export DB_HOST=$db_host
export DJANGO_DEBUG=False
export RABBITMQ_HOST=$rabbit_host
export RABBITMQ_USER=$rabbit_user
export RABBITMQ_PASSWORD=$rabbit_password
export RABBITMQ_PORT=$rabbit_port
celery -A os_judge worker -l info --concurrency 3 --without-gossip --without-mingle --without-heartbeat
