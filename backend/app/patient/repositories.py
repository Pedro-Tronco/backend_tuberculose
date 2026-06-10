from typing import Any

from .schemas import PatientDTO, ExamDataDTO
from ..exceptions import ResourceNotFoundError

class PatientRepository:
    def __init__(self) -> None:
        self._db = {} # USING SIMPLE DICT AS STORAGE FOR NOW
        self._counter = 1
        
    def save_exam_data(self, patient: PatientDTO, results: ExamDataDTO) -> ExamDataDTO:
        key = str(tuple(patient.model_dump().values()))
        values = results.model_dump()
        
        self._db[key] = values
        
        return ExamDataDTO.model_validate(values)
        
    def get_exam_data_by_patient_data(self, patient: PatientDTO) -> dict[str, Any]:
        key = str(tuple(patient.model_dump().values()))
        data = self._db[key]
        
        if data is None:
            raise ResourceNotFoundError(f'No resource found for key {key}')
        
        return data

        