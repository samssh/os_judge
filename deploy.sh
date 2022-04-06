source venv/bin/activate
source set-env.sh
envsubst <docker-compose.yml.sample > docker-compose.yml
envsubst <rabbitmq/rabbitmq.conf.sample > rabbitmq/rabbitmq.conf
docker-compose up -d --build
