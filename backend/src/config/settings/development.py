from src.config.settings.base import BackendBaseSettings
from src.config.settings.environment import Environment


class BackendDevSettings(BackendBaseSettings):
    DESCRIPTION: str | None = "Project description."
    DEBUG: bool = True
    ENVIRONMENT: Environment = Environment.DEVELOPMENT
