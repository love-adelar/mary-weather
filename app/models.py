from app import db


class Date(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, primary_key=True)
    min_temperature = db.Column(db.Float)
    max_temperature = db.Column(db.Float)
    weather_type = db.Column(db.String(128))
    rainfall_probability = db.Column(db.Float)

    def __repr__(self):
        return '<Today is {}>'.format(self.date)
