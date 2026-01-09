from fastapi import APIRouter
from app.storage.memory import INSTRUMENTS

router = APIRouter()


@router.get("/api/v1/instruments")
def get_instruments():
    return INSTRUMENTS
