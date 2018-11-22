from app.weathers import WeatherRepository
from flask import Flask
import config
from app import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.Config().SQLALCHEMY_DATABASE_URI

with app.app_context():
    db.init_app(app)
    w = WeatherRepository('sunny')
    w.retrieve_weather()
