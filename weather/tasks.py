from time import sleep

from utils.weather_data_to_db import all_in_one

from settings import celery


@celery.task
def periodic_update_publish_weather():
    while True:
        all_in_one()
        sleep(60*15)# per 15 minutes
