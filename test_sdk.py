from sdk.trading_sdk import TradingSDK

# Create SDK client
client = TradingSDK()

print("========== INSTRUMENTS ==========")
instruments = client.get_instruments()
print(instruments)

print("\n========== PLACE ORDER ==========")
order = client.place_order(
    symbol="RELIANCE",
    side="BUY",
    order_type="MARKET",
    quantity=5
)
print(order)

print("\n========== TRADES ==========")
trades = client.get_trades()
print(trades)

print("\n========== PORTFOLIO ==========")
portfolio = client.get_portfolio()
print(portfolio) 
