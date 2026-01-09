import requests


class TradingSDK:
    def __init__(self,base_url:str = "http://127.0.0.1:8000"): 
        
        self.base_url = base_url

    # Instruments

    def get_instruments(self):
        """
        Fetch all tradable instruments
        """
        url = f"{self.base_url}/api/v1/instruments"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    # Orders 

    def place_order(
        self,
        symbol: str,
        side: str,
        order_type: str,
        quantity: int,
        price: float = None
    ):
        """
        Place a BUY or SELL order
        """
        url = f"{self.base_url}/api/v1/orders"

        payload = {
            "symbol": symbol,
            "side": side,
            "orderType": order_type,
            "quantity": quantity
        }

        if price is not None:
            payload["price"] = price

        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()

    def get_order(self, order_id: str):
        """
        Fetch order status by orderId
        """
        url = f"{self.base_url}/api/v1/orders/{order_id}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    # Trades

    def get_trades(self):
        """
        Fetch all executed trades
        """
        url = f"{self.base_url}/api/v1/trades"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    # Portfolio

    def get_portfolio(self):
        """
        Fetch current portfolio holdings
        """
        url = f"{self.base_url}/api/v1/portfolio"
        response = requests.get(url)
        response.raise_for_status()
        return response.json() 
