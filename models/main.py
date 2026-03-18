from models import config
from models import transactions
from models import savings_goals
from models import investments
from models import debts
from models import crypto_holding
from models import portfolio_snapshot
#from sqlalchemy import text

config.Base.metadata.create_all(config.engine)

# with config.engine.connect() as connection:
#     connection.execute(text("ALTER TABLE crypto_holding ADD COLUMN name VARCHAR(255)"))
#     connection.commit()
