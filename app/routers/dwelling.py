from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.base import get_db
from app.repository.dwelling import DwellingRepository
from app.schemas.dwellingschema import DwellingSchema
from app.service.dwelling import DwellingService

router = APIRouter(tags=["Dwelling"])


@router.get("/")
def get_all_dwellings():
    return {"message": "This is a placeholder for getting all dwellings."}


@router.post("/create")
def create_dwelling(dwelling_to_add: DwellingSchema, session: Session = Depends(get_db)):
    dwelling_repository = DwellingRepository(session)
    return DwellingService(dwelling_repository).create_dwelling(dwelling_to_add)


@router.get("/{dwelling_id}")
def get_dwelling(dwelling_id: int, session: Session = Depends(get_db)):
    dwelling_repository = DwellingRepository(session)
    dwelling_service = DwellingService(dwelling_repository).get_dwelling(dwelling_id)
    if not dwelling:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Dwelling not found")
    return DwellingSchema().dump(dwelling)
