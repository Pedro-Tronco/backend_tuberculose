from flask import Flask

from .patient.controllers import create_patient_blueprint
from .errors import register_error_handlers

def create_app() -> Flask:

    app = Flask(__name__)
    
    register_error_handlers(app)
    
    app.register_blueprint(create_patient_blueprint(), url_prefix='/api/exam')
    
    return app

