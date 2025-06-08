from fastapi import FastAPI

from app.database.base import Base
from app.database.database import engine
from app.routers import dwelling, device, hub
from app.models import DeviceModel, DwellingModel, HubModel # noqa

API_PREFIX_VERSION = "/v1"
Base.metadata.create_all(bind=engine)
app = FastAPI(
    title="Ambient Challenge",
    description="API for managing dwellings, devices, and hubs in the Ambient Challenge project.",
    version="1.0.0",
    docs_url=f"{API_PREFIX_VERSION}/docs",
    openapi_url=f"{API_PREFIX_VERSION}/openapi.json"
)

app.include_router(dwelling.router, prefix=f"{API_PREFIX_VERSION}/dwellings", tags=["Dwelling"])
app.include_router(device.router, prefix=f"{API_PREFIX_VERSION}/device", tags=["Device"])
app.include_router(hub.router, prefix=f"{API_PREFIX_VERSION}/hub", tags=["Hub"])
