import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

BACKEND_MOVIES_PORT = os.environ.get('BACKEND_MOVIES_PORT') or 5000


def set_project_paths():
    import os, sys
    sys.path.append(os.path.abspath('..'))
