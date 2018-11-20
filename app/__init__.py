from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)
    #
    # app.config.from_object(os.environ['APP_SETTINGS'])
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    return app


from app import models
from app.main import routes


