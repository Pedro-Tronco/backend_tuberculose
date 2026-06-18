from unidecode import unidecode
from typing import Any
import joblib
import cloudpickle
import xgboost
import numpy as np
import pandas as pd
from pathlib import Path

from pydantic import BaseModel

from .repositories import ModelRepository
from .schemas import ModelMetadata

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

    def load_artifact(self, model_id: str | Path) -> object:
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

        if artifact.suffix == ".joblib":
            model = joblib.load(artifact)

        elif artifact.suffix == ".pkl" or artifact.suffix == ".pickle":
            with open(artifact, "rb") as f:
                model = cloudpickle.load(f)
                
        else:
            raise InternalServerError(f"Unsopported extension for model: {artifact.suffix}") 
                
        self._model_cache[key] = model
        return model

    def predict_with_model(self, model_id: str | Path, data: ExamDataDTO) -> float:
        model = self.load_artifact(model_id)
        
        reg_data = self.regularize_exam_data(data)

        # if model implements sklearn-like API
        try:
            features = np.array([list(reg_data)])
            result = model.predict_proba(features) if hasattr(model, 'predict_proba') else model.predict(features)
            # handle classifiers returning array
            if hasattr(result, '__len__') and not isinstance(result, float):
                # predict_proba -> take positive class prob if shape (n,2)
                if result.ndim == 2 and result.shape[1] > 1:
                    return float(result[0][1])
                return float(result[0])
            return float(result)
        except Exception as exc:
            raise InternalServerError(f'Error running model prediction: {exc}')

    def regularize_exam_data(self, exam_data: ExamDataDTO) -> pd.DataFrame:
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

        reg_df = pd.DataFrame([{
            key: (unidecode(value).lower().replace(' ', '_') if isinstance(value, str) else value)
            for key, value in data_items
        }])
        
        # print(reg_df)
        
        # # ==preprocessor = joblib.load(r"C:\Users\Pedro Augusto\Documents\Atitus\projetos\5o_semestre\projeto_tuberculose\backend\models\Processador_Exec-1_3Camadas_2048Neur_AUC-0.8217_F1-0.8195.joblib")

        # reg_data = preprocessor.transform(reg_df)

        return reg_df