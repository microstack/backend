# -*- encoding: utf-8 -*-

from models import Publish, publish_schema, publish_list_schema
from models import Weather, weather_list_schema

from flask import Flask
from flask_restful import Resource


class PublishList(Resource):
    def get(self):
        data = Publish.query.all()
        return publish_list_schema.dump(data).data


# date format : yyyy-mm-dd
class PublishDetail(Resource):
    def get(self, date):
        data = Publish.query.filter_by(date=date)
        if data.count() > 0:
            data = data[0]
        return publish_schema.dump(data).data


class PublishWeather(Resource):
    def get(self, date):
        data = Publish.query.filter_by(date=date)
        weather_data = []
        if data.count() > 0:
            data = data[0]
            weather_data = list(data.weathers)
            print(weather_data)

        return weather_list_schema.dump(weather_data).data


from flask_restful import Api
from settings import app

api = Api(app)
api.add_resource(PublishList, '/weather/publishes/')
api.add_resource(PublishDetail, '/weather/publishes/<string:date>/')
api.add_resource(PublishWeather, '/weather/publishes/<string:date>/weather/')
