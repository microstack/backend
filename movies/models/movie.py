from . import db, ma
from .actor import Actor


actors = db.Table('actors',
    db.Column('actor_id', db.Integer, db.ForeignKey('actor.id')),
    db.Column('movie_id', db.Integer, db.ForeignKey('movie.id'))
)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    age = db.Column(db.String(20))
    director = db.Column(db.String(50))
    netizen_grade = db.Column(db.Float)
    release_date = db.Column(db.DateTime)
    running_time = db.Column(db.Integer)
    story = db.Column(db.String(8000))
    thumbnail = db.Column(db.String(512))
    actors = db.relationship('Actor', secondary=actors,
        backref=db.backref('movies', lazy='dynamic'))

    def __repr__(self):
        return self.title


class MovieSchema(ma.ModelSchema):
    class Meta:
        model = Movie


movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)
