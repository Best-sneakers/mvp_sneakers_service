import logging
from abc import ABC, abstractmethod
from http import HTTPStatus
from typing import Any

import aiohttp
from fastapi import HTTPException

logger = logging.getLogger("fast_api_inference")


class BaseHttpInferenceService(ABC):
    def __init__(self, inference_endpoint: str):
        self.inference_endpoint = inference_endpoint

    async def send_request(self, payload: str):
        headers = {"Content-Type": "application/json"}
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    self.inference_endpoint, data=payload, headers=headers
                ) as response:
                    if response.status == HTTPStatus.OK:
                        return await response.text()
                    raise HTTPException(
                        status_code=response.status,
                        detail=await response.text(),
                    )
        except Exception as err:
            logger.error("Error sending inference request", exc_info=err)
            raise err

    @abstractmethod
    async def infer(self, data: Any) -> Any:
        raise NotImplementedError
