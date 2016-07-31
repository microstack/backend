import requests
import os

from models.movie import Movie, movie_list_schema, movies_schema, movie_schema

from flask import jsonify, json

from settings import app


@app.route('/movies/', methods=['GET'])
def movie_list():
    data = Movie.query.all()
    result = movie_list_schema.jsonify(data)
    return result
