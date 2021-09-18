import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
from portfolio import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

app = Celery('portfolio')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# load tasks.py in django apps
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


app.conf.beat_schedule = {
    'update-every-day': {
        'task': 'portfolio.tasks.update_currencies_info',
        'schedule': crontab(),
    }
}
