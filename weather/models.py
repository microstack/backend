from settings import db, ma


class PubDate(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    date = db.Column(db.String(40), unique=True)

    def __repr__(self):
        return self.date


class Weather(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    date = db.Column(db.String(40))
    province = db.Column(db.String(40))
    city = db.Column(db.String(30))
    min_temparature = db.Column(db.Integer)
    max_temparature = db.Column(db.Integer)
    reliablity = db.Column(db.String(20))

    def __repr__(self):
        return self.date


class WeatherSchema(ma.ModelSchema):
    class Meta:
        model = Weather


class PubDateSchema(ma.ModelSchema):
    class Meta:
        model = PubDate


pub_date_schema = PubDateSchema(many=True)
weather_schema = WeatherSchema()
