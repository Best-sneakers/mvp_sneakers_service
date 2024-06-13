import logging
from http import HTTPStatus

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile

from mvp_sneakers_api.models.efficientnet import InferenceResponse
from mvp_sneakers_api.services.efficientnet_inference import (
    EfficientnetInference,
    get_inference_service,
)

logger = logging.getLogger("fast_api_inference")
router = APIRouter()


@router.post("/infer_batch")
async def predict_item(
    file: UploadFile = File(...),
    inference_service: EfficientnetInference = Depends(get_inference_service),
) -> InferenceResponse:
    try:
        image = await file.read()
        response = await inference_service.infer(image)
        return response
    except Exception as e:
        logger.error("Exception occurred", exc_info=e)
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail=str(e)
        ) from e
