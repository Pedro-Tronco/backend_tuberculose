from flask import Blueprint, request, jsonify

from .services import ExamService

def create_exam_blueprint(exam_service: ExamService) -> Blueprint:

    exam_bp = Blueprint('exam_blueprint', __name__)

    @exam_bp.route('/predict', methods=['GET'])
    def create_exam():
        data = request.json or {}
        created_exam = exam_service.generate_results(data)
        return jsonify(created_exam), 200
        
    @exam_bp.route('/history', methods=['GET'])
    def get_exam_data():
        data = request.json or {}
        exam_data = exam_service.get_exam_data(data)
        return jsonify(exam_data), 200
    
    @exam_bp.route('/results', methods=['GET'])
    def get_exam_results():
        data = request.json or {}
        exam_results = exam_service.get_results(data)
        return jsonify(exam_results), 200
        
    return exam_bp