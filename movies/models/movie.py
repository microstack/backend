from . import db

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True)
    age = db.Column(db.String(20))
    director = db.Column(db.String(50)) 
    netizen_grade = db.Column(db.Float)
    release_date = db.Column(db.DateTime)
    running_time = db.Column(db.Integer)
    story = db.Column(db.String(8000))
    thumbnail = db.Column(db.String(512))

    def __repr__(self):
        return self.title
