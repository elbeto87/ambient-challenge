from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.exceptions import DwellingNotFoundException
from app.repository.dwelling import DwellingRepository
from app.repository.hub import HubRepository
from app.schemas.dwelling import DwellingCreateSchema, DwellingUpdateSchema, InstallHubSchema
from app.service.dwelling import DwellingService
from logger import logger

router = APIRouter(tags=["Dwelling"])


@router.post("/create")
def create_dwelling(dwelling_to_add: DwellingCreateSchema, session: Session = Depends(get_db)):
    logger.info(f"Creating new dwelling: {dwelling_to_add.name}")
    dwelling_repository = DwellingRepository(session)
    hub_repository = HubRepository(session)
    return DwellingService(dwelling_repository, hub_repository).create_dwelling(dwelling_to_add)


@router.put("/{dwelling_id}")
def update_occupied_status(dwelling_id: str, occupied_status: DwellingUpdateSchema, session: Session = Depends(get_db)):
    try:
        logger.info(f"Updating occupied status for dwelling: {dwelling_id} to {occupied_status.occupied}")
        dwelling_repository = DwellingRepository(session)
        hub_repository = HubRepository(session)
        return DwellingService(dwelling_repository, hub_repository).update_dwelling(dwelling_id, occupied_status)
    except DwellingNotFoundException as e:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=str(e))


@router.get("/{dwelling_id}")
def get_dwelling(dwelling_id: str, session: Session = Depends(get_db)):
    try:
        logger.info(f"Getting dwelling for dwelling: {dwelling_id}")
        dwelling_repository = DwellingRepository(session)
        hub_repository = HubRepository(session)
        dwelling = DwellingService(dwelling_repository, hub_repository).get_dwelling(dwelling_id)
        return dwelling
    except DwellingNotFoundException as e:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=str(e))


@router.get("/")
def get_all_dwellings(session: Session = Depends(get_db)):
    logger.info("Fetching all dwellings")
    dwelling_repository = DwellingRepository(session)
    hub_repository = HubRepository(session)
    return DwellingService(dwelling_repository, hub_repository).get_all_dwellings()


@router.put("/{dwelling_id}/{hub_id}")
def install_hub(dwelling_id: str, hub_id: str, session: Session = Depends(get_db)):
    try:
        logger.info(f"Installing hub for dwelling: {dwelling_id}")
        dwelling_repository = DwellingRepository(session)
        hub_repository = HubRepository(session)
        dwelling = DwellingService(dwelling_repository, hub_repository).install_hub(dwelling_id, hub_id)
        return dwelling
    except DwellingNotFoundException as e:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=str(e))
