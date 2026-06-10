from typing import Any

from .repositories import PatientRepository
from .schemas import PatientExamPayload, PatientDTO

class PatientService:
    def __init__(self, patient_repo: PatientRepository) -> None:
        self.patient_repo = patient_repo
        
    def save_exam_data(self, payload: dict[Any, Any]) -> dict[str, Any]:
        validated_pl = PatientExamPayload.model_validate(payload)
        
        patient_data = validated_pl.PACIENTE
        exam_data = validated_pl.DADOS
        
        return self.patient_repo.save_exam_data(patient_data, exam_data)
    
    def get_exam_data(self, payload: dict[Any, Any]) -> dict[str, Any]:
        patient_data = PatientDTO.model_validate(payload)
        
        return self.patient_repo.get_exam_data_by_patient_data(patient_data)
        
        
        
        