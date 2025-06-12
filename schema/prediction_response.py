from pydantic import BaseModel, Field
from typing import Dict

class PredictionResponse(BaseModel):
    predicted_category: str = Field(
        ...,
        description="The predicted category for the insurance premium based on user input.",
        example="High"
    )
    confidence: float = Field(
        ...,
        description="The confidence level of the prediction, ranging from 0 to 1.",
        example=0.85
    )
    class_probabilities: Dict[str, float] = Field(
        ...,
        description="A dictionary containing the probabilities for each class.",
        example={
            "Low": 0.1,
            "Medium": 0.15,
            "High": 0.75
        }
    )