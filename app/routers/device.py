from fastapi import APIRouter

router = APIRouter(tags=["Device"])

@router.get("/")
def get_all_devices():
    return {"message": "This is a placeholder for getting all devices."}

# TODO: Add new device
# TODO: Remove device (only if its not paired)
# TODO: Get status
# TODO: Modify status
# TODO: List all devices