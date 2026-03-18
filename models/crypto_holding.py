from models import config
from models import enums
from sqlalchemy import Column, Integer, Enum, String, DateTime, func, Numeric, Date, Text, select
import requests
import os

class CryptoHolding(config.Base):
    __tablename__ = 'crypto_holding'

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(100), nullable=False)
    symbol = Column(String(10), nullable=False)
    quantity = Column(Numeric(18,8), nullable=False)
    avg_purchase_price = Column(Numeric(10,2), nullable=False)
    purchase_date = Column(Date, server_default=func.now())
    exchange = Column(Enum(enums.CryptoHoldingExchangeEnum), default="coinbase")
    notes = Column(Text)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    def add_crypto_holding(self, session):
        session.add(self)
        session.commit()
    
    def get_crypto_holding(self, session, id):
        return session.get(CryptoHolding, id)
    
    def update_crypto_holding(self, session, id, **kwargs):
        crypto_holding = session.get(CryptoHolding, id)

        if crypto_holding:
            for key, value in kwargs.items():
                setattr(crypto_holding, key, value)
            session.commit()

        
    def delete_crypto_holding(self, session, id):
        crypto_holding = session.get(CryptoHolding, id)

        if crypto_holding:
            session.delete(crypto_holding)
            session.commit()

    def get_portfolio_value(self, session):
        
        api_key = os.getenv("API_KEY")
        # call CoinGecko API for crypto holdings and store it as a dictionary
        url = "https://api.coingecko.com/api/v3/simple/price?vs_currencies=usd&ids=bitcoin%2Cethereum%2Csolana%2Cdogecoin&names=Bitcoin%2CEthereum%2CSolana%2CDodge&symbols=btc%2Ceth%2Csol%2Cdoge"
        headers = {"x-cg-demo-api-key": api_key}
        response = requests.get(url, headers=headers)
        data = response.json()

        # query db for the name of the coin as a lowercase to match api response and it's quantity
        stmt = select(CryptoHolding.name, CryptoHolding.quantity) # type: ignore
        portfolio_dict = {row.name.lower(): row.quantity for row in session.execute(stmt)}

        # loop through the query results dictionary and find the matching coins in api response, then calulate total holding value
        for key, value in portfolio_dict.items():
            total_worth = data[key]["usd"] * value
            print(total_worth)

    def get_current_pnl(self, session):
        
        api_key = os.getenv("API_KEY")
        # call CoinGecko API for crypto holdings and store it as a dictionary
        url = "https://api.coingecko.com/api/v3/simple/price?vs_currencies=usd&ids=bitcoin%2Cethereum%2Csolana%2Cdogecoin&names=Bitcoin%2CEthereum%2CSolana%2CDodge&symbols=btc%2Ceth%2Csol%2Cdoge"
        headers = {"x-cg-demo-api-key": api_key}
        response = requests.get(url, headers=headers)
        data = response.json()

        # query db for the name of the coin as a lowercase to match api response and it's quantity
        stmt = select(CryptoHolding.name, CryptoHolding.quantity, CryptoHolding.avg_purchase_price) # type: ignore
        portfolio_value_dict = {row.name.lower(): {"quantity": row.quantity, "average_price":row.avg_purchase_price} for row in session.execute(stmt)}

        # loop through the query results dictionary and find the matching coins in api response, then calulate total holding value
        for key, value in portfolio_value_dict.items():
            current_price = data[key]["usd"] * value["quantity"]
            cost_basis = value["average_price"] * value["quantity"]
            unrealised_pnl = current_price - cost_basis
            print(current_price, ", ", cost_basis, ", ", unrealised_pnl)