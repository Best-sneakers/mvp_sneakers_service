import logging
from typing import Dict

from fastapi import APIRouter, File, UploadFile

from mvp_sneakers_api.services.inference_model_loader import BestPickleGetter
from mvp_sneakers_api.services.model_inference import infer_model
from mvp_sneakers_api.settings.settings import settings

logger = logging.getLogger()
router = APIRouter()


@router.post("/classificate")
async def predict_item(file: UploadFile = File(...)) -> Dict:
    model = BestPickleGetter(
        settings.project.base_dir / "models", loss="accuracy_score"
    ).get_best_model()
    image = await file.read()

    prediction_result = infer_model(model, image)

    return prediction_result
