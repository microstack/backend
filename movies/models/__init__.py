import os, sys
sys.path.insert(0, os.path.abspath(".."))

from movies.settings import db, ma
from . import movie
from . import actor
