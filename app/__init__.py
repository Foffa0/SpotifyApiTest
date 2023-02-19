from flask import Flask
from app.config import Config
import os


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    from app.main.routes import main
    app.register_blueprint(main)

    from app.data.Song import song
    app.register_blueprint(song)

    app.config['SECRET_KEY'] = os.urandom(64)
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['SESSION_FILE_DIR'] = './.flask_session/'

    return app