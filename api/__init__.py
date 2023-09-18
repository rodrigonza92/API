from flask import Flask
from flask_cors import CORS
from config import Config

from .routes.user_bp import user_bp

from .database import DatabaseConnection

def init_app():
    """Crea y configura la aplicación Flask"""
    
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    
    CORS(app, supports_credentials=True)

    app.config.from_object(
        Config
    )

    DatabaseConnection.set_config(app.config)

    app.register_blueprint(user_bp, url_prefix = '/users')
    #app.register_blueprint(server_bp, url_prefix = '/server')
    #app.register_blueprint(channel_bp, url_prefix = '/channel')
    #app.register_blueprint(massage_bp, url_prefix = '/massages')

    #app.register_blueprint(errors, url_prefix = '/errors')

    return app