from flask import Blueprint, jsonify

from .services import ModelService

def create_model_blueprint(model_service: ModelService) -> Blueprint:

    model_bp = Blueprint('model_blueprint', __name__)
    
    @model_bp.route('/list', methods=['GET'])
    def get_all_models():
        models = model_service.get_models()
        return jsonify(models), 200
        
    return model_bp