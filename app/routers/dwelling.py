from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.base import get_db
from app.exceptions import DwellingNotFoundException
from app.repository.dwelling import DwellingRepository
from app.schemas.dwelling import DwellingSchema, DwellingUpdateSchema
from app.service.dwelling import DwellingService

router = APIRouter(tags=["Dwelling"])


@router.get("/")
def get_all_dwellings():
    return {"message": "This is a placeholder for getting all dwellings."}


@router.post("/create")
def create_dwelling(dwelling_to_add: DwellingSchema, session: Session = Depends(get_db)):
    dwelling_repository = DwellingRepository(session)
    return DwellingService(dwelling_repository).create_dwelling(dwelling_to_add)


@router.put("/{dwelling_id}")
def update_occupied_status(dwelling_id: int, occupied_status: DwellingUpdateSchema, session: Session = Depends(get_db)):
    try:
        dwelling_repository = DwellingRepository(session)
        return DwellingService(dwelling_repository).update_dwelling(dwelling_id, occupied_status)
    except DwellingNotFoundException as e:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=str(e))


@router.get("/{dwelling_id}")
def get_dwelling(dwelling_id: int, session: Session = Depends(get_db)):
    try:
        dwelling_repository = DwellingRepository(session)
        dwelling = DwellingService(dwelling_repository).get_dwelling(dwelling_id)
        return dwelling
    except DwellingNotFoundException as e:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=str(e))


@router.get("/")
def get_all_dwellings(session: Session = Depends(get_db)):
    dwelling_repository = DwellingRepository(session)
    return DwellingService(dwelling_repository).get_all_dwellings()
