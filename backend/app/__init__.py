from flask import Flask

from .wiring import build_container
from .error_handlers import register_error_handlers
from .patient.controllers import create_patient_blueprint
from .healthcheck.controllers import create_heatlcheck_blueprint
from .exam.controller import create_exam_blueprint

def create_app() -> Flask:

    app = Flask(__name__)
    
    register_error_handlers(app)
    
    container = build_container()

    app.register_blueprint(create_patient_blueprint(container.patient_service), url_prefix='/api/patient')
    app.register_blueprint(create_heatlcheck_blueprint(container.health_service), url_prefix='/api/health-check')
    app.register_blueprint(create_exam_blueprint(container.exam_service), url_prefix='/api/exam')
    
    return app
