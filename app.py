from flask import Flask, jsonify
from flask_cors import CORS
from application.setup.config import Config
from application.database.db import init_db
from application.controller.customer import customer_bp
from application.controller.penitipan import penitipan_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)
    init_db(app)

    app.register_blueprint(customer_bp, url_prefix='/customer')
    app.register_blueprint(penitipan_bp, url_prefix='/penitipan')

    @app.route('/')
    def index():
        return jsonify({ 'message': 'API Penitipan Hewan aktif.' })

    return app