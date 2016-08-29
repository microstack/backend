# -*- encoding: utf-8 -*-

from models import Publish, publish_schema

from flask import Flask
from flask_restful import Resource


class Publish(Resource):
    def get(self):
        data = Publish.query.all()
        return publish_schema.dump(data).data


from flask_restful import Api
from settings import app

api = Api(app)
api.add_resource(Publish, '/weather/publish/')
