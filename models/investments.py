from models import config
from models import enums
from sqlalchemy import Column, Integer, String, Enum, Numeric, DateTime, func, Text, Date

class Investments(config.Base):
    __table__name = "investments"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False),
    account_type = Column(Enum(enums.InvestmentsAccountTypeEnum), nullable=False),
    ticker = Column(String(10), nullable=False),
    shares = Column(Numeric(10,4), nullable=False),
    avg_cost_basis = Column(Numeric(10,2), nullable=False),
    date_added = Column(Date, server_default=func.now()),
    notes = Column(Text),
    created_at = Column(DateTime, server_default=func.now()),
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    def add_investment(self, session):
        session.add(self)
        session.commit()

    def get_investment(self, session, id):
        return session.get(Investments, id)
    
    def update_investment(self, session, id, **kwargs):
        investment = session.get(Investments, id)

        if investment:
            for key, value in kwargs.items():
                setattr(investment, key, value)
            session.commit()

    def delete_investment(self, session, id):
        investment = session.get(Investments, id)

        if investment:
            session.delete(investment)
            session.commit()