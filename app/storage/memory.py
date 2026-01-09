from app.models.instrument import Instrument

# Mocked list of tradable instruments
INSTRUMENTS = [
    Instrument(
        symbol="RELIANCE",
        exchange="NSE",
        instrumentType="EQUITY",
        lastTradedPrice=2500.50
    ),
    Instrument(
        symbol="TCS",
        exchange="NSE",
        instrumentType="EQUITY",
        lastTradedPrice=3900.75
    ),
    Instrument(
        symbol="INFY",
        exchange="NSE",
        instrumentType="EQUITY",
        lastTradedPrice=1450.20
    ), 
    Instrument( 
        symbol="Bajaj Finserv", 
        exchange="NSE" , 
        instrumentType="EQUITY", 
        lastTradedPrice=3000.40 
    ) 
]

ORDERS = {} 
TRADES = [] 

