from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.repository.device import DeviceRepository
from app.schemas.device import DeviceCreateSchema
from app.service.device import DeviceService

router = APIRouter(tags=["Device"])

@router.post("/")
def create_new_device(device_to_create: DeviceCreateSchema, session: Session = Depends(get_db)):
    device_repository = DeviceRepository(session)
    return DeviceService(device_repository).create_device(device_to_create)

@router.delete("/{device_id}")
def delete_device(device_id: str, session: Session = Depends(get_db)):
    device_repository = DeviceRepository(session)
    return DeviceService(device_repository).delete_device(device_id)

@router.get("/")
def get_all_devices(session: Session = Depends(get_db)):
    device_repository = DeviceRepository(session)
    return DeviceService(device_repository).get_all_devices()


# TODO: Get status
# TODO: Modify status