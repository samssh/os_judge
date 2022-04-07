import os
from celery import Celery
from django.conf import settings
from . import celery_config

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'os_judge.settings')
app = Celery('os_judge')

app.config_from_object(celery_config)
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
