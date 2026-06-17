from typing import Any
from unidecode import unidecode 

from .repositories import PatientRepository
from .schemas import PatientDTO

from ..exceptions import ResourceNotFoundError

class PatientService:
    def __init__(self, patient_repo: PatientRepository) -> None:
        self.patient_repo = patient_repo
       
    def create_patient(self, patient_payload: dict[str, Any] | PatientDTO):
        val_patient = PatientDTO.model_validate(patient_payload)
        
        # Verify if user already exists before saving
        patient = next(
            (value for value in self.patient_repo.get_all_values() if value["CPF"] == val_patient.CPF),
            None
        )
        
        if patient is None:
            patient = self.patient_repo.create_user(val_patient)
        
        return dict(patient)
    
    def get_all_patients(self):
        patients = self.patient_repo.get_all_values()
        
        if patients is None or len(patients) == 0:
            raise ResourceNotFoundError("Nenhum paciente cadastrado")

        return patients
        