from unidecode import unidecode
from typing import Any

from ..exam.schemas import ExamDataDTO

class ModelService:

    def predict(self, data: ExamDataDTO) -> float:
        reg_data = self.regularize_exam_data(data)
        return 50

    def regularize_exam_data(self, exam_data: ExamDataDTO) -> dict[str, Any]:
        reg_data = {
            key: (unidecode(value).lower().replace(' ', '_') if isinstance(value, str) else value)
            for key, value in exam_data
        }
        
        return reg_data