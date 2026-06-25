from flask import Flask
from flask_cors import CORS
from .controllers.velaxing import velaxing_endpoints

def create_app():
    app = Flask(__name__)

    app.register_blueprint(
        velaxing_endpoints,
        url_prefix="/estudiantes/api/v1"
    )

    CORS(app, origins="*")

    return app