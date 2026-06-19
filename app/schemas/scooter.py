from pydantic import BaseModel

class ScooterRequest(BaseModel):
    speed: float
    battery: int


class ScooterResponse(BaseModel):
    status: str
    recommendation: str
