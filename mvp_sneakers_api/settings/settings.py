__all__ = "settings"

from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings


class EfficientSettings(BaseSettings):
    class Config:
        env_prefix = "EFFICIENTNET_"

    host: str = "triton"
    port: int = 8000
    path: str = "efficientnet/infer"


class Redis(BaseSettings):
    class Config:
        env_prefix = "REDIS_"

    host: str = "localhost"
    port: int = 6379
    db: int = 1


class UvicornURL(BaseSettings):
    """Represents Uvicorn settings"""

    class Config:
        env_prefix = "UVICORN_"

    host: str = "0.0.0.0"
    port: str = "8000"


class ProjectSettings(BaseSettings):
    """Represents Project settings"""

    class Config:
        env_prefix = "SETTINGS_"

    base_dir: Path = Path(__file__).resolve().parent.parent.parent
    project_name: str = "mvp_sneakers"
    log_file: bool = False
    models_path: str = "/data/models"


class Settings(BaseSettings):
    api: UvicornURL = UvicornURL()
    project: ProjectSettings = ProjectSettings()
    redis: Redis = Redis()
    efficientnet: EfficientSettings = EfficientSettings()


@lru_cache
def get_settings() -> Settings:
    """Singleton"""
    return Settings()


settings = get_settings()
