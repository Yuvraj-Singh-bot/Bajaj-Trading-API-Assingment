from fastapi import APIRouter
from app.storage.memory import TRADES

router = APIRouter()


@router.get("/api/v1/trades")
def get_trades():
    return TRADES
