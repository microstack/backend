# -*- encoding: utf-8 -*-


from flask import Flask
from flask_restful import Resource

from flask_restful import Api
from settings import app

api = Api(app)
