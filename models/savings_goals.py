import config
import enums
from sqlalchemy import Column, Integer, String, Numeric, DateTime, Enum, Text, ForeignKey, func

class SavingsGoals(config.Base):
    __tablename__ = 'savings_goals'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(100), nullable=False)
    target_amount = Column(Numeric(10,2), nullable=False)
    current_amount = Column(Numeric(10,2), server_default="0.00")
    deadline = Column(DateTime, server_default=func.now(), nullable=False) # enum datatype that has all possible values in enums.py
    description = Column(Text)
    monthly_contribution = Column(Numeric(10,2), nullable=False)
    status = Column(Enum(enums.SavingsGoalsStatusEnum), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
