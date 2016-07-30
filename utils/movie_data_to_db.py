import json
import datetime

from movies.models import db
from movies.models.actor import Actor
from movies.models.movie import Movie

def read_movie_data_as_objects(file_name):
    data = []
    with open(file_name, 'r') as f:
        data = json.loads(f.read())
    return data


def one_movie_data_to_db(partial):
    def actors_to_db():
        for name, link in partial['actors']:
            actor = Actor()
            actor.name, actor.link = name, link
            db.session.add(actor)
            db.session.commit()

    def movie_to_db():
        movie = Movie()

        movie.title = partial['title']
        movie.age = partial['age']
        movie.director = partial['director']
        movie.netizen_grade = float(partial['netizen_grade'])

        year, month, day = partial['release_date'].split('.')
        movie.release_date = datetime.date(int(year), int(month), int(day))

        running_time = partial['running_time']
        movie.running_time = ''.join(
            filter(lambda x: x.isdigit(), running_time))

        movie.story = partial['story']
        movie.thumbnail = partial['thumbnail']

        for name in partial['actors']:
            link = partial['links']['actors'][0][name]
            actor = Actor.query.filter_by(link=link).first()
            movie.actors.append(actor)

        db.session.add(movie)
        db.session.commit()

    actors_to_db()
    movie_to_db()

movie_data_file = 'utils/data/movie_data.csv'
