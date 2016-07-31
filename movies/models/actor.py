from . import db, ma


class Actor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    link = db.Column(db.String(512), unique=True)

    def __repr__(self):
        return self.name


class ActorSchema(ma.ModelSchema):
    class Meta:
        model = Actor


actor_schema = ActorSchema()
actors_schema = ActorSchema(many=True)
