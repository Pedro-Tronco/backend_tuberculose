from typing import TypedDict


class ModelMetadata(TypedDict):
    id: str
    name: str
    description: str
    path: str
    
class ModelOutput(TypedDict):
    CLASSIFICACAO: str
    PROBABILIDADE: float