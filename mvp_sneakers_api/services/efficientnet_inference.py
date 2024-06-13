import json
import logging

import numpy as np

from mvp_sneakers_api.models.efficientnet import InferenceResponse
from mvp_sneakers_api.services.base_inference import BaseHttpInferenceService
from mvp_sneakers_api.settings.settings import settings

logger = logging.getLogger("fast_api_inference")


class EfficientnetInference(BaseHttpInferenceService):
    @staticmethod
    def prepare_payload(file):
        image_data_list = []
        image_np = np.frombuffer(file, dtype=np.uint8)
        image_data_list.append(image_np.tolist())
        payload = {
            "inputs": [
                {
                    "name": "input_data",
                    "shape": [len(image_data_list), len(image_data_list[0])],
                    "datatype": "UINT8",
                    "data": image_data_list,
                }
            ]
        }
        return json.dumps(payload)

    async def infer(self, data: bytes) -> InferenceResponse:
        payload = self.prepare_payload(data)
        resp = await self.send_request(payload)
        return InferenceResponse.model_validate_json(resp)


def get_inference_service() -> EfficientnetInference:
    return EfficientnetInference(
        f"http://{settings.efficientnet.host}:"
        f"{settings.efficientnet.port}/v2/models/{settings.efficientnet.path}"
    )
