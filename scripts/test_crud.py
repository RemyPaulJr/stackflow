from models import config, transactions, enums, savings_goals
from datetime import datetime

transaction = transactions.Transactions(
    amount = '50.00',
    category = enums.TransactionCategoryEnum.food,
    description = "Grocery shopping at Kroger",
    date = datetime(2026, 3, 11),
    type = enums.TransactionTypeEnum.expense,
    savings_goal_id = None
)

#transaction.add_transaction(config.session)
#transaction.get_transaction(config.session, 2)
#transaction.update_transaction(config.session, 2, description= "Grocery shopping at Walmart")
transaction.delete_transaction(config.session, 2)