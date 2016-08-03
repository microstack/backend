from . import db, ma


class Genre(db.Model):
    name = db.Column(db.String(20), unique=True, primary_key=True)

    def __repr__(self):
        return self.name


class GenreSchema(ma.ModelSchema):
    class Meta:
        model = Genre


genres_schema = GenreSchema(many=True)
