from celery import shared_task
from django.core.management import call_command


@shared_task
def load_data_from_api():
    call_command('load_data')
