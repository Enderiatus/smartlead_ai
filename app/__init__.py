from flask import Flask
from flask_cors import CORS
from config import Configs
from app.database import createDatabase

def createApp():
    app = Flask(__name__)
    
    CORS(app, origins=Configs.CORS_ALLOWED_ORIGINS)
    
    with app.app_context():
        createDatabase()
        
    # Rotaları API öneki ile sisteme kaydediyoruz
    from app.routes import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')
    
    return app
