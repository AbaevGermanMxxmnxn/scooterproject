from fastapi import APIRouter
from app.schemas.scooter import ScooterRequest, ScooterResponse
from app.services.scooter_service import analyze_scooter

router = APIRouter()

@router.post("/analyze", response_model=ScooterResponse)
def analyze(data: ScooterRequest):
    result = analyze_scooter(data.speed, data.battery)
    return result
