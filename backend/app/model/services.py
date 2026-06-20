from unidecode import unidecode
from typing import Any
import cloudpickle
import pandas as pd
from pathlib import Path
import keras

from pydantic import BaseModel

from .repositories import ModelRepository
from .schemas import ModelMetadata, ModelOutput

from ..exam.schemas import ExamDataDTO

from ..exceptions import InternalServerError


class ModelService:

    def __init__(self, model_repo: ModelRepository) -> None:
        self.model_repo = model_repo
        self._model_cache: dict[str, object] = {}

    def get_models(self) -> list[ModelMetadata]:
        models = self.model_repo.list_models()

        if models is None or len(models) == 0:
            raise InternalServerError('Nenhum modelo registrado corretamente dentro de /models')

        return models

    def load_artifact(self, model_id: str | Path):
        key = str(model_id)
        if key in self._model_cache:
            return self._model_cache[key]

        # resolve artifact path
        if isinstance(model_id, (str,)):
            artifact = self.model_repo.get_model_artifact(model_id)
        else:
            artifact = Path(model_id)

        if artifact is None or not Path(artifact).exists():
            raise InternalServerError(f"Model artifact not found for '{model_id}'")

        prepro_file = self.model_repo.read_model_metadata(artifact.parent).get("preprocessor")

        if prepro_file is None:
            preprocessor = None
        else:
            prepro_artifact = Path(__file__).resolve().parents[3] / "preprocessing" / prepro_file
            with open(prepro_artifact, 'rb') as f:
                preprocessor = cloudpickle.load(f)

        if artifact.suffix == ".pkl" or artifact.suffix == ".pickle":
            with open(artifact, "rb") as f:
                model = cloudpickle.load(f)
                
        elif artifact.suffix == '.keras':
            model = keras.models.load_model(artifact)
                
        else:
            raise InternalServerError(f"Unsopported extension for model: {artifact.suffix}") 
                
        self._model_cache[key] = model
        return model, preprocessor

    def predict_with_model(self, model_artifact: str | Path, data: ExamDataDTO) -> ModelOutput:
        # return 100.0 # fallback to test the rest of the backend
        model, preprocesor = self.load_artifact(model_artifact)
        features = self.regularize_exam_data(data)
        try:
            if preprocesor is not None:
                features = preprocesor.transform(features)
                
            result = model.predict_proba(features) if hasattr(model, 'predict_proba') else model.predict(features)
            
            probability = float(result[0][1])
            
            if probability <= 0.25:
                category = 'Muito improvável'
            elif probability <= 0.5:
                category = 'Improvável'
            elif probability <= 0.75:
                category = 'Provável'
            else:
                category = 'Muito provável'

            output = ModelOutput(
                CLASSIFICACAO=category,
                PROBABILIDADE=round(probability, 2)
            )
            
            return output
            
        except Exception as exc:
            raise InternalServerError(f'Error running model prediction: {exc}')

    def regularize_exam_data(self, exam_data: ExamDataDTO):
        # support Pydantic BaseModel and plain dict
        if isinstance(exam_data, BaseModel):
            data_items = exam_data.model_dump().items()
        elif isinstance(exam_data, dict):
            data_items = exam_data.items()
        else:
            # try to coerce
            try:
                data_items = dict(exam_data).items()
            except Exception:
                raise InternalServerError('Unsupported exam data format for regularization')

        features = pd.DataFrame([{
            key: (unidecode(value).lower().replace(' ', '_') if isinstance(value, str) else value)
            for key, value in data_items
        }])

        return features