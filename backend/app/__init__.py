from flask import Flask

from .errors import register_error_handlers
from .patient.controllers import create_patient_blueprint
from .healthcheck.controllers import create_heatlcheck_blueprint

def create_app() -> Flask:

    app = Flask(__name__)
    
    register_error_handlers(app)
    
    app.register_blueprint(create_patient_blueprint(), url_prefix='/api/exam')
    app.register_blueprint(create_heatlcheck_blueprint(), url_prefix='/api/health-check')
    
    return app
