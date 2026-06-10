from flask import Blueprint, request, jsonify

from .repositories import PatientRepository
from .services import PatientService

def create_patient_blueprint() -> Blueprint:

    patient_bp = Blueprint('patient_blueprint', __name__)

    patient_repo = PatientRepository()
    patient_service = PatientService(patient_repo)

    @patient_bp.route('/predict', methods=['GET'])
    def create_exam():
        data = request.json or {}
        created_exam = patient_service.save_exam_data(data)
        return jsonify(created_exam), 200
        
    @patient_bp.route('/history', methods=['GET'])
    def get_exam_data():
        data = request.json or {}
        exam_data = patient_service.get_exam_data(data)
        return jsonify(exam_data), 200
        
    return patient_bp