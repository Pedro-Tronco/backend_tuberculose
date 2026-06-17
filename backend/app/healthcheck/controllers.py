from flask import Blueprint, request, jsonify

from .services import HealthcheckService

def create_heatlcheck_blueprint(health_service: HealthcheckService) -> Blueprint:
    
    health_bp = Blueprint('healthcheck_blueprint', __name__)
    
    @health_bp.route('', methods=['GET'])
    def check_health():
        health_status = health_service.check_api_liveliness()
        return jsonify(health_status), 200
    
    return health_bp
    