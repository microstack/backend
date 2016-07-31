# -*- encoding: utf-8 -*-

from models.movie import Movie, movie_list_schema, movies_schema, movie_schema
from models.actor import Actor, actors_schema, actor_schema
from models import db

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class MovieList(Resource):
    def get(self):
        data = Movie.query.all()
        return movie_list_schema.dump(data).data


class MovieDetail(Resource):
    def get(self, id):
        data = Movie.query.filter_by(id=id).first()
        return movie_schema.dump(data).data


class MovieDetailActors(Resource):
    def get(self, id):
        data = Movie.query.filter_by(id=id).first()
        actors = []
        for actor in data.actors:
            actors.append(actor)
        return actors_schema.dump(actors).data


class MoviesLatest(Resource):
    def get(self):
        data = Movie.query.order_by(Movie.release_date.desc())[:10]
        return movies_schema.dump(data).data


class MoviesHighGrade(Resource):
    def get(self):
        data = Movie.query.order_by(Movie.netizen_grade.desc())[:10]
        return movies_schema.dump(data).data


class ActorList(Resource):
    def get(self):
        data = Actor.query.all()
        return actors_schema.dump(data).data


class ActorDetail(Resource):
    def get(self, id):
        data = Actor.query.filter_by(id=id).first()
        return actor_schema.dump(data).data


api.add_resource(MovieList, '/movies/')
api.add_resource(MovieDetail, '/movies/<id>/')
api.add_resource(MovieDetailActors, '/movies/<id>/actors/')
api.add_resource(MoviesLatest, '/movies/latest/')
api.add_resource(MoviesHighGrade, '/movies/grade/')

api.add_resource(ActorList, '/actors/')
api.add_resource(ActorDetail, '/actors/<id>')

if __name__ == '__main__':
    app.run(debug=True)
