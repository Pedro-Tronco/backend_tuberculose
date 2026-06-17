from flask import Blueprint, request, jsonify

from .services import PatientService

def create_patient_blueprint(patient_service: PatientService) -> Blueprint:

    patient_bp = Blueprint('patient_blueprint', __name__)

    @patient_bp.route('/create', methods=['POST'])
    def create_patient():
        data = request.json or {}
        created_patient = patient_service.create_patient(data)
        return jsonify(created_patient), 201
    
    @patient_bp.route('/all', methods=['GET'])
    def get_all_patients():
        patients = patient_service.get_all_patients()
        return jsonify(patients), 200
        
    return patient_bp