import os

from django.apps import apps

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erp_reloaded.settings.dev')
app = Celery('erp_reloaded')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: [n.name for n in apps.get_app_configs()])
