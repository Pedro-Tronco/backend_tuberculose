from typing import Any
from unidecode import unidecode 

from .repositories import PatientRepository
from .schemas import PatientExamPayload, PatientDTO, ExamDataDTO

class PatientService:
    def __init__(self, patient_repo: PatientRepository) -> None:
        self.patient_repo = patient_repo
        
    def save_exam_data(self, payload: dict[Any, Any]) -> dict[str, Any]:
        validated_pl = PatientExamPayload.model_validate(payload)
        
        patient_data = PatientDTO.model_validate(validated_pl.PACIENTE)
        exam_data = ExamDataDTO.model_validate(validated_pl.DADOS)
        
        self.patient_repo.save_exam_data(patient_data, exam_data)
        
        return self.regularize_exam_data(exam_data)
    
    def get_exam_data(self, payload: dict[Any, Any]) -> dict[str, Any]:
        patient_data = PatientDTO.model_validate(payload)
        
        return self.patient_repo.get_exam_data_by_patient_data(patient_data)
        
    def regularize_exam_data(self, data: ExamDataDTO) -> dict[str, Any]:
        val_data = ExamDataDTO.model_validate(data) 
        
        reg_data = {
            key: (unidecode(value).lower() if isinstance(value, str) else value)
            for key, value in val_data
        }
        
        return reg_data
        