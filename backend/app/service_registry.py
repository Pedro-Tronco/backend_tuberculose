from dataclasses import dataclass

from .patient.repositories import PatientRepository
from .patient.services import PatientService

from .healthcheck.repositories import HealthCheckRepository
from .healthcheck.services import HealthcheckService

from .exam.repositories import ExamRepository
from .exam.services import ExamService

from .model.services import ModelService
from .model.repositories import ModelRepository

@dataclass(frozen=True)
class AppContainer:
    patient_service: PatientService
    health_service: HealthcheckService
    model_service: ModelService
    exam_service: ExamService

def build_container() -> AppContainer:
    patient_repo = PatientRepository()
    patient_service = PatientService(patient_repo)

    health_repo = HealthCheckRepository()
    health_service = HealthcheckService(health_repo)
    
    morel_repo = ModelRepository()
    model_service = ModelService(morel_repo)

    exam_repo = ExamRepository()
    exam_service = ExamService(exam_repo, model_service, patient_service)

    return AppContainer(
        patient_service=patient_service,
        health_service=health_service,
        model_service=model_service,
        exam_service=exam_service,
    )