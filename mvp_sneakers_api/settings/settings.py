__all__ = "settings"

from functools import lru_cache
from pathlib import Path
from typing import Dict

from pydantic_settings import BaseSettings


class Celery(BaseSettings):
    class Config:
        env_prefix = "CELERY_"

    max_loop_interval: str = "60"


class Model(BaseSettings):
    image_size: int = 128
    label: Dict = {
        0: "adidas",
        1: "Nike",
        2: "Vans",
        3: "Jordan",
        4: "New Balance",
    }


class RabbitMQ(BaseSettings):
    class Config:
        env_prefix = "RABBITMQ_"

    host: str = "localhost"
    port: int = 5672
    username: str = "parser"
    password: str = "parser"


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
    celery: Celery = Celery()
    rabbit: RabbitMQ = RabbitMQ()
    model: Model = Model()


@lru_cache
def get_settings() -> Settings:
    """Singleton"""
    return Settings()


settings = get_settings()
