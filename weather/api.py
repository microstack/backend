# -*- encoding: utf-8 -*-

from models import PubDate, pub_date_schema

from flask import Flask
from flask_restful import Resource


class PubDates(Resource):
    def get(self):
        data = PubDate.query.all()
        return pub_date_schema.dump(data).data


from flask_restful import Api
from settings import app

api = Api(app)
api.add_resource(PubDates, '/weather/pub-dates/')
