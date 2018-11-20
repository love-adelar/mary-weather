import os
import sys
from dotenv import load_dotenv
import app


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'weather.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 4000))
    print("Using:{}".format(os.environ['APP_SETTINGS']))
    app.debug=True if "-d" in sys.argv else False
    app.run('0.0.0.0', port=port)