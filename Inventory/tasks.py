from celery import shared_task


@shared_task()
def Print():
    print('Redis and celery are working!')

