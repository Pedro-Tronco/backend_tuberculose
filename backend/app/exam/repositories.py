from typing import Any
from datetime import datetime

from .schemas import ExamDataDTO
from ..patient.schemas import PatientDTO
from ..model.schemas import ModelOutput

from ..exceptions import ResourceNotFoundError

class ExamRepository:
    
    def __init__(self) -> None:
        self._db = {} # USING SIMPLE DICT AS STORAGE FOR NOW
        
    def save_exam_data(self, user:PatientDTO, exam_data: ExamDataDTO) -> None:
        dt_now = datetime.now().isoformat(sep=' ')
        key = str((user.CPF, 'exam_data', dt_now))
        value = dict(exam_data)
        value['DATA_HORA_EXAME'] = dt_now
        self._db[key] = value
        
    def get_exam_data(self, user:PatientDTO) -> list[dict] | list:
        key = str((user.CPF, 'exam_data')).rstrip(')')
        
        valores = list(
            v for k, v in self._db.items() 
            if k.startswith(key)
        )
        
        return valores
        
    def save_exam_results(self, user:PatientDTO, results:ModelOutput ) -> None:
        dt_now = datetime.now().isoformat(sep=' ')
        key = str((user.CPF, 'exam_result', dt_now))
        value = {
            "PROBABILIDADE": results.get('PROBABILIDADE'), 
            "CLASSIFICACAO": results.get('CLASSIFICACAO'), 
            'DATA_HORA_EXAME': dt_now
            }
        self._db[key] = value
        
    def get_exam_results(self, user:PatientDTO) -> list[dict] | list:
        key = str((user.CPF, 'exam_result')).rstrip(')')
        
        valores = list(
            v for k, v in self._db.items() 
            if k.startswith(key)
        )
        
        return valores
