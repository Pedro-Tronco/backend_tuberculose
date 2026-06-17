from typing import Any

from ..patient.schemas import PatientDTO
from .schemas import ExamDataDTO

from ..exceptions import ResourceNotFoundError

class ExamRepository:
    
    def __init__(self) -> None:
        self._db = {} # USING SIMPLE DICT AS STORAGE FOR NOW
        
    def save_exam_data(self, user:PatientDTO, exam_data: ExamDataDTO) -> None:
        key = str((user.CPF, 'exam_data'))
        value = exam_data
        self._db[key] = value
        
    def get_exam_data(self, user:PatientDTO) -> ExamDataDTO | None:
        try:
            key = str((user.CPF, 'exam_data'))
            return self._db[key]
        
        except KeyError:    
            raise ResourceNotFoundError('Nenhum registro de exames encontrado para paciente informado')
        
    def save_exam_results(self, user:PatientDTO, results: float) -> None:
        key = str((user.CPF, 'exam_result'))
        value = results
        self._db[key] = value
        
    def get_exam_results(self, user:PatientDTO) -> ExamDataDTO | None:
        try:
            key = str((user.CPF, 'exam_result'))
            return self._db[key]
        
        except KeyError:    
            raise ResourceNotFoundError('Nenhum resultado de exame encontrado para paciente informado')
