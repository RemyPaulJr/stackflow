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

saving_goal = savings_goals.SavingsGoals(
    name="House",
    target_amount="100000.00",
    current_amount="33000.00",
    deadline=datetime(2026,4,1),
    monthly_contribution="5.00",
    status=enums.SavingsGoalsStatusEnum.active   
)

# Transaction test
#transaction.add_transaction(config.session)
#transaction.get_transaction(config.session, 2)
#transaction.update_transaction(config.session, 2, description= "Grocery shopping at Walmart")
#transaction.delete_transaction(config.session, 2)

# Savings Goals test
#saving_goal.add_SavingsGoals(config.session)
#saving_goal.get_SavingsGoals(config.session, 1)
#saving_goal.update_SavingsGoals(config.session, 2, monthly_contribution="12000")
#saving_goal.delete_SavingsGoals(config.session, 1)
saving_goal.calculate_Trajectory(config.session, 2)