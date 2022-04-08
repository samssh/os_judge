import os

RABBITMQ_CELERY_URL = "amqp://{user_name}:{password}@{host}:{port}/{vhost}".format(
    host=os.getenv('RABBITMQ_HOST', 'localhost'),
    port=os.getenv('RABBITMQ_PORT', '5672'),
    user_name=os.getenv('RABBITMQ_USER', 'test_user'),
    password=os.getenv('RABBITMQ_PASSWORD', 'test_password'),
    vhost=os.getenv('RABBITMQ_VHOST', '')
)
# Celery
broker_url = RABBITMQ_CELERY_URL
accept_content = ['json']
result_serializer = 'json'
task_serializer = 'json'

result_backend_always_retry = True
result_backend = 'django-db'

task_annotations = {'*': {'rate_limit': '20/m'}}

worker_send_task_event = False
