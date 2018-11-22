import app
from app import models, db
import urllib.request
import ssl
from bs4 import BeautifulSoup
from datetime import datetime
import pytz
from sqlalchemy import asc

ssl._create_default_https_context = ssl._create_unverified_context


class WeatherRepository:
    def __init__(self, weather_type):
        self.weather_type = weather_type
        self.weather_specification = {
            'sunny': '맑음',
            'cloudy_less': '구름조금',
            'cloudy_much': '구름많음',
            'overcast': '흐림',
            'foggy': '안개',
            'rain': '비',
            'drizzle': '이슬비',
            'shower': '소나기',
            'lightens_and_thunders': '천둥번개',
            'sleet': '진눈깨비',
            'snow': '눈'
        }[weather_type]

    @staticmethod
    def create_db():
        app.models.create_db()

    def print_weather(self):
        session = db.session
        for row in session.query(models.Weather) \
                .filter(models.Weather.weather_type == self.weather_type) \
                .order_by(asc(models.Weather.date)) \
                .all():
            print("{} 오늘 날씨 \n {}: {}°C, {}, 강수확률 {}%") \
                .format(row.date, row.meridiem, row.temperature, row.weather_type, row.rain_probability)

    def retrieve_weather(self):
        session = db.session

        url = "https://weather.naver.com/rgn/townWetr.nhn?naverRgnCd=09230109"
        page = urllib.request.urlopen(url)
        weather_type = BeautifulSoup(page, "html.parser")

        today = datetime.now(pytz.timezone('Asia/Seoul'))
        subject_text = "{} 오늘 날씨\n".format(today)

        for cell in weather_type.find_all("div", "cell", limit=2):
            meridiem = cell.find("b").string
            temperature = cell.find("span", "temp").string

            weather_type = cell.img['alt']
            rainfall_probability = cell.find("strong").string
            subject_text += "{}: {}°C, {}, 강수확률 {}%\n" \
                .format(meridiem, temperature, weather_type, rainfall_probability)
            print(subject_text)

            session.merge(models.Weather(today, meridiem, temperature,
                                         weather_type, rainfall_probability))
        session.commit()

    def get_query_data(self, session):
        return session.query(models.Weather) \
            .filter(models.Weather.weather_type == self.weather_specification) \
            .order_by(asc(models.Weather.date))
