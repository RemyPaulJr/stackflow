from models import config
from models import enums
from sqlalchemy import Column, Integer, Enum, String, DateTime, func, Numeric, Date, Text

class CryptoHolding(config.Base):
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False),
    symbol = Column(String(10), nullable=False),
    quantity = Column(Numeric(18,8), nullable=False),
    avg_purchase_price = Column(Numeric(10,2), nullable=False),
    purchase_date = Column(Date, server_default=func.now()),
    exchange = Column(Enum(enums.CryptoHoldingExchangeEnum), default="coinbase"),
    notes = Column(Text),
    created_at = Column(DateTime, server_default=func.now()),
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