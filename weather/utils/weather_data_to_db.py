import os

import requests
from bs4 import BeautifulSoup

URL = os.environ['SEOUL_GYEONGGI_URL']


def get_bs_object_from_url(url=URL):
    response = requests.get(url)
    # exception handling needed.
    bs_object = BeautifulSoup(response.text, "html.parser")

    return bs_object

def parse_data_as_publish_publish_object(bs_object):
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
    """

    publish_object = dict()

    header = bs_object.find('header')

    # format yyyy-mm-dd
    tm_data = header.find('tm').text
    pub_date = '%s-%s-%s' % (tm_data[:4], tm_data[4:6], tm_data[6:8])

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


publish_object = parse_data_as_publish_publish_object(
    get_bs_object_from_url())
def publish_object_to_db(publish_object=publish_object):
    pass
