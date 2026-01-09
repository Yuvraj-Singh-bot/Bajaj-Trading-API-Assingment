from fastapi import FastAPI
from app.routes.orders import router as orders_router
from app.routes.trades import router as trades_router
from app.routes.portfolio import router as portfolio_router



from app.routes.instruments import router as instruments_router

app = FastAPI(
    title="Bajaj Broking Trading API",
    description="Simplified Trading Backend",
    version="1.0.0"
)

@app.get("/")
def health_check():
    return {
        "status": "running",
        "message": "Bajaj Broking Trading API is up"
    }

# Register routes
app.include_router(instruments_router) 
app.include_router(orders_router)
app.include_router(trades_router)
app.include_router(portfolio_router) 


