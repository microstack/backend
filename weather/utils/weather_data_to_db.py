import os

import requests
from bs4 import BeautifulSoup

URL = os.environ['SEOUL_GYEONGGI_URL']


def get_bs_objects_from_url(url=URL):
    response = requests.get(url)
    # exception handling needed.
    bs_objects = BeautifulSoup(response.text, "html.parser")

    return bs_objects

def parse_data_as_json(bs_objects):
    json_objects = dict()

    header = bs_objects.find('header')

    # format yyyy-mm-dd
    tm_data = header.find('tm').text
    pub_date = '%s-%s-%s' % (tm_data[:4], tm_data[4:6], tm_data[6:8])

    summary = header.find('wf').text

    json_objects['publish'] = {'pub_date': pub_date, 'summary': summary}

    locationed_data_list = bs_objects.find_all('location')

    json_objects['cities'] = []
    cities = json_objects['cities']
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

    return json_objects

data = parse_data_as_json(get_bs_objects_from_url())
