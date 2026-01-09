# Bajaj Broking – Trading API & Python SDK

##  Overview

This project is a **simplified trading backend system** built as part of a campus hiring assignment.  
It simulates the core functionalities of an online stock broking platform, including:

- Viewing tradable instruments
- Placing buy/sell orders
- Tracking order status
- Viewing executed trades
- Fetching portfolio holdings

The system is implemented using **Python and FastAPI** with **in-memory storage**, and also includes a **Python Wrapper SDK** to simplify API consumption.

---

##  High-Level Architecture

The project consists of two main components:

1. **Backend REST API**
   - Handles trading logic
   - Exposes RESTful endpoints
   - Uses in-memory data storage

2. **Python SDK (Wrapper)**
   - Wraps REST APIs into simple Python methods
   - Abstracts HTTP and JSON handling for clients

---

##  Technology Stack

- **Language:** Python
- **Backend Framework:** FastAPI
- **API Format:** JSON
- **Server:** Uvicorn
- **Storage:** In-memory (Python data structures)
- **Client SDK:** Python (`requests`)

---

##  Project Structure

Bajaj Assignment/
│
├── app/ # Backend application
│ ├── main.py # FastAPI entry point
│ ├── models/ # Data models (Instrument, Order, Trade, Portfolio)
│ ├── routes/ # API routes
│ └── storage/ # In-memory storage
│
├── sdk/ # Python SDK wrapper
│ └── trading_sdk.py
│
├── test_sdk.py # SDK test script
├── requirements.txt
└── README.md 


---

## 🔹 Functional APIs

### 1️. Instruments API
Fetch all tradable instruments.


**Fields:**
- symbol
- exchange
- instrumentType
- lastTradedPrice

---

### 2️. Order Management APIs

#### ➤ Place Order

**Supported:**
- BUY / SELL
- MARKET / LIMIT

**Validations:**
- Quantity must be greater than 0
- Price is mandatory for LIMIT orders

---

#### ➤ Fetch Order Status

**Order States:**
- NEW
- EXECUTED (simulated execution)

---

### 3️. Trades API
Fetch all executed trades.


---

### 4️. Portfolio API
Fetch current portfolio holdings.


**Portfolio Fields:**
- symbol
- quantity
- averagePrice
- currentValue

Portfolio is **derived dynamically from executed trades** to avoid data inconsistency.

---

##  Key Design Decisions

- **UUID-based Order IDs** for global uniqueness
- **Separation of Orders and Trades**
  - Orders represent intent
  - Trades represent execution
- **Derived Portfolio**
  - Portfolio is calculated from trades instead of being stored
- **In-memory Storage**
  - Lightweight and sufficient for simulation
- **Mock Authentication**
  - Single user assumed as per assignment scope

---

##  Python SDK (Wrapper)

A lightweight Python SDK is provided to abstract REST API usage . 

