from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field, HttpUrl


class ObjectType(str, Enum):
    pedestrian = "pedestrian"
    bicycle = "bicycle"
    scooter = "scooter"
    motorcycle = "motorcycle"
    car = "car"
    truck = "truck"
    traffic_light = "traffic_light"
    road_sign = "road_sign"
    curb = "curb"
    pothole = "pothole"
    obstacle = "obstacle"


class RiskLevel(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"
    critical = "critical"


class BoundingBox(BaseModel):
    x: float = Field(..., description="Top-left X coordinate")
    y: float = Field(..., description="Top-left Y coordinate")
    width: float
    height: float


class DetectedObject(BaseModel):
    object_id: str

    type: ObjectType

    confidence: float = Field(
        ...,
        ge=0,
        le=1,
        description="Detection confidence"
    )

    distance_m: float = Field(
        ...,
        ge=0,
        description="Distance to object in meters"
    )

    risk: RiskLevel

    bbox: BoundingBox


class ObstacleDetectionRequest(BaseModel):
    scooter_id: str

    frame_id: str

    image_url: Optional[HttpUrl] = None

    timestamp: str


class ObstacleDetectionResponse(BaseModel):
    scooter_id: str

    frame_id: str

    objects: List[DetectedObject]

    recommended_action: str

    max_allowed_speed: float

    emergency_brake: bool = False