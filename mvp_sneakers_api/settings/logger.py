__all__ = "LOGGING"
from pathlib import Path

log_dir = Path(__file__).parent.parent.parent / "logs"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "json": {
            "()": "ecs_logging.StdlibFormatter",
        },
        "uvicorn-default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "use_colors": None,
        },
        "uvicorn-access": {
            "()": "uvicorn.logging.AccessFormatter",
            "use_colors": None,
        },
    },
    "handlers": {
        "fast_api_inference_handler": {
            "level": "INFO",
            "formatter": "json",
            "class": "logging.FileHandler",
            "filename": log_dir / "mvp_sneakers_api.json",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
        },
        "uvicorn-default": {
            "level": "INFO",
            "formatter": "json",
            "class": "logging.FileHandler",
            "filename": log_dir / "uvicorn.json",
        },
        "uvicorn-access": {
            "formatter": "uvicorn-access",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
    },
    "loggers": {
        "": {
            "handlers": ["console"],
            "level": "INFO",
        },
        "fast_api_inference": {
            "handlers": ["fast_api_inference_handler"],
            "level": "INFO",
            "propagate": False,
        },
        "uvicorn.error": {
            "handlers": ["uvicorn-default", "console"],
            "level": "INFO",
            "propagate": False,
        },
        "uvicorn.access": {
            "handlers": ["uvicorn-access", "console"],
            "level": "INFO",
            "propagate": False,
        },
    },
    "root": {
        "level": "INFO",
        "handlers": [
            "console",
        ],
    },
}
