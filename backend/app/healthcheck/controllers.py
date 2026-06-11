from flask import Blueprint, request, jsonify

from .repositories import DBHealthRepository
from .services import HealthcheckService

def create_heatlcheck_blueprint() -> Blueprint:
    
    health_bp = Blueprint('healthcheck_blueprint', __name__)
    
    health_repo = DBHealthRepository()
    health_service = HealthcheckService(health_repo)
    
    @health_bp.route('', methods=['GET'])
    def check_health():
        health_status = health_service.check_api_liveliness()
        return jsonify(health_status), 200
    
    return health_bp
    