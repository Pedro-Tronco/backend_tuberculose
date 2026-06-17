from __future__ import annotations

import json
from pathlib import Path

from .schemas import ModelMetadata

class ModelRepository:
    def __init__(self, models_path: Path | str | None = None) -> None:
        self.models_path = Path(models_path) if models_path else Path(__file__).resolve().parents[2] / "models"
        if not self.models_path.exists() or not self.models_path.is_dir():
            raise FileNotFoundError(f"Models directory not found: {self.models_path}")

    def list_models(self) -> list[ModelMetadata]:
        models = []
        for folder in sorted(self.models_path.iterdir()):
            if not folder.is_dir():
                continue
            models.append(self._read_model_metadata(folder))
        return models

    def _read_model_metadata(self, folder: Path) -> ModelMetadata:
        metadata_file = folder / "model.json"
        model_path = str(folder.resolve())

        if metadata_file.exists() and metadata_file.is_file():
            try:
                metadata = json.loads(metadata_file.read_text(encoding="utf-8"))
                return {
                    "id": folder.name,
                    "name": str(metadata.get("name", folder.name)),
                    "description": str(metadata.get("description", "")),
                    "path": model_path,
                }
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON in {metadata_file}: {exc}") from exc

        return {
            "id": folder.name,
            "name": folder.name,
            "description": "",
            "path": model_path,
        }
