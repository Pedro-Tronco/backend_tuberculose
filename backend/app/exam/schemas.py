from typing import Literal, TypedDict
from pydantic import BaseModel
from datetime import datetime

from ..patient.schemas import PatientDTO


class ExamDataDTO(BaseModel):
    AGRAVTABAC: Literal[
        "Ignorado",
        "Não",
        "Sim",
        None
    ]
    AGRAVDROGA: Literal[
        "Ignorado",
        "Não",
        "Sim",
        None
    ]
    AGRAVAIDS: Literal[
        "Ignorado",
        "Não",
        "Sim",
        None
    ]    
    AGRAVDIABE: Literal[
        "Ignorado",
        "Não",
        "Sim",
        None
    ]
    HIV: Literal[
        "Não realizado",
        "Negativo",
        "Positivo",
        "Em andamento",
        None
    ]
    POP_RUA: Literal[
        "Não",
        "Sim"
    ]
    POP_LIBER: Literal[
        "Não",
        "Sim"
    ]
    POP_IMIG: Literal[
        "Não",
        "Sim"
    ]
    CS_SEXO: Literal[
        "M",
        "F",
        "I"
    ]
    BACILOSC_E: Literal[
        "Positivo",
        "Negativo",
        "Não realizado",
        "Não se aplica"
    ]
    RAIOX_TORA: Literal[
        "Suspeito",
        "Normal",
        "Outra patologia",
        "Não realizado",
        None
    ]
    CS_RACA: Literal[
        "Branca",
        "Preta",
        "Amarela",
        "Parda",
        "Indígena",
        "Ignorado",
        None
    ]
    TRATAMENTO: Literal[
        "Caso novo",
        "Recidiva",
        "Reingresso após abandono",
        "Transferência",
        "Não sabe"
    ]
    CS_ESCOL_N: Literal[
        "Analfabeto",
        "1ª a 4ª série incompleta",
        "4ª série completa",
        "5ª a 8ª série incompleta",
        "Ensino fundamental completo",
        "Ensino médio incompleto",
        "Ensino médio completo",
        "Superior incompleto",
        "Superior completo",
        "Ignorado",
        "Não se aplica"
    ]
    SG_UF_NOT: Literal [
        "AC", "AL", "AP", "AM", "BA",
        "CE", "DF", "ES", "GO", "MA",
        "MT", "MS", "MG", "PA", "PB",
        "PR", "PE", "PI", "RJ", "RN",
        "RS", "RO", "RR", "SC", "SP",
        "SE", "TO"
    ]
    IDADE_ANOS: int
    
class PatientExamPayload(BaseModel):
    PACIENTE: PatientDTO
    DADOS: ExamDataDTO
    MODELO: str