import os

from models import Publish, Weather
from settings import db

import requests
from bs4 import BeautifulSoup

URL = os.environ['SEOUL_GYEONGGI_URL']


def get_bs_object_from_url(url=URL):
    try:
        response = requests.get(url)
    except requests.ConnectionError:
        objects = {'error': 'ConnectionError'}
        return objects

    if response.status_code != 200:
        objects = {'error': 'Statuscode : %s' % response.status_code}
        return objects

    # exception handling needed.
    bs_object = BeautifulSoup(response.text, "html.parser")

    return bs_object


def parse_data_as_publish_publish_object(bs_object):

    def is_duplicate_pub_date(pub_date):
        if Publish.query.filter_by(date=pub_date).count() > 0:
            return True
        return False

    def is_error_bs_object():
        error = bs_object.get('error')
        if error is not None:
            return error

    """
    publish_object will be like
    publish objects =
        {'cities': [{'city': '서울',
            'weathers': [{
                'date': '2016-09-02',
                'reliability': '보통',
                'temp_max': '28',
                'temp_min': '23',
                'weather': '구름많음'
            },
            ...
            }]
        'publish': {'pub_date': '2016-08-30',
        'summary': '이번 예보기간에는...'}}

    But if the pub_date is already registered, then return {'duplicate': True}
    """
    is_error_bs_object()

    publish_object = dict()

    header = bs_object.find('header')

    # format yyyy-mm-dd
    tm_data = header.find('tm').text
    pub_date = '%s-%s-%s' % (tm_data[:4], tm_data[4:6], tm_data[6:8])
    if is_duplicate_pub_date(pub_date):
        return {'duplicate': True}

    summary = header.find('wf').text

    publish_object['publish'] = {'pub_date': pub_date, 'summary': summary}

    locationed_data_list = bs_object.find_all('location')

    publish_object['cities'] = []
    cities = publish_object['cities']
    city = ''
    for locationed_data in locationed_data_list:
        city = locationed_data.find('city').text
        weather_data_list = locationed_data.find_all('data')
        city_weathers = {'city': city, 'weathers': []}
        weathers = city_weathers['weathers']

        for weather_data in weather_data_list:
            date = weather_data.find('tmef').text[:10]# yyyy-mm-dd
            weather = weather_data.find('wf').text
            temp_min = weather_data.find('tmn').text
            temp_max = weather_data.find('tmx').text
            reliability = weather_data.find('reliability').text
            weathers.append({'date': date, 'weather': weather,
                'temp_min': temp_min, 'temp_max': temp_max,
                'reliability': reliability
            })
        cities.append(city_weathers)

    return publish_object


def is_duplicate_publish_object(publish_object):
    if publish_object.get('duplicate'):
        return True


def publish_object_to_db(publish_object, db):
    '''
    It assumes all the data has correct format. But it should be checked later.
    For example, pub_date format shoul be 'yyyy-mm-dd', not other format.
    '''

    if is_duplicate_publish_object(publish_object):
        print('temporary log: duplicate publish data, SO SKIPPED')
        return db

    pub_date = publish_object['publish']['pub_date']
    summary = publish_object['publish']['summary']
    publish = Publish(date=pub_date, summary=summary)

    cities = publish_object['cities']
    for city in cities:
        city_name = city['city']
        weathers = city['weathers']
        for weather in weathers:
            weather = Weather(
                date=weather['date'], reliability=weather['reliability'],
                min_temparature=weather['temp_min'],
                max_temparature=weather['temp_max'],
                weather=weather['weather'], city=city_name,
                publish_date=publish.date
            )
            db.session.add(weather)
    db.session.add(publish)
    db.session.commit()
    print('Complete. happy coding :*:')

    return db


def all_in_one(url=URL, db=db):
    '''
    Used function for dynamic request. Be careful to use function as the
    argument of function, because they have a status. In this case, it causes
    data integrity error.
    '''
    def get_publish_object(bs_object):
        publish_object = parse_data_as_publish_publish_object(bs_object)
        return publish_object

    bs_object = get_bs_object_from_url(url)
    publish_object = get_publish_object(bs_object)

    publish_object_to_db(publish_object, db)
    return db
