from fastapi import APIRouter

router = APIRouter(tags=["Device"])

@router.get("/")
def get_all_devices():
    return {"message": "This is a placeholder for getting all devices."}
