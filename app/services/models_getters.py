import logging
import os
from abc import ABC, abstractmethod

from app.settings.settings import settings

LOCAL_MODELS_PATH = (
    os.path.dirname(settings.project.base_dir) + settings.project.models_path
)

logger = logging.getLogger(__name__)


class AbstractModelGetter(ABC):
    @property
    @abstractmethod
    def sk_model_name(self) -> str:
        pass

    @property
    @abstractmethod
    def sk_model(self):
        pass

    def get_model(self):
        """Get model from S3 if possible , if not load reserved model"""

        raise NotImplementedError
