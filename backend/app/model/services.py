from unidecode import unidecode
from typing import Any

from .repositories import ModelRepository
from .schemas import ModelMetadata

from ..exam.schemas import ExamDataDTO

from ..exceptions import InternalServerError

class ModelService:

    def __init__(self, model_repo: ModelRepository) -> None:
        self.model_repo = model_repo

    def predict(self, data: ExamDataDTO) -> float:
        reg_data = self.regularize_exam_data(data)
        return 50
    
    def get_models(self) -> list[ModelMetadata]:
        models = self.model_repo.list_models()
        
        if models is None or len(models) == 0:
            raise InternalServerError('Nenhum modelo registrado corretamente dentro de /models')
        
        return models

    def regularize_exam_data(self, exam_data: ExamDataDTO) -> dict[str, Any]:
        reg_data = {
            key: (unidecode(value).lower().replace(' ', '_') if isinstance(value, str) else value)
            for key, value in exam_data
        }
        
        return reg_data