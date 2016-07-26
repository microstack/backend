# -*- coding: utf-8 -*-
import os
import json

import requests


daum_movie_api_url = os.environ.get('DAUM_MOVIE_API_URL')
query = "곡성"
request_url = daum_movie_api_url.replace("q=", "q=%s" % (query))

response = requests.get(request_url)
json_contents = json.loads(response.text)
common = json_contents['channel']['item'][0]
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

title = json_contents['channel']['q']
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
