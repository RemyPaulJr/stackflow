from models import config
from models import enums
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

    def add_SavingsGoals(self, session):
        session.add(self)
        session.commit()
    
    def get_SavingsGoals(self, session, id):
        return session.get(SavingsGoals, id)

    def update_SavingsGoals(self, session, id, **kwargs):
        saving_goal = session.get(SavingsGoals, id)

        if saving_goal:
            for key, value in kwargs.items():
                setattr(saving_goal, key, value)
            session.commit()
        
    def delete_SavingsGoals(self, session, id):
        saving_goal = session.get(SavingsGoals, id)

        if saving_goal:
            session.delete(saving_goal)
            session.commit()

    def calculate_Trajectory(self, session, id):
        saving_goal = session.get(SavingsGoals, id)

        if saving_goal:
            trajectory = round((saving_goal.target_amount - saving_goal.current_amount) / saving_goal.monthly_contribution, 2)
            print(f"Will reach target goal in {trajectory} months")