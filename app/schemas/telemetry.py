from pydantic import BaseModel
from datetime import datetime


class Telemetry(BaseModel):
    scooter_id: str
    timestamp: datetime
    speed: float
    battery: float
    temperature: float
    vibration: float
    latitude: float
    longitude: float