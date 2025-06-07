from fastapi import APIRouter

router = APIRouter(tags=["Hub"])

@router.get("/")
def get_all_hubs():
    return {"message": "This is a placeholder for getting all hubs."}
