import config
from transactions import Transactions

config.base.metadata.create_all(config.engine)
