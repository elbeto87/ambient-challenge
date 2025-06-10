from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.repository.device import DeviceRepository
from app.schemas.device import DeviceCreateSchema, DeviceStateSchema, DeviceUpdateStateSchema, DeviceSchema
from app.service.device import DeviceService
from logger import logger

router = APIRouter(tags=["Device"])

@router.post("/", response_model=DeviceSchema, status_code=HTTPStatus.CREATED)
def create_new_device(device_to_create: DeviceCreateSchema, session: Session = Depends(get_db)):
    logger.info(f"Creating new device: {device_to_create.name}")
    device_repository = DeviceRepository(session)
    return DeviceService(device_repository).create_device(device_to_create)

@router.delete("/{device_id}")
def delete_device(device_id: str, session: Session = Depends(get_db)):
    logger.info(f"Deleting device: {device_id}")
    device_repository = DeviceRepository(session)
    return DeviceService(device_repository).delete_device(device_id)

@router.get("/")
def get_all_devices(session: Session = Depends(get_db)):
    logger.info("Fetching all devices")
    device_repository = DeviceRepository(session)
    return DeviceService(device_repository).get_all_devices()

@router.get("/{device_id}")
def get_device_state(device_id: str, session: Session = Depends(get_db)):
    logger.info(f"Fetching device state: {device_id}")
    device_repository = DeviceRepository(session)
    return DeviceService(device_repository).get_device_state(device_id)

@router.put("/{device_id}")
def modify_device_state(device_id: str, device_state: DeviceUpdateStateSchema, session: Session = Depends(get_db)):
    logger.info(f"Modifying device state: {device_id}")
    device_repository = DeviceRepository(session)
    return DeviceService(device_repository).modify_device_state(device_id, device_state)
