from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

stocks_dict = {"AAPL":{"name":"Apple", "price": 136.69, "per_change": 0.05, "volume": 987654321, "mkt_cap": 234567890123},
                "TSLA":{"name":"Tesla", "price": 666.66, "per_change": 0.06, "volume": 876543210, "mkt_cap": 345678901234},
                "AMZN":{"name":"Amazon", "price": 3000.00, "per_change": 0.07, "volume": 765432109, "mkt_cap": 456789012345},
                "GOOG":{"name":"Google", "price": 2000.00, "per_change": 0.08, "volume": 654321098, "mkt_cap": 567890123456},
                "MSFT":{"name":"Microsoft", "price": 1000.00, "per_change": 0.09, "volume": 543210987, "mkt_cap": 678901234567},
                "FB":{"name":"Facebook", "price": 500.00, "per_change": 0.10, "volume": 432109876, "mkt_cap": 789012345678},
}

crypto_dict = {"BTC":{"name":"Bitcoin", "price": 50000.00, "per_change": 0.05, "volume": 987654321, "mkt_cap": 234567890123},
                "ETH":{"name":"Ethereum", "price": 2000.00, "per_change": 0.06, "volume": 876543210, "mkt_cap": 345678901234},
                "XRP":{"name":"Ripple", "price": 1.00, "per_change": 0.07, "volume": 765432109, "mkt_cap": 456789012345},
                "LTC":{"name":"Litecoin", "price": 200.00, "per_change": 0.08, "volume": 654321098, "mkt_cap": 567890123456},
                "BCH":{"name":"Bitcoin Cash", "price": 500.00, "per_change": 0.09, "volume": 543210987, "mkt_cap": 678901234567},
                "LINK":{"name":"Chainlink", "price": 100.00, "per_change": 0.10, "volume": 432109876, "mkt_cap": 789012345678},
}

stocks = [{"name":"JPM", "price": 136.69, "per_change": 0.05, "volume": 987654321, "mkt_cap": 234567890123}]
cryptos = [{"name":"ADA", "price": 50000.00, "per_change": 0.05, "volume": 987654321, "mkt_cap": 234567890123}]

@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to your todo list."}

@app.get("/stock", tags=["stocks"])
async def get_stocks():
    return {"data": stocks}

@app.get("/crypto", tags=["cryptos"])
async def get_cryptos():
    return {"data": cryptos}

@app.post("/stock", tags=["stocks"])
async def add_stock(stock: dict):
    try:
        stocks.append(stocks_dict[stock["item"]])
        return {"data": "Stock added"}
    except:
        return {"data": "Stock not found"}

@app.post("/crypto", tags=["cryptos"])
async def add_crypto(crypto: dict):
    try:
        cryptos.append(crypto_dict[crypto["item"]])
        return {"data": "Crypto added"}
    except:
        return {"data": "Crypto not found"}