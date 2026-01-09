from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum


class OrderSide(str, Enum):
    BUY = "BUY"
    SELL = "SELL"


class OrderType(str, Enum):
    MARKET = "MARKET"
    LIMIT = "LIMIT"


class OrderStatus(str, Enum):
    NEW = "NEW"
    PLACED = "PLACED"
    EXECUTED = "EXECUTED"
    CANCELLED = "CANCELLED"


class OrderRequest(BaseModel):
    symbol: str
    side: OrderSide
    orderType: OrderType
    quantity: int = Field(gt=0)
    price: Optional[float] = None


class Order(BaseModel):
    orderId: str
    symbol: str
    side: OrderSide
    orderType: OrderType
    quantity: int
    price: Optional[float]
    status: OrderStatus
