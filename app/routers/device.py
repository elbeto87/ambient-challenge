from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.repository.device import DeviceRepository
from app.schemas.device import DeviceCreateSchema
from app.service.device import DeviceService

router = APIRouter(tags=["Device"])

@router.get("/")
def get_all_devices():
    return {"message": "This is a placeholder for getting all devices."}

@router.post("/")
def create_new_device(device_to_create: DeviceCreateSchema, session: Session = Depends(get_db)):
    device_repository = DeviceRepository(session)
    return DeviceService(device_repository).create_device(device_to_create)



# TODO: Add new device
# TODO: Remove device (only if its not paired)
# TODO: Get status
# TODO: Modify status
# TODO: List all devices