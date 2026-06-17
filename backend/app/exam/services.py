from typing import Any

from .repositories import ExamRepository
from ..model.services import ModelService
from ..patient.services import PatientService

from .schemas import ExamDataDTO, PatientExamPayload
from ..patient.schemas import PatientDTO

from ..exceptions import ResourceNotFoundError

class ExamService:
    
    def __init__(self, exam_repo: ExamRepository, model_service: ModelService, patient_service: PatientService) -> None:
        self.exam_repo = exam_repo
        self.model_service = model_service
        self.patient_service = patient_service

    def generate_results(self, data: dict) -> dict[str, Any]:
        payload = PatientExamPayload.model_validate(data)
        patient = payload.PACIENTE
        exam_data = payload.DADOS
        
        self.patient_service.create_patient(patient)
        self.exam_repo.save_exam_data(patient, exam_data)
        
        exam_results = self.model_service.predict(exam_data)
        
        self.exam_repo.save_exam_results(patient, exam_results)
        
        return {'PROBABILIDADE': exam_results}
    
    def get_exam_data(self, data: dict):
        patient = PatientDTO.model_validate(data)
        exam_data = self.exam_repo.get_exam_data(patient)
    
        if exam_data is None:
            raise ResourceNotFoundError("Exam data not found for specified patient")
        
        return dict(exam_data)
    
    def get_results(self, data: dict):
        patient = PatientDTO.model_validate(data)
        result = self.exam_repo.get_exam_results(patient)
         
        if result is None:
            raise ResourceNotFoundError("Exam results not found for specified patient")
        
        return {'RESULTADO': result}
         

    