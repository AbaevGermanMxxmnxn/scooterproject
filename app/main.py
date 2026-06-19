from fastapi import FastAPI

from app.routers.telemetry import router as telemetry_router
from app.routers.safety import router as safety_router
from app.routers.maintenance import router as maintenance_router
from app.routers.pricing import router as pricing_router
from app.routers.logistics import router as logistics_router

app = FastAPI(
    title="Whoosh Neural-Core",
    version="1.0.0"
)

app.include_router(telemetry_router)
app.include_router(safety_router)
app.include_router(maintenance_router)
app.include_router(pricing_router)
app.include_router(logistics_router)


@app.get("/")
async def root():
    return {
        "service": "Whoosh Neural-Core",
        "status": "running"
    }