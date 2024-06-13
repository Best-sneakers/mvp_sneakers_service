from typing import List

from pydantic import BaseModel, Field


class LabelOutput(BaseModel):
    name: str
    datatype: str
    shape: List[int]
    data: List[str]


class InferenceResponse(BaseModel):
    model_name: str = Field(
        ..., description="Name of the model used for inference"
    )
    model_version: str = Field(
        ..., description="Version of the model " "used for inference"
    )
    outputs: List[LabelOutput]

    class Config:
        arbitrary_types_allowed = True
