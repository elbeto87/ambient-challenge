from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.repository.hub import HubRepository
from app.schemas.dwelling import DwellingSchema
from app.schemas.hub import HubCreateSchema, DeviceToDeleteSchema, DeviceToPairSchema, HubSchema
from app.service.hub import HubService
from logger import logger

router = APIRouter(tags=["Hub"])

@router.post("/", response_model=HubSchema, status_code=HTTPStatus.CREATED)
def create_hub(hub_to_create: HubCreateSchema, session: Session = Depends(get_db)):
    logger.info(f"Creating new hub: {hub_to_create}")
    hub_repository = HubRepository(session)
    return HubService(hub_repository).create_hub(hub_to_create)

@router.get("/")
def get_all_hubs(session: Session = Depends(get_db)):
    logger.info(f"Getting all hubs: {session}")
    hub_repository = HubRepository(session)
    return HubService(hub_repository).get_all_hubs()

@router.get("/{hub_id}")
def get_devices_by_hud(hub_id: str, session: Session = Depends(get_db)):
    logger.info(f"Getting devices for hub: {hub_id}")
    hub_repository = HubRepository(session)
    return HubService(hub_repository).get_devices(hub_id)

@router.delete("/{hub_id}")
def delete_devices_by_hub(hub_id: str, device_to_delete: DeviceToDeleteSchema, session: Session = Depends(get_db)):
    logger.info(f"Deleting devices for hub: {hub_id}")
    hub_repository = HubRepository(session)
    device_deleted = HubService(hub_repository).delete_device(hub_id, device_to_delete)
    if not device_deleted:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Hub or Device not found")
    return device_deleted

@router.put("/{hub_id}")
def pair_device(hub_id: str, device_to_pair: DeviceToPairSchema, session: Session = Depends(get_db)):
    logger.info(f"Pairing device for hub: {hub_id}")
    hub_repository = HubRepository(session)
    return HubService(hub_repository).pair_device(hub_id, device_to_pair)

@router.get("/{hub_id}/{device_id}")
def get_device_status(hub_id: str, device_id: str, session: Session = Depends(get_db)):
    logger.info(f"Getting device status for hub: {hub_id}/{device_id}")
    hub_repository = HubRepository(session)
    return HubService(hub_repository).get_device_status(hub_id, device_id)
