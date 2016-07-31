# -*- encoding: utf-8 -*-

from models.movie import Movie, movies_schema
from models import db

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class MovieList(Resource):
    def get(self):
        data = Movie.query.all()
        return movies_schema.dump(data).data


api.add_resource(MovieList, '/movies/')

if __name__ == '__main__':
    app.run(debug=True)
