from app import models
import urllib.requests
import ssl
from bs4 import BeautifulSoup
from datetime import datetime
import pytz

ssl._create_default_https_context = ssl._create_unverified_context


class WeatherRepository:
    def print_weather(self):
        session = models.Session()
        for row in session.query(models.Weather) \
                .filter(models.Weather.today==self.today) \
                .all():
            print("{} 오늘 날씨 \n {}: {}°C, {}, 강수확률 {}%").format(today, meridiem, temperature, weather_type, rain_probability)

    def get_weather(self):
        url = "https://weather.naver.com/rgn/townWetr.nhn?naverRgnCd=09230109"
        page = urllib.request.urlopen(url)
        weather_type = BeautifulSoup(page, "html.parser")

        today = datetime.now(pytz.timezone('Asia/Seoul')).strftime("%y년 %m월 %d일")
        text = "{} 오늘 날씨\n".format(today)

        for cell in weather_type.find_all("div", "cell", limit=2):
            meridiem = cell.find("b").string
            temperature = cell.find("span", "temp").string
            weather_type = cell.img['alt']
            rain_probability = cell.find("strong").string
            text += "{}: {}°C, {}, 강수확률 {}%\n".format(meridiem, temperature, weather_type, rain_probability)
            print(text)

        return text

