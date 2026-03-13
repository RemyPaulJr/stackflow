from models import config
from models import enums
from sqlalchemy import Column, Integer, Numeric, Enum, DateTime, String, func

class Debts(config.Base):
    __table__name = "debts"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False),
    name = Column(String(100), nullable=False),
    balance = Column(Numeric(10,2), nullable=False),
    interest_rate = Column(Numeric(5,2), nullable=False),
    minimum_payment = Column(Numeric(10,2), nullable=False),
    debt_type = Column(Enum(enums.DebtsTypeEnum), nullable=False),
    created_at = Column(DateTime, server_default=func.now()),
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    def add_debt(self, session):
        session.add(self)
        session.commit()

    def get_debt(self, session, id):
        return session.get(Debts, id)
    
    def update_debt(self, session, id, **kwargs):
        debt = session.get(Debts, id)

        if debt:
            for key, value in kwargs.items():
                setattr(debt, key, value)
            session.commit()
    
    def delete_debt(self, session, id):
        debt = session.get(Debts, id)

        if debt:
            session.delete(debt)
            session.commit()