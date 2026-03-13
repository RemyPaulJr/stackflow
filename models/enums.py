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

class InvestmentsAccountTypeEnum(enum.Enum):
    _401k = "401k"
    roth_ira = "roth_ira"
    brokerage = "brokerage"

class DebtsTypeEnum(enum.Enum):
    student_loan = "student_loan"
    credit_card = "credit_card"
    personal_loan = "peronsal_loan"
    other = "other"

class CryptoHoldingExchangeEnum(enum.Enum):
    coinbase = "coinbase"
    binance = "binance"
    kraken = "kraken"
    other = "other"