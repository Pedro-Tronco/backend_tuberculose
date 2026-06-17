from typing import Literal
from pydantic import BaseModel

from ..patient.schemas import PatientDTO

class ExamDataDTO(BaseModel):
    AGRAVTABAC: Literal[
        "Ignorado",
        "Não",
        "Sim"
    ]
    AGRAVDROGA: Literal[
        "Ignorado",
        "Não",
        "Sim"
    ]
    AGRAVAIDS: Literal[
        "Ignorado",
        "Não",
        "Sim"
    ]    
    AGRAVDIABE: Literal[
        "Ignorado",
        "Não",
        "Sim"
    ]
    HIV: Literal[
        "Não realizado",
        "Negativo",
        "Positivo",
        "Em andamento"
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
        "Masculino",
        "Feminino",
        "Ignorado"
    ]
    BACILOSC_E: Literal[
        "Positivo",
        "Negativo",
        "Não realizado"
    ]
    CULTURA_ES: Literal[
        "Positiva",
        "Negativa",
        "Em andamento",
        "Não realizada"
    ]
    RAIOX_TORA: Literal[
        "Suspeito",
        "Normal",
        "Outra patologia",
        "Não realizado"
    ]
    CS_RACA: Literal[
        "Branca",
        "Preta",
        "Amarela",
        "Parda",
        "Indígena",
        "Ignorado"
    ]
    TRATAMENTO: Literal[
        "Caso novo",
        "Recidiva",
        "Reingresso após abandono",
        "Transferência",
        "Não sabe"
    ]
    CULTURA_OU: Literal[
        "Positiva",
        "Negativa",
        "Em andamento",
        "Não realizada"
    ]
    HISTOPATOL: Literal[
        "BAAR positivo",
        "Sugestivo TB",
        "Não sugestivo",
        "Não realizado"
    ]
    TRATSUP_AT: Literal[
        "Sim",
        "Não"
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
        "Ignorado"
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