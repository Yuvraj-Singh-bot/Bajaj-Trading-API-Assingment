from fastapi import APIRouter
from app.storage.memory import TRADES, INSTRUMENTS
from app.models.portfolio import PortfolioItem

router = APIRouter()


@router.get("/api/v1/portfolio")
def get_portfolio():
    portfolio = {}

    for trade in TRADES:
        if trade.symbol not in portfolio:
            portfolio[trade.symbol] = {
                "quantity": 0,
                "totalCost": 0.0
            }

        portfolio[trade.symbol]["quantity"] += trade.quantity
        portfolio[trade.symbol]["totalCost"] += trade.quantity * trade.price

    result = []

    for symbol, data in portfolio.items():
        instrument = next(i for i in INSTRUMENTS if i.symbol == symbol)
        avg_price = data["totalCost"] / data["quantity"]
        current_value = data["quantity"] * instrument.lastTradedPrice

        result.append(
            PortfolioItem(
                symbol=symbol,
                quantity=data["quantity"],
                averagePrice=round(avg_price, 2),
                currentValue=round(current_value, 2)
            )
        )

    return result
