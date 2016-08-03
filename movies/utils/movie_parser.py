# -*- coding: utf-8 -*-
import os
import json

import requests


def write_movie_data_as_json(file_name, movie_data):
    json_data = json.dumps(movie_data)
    with open(file_name, 'w') as f:
        f.write(json_data)


def read_raw_movie_data_as_py_object(file_name):
    data = [] 
    with open(file_name, 'r') as f:
        json_data = f.read()
        data = json.loads(json_data)
        return data


def read_movie_names(file_name):
    movie_names = []
    with open(file_name, 'r') as f:
        data = f.read()
        movie_names = data.splitlines()
    return movie_names


def request_movie_api_range(url, movie_names, start=0, end=1):
    movies_contents_list = []
    for movie_name in movie_names[start:end]:
        try:
            data = request_movie_api(daum_movie_api_url, movie_name)
        except:
            continue

        movies_contents_list.append(data)
    return movies_contents_list


def request_movie_api(url, query):
    request_url = daum_movie_api_url.replace("q=", "q=%s" % (query))

    response = requests.get(request_url)
    status_code =  response.status_code

    if status_code != 200:
        msg = ""
        if status_code == 429:
            msg = "query exceeded 300"
        elif status_code == 400:
            msg = "bad request : not exist, query : %s" % query
        raise Exception(msg)

    movies_contents = json.loads(response.text)

    return movies_contents 


def parse_all_movie_data(movies_contents_list):
    movie_data = []
    for movies_contents in movies_contents_list:
        data = parse_movie_data(movies_contents)
        if data != []:
            movie_data.append(data)
    return movie_data


def parse_movie_data(data):
    try:
        common = data['channel']['item'][0]
    except IndexError:
        print("not found, query items") 
        return []

    movie_info = {}
    
    actors = dict()
    for actor_info in common['actor']:
        actor = actor_info['content']
        actors.update({actor: actor_info['link']})
    movie_info.update({'actors': actors})
    
    title = data['channel']['q']
    movie_info.update({'title': title})
    
    director_info = common['director'][0]
    director = director_info['content']
    movie_info.update({'director': director})
    movie_info.update({'director': director})
    
    genres = []
    for genre_info in common['genre']:
        genres.append(genre_info['content'])
    movie_info.update({'genres': genres})
    
    grade_info = common['grades'][0]
    netizen_grade = grade_info['content']
    movie_info.update({'netizen_grade': netizen_grade})
    
    story = common['story'][0]['content']
    movie_info.update({'story': story})
    
    open_info = common['open_info']
    release_date = open_info[0]['content']
    movie_info.update({'release_date': release_date})
    age = open_info[1]['content']
    movie_info.update({'age': age})
    running_time = open_info[2]['content']
    movie_info.update({'running_time': running_time})
    
    thumbnail = common['thumbnail'][0]['content']
    movie_info.update({'thumbnail': thumbnail})

    return movie_info


def dumps_pretty(data):
    return json.dumps(data, ensure_ascii=False, indent=4)


daum_movie_api_url = os.environ.get('DAUM_MOVIE_API_URL')
path = os.environ.get('MOVIES_UTIL_DATA_PATH')
movie_names_path = path + 'movie_names.csv'
movie_data_path = path + 'movie_data.json'
raw_movie_data_path = path + 'raw_movie_data.json'
