import datetime

from celery import shared_task, task
from time import sleep
from .models import trucks
from datetime import datetime


@shared_task()
def sleepy(duration):
    sleep(duration)
    return None

#@shared_task()
#def send_warning():