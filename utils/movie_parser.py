# -*- coding: utf-8 -*-
import os
import json

import requests


def write_movie_info_list_as_json(file_name, movie_info_list):
    json_data = json.dumps(movie_info_list)
    with open(movie_info_list_file, 'w') as f:
        f.write(json_data)


def read_movie_names(file_name):
    movie_names = []
    with open(file_name, 'r') as f:
        data = f.read()
        movie_names = data.splitlines()
    return movie_names


def request_movie_api_range(url, movie_names, start=0, end=1):
    json_contents_list = []
    for movie_name in movie_names[start:end]:
        try:
            data = request_movie_api(daum_movie_api_url, movie_name)
        except:
            continue

        json_contents_list.append(data)
    return json_contents_list


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

    json_contents = json.loads(response.text)

    return json_contents 


def parse_all_movie_data(json_contents_list):
    movie_info_list = []
    for json_contents in json_contents_list:
        data = parse_movie_data(json_contents)
        movie_info_list.append(data)
    return movie_info_list


def parse_movie_data(data):
    try:
        common = data['channel']['item'][0]
    except IndexError:
        raise Exception("not found, query items : %s" % query) 

    movie_info = {}
    
    actors = []
    links = {}
    links.update({'actors': []})
    actor_links = links['actors']
    for actor_info in common['actor']:
        actor = actor_info['content']
        actors.append(actor)
        actor_links.append({actor: actor_info['link']})
    movie_info.update({'actors': actors})
    
    title = data['channel']['q']
    movie_info.update({'title': title})
    
    director_info = common['director'][0]
    director = director_info['content']
    movie_info.update({'director': director})
    links.update({'director': director_info['link']})
    
    genres = []
    for genre_info in common['genre']:
        genres.append(genre_info['content'])
    movie_info.update({'director': director})
    
    grade_info = common['grades'][0]
    netizen_grade = grade_info['content']
    movie_info.update({'netizen_grade': netizen_grade})
    links.update({'netizen_grade': grade_info['link']})
    
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

    movie_info.update({'links': links})

    return movie_info


daum_movie_api_url = os.environ.get('DAUM_MOVIE_API_URL')
movie_names_file = 'movie_names.csv'
movie_info_list_file = 'movie_info_list.csv'
