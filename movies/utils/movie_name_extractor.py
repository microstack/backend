# -*- coding: utf-8 -*-
import os
import re

import requests
from bs4 import BeautifulSoup


request_url = os.environ.get('MOVIE_NAME_URL')
response = requests.get(request_url)
contents = response.text

bs = BeautifulSoup(contents, 'html.parser')
bs_movie_tags = bs.findAll('a', {'class': 'wiki-link-internal'})

titles = []
for movie in bs_movie_tags[1:]:
    """
    subtract data in parenthesis, it will may cause error title contains infix
     parenthesis.
    """
    title = ""
    title = re.sub(r'\([^()]*\)', title, movie['title'])
    titles.append(title)

with open('movie_names.csv', 'w') as f:
    for title in titles:
        f.write(title + '\n')
