from models import config
from sqlalchemy import Column, Integer, Numeric, func, DateTime, select, Date
from datetime import date

class PortfolioSnapshot(config.Base):
    __tablename__ = 'portfolio_snapshot'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    total_value = Column(Numeric(10,2), nullable=False)
    pnl_today = Column(Numeric(10,2), nullable=False)
    pnl_percent = Column(Numeric(5,2), nullable=False)
    btc_price = Column(Numeric(10,2), nullable=False)
    eth_price = Column(Numeric(10,2), nullable=False)
    sol_price = Column(Numeric(10,2), nullable=False)
    doge_price = Column(Numeric(10,6), nullable=False)
    recorded_at = Column(Date, server_default=func.now())

    def add_portfolio_snapshot(self, session):
        session.add(self)
        session.commit()
    
    def get_portfolio_snapshot(self, session, id):
        return session.get(PortfolioSnapshot, id)
    
    def update_portfolio_snapshot(self, session, id, **kwargs):
        portfolio_snapshot = session.get(PortfolioSnapshot, id)

        if portfolio_snapshot:
            for key, value in kwargs.items():
                setattr(portfolio_snapshot, key, value)
            session.commit()

        
    def delete_portfolio_snapshot(self, session, id):
        portfolio_snapshot = session.get(PortfolioSnapshot, id)

        if portfolio_snapshot:
            session.delete(portfolio_snapshot)
            session.commit()

    def get_latest_snapshot(self, session):
        stmt = select(PortfolioSnapshot).order_by(PortfolioSnapshot.recorded_at.desc()).limit(1)
        result = session.execute(stmt).scalars().all()

        for row in result:
            print(row.id, row.btc_price, row.recorded_at)
    
    def get_snapshots_range(self, session, start_date, end_date):
        stmt = select(PortfolioSnapshot).where(start_date <= PortfolioSnapshot.recorded_at, end_date >= PortfolioSnapshot.recorded_at)
        result = session.execute(stmt).scalars().all()
        
        for row in result:
            print(row.id, row.btc_price, row.recorded_at)
           
           