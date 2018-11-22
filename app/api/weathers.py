from flask import jsonify, request
from app import db
from app.models import Weather
from app.api import bp


@bp.route('/weathers', methods=['GET'])
def get_weathers():
    weather = request.args.get('page', 1, type=int)
    data = Weather.to_collection_dict(Weather.query, weather, 'api.get_weathers')
    return jsonify(data)