from flask import render_template
from app.main import bp
from app.models import Weather
import random

file_names = [
    "photo-1511765224389-37f0e77cf0eb",
    "photo-1497445462247-4330a224fdb1",
    "photo-1426604966848-d7adac402bff",
    "photo-1502630859934-b3b41d18206c",
    "photo-1498471731312-b6d2b8280c61",
    "photo-1515023115689-589c33041d3c",
    "photo-1504214208698-ea1916a2195a",
    "photo-1515814472071-4d632dbc5d4a",
    "photo-1511407397940-d57f68e81203",
    "photo-1518481612222-68bbe828ecd1",
    "photo-1505058707965-09a4469a87e4",
    "photo-1423012373122-fff0a5d28cc9"
]


@bp.route('/', methods=['GET'])
@bp.route('/index', methods=['GET'])
def index():
    weathers = Weather.query.all()

    for weather in weathers:
        weather.image_filename = random.choice(file_names)
    return render_template('index.html', title='Home', weathers=weathers)


@bp.route('/weather', methods=['GET'])
def get_weather():
    weathers = Weather.query.all()
    return render_template('weather.html', title='Home', weathers=weathers)
