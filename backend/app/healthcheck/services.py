from .repositories import HealthCheckRepository

class HealthcheckService:
    def __init__(self, healt_repo: HealthCheckRepository) -> None:
        self.health_repo = healt_repo
        
    def check_api_liveliness(self) -> dict:
        return {
            "api_status": True,
            "db_status": self.health_repo.check_db_health()
        }