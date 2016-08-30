import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from celery import Celery


app = Flask(__name__)

# http://blog.miguelgrinberg.com/post/using-celery-with-flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['CELERY_BROKER_URL'] = 'amqp://guest@localhost//'
db = SQLAlchemy(app)
ma = Marshmallow(app)

BACKEND_WEATHER_PORT = os.environ.get('BACKEND_WEATHER_PORT') or 5000

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)


def set_project_paths():
    import os, sys
    sys.path.append(os.path.abspath('..'))
