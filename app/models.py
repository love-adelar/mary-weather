from datetime import datetime
from app import db
import pytz


class Weather(db.Model):
    __tablename__ = 'weathers'
    id = db.Column(db.Integer, primary_key=True)
    today = db.Column(db.DateTime, primary_key=True, default=datetime.now(pytz.timezone('Asia/Seoul')))
    temperature = db.Column(db.Float)
    weather_type = db.Column(db.String(128))
    rainfall_probability = db.Column(db.Float)

    def __init__(self, date, today, temperature, weather_type, rainfall_probability):
        self.date = date
        self.today = today
        self.temperature = temperature
        self.weather_type = weather_type
        self.rainfall_probability = rainfall_probability

    def __repr__(self):
        return '<오늘 {}의 최저기온은 {}, and 최대기온은 {}입니다. 강수확률은 {}로 {}이겠습니다. >'\
            .format(self.today, self.low, self.high, self.rainfall_probability, self.weather_type)

