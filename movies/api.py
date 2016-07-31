# -*- encoding: utf-8 -*-

from models.movie import Movie, movies_schema
from models.actor import Actor, actors_schema
from models import db

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class MovieList(Resource):
    def get(self):
        data = Movie.query.all()
        return movies_schema.dump(data).data


class ActorList(Resource):
    def get(self):
        data = Actor.query.all()
        return actors_schema.dump(data).data


api.add_resource(MovieList, '/movies/')
api.add_resource(ActorList, '/actors/')

if __name__ == '__main__':
    app.run(debug=True)
