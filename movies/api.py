# -*- encoding: utf-8 -*-

from models.movie import Movie, movie_list_schema, movies_schema,\
    movie_schema
from models.actor import Actor, actors_schema, actor_schema
from models.genre import Genre, genres_schema

from flask import Flask
from flask_restful import Resource


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
        return actors_schema.dump(data.actors)


class MovieDetailGenres(Resource):
    def get(self, id):
        data = Movie.query.filter_by(id=id).first()
        return genres_schema.dump(data.genres)


class MoviesLatest(Resource):
    def get(self):
        data = Movie.query.order_by(Movie.release_date.desc())[:5]
        return movies_schema.dump(data).data


class MoviesHighGrade(Resource):
    def get(self):
        data = Movie.query.order_by(Movie.netizen_grade.desc())[:5]
        return movies_schema.dump(data).data


class ActorList(Resource):
    def get(self):
        data = Actor.query.all()
        return actors_schema.dump(data).data


class ActorDetail(Resource):
    def get(self, id):
        data = Actor.query.filter_by(id=id).first()
        return actor_schema.dump(data).data


class GenreList(Resource):
    def get(self):
        data = Genre.query.all()
        return genres_schema.dump(data).data

class GenreMovieList(Resource):
    def get(self, name):

        data = Movie.query.filter(Movie.genres.any(name=name)).all()

        if data == []:
            # execute an exception or showing an info later
            pass

        return movies_schema.dump(data).data


from flask_restful import Api
from settings import app

api = Api(app)
api.add_resource(MovieList, '/movies/')
api.add_resource(MovieDetail, '/movies/<int:id>/')
api.add_resource(MovieDetailActors, '/movies/<int:id>/actors/')
api.add_resource(MovieDetailGenres, '/movies/<int:id>/genres/')
api.add_resource(MoviesLatest, '/movies/latest/')
api.add_resource(MoviesHighGrade, '/movies/grade/')

api.add_resource(ActorList, '/movies/actors/')
api.add_resource(ActorDetail, '/movies/actors/<int:id>')

api.add_resource(GenreList, '/movies/genres/')
api.add_resource(GenreMovieList, '/movies/genres/<string:name>/')
