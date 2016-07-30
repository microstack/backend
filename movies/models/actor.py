from . import db


class Actor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    link = db.Column(db.String(512), unique=True)

    def __repr__(self):
        return self.name
