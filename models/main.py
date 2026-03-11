import config
from transactions import Transactions
from savings_goals import SavingsGoals

config.Base.metadata.create_all(config.engine)
