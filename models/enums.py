import enum

class TransactionCategoryEnum(enum.Enum):
    food = "food"
    rent = "rent"
    transport = "transport"
    entertainment = "entertainment"
    utilities = "utilities"
    subscriptions = "subscriptions"
    concerts = "concerts"
    savings = "savings"
    investment = "investments"
    debt_payment = "debt_payment"

class TransactionTypeEnum(enum.Enum):
    income = "income"
    expense = "expense"

