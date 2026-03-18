from models import config, transactions, enums, savings_goals, crypto_holding, portfolio_snapshot
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

crypto_holdings = crypto_holding.CryptoHolding(
    symbol = "btc",
    quantity = 10,
    avg_purchase_price = 50000.00,
)

portfolio_snapshots = portfolio_snapshot.PortfolioSnapshot(
    total_value = 50000.00,
    pnl_today = 120.00,
    pnl_percent = 15.00,
    btc_price = 10000.00,
    eth_price = 5000.00,
    sol_price = 120.00,
    doge_price = 1.000950,
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
#saving_goal.calculate_Trajectory(config.session, 2)

#crypto_holdings.get_portfolio_value(config.session)
#crypto_holdings.get_current_pnl(config.session)
#crypto_holdings.update_crypto_holding(config.session, 1, name="Bitcoin")

#portfolio_snapshots.add_portfolio_snapshot(config.session)
#portfolio_snapshots.get_snapshots_range(config.session, '03-02-2026', '03-07-2026')
#portfolio_snapshots.get_latest_snapshot(config.session)