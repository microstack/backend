from settings import db, ma


class Publish(db.Model):
    '''
    Actually, weather rss provides 2 data in a day, but this service only save
    a data. Therefore date should be 'yyyy-mm-dd'
    '''
    date = db.Column(db.String(40), unique=True, primary_key=True)
    summary = db.Column(db.String(1024))

    weathers = db.relationship('Weather', backref='publish', lazy='dynamic')

    def __repr__(self):
        return self.date


class Weather(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    date = db.Column(db.String(40))
    province = db.Column(db.String(40))
    min_temparature = db.Column(db.Integer)
    max_temparature = db.Column(db.Integer)
    weather = db.Column(db.String(20))
    reliability = db.Column(db.String(20))
    city = db.Column(db.String(30))

    publish_date = db.Column(db.String, db.ForeignKey('publish.date'))

    def __repr__(self):
        return self.date


class WeatherSchema(ma.ModelSchema):
    class Meta:
        model = Weather


class PublishSchema(ma.ModelSchema):
    class Meta:
        model = Publish


class PublishListSchema(PublishSchema):
    class Meta:
        fields = ('id', 'date')


publish_schema = PublishSchema()
publish_list_schema = PublishListSchema(many=True)
weather_schema = WeatherSchema()
