from pydantic import BaseModel
from datetime import datetime


class Trade(BaseModel):
    tradeId: str
    orderId: str
    symbol: str
    quantity: int
    price: float
    timestamp: datetime 

