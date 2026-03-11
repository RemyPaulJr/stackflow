import config
import enums
from sqlalchemy import Column, Integer, String, Numeric, DateTime, Enum, Text, ForeignKey, func



class Transactions(config.Base):
    __tablename__ = 'transactions' # create table

    # define columns, datatypes, and constraints
    id = Column(Integer, autoincrement=True, primary_key=True)
    amount = Column(Numeric(10,2),nullable=False)
    category = Column(Enum(enums.TransactionCategoryEnum), nullable=False) # enum datatype that has all possible values in enums.py
    description = Column(Text)
    date = Column(DateTime, nullable=False)
    type = Column(Enum(enums.TransactionTypeEnum), nullable=False)
    savings_goal_id = Column(Integer, ForeignKey("savings_goals.id"))
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    '''
    take in an instance of transaction (whatever is passed as the transaction)
    and take in a session. then take that session we received
    and add the instance of the transaction
    then commit it (INSERT INTO)
    '''
    def add_transaction(self, session):
        session.add(self)
        session.commit()

    def get_transaction(self, session, id) -> "Transactions":
        return session.query(Transactions).filter_by(id=id).first()

    def update_transaction(self, session, id, **kwargs):
        transaction = session.query(Transactions).filter_by(id=id).first()
        if transaction:
            for key, value in kwargs.items():
                setattr(transaction, key, value)
            session.commit()
    
    def delete_transaction(self, session, id):
        transaction = session.query(Transactions).filter_by(id=id).first()
        if transaction:
            session.delete(transaction)
            session.commit()