from pydantic import BaseModel

class PatientDTO(BaseModel):
    NOME: str
    CPF: int