import requests
import os

from models.movie import Movie, movie_list_schema, movies_schema, movie_schema
from models.actor import Actor, actors_schema, actor_schema

from flask import jsonify, json

from settings import app


@app.route('/movies/', methods=['GET'])
def movie_list():
    data = Movie.query.all()
    result = movie_list_schema.jsonify(data)
    return result

@app.route('/movies/<id>/', methods=['GET'])
def movie_detail(id):
    data = Movie.query.filter_by(id=id).first()
    result = movie_schema.jsonify(data)
    return result

@app.route('/movies/<id>/actors', methods=['GET'])
def movie_actors(id):
    data = Movie.query.filter_by(id=id).first()
    result = actors_schema.jsonify(data.actors)
    return result
