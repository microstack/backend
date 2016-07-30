import requests
import os

from flask import render_template
from flask import Flask
app = Flask(__name__)


@app.route('/movies/')
def movie_list():
    return '/movies/ from movies_backed'


if __name__ == '__main__':
    port = os.environ.get('MOVIES_BACKEND_PORT')
    app.run(port=port)
