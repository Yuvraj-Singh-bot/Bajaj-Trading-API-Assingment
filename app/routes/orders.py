import uuid
from datetime import datetime
from fastapi import APIRouter, HTTPException
from app.models.order import OrderRequest, Order, OrderStatus
from app.models.trade import Trade
from app.storage.memory import ORDERS, TRADES, INSTRUMENTS

router = APIRouter()


@router.post("/api/v1/orders")
def place_order(order_req: OrderRequest):
    if order_req.orderType == "LIMIT" and order_req.price is None:
        raise HTTPException(status_code=400, detail="Price is required for LIMIT orders")

    # Find instrument price
    instrument = next((i for i in INSTRUMENTS if i.symbol == order_req.symbol), None)
    if not instrument:
        raise HTTPException(status_code=404, detail="Instrument not found")

    execution_price = (
        instrument.lastTradedPrice
        if order_req.orderType == "MARKET"
        else order_req.price
    )

    order_id = str(uuid.uuid4())

    order = Order(
        orderId=order_id,
        symbol=order_req.symbol,
        side=order_req.side,
        orderType=order_req.orderType,
        quantity=order_req.quantity,
        price=execution_price,
        status=OrderStatus.EXECUTED
    )

    ORDERS[order_id] = order

    # Create trade
    trade = Trade(
        tradeId=str(uuid.uuid4()),
        orderId=order_id,
        symbol=order.symbol,
        quantity=order.quantity,
        price=execution_price,
        timestamp=datetime.utcnow()
    )

    TRADES.append(trade)

    return order
