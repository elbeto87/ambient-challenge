from fastapi import APIRouter

router = APIRouter(tags=["Dwelling"])

@router.get("/")
def get_all_dwellings():
    return {"message": "This is a placeholder for getting all dwellings."}
