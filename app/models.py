from datetime import datetime
from app import db
import pytz


class Weather(db.Model):
    __tablename__ = 'weathers'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.now(pytz.timezone('Asia/Seoul')))
    meridiem = db.Column(db.String(64))
    temperature = db.Column(db.Float)
    weather_type = db.Column(db.String(128))
    rainfall_probability = db.Column(db.Float)
    # image_filename = "photo-1511765224389-37f0e77cf0eb"

    def __init__(self, date, meridiem, temperature, weather_type, rainfall_probability):
        self.date = date
        self.meridiem = meridiem
        self.temperature = temperature
        self.weather_type = weather_type
        self.rainfall_probability = rainfall_probability

    def __repr__(self):
        return "<{} 오늘 {} 날씨: {}°C, {}, 강수확률 {}% >" \
            .format(self.date, self.meridiem, self.temperature, self.weather_type, self.rainfall_probability)
