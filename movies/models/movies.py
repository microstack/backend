from . import db

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, 
        nullable=False)
    title = db.Column(db.String(120), unique=True)
