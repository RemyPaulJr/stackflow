import enum

class TransactionCategoryEnum(enum.Enum): # inherit the Enum class from the enum builtin module
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

class SavingsGoalsStatusEnum(enum.Enum):
    active = "active"
    completed = "completed"
    paused = "paused"